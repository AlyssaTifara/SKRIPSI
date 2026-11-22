import pandas as pd
import numpy as np
from scipy import stats
import json

df = pd.read_csv(r'C:\SKRIPSI\02_Raw_Data\Dataset_03_Chiapas\Chiapas_Data.csv')

num_cols = ['Nitrogen', 'Phosphorus', 'Potassium', 'Planting', 'Clay', 'CEC', 'SOM', 'PH', 'Elev', 'Slope']
cat_cols = ['System', 'Tillage']
target = 'YIELD'

results = {}

# 1. Detailed Univariate Numerical
univariate_num = []
percentiles = [1, 5, 10, 25, 50, 75, 90, 95, 99]

for c in num_cols:
    s = df[c]
    p_vals = np.percentile(s, percentiles)
    p_dict = {f'P{p}': float(v) for p, v in zip(percentiles, p_vals)}
    
    q1 = float(s.quantile(0.25))
    q3 = float(s.quantile(0.75))
    iqr = q3 - q1
    mean_val = float(s.mean())
    std_val = float(s.std())
    cv = (std_val / mean_val * 100) if mean_val != 0 else np.nan
    
    univariate_num.append({
        'Feature': c,
        'N': int(len(s)),
        'Mean': mean_val,
        'Std': std_val,
        'Variance': float(s.var()),
        'CV_pct': float(cv),
        'Min': float(s.min()),
        'Q1': q1,
        'Median': float(s.median()),
        'Q3': q3,
        'Max': float(s.max()),
        'IQR': float(iqr),
        'Range': float(s.max() - s.min()),
        'Skewness': float(s.skew()),
        'Kurtosis': float(s.kurt()),
        'Zeros_Count': int((s == 0).sum()),
        'Zeros_Pct': float((s == 0).sum() / len(s) * 100),
        'Percentiles': p_dict
    })
results['univariate_numerical'] = univariate_num

# 2. Detailed Univariate Categorical
univariate_cat = {}
for c in cat_cols:
    vc = df[c].value_counts()
    vp = df[c].value_counts(normalize=True) * 100
    univariate_cat[c] = []
    for k in vc.index:
        univariate_cat[c].append({
            'Category': str(k),
            'Count': int(vc[k]),
            'Percentage': float(vp[k])
        })
results['univariate_categorical'] = univariate_cat

# Cross-tabulation System x Tillage
ct = pd.crosstab(df['System'], df['Tillage'], margins=True)
ct_pct = pd.crosstab(df['System'], df['Tillage'], normalize='all') * 100
results['crosstab_system_tillage'] = {
    'counts': ct.to_dict(),
    'percentages': ct_pct.to_dict()
}

# Fertilizer zeros by System
fert_zeros = {}
for fert in ['Nitrogen', 'Phosphorus', 'Potassium']:
    fert_zeros[fert] = {
        'Hybrid_zeros': int(((df['System'] == 'Hybrid') & (df[fert] == 0)).sum()),
        'Hybrid_zeros_pct': float(((df['System'] == 'Hybrid') & (df[fert] == 0)).sum() / (df['System'] == 'Hybrid').sum() * 100),
        'Landrace_zeros': int(((df['System'] == 'Landrace') & (df[fert] == 0)).sum()),
        'Landrace_zeros_pct': float(((df['System'] == 'Landrace') & (df[fert] == 0)).sum() / (df['System'] == 'Landrace').sum() * 100),
    }
results['fertilizer_zeros_by_system'] = fert_zeros

# 3. Bivariate Analysis with YIELD
# 3a. Numerical correlations
bivariate_num = []
for c in num_cols:
    s = df[c]
    y = df[target]
    
    # Global
    p_r, p_p = stats.pearsonr(s, y)
    s_r, s_p = stats.spearmanr(s, y)
    
    # By System
    hyb_mask = df['System'] == 'Hybrid'
    land_mask = df['System'] == 'Landrace'
    
    p_r_hyb, p_p_hyb = stats.pearsonr(df.loc[hyb_mask, c], df.loc[hyb_mask, target])
    s_r_hyb, s_p_hyb = stats.spearmanr(df.loc[hyb_mask, c], df.loc[hyb_mask, target])
    
    p_r_land, p_p_land = stats.pearsonr(df.loc[land_mask, c], df.loc[land_mask, target])
    s_r_land, s_p_land = stats.spearmanr(df.loc[land_mask, c], df.loc[land_mask, target])
    
    # Polynomial Fit (Degree 1 vs 2)
    p1 = np.polyfit(s, y, 1)
    p2 = np.polyfit(s, y, 2)
    y_pred1 = np.polyval(p1, s)
    y_pred2 = np.polyval(p2, s)
    r2_deg1 = 1 - np.sum((y - y_pred1)**2) / np.sum((y - y.mean())**2)
    r2_deg2 = 1 - np.sum((y - y_pred2)**2) / np.sum((y - y.mean())**2)
    
    bivariate_num.append({
        'Feature': c,
        'Pearson_r': float(p_r),
        'Pearson_p': float(p_p),
        'Spearman_rho': float(s_r),
        'Spearman_p': float(s_p),
        'Hybrid_Pearson_r': float(p_r_hyb),
        'Hybrid_Spearman_rho': float(s_r_hyb),
        'Landrace_Pearson_r': float(p_r_land),
        'Landrace_Spearman_rho': float(s_r_land),
        'R2_linear': float(r2_deg1),
        'R2_quadratic': float(r2_deg2),
        'R2_delta': float(r2_deg2 - r2_deg1),
        'Quad_coef_a': float(p2[0]),
        'Quad_coef_b': float(p2[1]),
        'Quad_coef_c': float(p2[2])
    })
