import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set global aesthetics
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 11
plt.rcParams['axes.titleweight'] = 'bold'
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9
plt.rcParams['legend.fontsize'] = 9
plt.rcParams['figure.titlesize'] = 13
plt.rcParams['figure.titleweight'] = 'bold'

csv_path = r'C:\SKRIPSI\02_Raw_Data\Dataset_03_Chiapas\Chiapas_Data.csv'
out_dir = r'C:\SKRIPSI\03_Exploration\Dataset_03_Chiapas\Output'
os.makedirs(out_dir, exist_ok=True)

df = pd.read_csv(csv_path)

# Color palettes
c_primary = '#023047'
c_secondary = '#219ebc'
c_light = '#8ecae6'
c_accent = '#fb8500'
c_red = '#d90429'
c_green = '#2a9d8f'
c_gray = '#6c757d'

palette_system = {'Hybrid': '#023047', 'Landrace': '#e76f51'}
palette_tillage = {'Conventional': '#2a9d8f', 'Reduced': '#e9c46a', 'No-till': '#f4a261'}

# ==============================================================================
# GAMBAR 1: Distribusi Univariat Fitur Agronomi (N, P, K, Planting, System, Tillage)
# ==============================================================================
fig = plt.figure(figsize=(15, 12), dpi=300)
gs = fig.add_gridspec(3, 4, hspace=0.35, wspace=0.3)

# 1. Nitrogen (Hist + Box)
ax_n_box = fig.add_subplot(gs[0, 0])
ax_n_hist = fig.add_subplot(gs[1, 0])
sns.boxplot(x=df['Nitrogen'], ax=ax_n_box, color=c_light, flierprops={'marker': 'o', 'markersize': 3, 'alpha': 0.5})
ax_n_box.axvline(df['Nitrogen'].mean(), color=c_red, linestyle='--', linewidth=1.5, label=f"Mean: {df['Nitrogen'].mean():.1f}")
ax_n_box.axvline(df['Nitrogen'].median(), color=c_primary, linestyle='-', linewidth=1.8, label=f"Median: {df['Nitrogen'].median():.1f}")
ax_n_box.set_title('(A1) Nitrogen (kg N ha⁻¹)')
ax_n_box.set_xlabel('')
ax_n_box.legend(loc='upper right', fontsize=8)

