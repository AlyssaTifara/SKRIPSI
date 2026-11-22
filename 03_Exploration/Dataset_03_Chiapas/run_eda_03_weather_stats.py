import pandas as pd
import numpy as np
from scipy import stats
import json

df = pd.read_csv(r'C:\SKRIPSI\02_Raw_Data\Dataset_03_Chiapas\Chiapas_Data.csv')

weather_types = ['prcp', 'srad', 'tmax', 'tmin', 'vp']
intervals = [f'V{i}' for i in range(1, 31)]
target = 'YIELD'

results = {}

# 1. Temporal Descriptive Stats for all 150 variables
temporal_stats = {}
for w in weather_types:
    temporal_stats[w] = []
    for i in range(1, 31):
        col = f'{w}_V{i}'
        s = df[col]
        temporal_stats[w].append({
            'interval': f'V{i}',
            'index': i,
            'mean': float(s.mean()),
            'std': float(s.std()),
            'median': float(s.median()),
            'q1': float(s.quantile(0.25)),
            'q3': float(s.quantile(0.75)),
            'min': float(s.min()),
            'max': float(s.max())
        })
results['temporal_stats'] = temporal_stats

# 2. Correlations with YIELD across V1-V30
correlations = {}
for w in weather_types:
    correlations[w] = []
    for i in range(1, 31):
        col = f'{w}_V{i}'
        s = df[col]
        y = df[target]
        
        pr, pp = stats.pearsonr(s, y)
        sr, sp = stats.spearmanr(s, y)
        
        # Stratified by System
        hyb_mask = df['System'] == 'Hybrid'
        land_mask = df['System'] == 'Landrace'
        
        pr_hyb, _ = stats.pearsonr(df.loc[hyb_mask, col], df.loc[hyb_mask, target])
        sr_hyb, _ = stats.spearmanr(df.loc[hyb_mask, col], df.loc[hyb_mask, target])
        
        pr_land, _ = stats.pearsonr(df.loc[land_mask, col], df.loc[land_mask, target])
        sr_land, _ = stats.spearmanr(df.loc[land_mask, col], df.loc[land_mask, target])
        
        correlations[w].append({
            'interval': f'V{i}',
            'index': i,
            'pearson_r': float(pr),
            'pearson_p': float(pp),
            'spearman_rho': float(sr),
            'spearman_p': float(sp),
            'hybrid_pearson_r': float(pr_hyb),
            'hybrid_spearman_rho': float(sr_hyb),
            'landrace_pearson_r': float(pr_land),
            'landrace_spearman_rho': float(sr_land)
        })
results['correlations_with_yield'] = correlations

# 3. Autocorrelation & Inter-interval correlation analysis
autocorr_results = {}
for w in weather_types:
    cols = [f'{w}_V{i}' for i in range(1, 31)]
    corr_mat = df[cols].corr(method='pearson')
    
    # Lag 1 autocorrelations: corr(V_i, V_{i+1})
    lag1 = [float(corr_mat.iloc[i, i+1]) for i in range(29)]
    # Lag 2 autocorrelations: corr(V_i, V_{i+2})
    lag2 = [float(corr_mat.iloc[i, i+2]) for i in range(28)]
    # Lag 3 autocorrelations: corr(V_i, V_{i+3})
    lag3 = [float(corr_mat.iloc[i, i+3]) for i in range(27)]
    
    autocorr_results[w] = {
        'mean_lag1': float(np.mean(lag1)),
        'min_lag1': float(np.min(lag1)),
        'max_lag1': float(np.max(lag1)),
        'mean_lag2': float(np.mean(lag2)),
        'mean_lag3': float(np.mean(lag3)),
        'mean_matrix_corr': float(corr_mat.values[np.triu_indices(30, k=1)].mean())
    }
results['autocorrelation_summary'] = autocorr_results

# 4. Period Comparison: Pre-planting (V1-V6) vs In-season (V7-V24) vs Late (V25-V30)
# Aggregate features
# Total rainfall: prcp is mm/day over 10 days, so total mm in interval is prcp * 10
prcp_cols_pre = [f'prcp_V{i}' for i in range(1, 7)]
prcp_cols_in = [f'prcp_V{i}' for i in range(7, 25)]
prcp_cols_late = [f'prcp_V{i}' for i in range(25, 31)]

df['tot_prcp_pre'] = df[prcp_cols_pre].sum(axis=1) * 10
df['tot_prcp_in'] = df[prcp_cols_in].sum(axis=1) * 10
df['tot_prcp_late'] = df[prcp_cols_late].sum(axis=1) * 10
df['tot_prcp_season'] = df['tot_prcp_in'] + df['tot_prcp_late']

