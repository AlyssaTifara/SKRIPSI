import json
import os
import pandas as pd
import numpy as np

def run_audit():
    base_dir = r"C:\SKRIPSI"
    csv_path = os.path.join(base_dir, "02_Raw_Data", "Dataset_03_Chiapas", "Chiapas_Data.csv")
    excel_path = os.path.join(base_dir, "02_Raw_Data", "Dataset_03_Chiapas", "Chiapas Field Data 2012-2018.xlsx")
    
    print("Reading dataset files...")
    df = pd.read_csv(csv_path)
    xl = pd.ExcelFile(excel_path)
    
    audit_data = {}
    audit_data["files"] = {
        "csv_path": csv_path,
        "excel_path": excel_path,
        "excel_sheets": xl.sheet_names,
        "total_rows": int(len(df)),
        "total_columns": int(len(df.columns))
    }
    
    # Target audit
    y = df["YIELD"]
    audit_data["target_audit"] = {
        "column": "YIELD",
        "missing_count": int(y.isna().sum()),
        "non_finite_count": int((~np.isfinite(y)).sum()),
        "min": float(y.min()),
        "max": float(y.max()),
        "mean": float(y.mean()),
        "std": float(y.std()),
        "median": float(y.median()),
        "zeros_count": int((y == 0).sum()),
        "negative_count": int((y < 0).sum())
    }
    
    # Year distribution
    year_counts = df["Year"].value_counts().sort_index().to_dict()
    audit_data["year_distribution"] = {int(k): int(v) for k, v in year_counts.items()}
    
    # Expanding folds check
    folds_def = [
        {"fold": 1, "train_years": [2012, 2013, 2014], "test_years": [2015]},
        {"fold": 2, "train_years": [2012, 2013, 2014, 2015], "test_years": [2016]},
        {"fold": 3, "train_years": [2012, 2013, 2014, 2015, 2016], "test_years": [2017]},
        {"fold": 4, "train_years": [2012, 2013, 2014, 2015, 2016, 2017], "test_years": [2018]}
    ]
    
    fold_audits = []
    total_test_rows = 0
    for f in folds_def:
        tr_mask = df["Year"].isin(f["train_years"])
        te_mask = df["Year"].isin(f["test_years"])
        tr_indices = set(df[tr_mask].index)
        te_indices = set(df[te_mask].index)
        overlap = tr_indices.intersection(te_indices)
        
        tr_count = int(tr_mask.sum())
        te_count = int(te_mask.sum())
        total_test_rows += te_count
        
        fold_audits.append({
            "fold": f["fold"],
            "train_years": f["train_years"],
            "test_years": f["test_years"],
            "train_rows": tr_count,
            "test_rows": te_count,
            "index_overlap": len(overlap),
            "no_overlap": len(overlap) == 0,
            "train_y_missing": int(df.loc[tr_mask, "YIELD"].isna().sum()),
            "test_y_missing": int(df.loc[te_mask, "YIELD"].isna().sum())
        })
    audit_data["folds_audit"] = fold_audits
    audit_data["total_test_rows_all_folds"] = total_test_rows
    
    # Feature definition audit
    env_soil_topo = ["Clay", "CEC", "SOM", "PH", "Elev", "Slope"]
    weather_v1_v6 = {
        "prcp": [f"prcp_V{i}" for i in range(1, 7)],
        "srad": [f"srad_V{i}" for i in range(1, 7)],
        "tmax": [f"tmax_V{i}" for i in range(1, 7)],
        "tmin": [f"tmin_V{i}" for i in range(1, 7)],
        "vp": [f"vp_V{i}" for i in range(1, 7)]
    }
    
    missing_features = {}
    for col in env_soil_topo:
        missing_features[col] = int(df[col].isna().sum())
    for p, cols in weather_v1_v6.items():
        for col in cols:
            missing_features[col] = int(df[col].isna().sum())
            
    audit_data["raw_feature_missing"] = missing_features
    
    # Weather aggregations audit
    rain_pre60d = 10 * df[weather_v1_v6["prcp"]].sum(axis=1)
    srad_mean = df[weather_v1_v6["srad"]].mean(axis=1)
    tmax_mean = df[weather_v1_v6["tmax"]].mean(axis=1)
    tmin_mean = df[weather_v1_v6["tmin"]].mean(axis=1)
    vp_mean = df[weather_v1_v6["vp"]].mean(axis=1)
    
    audit_data["engineered_weather_stats"] = {
        "rain_pre60d": {
            "formula": "10 * sum(prcp_V1..prcp_V6)",
            "min": float(rain_pre60d.min()),
            "max": float(rain_pre60d.max()),
            "mean": float(rain_pre60d.mean()),
            "missing": int(rain_pre60d.isna().sum())
        },
        "srad_mean_pre60d": {
            "formula": "mean(srad_V1..srad_V6)",
            "min": float(srad_mean.min()),
            "max": float(srad_mean.max()),
            "mean": float(srad_mean.mean()),
            "missing": int(srad_mean.isna().sum())
        },
        "tmax_mean_pre60d": {
            "formula": "mean(tmax_V1..tmax_V6)",
            "min": float(tmax_mean.min()),
            "max": float(tmax_mean.max()),
            "mean": float(tmax_mean.mean()),
            "missing": int(tmax_mean.isna().sum())
        },
        "tmin_mean_pre60d": {
            "formula": "mean(tmin_V1..tmin_V6)",
            "min": float(tmin_mean.min()),
            "max": float(tmin_mean.max()),
            "mean": float(tmin_mean.mean()),
            "missing": int(tmin_mean.isna().sum())
        },
        "vp_mean_pre60d": {
            "formula": "mean(vp_V1..vp_V6)",
            "min": float(vp_mean.min()),
            "max": float(vp_mean.max()),
            "mean": float(vp_mean.mean()),
            "missing": int(vp_mean.isna().sum())
        }
    }
    
    # Categoricals audit
    audit_data["system_counts"] = {str(k): int(v) for k, v in df["System"].value_counts().items()}
    audit_data["cultivar_audit"] = {
        "unique_raw_count": int(df["Cultivar"].nunique(dropna=False)),
        "missing_count": int(df["Cultivar"].isna().sum()),
        "missing_handled_as": "UNKNOWN",
        "rare_threshold": "< 5 in training fold",
        "unseen_in_test_handled_as": "RARE_OR_UNSEEN"
    }
    
    # Excluded features check
    excluded_requested = ["Field_ID", "Lat", "Long", "Mun_yield", "Year", "Nitrogen", "Phosphorus", "Potassium", "Planting", "Tillage"]
    audit_data["excluded_features"] = {
        "features": excluded_requested,
        "all_present_in_raw_dataset": all(c in df.columns for c in excluded_requested),
        "status": "STRICTLY EXCLUDED FROM MODEL FEATURES (X)"
    }
    
    out_path = os.path.join(base_dir, "05_Modeling", "exp_cultivar_comparison", "audit_trail", "data_audit.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(audit_data, f, indent=2)
    print(f"Data audit written to {out_path}")

if __name__ == "__main__":
    run_audit()