sns.histplot(df['Nitrogen'], ax=ax_n_hist, kde=True, color=c_secondary, bins=30, edgecolor='white')
ax_n_hist.set_xlabel('Nitrogen (kg N ha⁻¹)')
ax_n_hist.set_ylabel('Frekuensi')
ax_n_hist.text(0.95, 0.85, f"N=4.585\nZero: 218 (4.8%)\nIQR: 92.0\nSkew: +0.25", 
               transform=ax_n_hist.transAxes, ha='right', va='top', fontsize=8,
               bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

# 2. Phosphorus (Hist + Box)
ax_p_box = fig.add_subplot(gs[0, 1])
ax_p_hist = fig.add_subplot(gs[1, 1])
sns.boxplot(x=df['Phosphorus'], ax=ax_p_box, color='#a8dadc', flierprops={'marker': 'o', 'markersize': 3, 'alpha': 0.5})
ax_p_box.axvline(df['Phosphorus'].mean(), color=c_red, linestyle='--', linewidth=1.5, label=f"Mean: {df['Phosphorus'].mean():.1f}")
ax_p_box.axvline(df['Phosphorus'].median(), color=c_primary, linestyle='-', linewidth=1.8, label=f"Median: {df['Phosphorus'].median():.1f}")
ax_p_box.set_title('(A2) Phosphorus (kg P₂O₅ ha⁻¹)')
ax_p_box.set_xlabel('')
ax_p_box.legend(loc='upper right', fontsize=8)

sns.histplot(df['Phosphorus'], ax=ax_p_hist, kde=True, color='#457b9d', bins=30, edgecolor='white')
ax_p_hist.set_xlabel('Phosphorus (kg P₂O₅ ha⁻¹)')
ax_p_hist.set_ylabel('')
ax_p_hist.text(0.95, 0.85, f"N=4.585\nZero: 1.882 (41.0%)\nIQR: 46.0\nSkew: +0.93", 
               transform=ax_p_hist.transAxes, ha='right', va='top', fontsize=8,
               bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

# 3. Potassium (Hist + Box)
ax_k_box = fig.add_subplot(gs[0, 2])
ax_k_hist = fig.add_subplot(gs[1, 2])
sns.boxplot(x=df['Potassium'], ax=ax_k_box, color='#d8e2dc', flierprops={'marker': 'o', 'markersize': 3, 'alpha': 0.5})
ax_k_box.axvline(df['Potassium'].mean(), color=c_red, linestyle='--', linewidth=1.5, label=f"Mean: {df['Potassium'].mean():.1f}")
ax_k_box.axvline(df['Potassium'].median(), color=c_primary, linestyle='-', linewidth=1.8, label=f"Median: {df['Potassium'].median():.1f}")
ax_k_box.set_title('(A3) Potassium (kg K₂O ha⁻¹)')
ax_k_box.set_xlabel('')
ax_k_box.legend(loc='upper right', fontsize=8)

sns.histplot(df['Potassium'], ax=ax_k_hist, kde=True, color='#2a9d8f', bins=30, edgecolor='white')
ax_k_hist.set_xlabel('Potassium (kg K₂O ha⁻¹)')
ax_k_hist.set_ylabel('')
ax_k_hist.text(0.95, 0.85, f"N=4.585\nZero: 3.025 (66.0%)\nIQR: 12.5\nSkew: +1.98", 
               transform=ax_k_hist.transAxes, ha='right', va='top', fontsize=8,
               bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

# 4. Planting DOY (Hist + Box)
ax_pl_box = fig.add_subplot(gs[0, 3])
ax_pl_hist = fig.add_subplot(gs[1, 3])
sns.boxplot(x=df['Planting'], ax=ax_pl_box, color='#ffe5d9', flierprops={'marker': 'o', 'markersize': 3, 'alpha': 0.5})
ax_pl_box.axvline(df['Planting'].mean(), color=c_red, linestyle='--', linewidth=1.5, label=f"Mean: {df['Planting'].mean():.1f}")
ax_pl_box.axvline(df['Planting'].median(), color=c_primary, linestyle='-', linewidth=1.8, label=f"Median: {df['Planting'].median():.1f}")
ax_pl_box.set_title('(A4) Planting (Day of Year / DOY)')
ax_pl_box.set_xlabel('')
ax_pl_box.legend(loc='upper right', fontsize=8)

sns.histplot(df['Planting'], ax=ax_pl_hist, kde=True, color='#f4a261', bins=30, edgecolor='white')
ax_pl_hist.set_xlabel('Planting Day of Year (DOY)')
ax_pl_hist.set_ylabel('')
ax_pl_hist.text(0.95, 0.85, f"N=4.585\nRange: 91-242\nIQR: 27.0\nSkew: -0.43", 
               transform=ax_pl_hist.transAxes, ha='right', va='top', fontsize=8,
               bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

# 5. System (Bar chart)
ax_sys = fig.add_subplot(gs[2, 0:2])
sys_counts = df['System'].value_counts()
sys_bars = ax_sys.bar(sys_counts.index, sys_counts.values, color=['#023047', '#e76f51'], width=0.55, edgecolor='black', linewidth=1)
ax_sys.set_title('(B1) Komposisi Sistem Budidaya (System)')
ax_sys.set_ylabel('Jumlah Petak (Observasi)')
for bar in sys_bars:
    yval = bar.get_height()
    pct = yval / len(df) * 100
    ax_sys.text(bar.get_x() + bar.get_width()/2, yval + 50, f"{yval:,} petak\n({pct:.2f}%)", ha='center', va='bottom', fontweight='bold', fontsize=9)
ax_sys.set_ylim(0, 3600)

# 6. Tillage (Bar chart)
ax_til = fig.add_subplot(gs[2, 2:4])
til_counts = df['Tillage'].value_counts()
til_bars = ax_til.bar(til_counts.index, til_counts.values, color=['#2a9d8f', '#f4a261', '#e9c46a'], width=0.55, edgecolor='black', linewidth=1)
ax_til.set_title('(B2) Komposisi Praktik Olah Tanah (Tillage)')
ax_til.set_ylabel('Jumlah Petak (Observasi)')
for bar in til_bars:
    yval = bar.get_height()
    pct = yval / len(df) * 100
    ax_til.text(bar.get_x() + bar.get_width()/2, yval + 50, f"{yval:,} petak\n({pct:.2f}%)", ha='center', va='bottom', fontweight='bold', fontsize=9)
ax_til.set_ylim(0, 2500)

fig.suptitle('Visualisasi Univariat Komprehensif: Fitur-Fitur Agronomi Dataset Chiapas (N = 4.585)', fontsize=14, y=0.98)
plt.savefig(os.path.join(out_dir, 'eda_02_agronomy_univariate.png'), bbox_inches='tight')
plt.close()
print("Saved eda_02_agronomy_univariate.png")

# ==============================================================================
# GAMBAR 2: Distribusi Univariat Fitur Tanah & Topografi
# ==============================================================================
fig, axes = plt.subplots(3, 4, figsize=(16, 11), dpi=300, 
                         gridspec_kw={'height_ratios': [0.25, 0.75, 0.05], 'hspace': 0.35, 'wspace': 0.25})

soil_topo_feats = [
    ('Clay', 'Soil Clay Content (%)', '#2a9d8f', '%'),
    ('CEC', 'Cation Exchange Capacity (cmolc dm⁻³)', '#457b9d', 'cmolc dm⁻³'),
    ('SOM', 'Soil Organic Matter (%)', '#e76f51', '%'),
    ('PH', 'Soil pH', '#9d4edd', 'pH unit'),
    ('Elev', 'Elevation (m dpl)', '#023047', 'm'),
    ('Slope', 'Field Slope (%)', '#f4a261', '%')
]

# Grid layout: 2 rows of features (first row: Clay, CEC, SOM, PH; second row: Elev, Slope + 2 empty/combined)
# Let's organize as a 2x3 grid of subplots, each with boxplot + histplot
plt.close()

fig = plt.figure(figsize=(16, 10), dpi=300)
gs = fig.add_gridspec(4, 3, height_ratios=[0.25, 0.75, 0.25, 0.75], hspace=0.35, wspace=0.25)

feats_config = [
    ('Clay', '(A1) Kandungan Liat Tanah (Clay, %)', '#8ecae6', '#219ebc', 0, 0, 1, 0),
    ('CEC', '(A2) Kapasitas Tukar Kation (CEC, cmolc dm⁻³)', '#a8dadc', '#457b9d', 0, 1, 1, 1),
    ('SOM', '(A3) Bahan Organik Tanah (SOM, %)', '#ffe5d9', '#e76f51', 0, 2, 1, 2),
    ('PH', '(B1) Derajat Keasaman Tanah (Soil pH)', '#e2afff', '#9d4edd', 2, 0, 3, 0),
    ('Elev', '(B2) Elevasi Lahan (Elev, m dpl)', '#d8e2dc', '#023047', 2, 1, 3, 1),
    ('Slope', '(B3) Kemiringan Lahan (Slope, %)', '#ffdfba', '#fb8500', 2, 2, 3, 2),
]

for col_name, title, c_box, c_hist, r_box, c_b, r_hist, c_h in feats_config:
    ax_b = fig.add_subplot(gs[r_box, c_b])
    ax_h = fig.add_subplot(gs[r_hist, c_h])
    
    s = df[col_name]
    mean_v = s.mean()
    med_v = s.median()
    iqr_v = s.quantile(0.75) - s.quantile(0.25)
    skew_v = s.skew()
    
    sns.boxplot(x=s, ax=ax_b, color=c_box, flierprops={'marker': 'o', 'markersize': 3, 'alpha': 0.4})
    ax_b.axvline(mean_v, color=c_red, linestyle='--', linewidth=1.4, label=f"Mean: {mean_v:.2f}")
    ax_b.axvline(med_v, color=c_primary, linestyle='-', linewidth=1.6, label=f"Med: {med_v:.2f}")
    ax_b.set_title(title, fontsize=10)
    ax_b.set_xlabel('')
    ax_b.legend(loc='upper right', fontsize=8)
    
    sns.histplot(s, ax=ax_h, kde=True, color=c_hist, bins=30, edgecolor='white')
    ax_h.set_xlabel(title.split('(')[1].split(')')[0])
    ax_h.set_ylabel('Frekuensi')
    ax_h.text(0.95, 0.85, f"Min: {s.min():.1f} | Max: {s.max():.1f}\nIQR: {iqr_v:.2f} | Skew: {skew_v:+.2f}", 
              transform=ax_h.transAxes, ha='right', va='top', fontsize=8,
              bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

fig.suptitle('Visualisasi Univariat Komprehensif: Fitur Tanah & Topografi Dataset Chiapas (N = 4.585)', fontsize=14, y=0.98)
plt.savefig(os.path.join(out_dir, 'eda_02_soil_topography_univariate.png'), bbox_inches='tight')
plt.close()
print("Saved eda_02_soil_topography_univariate.png")

# ==============================================================================
# GAMBAR 3: Bivariate Scatter Plots Fitur Agronomi vs YIELD (dengan pemisahan System)
# ==============================================================================
fig, axes = plt.subplots(2, 2, figsize=(15, 12), dpi=300)

agronomy_biv = [
    ('Nitrogen', 'Nitrogen Diberikan (kg N ha⁻¹)', axes[0, 0], '(A) Nitrogen vs YIELD'),
    ('Phosphorus', 'Phosphorus Diberikan (kg P₂O₅ ha⁻¹)', axes[0, 1], '(B) Phosphorus vs YIELD'),
    ('Potassium', 'Potassium Diberikan (kg K₂O ha⁻¹)', axes[1, 0], '(C) Potassium vs YIELD'),
    ('Planting', 'Tanggal Tanam (Day of Year / DOY)', axes[1, 1], '(D) Planting DOY vs YIELD')
]

for col_name, xlabel, ax, title in agronomy_biv:
    # Scatter points by system
    sns.scatterplot(data=df, x=col_name, y='YIELD', hue='System', palette=palette_system, 
                    alpha=0.4, s=20, ax=ax, edgecolor='none')
    
    # Regression trend lines overall & by system
    sns.regplot(data=df, x=col_name, y='YIELD', scatter=False, ax=ax, color='#000000', 
                line_kws={'linewidth': 2.2, 'label': 'Tren Global (OLS)'})
    sns.regplot(data=df[df['System']=='Hybrid'], x=col_name, y='YIELD', scatter=False, ax=ax, 
                color='#023047', line_kws={'linewidth': 1.8, 'linestyle': '--', 'label': 'Tren Hybrid'})
    sns.regplot(data=df[df['System']=='Landrace'], x=col_name, y='YIELD', scatter=False, ax=ax, 
                color='#e76f51', line_kws={'linewidth': 1.8, 'linestyle': ':', 'label': 'Tren Landrace'})
    
    # Correlations
    p_r = df[col_name].corr(df['YIELD'])
    s_r = df[col_name].corr(df['YIELD'], method='spearman')
    s_r_hyb = df.loc[df['System']=='Hybrid', col_name].corr(df.loc[df['System']=='Hybrid', 'YIELD'], method='spearman')
    s_r_lan = df.loc[df['System']=='Landrace', col_name].corr(df.loc[df['System']=='Landrace', 'YIELD'], method='spearman')
    
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel('Produktivitas Jagung YIELD (Mg ha⁻¹)')
    ax.text(0.04, 0.94, f"Global: Pearson r={p_r:+.3f}, Spearman ρ={s_r:+.3f}\nHybrid: Spearman ρ={s_r_hyb:+.3f} | Landrace: Spearman ρ={s_r_lan:+.3f}", 
            transform=ax.transAxes, ha='left', va='top', fontsize=8.5,
            bbox=dict(boxstyle='round,pad=0.35', facecolor='white', alpha=0.9, edgecolor='gray'))
    ax.legend(loc='lower right', fontsize=8)

fig.suptitle('Analisis Bivariat Fitur Agronomi vs Produktivitas Jagung (YIELD)', fontsize=14, y=0.98)
plt.savefig(os.path.join(out_dir, 'eda_02_agronomy_vs_yield_bivariate.png'), bbox_inches='tight')
plt.close()
print("Saved eda_02_agronomy_vs_yield_bivariate.png")

# ==============================================================================
# GAMBAR 4: Bivariate Scatter Plots Fitur Tanah & Topografi vs YIELD
# ==============================================================================
fig, axes = plt.subplots(3, 2, figsize=(15, 16), dpi=300)

soil_topo_biv = [
    ('Elev', 'Elevasi Lahan (m dpl)', axes[0, 0], '(A) Elevasi (Elev) vs YIELD'),
    ('Slope', 'Kemiringan Lahan (Slope, %)', axes[0, 1], '(B) Kelerengan (Slope) vs YIELD'),
    ('Clay', 'Kandungan Liat (Clay, %)', axes[1, 0], '(C) Kandungan Liat (Clay) vs YIELD'),
    ('CEC', 'Kapasitas Tukar Kation (CEC, cmolc dm⁻³)', axes[1, 1], '(D) KTK Tanah (CEC) vs YIELD'),
    ('SOM', 'Bahan Organik Tanah (SOM, %)', axes[2, 0], '(E) Bahan Organik (SOM) vs YIELD'),
    ('PH', 'Derajat Keasaman Tanah (Soil pH)', axes[2, 1], '(F) Derajat Keasaman (pH) vs YIELD')
]

for col_name, xlabel, ax, title in soil_topo_biv:
    sns.scatterplot(data=df, x=col_name, y='YIELD', hue='System', palette=palette_system, 
                    alpha=0.4, s=20, ax=ax, edgecolor='none')
    
    # Regression trend lines overall & by system
    sns.regplot(data=df, x=col_name, y='YIELD', scatter=False, ax=ax, color='#000000', 
                line_kws={'linewidth': 2.2, 'label': 'Tren Global (OLS)'})
    sns.regplot(data=df[df['System']=='Hybrid'], x=col_name, y='YIELD', scatter=False, ax=ax, 
                color='#023047', line_kws={'linewidth': 1.8, 'linestyle': '--', 'label': 'Tren Hybrid'})
    sns.regplot(data=df[df['System']=='Landrace'], x=col_name, y='YIELD', scatter=False, ax=ax, 
                color='#e76f51', line_kws={'linewidth': 1.8, 'linestyle': ':', 'label': 'Tren Landrace'})
    
    p_r = df[col_name].corr(df['YIELD'])
    s_r = df[col_name].corr(df['YIELD'], method='spearman')
    s_r_hyb = df.loc[df['System']=='Hybrid', col_name].corr(df.loc[df['System']=='Hybrid', 'YIELD'], method='spearman')
    s_r_lan = df.loc[df['System']=='Landrace', col_name].corr(df.loc[df['System']=='Landrace', 'YIELD'], method='spearman')
    
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel('Produktivitas Jagung YIELD (Mg ha⁻¹)')
    ax.text(0.04, 0.94, f"Global: Pearson r={p_r:+.3f}, Spearman ρ={s_r:+.3f}\nHybrid: Spearman ρ={s_r_hyb:+.3f} | Landrace: Spearman ρ={s_r_lan:+.3f}", 
            transform=ax.transAxes, ha='left', va='top', fontsize=8.5,
            bbox=dict(boxstyle='round,pad=0.35', facecolor='white', alpha=0.9, edgecolor='gray'))
    ax.legend(loc='lower right', fontsize=8)

fig.suptitle('Analisis Bivariat Fitur Tanah & Topografi vs Produktivitas Jagung (YIELD)', fontsize=14, y=0.98)
plt.savefig(os.path.join(out_dir, 'eda_02_soil_topography_vs_yield_bivariate.png'), bbox_inches='tight')
plt.close()
print("Saved eda_02_soil_topography_vs_yield_bivariate.png")

# ==============================================================================
# GAMBAR 5: Perbandingan Antarkelompok Kategorikal (System, Tillage, Interaksi)
# ==============================================================================
fig, axes = plt.subplots(2, 2, figsize=(15, 12), dpi=300)

# Panel A: System Violin + Box
ax_sys = axes[0, 0]
sns.violinplot(data=df, x='System', y='YIELD', hue='System', palette=palette_system, ax=ax_sys, inner='quartile', alpha=0.8, legend=False)
sns.boxplot(data=df, x='System', y='YIELD', ax=ax_sys, width=0.18, color='white', flierprops={'marker': 'o', 'markersize': 2, 'alpha': 0.3})
ax_sys.set_title('(A) Distribusi YIELD Berdasarkan Sistem Budidaya (System)')
ax_sys.set_xlabel('Sistem Budidaya')
ax_sys.set_ylabel('Produktivitas Jagung YIELD (Mg ha⁻¹)')
ax_sys.text(0.04, 0.92, f"Hybrid: Mean=4.45, Med=4.60, IQR=2.00\nLandrace: Mean=1.92, Med=1.65, IQR=1.30\nWelch t = 64.45 (p < 0.001)\nMann-Whitney U = 4.21M (p < 0.001)",
            transform=ax_sys.transAxes, ha='left', va='top', fontsize=8.5,
            bbox=dict(boxstyle='round,pad=0.35', facecolor='white', alpha=0.9, edgecolor='gray'))

# Panel B: Tillage Violin + Box
ax_til = axes[0, 1]
sns.violinplot(data=df, x='Tillage', y='YIELD', hue='Tillage', palette=palette_tillage, ax=ax_til, inner='quartile', alpha=0.8, legend=False)
sns.boxplot(data=df, x='Tillage', y='YIELD', ax=ax_til, width=0.18, color='white', flierprops={'marker': 'o', 'markersize': 2, 'alpha': 0.3})
ax_til.set_title('(B) Distribusi YIELD Berdasarkan Olah Tanah Global (Tillage)')
ax_til.set_xlabel('Praktik Olah Tanah')
ax_til.set_ylabel('Produktivitas Jagung YIELD (Mg ha⁻¹)')
ax_til.text(0.04, 0.92, f"Conv: Mean=3.50, Med=3.50, IQR=3.40\nReduced: Mean=3.71, Med=4.00, IQR=3.00\nNo-till: Mean=3.65, Med=3.50, IQR=2.80\nANOVA F = 5.01 (p = 0.0067)\nKruskal H = 8.68 (p = 0.0130)",
            transform=ax_til.transAxes, ha='left', va='top', fontsize=8.5,
            bbox=dict(boxstyle='round,pad=0.35', facecolor='white', alpha=0.9, edgecolor='gray'))

# Panel C: Interaksi System x Tillage
ax_int = axes[1, 0]
sns.boxplot(data=df, x='System', y='YIELD', hue='Tillage', palette=palette_tillage, ax=ax_int, 
            boxprops=dict(alpha=0.85), flierprops={'marker': 'o', 'markersize': 3, 'alpha': 0.4})
ax_int.set_title('(C) Interaksi Sistem Budidaya × Olah Tanah (System × Tillage)')
ax_int.set_xlabel('Sistem Budidaya')
ax_int.set_ylabel('Produktivitas Jagung YIELD (Mg ha⁻¹)')
ax_int.text(0.04, 0.92, f"Hybrid: Conv(4.54) > No-till(4.44) > Red(4.26)\nLandrace: No-till(2.15) > Red(1.91) > Conv(1.77)\n*Perhatikan keunggulan No-till pada Landrace*",
            transform=ax_int.transAxes, ha='left', va='top', fontsize=8.5,
            bbox=dict(boxstyle='round,pad=0.35', facecolor='white', alpha=0.9, edgecolor='gray'))
ax_int.legend(loc='lower right', title='Tillage', fontsize=8.5)

# Panel D: Proporsi Petak Tanpa Pupuk (Zero Fertilizer) per Sistem
ax_fert = axes[1, 1]
fert_zero_df = pd.DataFrame({
    'Nutrient': ['Nitrogen', 'Phosphorus', 'Potassium'],
    'Hybrid': [1.91, 31.58, 56.95],
    'Landrace': [10.32, 59.57, 83.62]
})
x = np.arange(len(fert_zero_df))
width = 0.35

rects1 = ax_fert.bar(x - width/2, fert_zero_df['Hybrid'], width, label='Hybrid', color='#023047', edgecolor='black')
rects2 = ax_fert.bar(x + width/2, fert_zero_df['Landrace'], width, label='Landrace', color='#e76f51', edgecolor='black')

ax_fert.set_title('(D) Proporsi Petak Tanpa Pupuk Sama Sekali (Zero Fertilizer, 0 kg ha⁻¹)')
ax_fert.set_xlabel('Jenis Unsur Hara Pupuk')
ax_fert.set_ylabel('Persentase Petak Nol Pupuk (%)')
ax_fert.set_xticks(x)
ax_fert.set_xticklabels(['Nitrogen\n(N)', 'Phosphorus\n(P₂O₅)', 'Potassium\n(K₂O)'])
ax_fert.set_ylim(0, 100)
ax_fert.legend(loc='upper left', fontsize=8.5)

for rect in rects1:
    h = rect.get_height()
    ax_fert.annotate(f"{h:.1f}%", (rect.get_x() + rect.get_width()/2., h + 1.5),
                     ha='center', va='bottom', fontsize=8, fontweight='bold', color='#023047')
for rect in rects2:
    h = rect.get_height()
    ax_fert.annotate(f"{h:.1f}%", (rect.get_x() + rect.get_width()/2., h + 1.5),
                     ha='center', va='bottom', fontsize=8, fontweight='bold', color='#e76f51')

fig.suptitle('Evaluasi Perbedaan Antarkelompok dan Interaksi Faktor Budidaya terhadap YIELD', fontsize=14, y=0.98)
plt.savefig(os.path.join(out_dir, 'eda_02_categorical_yield_comparisons.png'), bbox_inches='tight')
plt.close()
print("Saved eda_02_categorical_yield_comparisons.png")

# ==============================================================================
# GAMBAR 6: Multikolinearitas (Heatmap Korelasi Pearson/Spearman & VIF)
# ==============================================================================
fig = plt.figure(figsize=(16, 12), dpi=300)
gs = fig.add_gridspec(2, 2, width_ratios=[1.1, 0.9], hspace=0.3, wspace=0.25)

num_cols = ['Nitrogen', 'Phosphorus', 'Potassium', 'Planting', 'Clay', 'CEC', 'SOM', 'PH', 'Elev', 'Slope']
corr_s = df[num_cols].corr(method='spearman')
corr_p = df[num_cols].corr(method='pearson')

# Panel A: Spearman Heatmap
ax_sp = fig.add_subplot(gs[0, 0])
mask = np.triu(np.ones_like(corr_s, dtype=bool))
sns.heatmap(corr_s, mask=mask, annot=True, fmt='.2f', cmap='coolwarm', vmin=-0.7, vmax=0.7, 
            ax=ax_sp, cbar_kws={'label': 'Koefisien Korelasi Rank Spearman (ρ)'}, square=True,
            annot_kws={'size': 8.5})
ax_sp.set_title('(A) Matriks Korelasi Rank Spearman Antar-Fitur Numerik')

# Panel B: Pearson Heatmap
ax_pe = fig.add_subplot(gs[1, 0])
mask_p = np.triu(np.ones_like(corr_p, dtype=bool))
sns.heatmap(corr_p, mask=mask_p, annot=True, fmt='.2f', cmap='coolwarm', vmin=-0.7, vmax=0.7, 
            ax=ax_pe, cbar_kws={'label': 'Koefisien Korelasi Linear Pearson (r)'}, square=True,
            annot_kws={'size': 8.5})
ax_pe.set_title('(B) Matriks Korelasi Linear Pearson Antar-Fitur Numerik')

# Panel C: Bar Chart VIF
ax_vif = fig.add_subplot(gs[:, 1])
inv_r = np.linalg.inv(corr_p.values)
vif_series = pd.Series([inv_r[i, i] for i in range(len(num_cols))], index=num_cols).sort_values(ascending=True)

vif_colors = ['#2a9d8f' if x < 2.5 else ('#e9c46a' if x < 5.0 else '#e76f51') for x in vif_series.values]
bars = ax_vif.barh(vif_series.index, vif_series.values, color=vif_colors, edgecolor='black', linewidth=0.8, height=0.6)
ax_vif.axvline(5.0, color='#e76f51', linestyle='--', linewidth=1.8, label='Ambang Waspada Konservatif (VIF = 5.0)')
ax_vif.axvline(10.0, color='#d90429', linestyle=':', linewidth=1.8, label='Batas Kritis Multikolinearitas (VIF = 10.0)')

ax_vif.set_title('(C) Variance Inflation Factor (VIF) Fitur Numerik')
ax_vif.set_xlabel('Nilai VIF')
ax_vif.set_xlim(0, 11)
ax_vif.legend(loc='lower right', fontsize=8.5)

for bar in bars:
    w = bar.get_width()
    ax_vif.text(w + 0.15, bar.get_y() + bar.get_height()/2, f"{w:.2f}", va='center', ha='left', fontweight='bold', fontsize=9)

ax_vif.text(0.5, 0.25, 
            "Temuan Diagnostik VIF:\n"
            "• Semua fitur memiliki VIF < 4.0\n"
            "• VIF tertinggi: CEC (3.64) & Clay (2.50)\n"
            "  karena korelasi alami geokimia tanah\n"
            "• Tidak ada multikolinearitas collinear\n"
            "  parah yang menghambat estimasi model",
            transform=ax_vif.transAxes, ha='left', va='center', fontsize=9,
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8f9fa', edgecolor='gray', alpha=0.95))

fig.suptitle('Pemeriksaan Diagnostik Multikolinearitas Antar-Fitur Numerik Prediktor', fontsize=14, y=0.98)
plt.savefig(os.path.join(out_dir, 'eda_02_multicollinearity_and_vif.png'), bbox_inches='tight')
plt.close()
print("Saved eda_02_multicollinearity_and_vif.png")

print("All EDA 02 charts generated successfully!")
