import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set global aesthetics
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['axes.titleweight'] = 'bold'
plt.rcParams['axes.labelsize'] = 11
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['figure.titlesize'] = 14
plt.rcParams['figure.titleweight'] = 'bold'

csv_path = r'C:\SKRIPSI\02_Raw_Data\Dataset_03_Chiapas\Chiapas_Data.csv'
out_dir = r'C:\SKRIPSI\03_Exploration\Dataset_03_Chiapas\Output'
os.makedirs(out_dir, exist_ok=True)

df = pd.read_csv(csv_path)
y = df['YIELD']

mean_val = y.mean()
median_val = y.median()
std_val = y.std()
min_val = y.min()
max_val = y.max()
q1_val = y.quantile(0.25)
q3_val = y.quantile(0.75)
iqr_val = q3_val - q1_val
skew_val = y.skew()
kurt_val = y.kurt()
lf_val = q1_val - 1.5 * iqr_val
uf_val = q3_val + 1.5 * iqr_val

# -------------------------------------------------------------
# Gambar 1: Distribusi Keseluruhan YIELD (Histogram + KDE & Boxplot)
# -------------------------------------------------------------
fig, (ax_box, ax_hist) = plt.subplots(2, 1, figsize=(10, 8), dpi=300, sharex=True, 
                                      gridspec_kw={'height_ratios': [0.25, 0.75]})

# Panel A: Boxplot
sns.boxplot(x=y, ax=ax_box, color='#8ecae6', flierprops={'marker': 'o', 'markersize': 5, 'markerfacecolor': '#d90429', 'markeredgecolor': 'none', 'alpha': 0.7})
ax_box.axvline(mean_val, color='#d90429', linestyle='--', linewidth=1.8, label=f'Mean: {mean_val:.2f} Mg ha⁻¹')
ax_box.axvline(median_val, color='#023047', linestyle='-', linewidth=2.0, label=f'Median: {median_val:.2f} Mg ha⁻¹')
ax_box.axvline(q1_val, color='#219ebc', linestyle=':', linewidth=1.5, label=f'Q1: {q1_val:.2f} Mg ha⁻¹')
ax_box.axvline(q3_val, color='#219ebc', linestyle=':', linewidth=1.5, label=f'Q3: {q3_val:.2f} Mg ha⁻¹')
ax_box.set(xlabel='')
ax_box.set_title('A. Boxplot Distribusi YIELD (Target Variable) dengan Pagar Tukey', pad=10)
ax_box.legend(loc='upper right', frameon=True, facecolor='white', framealpha=0.9, fontsize=9)
ax_box.grid(True, linestyle='--', alpha=0.5)