# Average temps, radiation, vp
for w in ['srad', 'tmax', 'tmin', 'vp']:
    df[f'avg_{w}_pre'] = df[[f'{w}_V{i}' for i in range(1, 7)]].mean(axis=1)
    df[f'avg_{w}_in'] = df[[f'{w}_V{i}' for i in range(7, 25)]].mean(axis=1)
    df[f'avg_{w}_late'] = df[[f'{w}_V{i}' for i in range(25, 31)]].mean(axis=1)

agg_features = ['tot_prcp_pre', 'tot_prcp_in', 'tot_prcp_late', 'tot_prcp_season',
                'avg_srad_pre', 'avg_srad_in', 'avg_srad_late',
                'avg_tmax_pre', 'avg_tmax_in', 'avg_tmax_late',
                'avg_tmin_pre', 'avg_tmin_in', 'avg_tmin_late',
                'avg_vp_pre', 'avg_vp_in', 'avg_vp_late']

agg_summary = []
for feat in agg_features:
    s = df[feat]
    pr, pp = stats.pearsonr(s, df[target])
    sr, sp = stats.spearmanr(s, df[target])
    
    # By system
    sr_hyb, _ = stats.spearmanr(df.loc[df['System']=='Hybrid', feat], df.loc[df['System']=='Hybrid', target])
    sr_land, _ = stats.spearmanr(df.loc[df['System']=='Landrace', feat], df.loc[df['System']=='Landrace', target])
    
    agg_summary.append({
        'feature': feat,
        'mean': float(s.mean()),
        'std': float(s.std()),
        'median': float(s.median()),
        'q1': float(s.quantile(0.25)),
        'q3': float(s.quantile(0.75)),
        'min': float(s.min()),
        'max': float(s.max()),
        'pearson_r': float(pr),
        'spearman_rho': float(sr),
        'spearman_p': float(sp),
        'hybrid_spearman_rho': float(sr_hyb),
        'landrace_spearman_rho': float(sr_land)
    })
results['aggregate_periods_summary'] = agg_summary

# 5. Incremental explanatory power: Linear Regression R2 of V1-V6 vs V7-V24
from sklearn.linear_model import LinearRegression

# Only V1-V6 (30 features)
X_v1_v6 = df[[f'{w}_V{i}' for w in weather_types for i in range(1, 7)]]
reg_pre = LinearRegression().fit(X_v1_v6, df[target])
r2_pre = float(reg_pre.score(X_v1_v6, df[target]))

# Only V7-V24 (90 features)
X_v7_v24 = df[[f'{w}_V{i}' for w in weather_types for i in range(7, 25)]]
reg_in = LinearRegression().fit(X_v7_v24, df[target])
r2_in = float(reg_in.score(X_v7_v24, df[target]))

# Full V1-V30 (150 features)
X_full = df[[f'{w}_V{i}' for w in weather_types for i in range(1, 31)]]
reg_full = LinearRegression().fit(X_full, df[target])
r2_full = float(reg_full.score(X_full, df[target]))

# Top 5 single weather features by absolute Spearman rho
all_weather_corrs = []
for w in weather_types:
    for i in range(1, 31):
        col = f'{w}_V{i}'
        sr, sp = stats.spearmanr(df[col], df[target])
        pr, pp = stats.pearsonr(df[col], df[target])
        all_weather_corrs.append({
            'variable': col,
            'weather_type': w,
            'interval': f'V{i}',
            'period': 'Pre-planting (V1-V6)' if i <= 6 else ('In-season (V7-V24)' if i <= 24 else 'Late (V25-V30)'),
            'spearman_rho': float(sr),
            'abs_spearman': float(abs(sr)),
            'pearson_r': float(pr)
        })

top_corrs = sorted(all_weather_corrs, key=lambda x: x['abs_spearman'], reverse=True)

results['modeling_context'] = {
    'r2_pre_planting_v1_v6': r2_pre,
    'r2_in_season_v7_v24': r2_in,
    'r2_full_weather_v1_v30': r2_full,
    'top_15_correlations': top_corrs[:15]
}

with open(r'C:\SKRIPSI\03_Exploration\Dataset_03_Chiapas\Output\eda_03_weather_stats_summary.json', 'w') as f:
    json.dump(results, f, indent=2)

print('Weather stats calculation complete! Saved to eda_03_weather_stats_summary.json')