results['bivariate_numerical'] = bivariate_num

# 3b. Categorical group comparisons
bivariate_cat = {}
# System
hyb_y = df.loc[df['System'] == 'Hybrid', target]
land_y = df.loc[df['System'] == 'Landrace', target]
t_stat, t_pval = stats.ttest_ind(hyb_y, land_y, equal_var=False)
u_stat, u_pval = stats.mannwhitneyu(hyb_y, land_y)

bivariate_cat['System'] = {
    'Hybrid': {
        'N': int(len(hyb_y)),
        'Mean': float(hyb_y.mean()),
        'Std': float(hyb_y.std()),
        'Median': float(hyb_y.median()),
        'Q1': float(hyb_y.quantile(0.25)),
        'Q3': float(hyb_y.quantile(0.75)),
        'IQR': float(hyb_y.quantile(0.75) - hyb_y.quantile(0.25)),
        'Min': float(hyb_y.min()),
        'Max': float(hyb_y.max())
    },
    'Landrace': {
        'N': int(len(land_y)),
        'Mean': float(land_y.mean()),
        'Std': float(land_y.std()),
        'Median': float(land_y.median()),
        'Q1': float(land_y.quantile(0.25)),
        'Q3': float(land_y.quantile(0.75)),
        'IQR': float(land_y.quantile(0.75) - land_y.quantile(0.25)),
        'Min': float(land_y.min()),
        'Max': float(land_y.max())
    },
    'Welch_t': float(t_stat),
    'Welch_p': float(t_pval),
    'MannWhitney_U': float(u_stat),
    'MannWhitney_p': float(u_pval)
}

# Tillage
till_groups = {}
groups_list = []
for t_val in df['Tillage'].unique():
    subset = df.loc[df['Tillage'] == t_val, target]
    groups_list.append(subset)
    till_groups[str(t_val)] = {
        'N': int(len(subset)),
        'Mean': float(subset.mean()),
        'Std': float(subset.std()),
        'Median': float(subset.median()),
        'Q1': float(subset.quantile(0.25)),
        'Q3': float(subset.quantile(0.75)),
        'IQR': float(subset.quantile(0.75) - subset.quantile(0.25)),
        'Min': float(subset.min()),
        'Max': float(subset.max())
    }

f_stat, f_pval = stats.f_oneway(*groups_list)
kw_stat, kw_pval = stats.kruskal(*groups_list)

bivariate_cat['Tillage'] = {
    'groups': till_groups,
    'ANOVA_F': float(f_stat),
    'ANOVA_p': float(f_pval),
    'Kruskal_H': float(kw_stat),
    'Kruskal_p': float(kw_pval)
}

# Tillage stratified by System
till_by_sys = {}
for s_val in ['Hybrid', 'Landrace']:
    till_by_sys[s_val] = {}
    sub_df = df[df['System'] == s_val]
    sub_groups = []
    for t_val in sorted(sub_df['Tillage'].unique()):
        t_sub = sub_df.loc[sub_df['Tillage'] == t_val, target]
        sub_groups.append(t_sub)
        till_by_sys[s_val][str(t_val)] = {
            'N': int(len(t_sub)),
            'Mean': float(t_sub.mean()),
            'Std': float(t_sub.std()),
            'Median': float(t_sub.median()),
            'IQR': float(t_sub.quantile(0.75) - t_sub.quantile(0.25))
        }
    f_sub, p_sub = stats.f_oneway(*sub_groups)
    h_sub, kh_sub = stats.kruskal(*sub_groups)
    till_by_sys[s_val]['ANOVA_F'] = float(f_sub)
    till_by_sys[s_val]['ANOVA_p'] = float(p_sub)
    till_by_sys[s_val]['Kruskal_H'] = float(h_sub)
    till_by_sys[s_val]['Kruskal_p'] = float(kh_sub)
bivariate_cat['Tillage_by_System'] = till_by_sys

results['bivariate_categorical'] = bivariate_cat

# 4. Multicollinearity Analysis
# Pearson correlation matrix
corr_p = df[num_cols].corr(method='pearson')
# Spearman correlation matrix
corr_s = df[num_cols].corr(method='spearman')

results['corr_pearson'] = {col: corr_p[col].to_dict() for col in num_cols}
results['corr_spearman'] = {col: corr_s[col].to_dict() for col in num_cols}

# VIF calculation using correlation matrix inverse
# VIF_j = (R^-1)_jj
inv_r = np.linalg.inv(corr_p.values)
vif_dict = {col: float(inv_r[i, i]) for i, col in enumerate(num_cols)}
results['vif'] = vif_dict

# Save results to json for detailed reporting
with open(r'C:\SKRIPSI\03_Exploration\Dataset_03_Chiapas\Output\eda_02_stats_summary.json', 'w') as f:
    json.dump(results, f, indent=2)

print('Detailed stats computation completed and saved to eda_02_stats_summary.json!')
