import os
import sys
import json
import time
import warnings
import traceback
from datetime import datetime
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, r2_score

from pipeline_builder import build_pipeline

warnings.filterwarnings("ignore", category=pd.errors.PerformanceWarning)

def compute_metrics(y_true, y_pred):
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    
    mae = float(mean_absolute_error(y_true, y_pred))
    rmse = float(np.sqrt(np.mean((y_true - y_pred) ** 2)))
    
    # Calculate R2; if variance is 0, handle safely
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    if ss_tot == 0:
        r2 = 0.0
    else:
        r2 = float(r2_score(y_true, y_pred))
        
    return {
        "MAE": mae,
        "RMSE": rmse,
        "R2": r2,
        "N": len(y_true)
    }

def run_fold(fold_id):
    fold_id = int(fold_id)
    exp_dir = r"C:\SKRIPSI\05_Modeling\exp_cultivar_comparison"
    manifest_path = os.path.join(exp_dir, "manifest.json")
    
    # Update manifest to RUNNING
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)
        
    manifest["status"] = "RUNNING"
    if manifest["start_time"] is None:
        manifest["start_time"] = datetime.now().isoformat()
    manifest["last_updated"] = datetime.now().isoformat()
    manifest["folds"][str(fold_id)]["status"] = "RUNNING"
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
        
    fold_start_time = time.time()
    
    try:
        print(f"\n{'='*60}")
        print(f"STARTING EXECUTION FOR FOLD {fold_id}")
        print(f"{'='*60}")
        
        # 1. Load data
        csv_path = r"C:\SKRIPSI\02_Raw_Data\Dataset_03_Chiapas\Chiapas_Data.csv"
        df = pd.read_csv(csv_path)
        print(f"Dataset loaded: {len(df)} rows, {len(df.columns)} columns.")
        
        # 2. Engineer weather aggregations
        df["rain_pre60d"] = 10 * df[["prcp_V1", "prcp_V2", "prcp_V3", "prcp_V4", "prcp_V5", "prcp_V6"]].sum(axis=1)
        df["srad_mean_pre60d"] = df[["srad_V1", "srad_V2", "srad_V3", "srad_V4", "srad_V5", "srad_V6"]].mean(axis=1)
        df["tmax_mean_pre60d"] = df[["tmax_V1", "tmax_V2", "tmax_V3", "tmax_V4", "tmax_V5", "tmax_V6"]].mean(axis=1)
        df["tmin_mean_pre60d"] = df[["tmin_V1", "tmin_V2", "tmin_V3", "tmin_V4", "tmin_V5", "tmin_V6"]].mean(axis=1)
        df["vp_mean_pre60d"] = df[["vp_V1", "vp_V2", "vp_V3", "vp_V4", "vp_V5", "vp_V6"]].mean(axis=1)
        
        # 3. Define fold train/test split
        fold_specs = {
            1: {"train": [2012, 2013, 2014], "test": [2015], "expected_train": 1578, "expected_test": 424},
            2: {"train": [2012, 2013, 2014, 2015], "test": [2016], "expected_train": 2002, "expected_test": 816},
            3: {"train": [2012, 2013, 2014, 2015, 2016], "test": [2017], "expected_train": 2818, "expected_test": 960},
            4: {"train": [2012, 2013, 2014, 2015, 2016, 2017], "test": [2018], "expected_train": 3778, "expected_test": 807}
        }
        
        spec = fold_specs[fold_id]
        train_df = df[df["Year"].isin(spec["train"])].copy()
        test_df = df[df["Year"].isin(spec["test"])].copy()
        
        # 4. Strict Validation Checks
        print(f"Fold {fold_id} validation:")
        print(f"  Train years: {spec['train']}, Train rows: {len(train_df)} (expected {spec['expected_train']})")
        print(f"  Test years: {spec['test']}, Test rows: {len(test_df)} (expected {spec['expected_test']})")
        
        assert len(train_df) == spec["expected_train"], f"Train row mismatch in Fold {fold_id}: {len(train_df)} vs {spec['expected_train']}"
        assert len(test_df) == spec["expected_test"], f"Test row mismatch in Fold {fold_id}: {len(test_df)} vs {spec['expected_test']}"
        
        overlap = set(train_df.index).intersection(set(test_df.index))
        assert len(overlap) == 0, f"Fatal error: train and test indices overlap ({len(overlap)} rows)!"
        print("  Index overlap check: PASSED (0 overlapping rows).")
        
        assert train_df["YIELD"].isna().sum() == 0, "Missing target in train set!"
        assert test_df["YIELD"].isna().sum() == 0, "Missing target in test set!"
        print("  Target integrity check: PASSED (0 missing target).")
        
        # 5. Baseline calculation: mean of training fold target
        y_train = train_df["YIELD"].values
        y_test = test_df["YIELD"].values
        
        y_train_mean = float(np.mean(y_train))
        pred_baseline = np.full(len(test_df), y_train_mean)
        
        # Baseline metrics
        baseline_metrics_overall = compute_metrics(y_test, pred_baseline)
        
        # 6. Models execution
        oof_preds = pd.DataFrame({
            "Field_ID": test_df["Field_ID"].values,
            "Year": test_df["Year"].values,
            "System": test_df["System"].values,
            "Cultivar": test_df["Cultivar"].fillna("UNKNOWN").values,
            "YIELD_actual": y_test,
            "pred_baseline": pred_baseline
        })
        
        models_to_run = [
            ("rf_scenario_a", "A", "rf", "Random Forest (Scenario A: Env+System)"),
            ("xgb_scenario_a", "A", "xgb", "XGBoost (Scenario A: Env+System)"),
            ("rf_scenario_b", "B", "rf", "Random Forest (Scenario B: Env+System+Cultivar)"),
            ("xgb_scenario_b", "B", "xgb", "XGBoost (Scenario B: Env+System+Cultivar)")
        ]
        
        model_results = {
            "baseline": {
                "name": "Training Mean Baseline",
                "train_mean_yield": y_train_mean,
                "overall": baseline_metrics_overall,
                "by_system": {}
            }
        }
        
        # Calculate baseline by system
        for sys_val in ["Hybrid", "Landrace"]:
            sys_mask = (test_df["System"] == sys_val).values
            if sys_mask.sum() > 0:
                model_results["baseline"]["by_system"][sys_val] = compute_metrics(
                    y_test[sys_mask], pred_baseline[sys_mask]
                )
        
        model_durations = {}
        
        for key, scenario, m_name, label in models_to_run:
            print(f"\n--- Training {label} ---")
            t0 = time.time()
            pipe = build_pipeline(scenario=scenario, model_name=m_name)
            
            # Fit pipeline strictly on train data
            pipe.fit(train_df, y_train)
            
            # Predict on test data
            y_pred = pipe.predict(test_df)
            dur = time.time() - t0
            model_durations[key] = round(dur, 2)
            
            # Verify finite predictions
            assert np.isfinite(y_pred).all(), f"Non-finite prediction encountered in model {key}!"
            oof_preds[f"pred_{key}"] = y_pred
            
            # Compute metrics
            overall_m = compute_metrics(y_test, y_pred)
            by_sys_m = {}
            for sys_val in ["Hybrid", "Landrace"]:
                sys_mask = (test_df["System"] == sys_val).values
                if sys_mask.sum() > 0:
                    by_sys_m[sys_val] = compute_metrics(y_test[sys_mask], y_pred[sys_mask])
                    
            model_results[key] = {
                "name": label,
                "scenario": scenario,
                "model_type": m_name,
                "training_duration_seconds": round(dur, 2),
                "overall": overall_m,
                "by_system": by_sys_m
            }
            
            print(f"  Finished in {dur:.2f}s: MAE={overall_m['MAE']:.4f}, RMSE={overall_m['RMSE']:.4f}, R2={overall_m['R2']:.4f}")
            for sys_val, sm in by_sys_m.items():
                print(f"    System {sys_val} (N={sm['N']}): MAE={sm['MAE']:.4f}, RMSE={sm['RMSE']:.4f}, R2={sm['R2']:.4f}")
                
        # 7. Save OOF predictions for this fold
        oof_path = os.path.join(exp_dir, "predictions", f"oof_predictions_fold_{fold_id}.csv")
        oof_preds.to_csv(oof_path, index=False)
        print(f"\nSaved OOF predictions: {oof_path}")
        
        total_fold_dur = round(time.time() - fold_start_time, 2)
        
        # 8. Save metrics for this fold
        metrics_payload = {
            "fold_id": fold_id,
            "train_years": spec["train"],
            "test_years": spec["test"],
            "train_rows": len(train_df),
            "test_rows": len(test_df),
            "total_duration_seconds": total_fold_dur,
            "model_durations": model_durations,
            "models": model_results
        }
        
        metrics_path = os.path.join(exp_dir, "metrics", f"metrics_fold_{fold_id}.json")
        with open(metrics_path, "w", encoding="utf-8") as f:
            json.dump(metrics_payload, f, indent=2)
        print(f"Saved fold metrics: {metrics_path}")
        
        # 9. Save checkpoint
        checkpoint_payload = {
            "fold_id": fold_id,
            "status": "COMPLETED",
            "completed_at": datetime.now().isoformat(),
            "duration_seconds": total_fold_dur,
            "oof_file": oof_path,
            "metrics_file": metrics_path
        }
        checkpoint_path = os.path.join(exp_dir, "checkpoints", f"checkpoint_fold_{fold_id}.json")
        with open(checkpoint_path, "w", encoding="utf-8") as f:
            json.dump(checkpoint_payload, f, indent=2)
        print(f"Saved checkpoint: {checkpoint_path}")
        
        # 10. Update manifest
        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest = json.load(f)
            
        manifest["last_updated"] = datetime.now().isoformat()
        manifest["folds"][str(fold_id)]["status"] = "COMPLETED"
        manifest["folds"][str(fold_id)]["duration_seconds"] = total_fold_dur
        manifest["folds"][str(fold_id)]["completed_at"] = datetime.now().isoformat()
        manifest["folds"][str(fold_id)]["error"] = None
        
        # Check if all folds completed
        all_completed = all(fold_info["status"] == "COMPLETED" for fold_info in manifest["folds"].values())
        if all_completed:
            manifest["status"] = "COMPLETED"
            manifest["completed_at"] = datetime.now().isoformat()
            
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2)
            
        print(f"Manifest successfully updated for Fold {fold_id} (Status: COMPLETED).")
        return True
        
    except Exception as e:
        err_msg = str(e)
        tb_str = traceback.format_exc()
        print(f"\n[ERROR] Fold {fold_id} FAILED: {err_msg}")
        print(tb_str)
        
        # Update manifest to FAILED
        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest = json.load(f)
        manifest["status"] = "FAILED"
        manifest["last_updated"] = datetime.now().isoformat()
        manifest["folds"][str(fold_id)]["status"] = "FAILED"
        manifest["folds"][str(fold_id)]["error"] = {
            "message": err_msg,
            "traceback": tb_str
        }
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2)
            
        # Write failure checkpoint
        ckpt_fail = {
            "fold_id": fold_id,
            "status": "FAILED",
            "failed_at": datetime.now().isoformat(),
            "error": err_msg,
            "traceback": tb_str
        }
        with open(os.path.join(exp_dir, "checkpoints", f"checkpoint_fold_{fold_id}.json"), "w", encoding="utf-8") as f:
            json.dump(ckpt_fail, f, indent=2)
            
        raise e

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_single_fold.py <fold_id>")
        sys.exit(1)
    fold_num = int(sys.argv[1])
    run_fold(fold_num)