# Annotate Tukey Upper Fence
ax_box.annotate(f'Upper Fence: {uf_val:.2f}\n(3 Outlier > 9.72)', 
                xy=(uf_val, 0), xytext=(uf_val - 1.8, -0.35),
                arrowprops=dict(arrowstyle='->', color='#d90429', lw=1.2),
                fontsize=8.5, fontweight='bold', color='#d90429',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#ffe3e0', edgecolor='#d90429', alpha=0.9))

# Panel B: Histogram + KDE
sns.histplot(y, kde=True, bins=40, color='#219ebc', edgecolor='white', stat='density', ax=ax_hist, alpha=0.6, label='Empirical Histogram')
ax_hist.axvline(mean_val, color='#d90429', linestyle='--', linewidth=2.0, label=f'Mean ({mean_val:.2f})')
ax_hist.axvline(median_val, color='#023047', linestyle='-', linewidth=2.0, label=f'Median ({median_val:.2f})')
ax_hist.axvline(q1_val, color='#023047', linestyle=':', linewidth=1.5, label=f'Q1 ({q1_val:.2f})')
ax_hist.axvline(q3_val, color='#023047', linestyle=':', linewidth=1.5, label=f'Q3 ({q3_val:.2f})')

# Text annotation for stats
stats_text = (
    f"N = {len(y):,}\n"
    f"Mean = {mean_val:.4f} Mg ha⁻¹\n"
    f"Median = {median_val:.4f} Mg ha⁻¹\n"
    f"Std Dev = {std_val:.4f} Mg ha⁻¹\n"
    f"Min = {min_val:.2f} | Max = {max_val:.2f}\n"
    f"Q1 = {q1_val:.2f} | Q3 = {q3_val:.2f}\n"
    f"IQR = {iqr_val:.2f} Mg ha⁻¹\n"
    f"Skewness = {skew_val:+.4f} (Positif Lemah)\n"
    f"Kurtosis = {kurt_val:+.4f} (Platykurtic)"
)
ax_hist.text(0.03, 0.95, stats_text, transform=ax_hist.transAxes, verticalalignment='top',
             fontsize=9.5, fontfamily='monospace',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8f9fa', edgecolor='#ced4da', alpha=0.95))

ax_hist.set_title('B. Histogram & Estimasi Densitas Kernel (KDE) Produktivitas Jagung (YIELD)', pad=10)
ax_hist.set_xlabel('Field YIELD (Mg ha⁻¹ atau Ton ha⁻¹)')
ax_hist.set_ylabel('Densitas Probabilitas')
ax_hist.set_xlim(-0.5, 10.5)
ax_hist.legend(loc='upper right', frameon=True, facecolor='white', framealpha=0.9, fontsize=9.5)
ax_hist.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
fig.savefig(os.path.join(out_dir, 'eda_01_yield_distribusi_overall.png'), dpi=300)
plt.close()
print('Chart 1 created: eda_01_yield_distribusi_overall.png')

# -------------------------------------------------------------
# Gambar 2: Distribusi YIELD Berdasarkan Sistem Budidaya (Hybrid vs Landrace)
# -------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5), dpi=300)

palette = {'Hybrid': '#1f77b4', 'Landrace': '#e377c2'}

# Panel A: Boxplot + Stripplot
sns.boxplot(data=df, x='System', y='YIELD', palette=palette, width=0.45, ax=ax1,
            boxprops=dict(alpha=0.8), flierprops={'marker': 'o', 'markersize': 4, 'alpha': 0.5})
# Overlay mean markers
means_sys = df.groupby('System')['YIELD'].mean()
medians_sys = df.groupby('System')['YIELD'].median()
for i, sys in enumerate(['Hybrid', 'Landrace']):
    m = means_sys[sys]
    med = medians_sys[sys]
    ax1.scatter(i, m, color='red', marker='D', s=50, zorder=5, label='Mean' if i == 0 else "")
    ax1.annotate(f"Mean: {m:.2f}\nMed: {med:.2f}", xy=(i, med), xytext=(i + 0.25, med - 0.2),
                 fontsize=9, fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='#cccccc', alpha=0.9))

ax1.set_title('A. Boxplot Komparatif YIELD: Hybrid vs Landrace', pad=12)
ax1.set_xlabel('Sistem Budidaya (System)')
ax1.set_ylabel('Field YIELD (Mg ha⁻¹)')
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(loc='upper right', frameon=True, facecolor='white')

# Panel B: Split KDE Density Plot (Demonstrating Bimodality Deconstruction)
sns.kdeplot(data=df, x='YIELD', hue='System', palette=palette, common_norm=False, fill=True, alpha=0.35, linewidth=2, ax=ax2)
ax2.axvline(df[df['System'] == 'Hybrid']['YIELD'].mean(), color='#1f77b4', linestyle='--', linewidth=1.5, label='Hybrid Mean (4.45)')
ax2.axvline(df[df['System'] == 'Landrace']['YIELD'].mean(), color='#e377c2', linestyle='--', linewidth=1.5, label='Landrace Mean (1.92)')
ax2.set_title('B. Dekomposisi Bimodalitas Densitas YIELD per Sistem', pad=12)
ax2.set_xlabel('Field YIELD (Mg ha⁻¹)')
ax2.set_ylabel('Densitas Probabilitas')
ax2.set_xlim(-0.5, 10.5)
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.legend(title='Sistem & Rata-rata', loc='upper right', frameon=True, facecolor='white')

plt.tight_layout()
fig.savefig(os.path.join(out_dir, 'eda_01_yield_by_system.png'), dpi=300)
plt.close()
print('Chart 2 created: eda_01_yield_by_system.png')

# -------------------------------------------------------------
# Gambar 3: Distribusi YIELD Berdasarkan Tahun Tanam (2012–2018)
# -------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 8.5), dpi=300, sharex=True, gridspec_kw={'height_ratios': [0.65, 0.35]})

# Panel A: Boxplot YIELD per Tahun dengan Mean Trend Line
sns.boxplot(data=df, x='Year', y='YIELD', color='#caf0f8', width=0.55, ax=ax1,
            flierprops={'marker': 'o', 'markersize': 3.5, 'alpha': 0.5, 'markerfacecolor': '#0077b6', 'markeredgecolor': 'none'})

# Calculate annual stats
yearly_stats = df.groupby('Year')['YIELD'].agg(['mean', 'median', 'std', 'count']).reset_index()
years = sorted(df['Year'].unique())
x_coords = list(range(len(years)))

# Plot mean line
ax1.plot(x_coords, yearly_stats['mean'], marker='o', markersize=7, color='#d90429', linewidth=2.2, label='Mean YIELD Tahunan', zorder=5)

for i, row in yearly_stats.iterrows():
    ax1.annotate(f"{row['mean']:.2f}", (i, row['mean']), xytext=(i, row['mean'] + 0.35),
                 ha='center', fontsize=9, fontweight='bold', color='#d90429')

ax1.set_title('A. Distribusi YIELD per Tahun Tanam (2012–2018) dan Tren Rata-rata', pad=10)
ax1.set_ylabel('Field YIELD (Mg ha⁻¹)')
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(loc='upper right', frameon=True, facecolor='white')

# Panel B: Komposisi Sistem per Tahun (Stacked Bar)
sys_counts = df.groupby(['Year', 'System']).size().unstack(fill_value=0)
sys_pct = sys_counts.div(sys_counts.sum(axis=1), axis=0) * 100

bar_h = ax2.bar(x_coords, sys_pct['Hybrid'], label='Hybrid (%)', color='#1f77b4', width=0.5, alpha=0.85)
bar_l = ax2.bar(x_coords, sys_pct['Landrace'], bottom=sys_pct['Hybrid'], label='Landrace (%)', color='#e377c2', width=0.5, alpha=0.85)

for i in range(len(years)):
    pct_h = sys_pct.loc[years[i], 'Hybrid']
    pct_l = sys_pct.loc[years[i], 'Landrace']
    tot_obs = sys_counts.loc[years[i]].sum()
    if pct_h > 10:
        ax2.text(i, pct_h / 2, f"{pct_h:.1f}%", ha='center', va='center', color='white', fontweight='bold', fontsize=8.5)
    if pct_l > 10:
        ax2.text(i, pct_h + pct_l / 2, f"{pct_l:.1f}%", ha='center', va='center', color='white', fontweight='bold', fontsize=8.5)
    ax2.text(i, 103, f"N={tot_obs}", ha='center', va='bottom', fontsize=8.5, fontweight='bold', color='#333333')

ax2.set_title('B. Pergeseran Komposisi Sampel (Hybrid vs Landrace) sebagai Confounder Tren Antar-Tahun', pad=10)
ax2.set_xlabel('Tahun Tanam (Year)')
ax2.set_ylabel('Proporsi Sampel (%)')
ax2.set_ylim(0, 120)
ax2.set_xticks(x_coords)
ax2.set_xticklabels(years)
ax2.legend(loc='lower left', ncol=2, frameon=True, facecolor='white')
ax2.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
fig.savefig(os.path.join(out_dir, 'eda_01_yield_by_year.png'), dpi=300)
plt.close()
print('Chart 3 created: eda_01_yield_by_year.png')

# -------------------------------------------------------------
# Gambar 4: Interaksi YIELD: Tahun vs Sistem Budidaya (Grouped Boxplot)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 6), dpi=300)

sns.boxplot(data=df, x='Year', y='YIELD', hue='System', palette=palette, ax=ax, width=0.6,
            flierprops={'marker': 'o', 'markersize': 3.5, 'alpha': 0.4})

# Overlay lines connecting medians for Hybrid and Landrace
med_interaction = df.groupby(['Year', 'System'])['YIELD'].median().unstack()
years_str = [str(yr) for yr in years]

# Calculate positions
pos_hybrid = [i - 0.15 for i in range(len(years))]
pos_landrace = [i + 0.15 for i in range(len(years))]

# Line for Hybrid medians
ax.plot(pos_hybrid, med_interaction['Hybrid'], color='#0d47a1', linestyle='--', marker='s', markersize=6, linewidth=1.5, label='Median Hybrid Tren')
# Line for Landrace medians
ax.plot(pos_landrace, med_interaction['Landrace'], color='#880e4f', linestyle='--', marker='^', markersize=6, linewidth=1.5, label='Median Landrace Tren')

ax.set_title('Distribusi Produktivitas Jagung per Sistem Budidaya Lintas Tahun (2012–2018)', pad=12)
ax.set_xlabel('Tahun Tanam (Year)')
ax.set_ylabel('Field YIELD (Mg ha⁻¹)')
ax.set_ylim(-0.5, 10.5)
ax.legend(title='Sistem Budidaya', frameon=True, facecolor='white', loc='upper right')
ax.grid(True, linestyle='--', alpha=0.5)

# Annotation for 2013 Landrace small sample
ax.annotate('Landrace 2013\nN = 3 petak', xy=(1 + 0.15, 2.4), xytext=(1 + 0.25, 0.8),
            arrowprops=dict(arrowstyle='->', color='#880e4f', lw=1.2),
            fontsize=8.5, fontweight='bold', color='#880e4f',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#fce4ec', edgecolor='#880e4f', alpha=0.9))

plt.tight_layout()
fig.savefig(os.path.join(out_dir, 'eda_01_yield_interaction_year_system.png'), dpi=300)
plt.close()
print('Chart 4 created: eda_01_yield_interaction_year_system.png')

# -------------------------------------------------------------
# Gambar 5: Analisis Profil Outlier YIELD Berdasarkan Konteks Agronomi
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(11, 6), dpi=300)

# Scatter plot of YIELD vs Elevation colored by System, highlighting outliers
sns.scatterplot(data=df, x='Elev', y='YIELD', hue='System', style='System', palette=palette, 
                alpha=0.55, s=35, ax=ax)

# Highlight overall top outliers (> 9.725 Mg ha⁻¹)
top_outliers = df[df['YIELD'] > uf_val]
ax.scatter(top_outliers['Elev'], top_outliers['YIELD'], color='none', edgecolor='#d90429', s=140, linewidth=2.2, label='Tukey Upper Outliers (> 9.72 Mg ha⁻¹)')

# Highlight Hybrid near failure (< 0.5 Mg ha⁻¹)
hybrid_low = df[(df['System'] == 'Hybrid') & (df['YIELD'] < 0.5)]
ax.scatter(hybrid_low['Elev'], hybrid_low['YIELD'], color='none', edgecolor='#ffb703', s=100, linewidth=2.0, label='Hybrid Gagal Panen / Ekstrem Rendah (< 0.50 Mg ha⁻¹)')

# Highlight Landrace superior performers (> 4.45 Mg ha⁻¹)
landrace_high = df[(df['System'] == 'Landrace') & (df['YIELD'] > 4.45)]
ax.scatter(landrace_high['Elev'], landrace_high['YIELD'], color='none', edgecolor='#7209b7', s=80, linewidth=1.5, label='Landrace Unggul Berkinerja Tinggi (> 4.45 Mg ha⁻¹)')

# Annotation of specific extreme points
ax.annotate('Top 3 Hasil Tertinggi (9.80 Mg ha⁻¹)\nDEKALB 390/395/7500 (Elev 580-640m, N > 165 kg/ha)', 
            xy=(600, 9.8), xytext=(850, 9.2),
            arrowprops=dict(arrowstyle='->', color='#d90429', lw=1.2),
            fontsize=8.5, fontweight='bold', color='#d90429',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#ffe3e0', edgecolor='#d90429', alpha=0.9))

ax.annotate('Kegagalan Hybrid Lokal (0.10 - 0.20 Mg ha⁻¹)\nDEKALB 395 (Pupuk NPK Lengkap, Diduga Hama/Kekeringan)', 
            xy=(560, 0.15), xytext=(850, 1.2),
            arrowprops=dict(arrowstyle='->', color='#b25e00', lw=1.2),
            fontsize=8.5, fontweight='bold', color='#b25e00',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#fff3cd', edgecolor='#b25e00', alpha=0.9))

ax.set_title('Identifikasi Outlier YIELD terhadap Elevasi Lahan: Variabilitas Lapangan Riil', pad=12)
ax.set_xlabel('Elevasi Lahan (Elev, meter di atas permukaan laut / m dpl)')
ax.set_ylabel('Field YIELD (Mg ha⁻¹)')
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper right', frameon=True, facecolor='white', fontsize=8.5)

plt.tight_layout()
fig.savefig(os.path.join(out_dir, 'eda_01_yield_outliers_profile.png'), dpi=300)
plt.close()
print('Chart 5 created: eda_01_yield_outliers_profile.png')
print('All EDA 1 charts successfully generated!')
