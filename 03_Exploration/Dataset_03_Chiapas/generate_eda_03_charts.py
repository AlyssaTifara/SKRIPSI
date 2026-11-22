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

# Palettes
c_primary = '#023047'
c_secondary = '#219ebc'
c_accent = '#fb8500'
c_red = '#d90429'
c_green = '#2a9d8f'
c_orange = '#f4a261'
c_purple = '#9d4edd'

intervals = [f'V{i}' for i in range(1, 31)]
x_indices = np.arange(1, 31)

# Helper function to shade temporal zones
def add_temporal_zones(ax, y_min=None, y_max=None):
    ax.axvspan(0.5, 6.5, color='#e9ecef', alpha=0.65, label='Pra-Tanam (V1–V6: -60 s.d. -1 hari)')
    ax.axvspan(6.5, 24.5, color='#e8f4f8', alpha=0.65, label='Dalam-Musim (V7–V24: 0 s.d. 179 hari)')
    ax.axvspan(24.5, 30.5, color='#fff3cd', alpha=0.65, label='Akhir/Pascapanen (V25–V30: 180 s.d. 239 hari)')
    ax.axvline(6.5, color='#d90429', linestyle='--', linewidth=1.5, alpha=0.85)
    ax.axvline(24.5, color='#6c757d', linestyle=':', linewidth=1.5, alpha=0.85)

# ==============================================================================
# GAMBAR 1: Profil Temporal Dinamika Cuaca Daymet (V1 s.d. V30)
# ==============================================================================
fig, axes = plt.subplots(5, 1, figsize=(15, 16), dpi=300, sharex=True)

weather_configs = [
    ('prcp', 'Presipitasi Rata-rata (mm hari⁻¹)', axes[0], '#219ebc', '(A) Presipitasi Harian per Interval 10-Harian (prcp_V1–V30)'),
    ('srad', 'Radiasi Surya (MJ m⁻² hari⁻¹)', axes[1], '#fb8500', '(B) Radiasi Surya per Interval 10-Harian (srad_V1–V30)'),
    ('tmax', 'Suhu Maksimum (°C)', axes[2], '#d90429', '(C) Suhu Maksimum per Interval 10-Harian (tmax_V1–V30)'),
    ('tmin', 'Suhu Minimum (°C)', axes[3], '#2a9d8f', '(D) Suhu Minimum per Interval 10-Harian (tmin_V1–V30)'),
    ('vp', 'Tekanan Uap Air (Pa)', axes[4], '#9d4edd', '(E) Tekanan Uap Air per Interval 10-Harian (vp_V1–V30)')
]

for w_code, y_label, ax, col_color, title in weather_configs:
    means = [df[f'{w_code}_V{i}'].mean() for i in range(1, 31)]
    q1s = [df[f'{w_code}_V{i}'].quantile(0.25) for i in range(1, 31)]
    q3s = [df[f'{w_code}_V{i}'].quantile(0.75) for i in range(1, 31)]
    
    add_temporal_zones(ax)
    ax.plot(x_indices, means, color=col_color, linewidth=2.4, marker='o', markersize=4.5, label=f'Rata-rata Populasi ({w_code})')
    ax.fill_between(x_indices, q1s, q3s, color=col_color, alpha=0.25, label='Rentang Interkuartil (Q1–Q3)')
    
    ax.set_title(title, fontsize=11)
    ax.set_ylabel(y_label, fontsize=10)
    ax.grid(True, linestyle='--', alpha=0.4)
    ax.set_xlim(0.5, 30.5)

axes[0].legend(loc='upper left', ncol=5, fontsize=8.5, framealpha=0.9)
axes[4].set_xticks(x_indices)
axes[4].set_xticklabels([f'V{i}' for i in range(1, 31)], rotation=0, fontsize=8.5)
axes[4].set_xlabel('Interval 10-Harian Relatif terhadap Hari Tanam (Planting = V7)', fontsize=11)

fig.suptitle('Profil Dinamika Temporal 5 Variabel Cuaca Daymet Relatif terhadap Waktu Tanam (N = 4.585)', fontsize=13, y=0.99)
plt.savefig(os.path.join(out_dir, 'eda_03_weather_temporal_trajectories.png'), bbox_inches='tight')
plt.close()
print("Saved eda_03_weather_temporal_trajectories.png")

# ==============================================================================
# GAMBAR 2: Lintasan Koefisien Korelasi Cuaca terhadap YIELD (V1 s.d. V30)
# ==============================================================================
fig, axes = plt.subplots(3, 2, figsize=(16, 14), dpi=300)
axes_flat = axes.flatten()

corrs_configs = [
    ('prcp', 'Presipitasi (prcp)', axes_flat[0], '#219ebc'),
    ('srad', 'Radiasi Surya (srad)', axes_flat[1], '#fb8500'),
    ('tmax', 'Suhu Maksimum (tmax)', axes_flat[2], '#d90429'),
    ('tmin', 'Suhu Minimum (tmin)', axes_flat[3], '#2a9d8f'),
    ('vp', 'Tekanan Uap Air (vp)', axes_flat[4], '#9d4edd')
]

for w_code, name, ax, col_color in corrs_configs:
    add_temporal_zones(ax)
    
    global_rhos = [df[f'{w_code}_V{i}'].corr(df['YIELD'], method='spearman') for i in range(1, 31)]
    hyb_rhos = [df.loc[df['System']=='Hybrid', f'{w_code}_V{i}'].corr(df.loc[df['System']=='Hybrid', 'YIELD'], method='spearman') for i in range(1, 31)]
    land_rhos = [df.loc[df['System']=='Landrace', f'{w_code}_V{i}'].corr(df.loc[df['System']=='Landrace', 'YIELD'], method='spearman') for i in range(1, 31)]
    
    ax.plot(x_indices, global_rhos, color='#000000', linewidth=2.2, marker='s', markersize=4, label='Global (N=4.585)')
    ax.plot(x_indices, hyb_rhos, color='#023047', linestyle='--', linewidth=1.8, marker='o', markersize=4, label='Hybrid (N=3.034)')
    ax.plot(x_indices, land_rhos, color='#e76f51', linestyle=':', linewidth=1.8, marker='^', markersize=4, label='Landrace (N=1.551)')
    
    ax.axhline(0, color='gray', linestyle='-', linewidth=0.8)
    ax.set_title(f'Korelasi Spearman {name} vs YIELD', fontsize=11)
    ax.set_ylabel('Koefisien Korelasi Rank Spearman (ρ)')
    ax.set_xticks(range(1, 31, 2))
    ax.set_xticklabels([f'V{i}' for i in range(1, 31, 2)], fontsize=8)
    ax.grid(True, linestyle='--', alpha=0.4)
    ax.set_ylim(-0.65, 0.65)
    ax.legend(loc='lower left', fontsize=8, framealpha=0.9)

# Panel 6: Summary of Maximum Absolute Correlations across periods
ax_sum = axes_flat[5]
w_labels = ['prcp', 'srad', 'tmax', 'tmin', 'vp']
pre_max_r = [max([abs(df[f'{w}_V{i}'].corr(df['YIELD'], method='spearman')) for i in range(1, 7)]) for w in w_labels]
in_max_r = [max([abs(df[f'{w}_V{i}'].corr(df['YIELD'], method='spearman')) for i in range(7, 25)]) for w in w_labels]
late_max_r = [max([abs(df[f'{w}_V{i}'].corr(df['YIELD'], method='spearman')) for i in range(25, 31)]) for w in w_labels]

x = np.arange(len(w_labels))
width = 0.25
ax_sum.bar(x - width, pre_max_r, width, label='Pra-Tanam (V1–V6)', color='#2a9d8f', edgecolor='black')
ax_sum.bar(x, in_max_r, width, label='Dalam-Musim (V7–V24)', color='#219ebc', edgecolor='black')
ax_sum.bar(x + width, late_max_r, width, label='Akhir (V25–V30)', color='#e76f51', edgecolor='black')

ax_sum.set_title('(F) Nilai Absolut Korelasi Maksimum (|ρ|) per Fase Temporal', fontsize=11)
ax_sum.set_ylabel('Korelasi Spearman Maksimum (|ρ|)')
ax_sum.set_xticks(x)
ax_sum.set_xticklabels(['Presipitasi\n(prcp)', 'Radiasi\n(srad)', 'T-Maks\n(tmax)', 'T-Min\n(tmin)', 'Vapor P.\n(vp)'])
ax_sum.set_ylim(0, 0.70)
ax_sum.grid(True, linestyle='--', alpha=0.4)
ax_sum.legend(loc='upper right', fontsize=8)

for i in range(len(w_labels)):
    ax_sum.text(x[i] - width, pre_max_r[i] + 0.015, f"{pre_max_r[i]:.2f}", ha='center', fontsize=7.5, fontweight='bold')
    ax_sum.text(x[i], in_max_r[i] + 0.015, f"{in_max_r[i]:.2f}", ha='center', fontsize=7.5, fontweight='bold')
    ax_sum.text(x[i] + width, late_max_r[i] + 0.015, f"{late_max_r[i]:.2f}", ha='center', fontsize=7.5, fontweight='bold')

fig.suptitle('Lintasan Korelasi Temporal 150 Variabel Cuaca terhadap YIELD dan Perbandingan Subgrup', fontsize=13, y=0.99)
plt.savefig(os.path.join(out_dir, 'eda_03_weather_yield_correlations.png'), bbox_inches='tight')
plt.close()
print("Saved eda_03_weather_yield_correlations.png")

# ==============================================================================
# GAMBAR 3: Struktur Ketergantungan Temporal & Redundansi (Heatmap Korelasi Antarinterval)
# ==============================================================================
fig = plt.figure(figsize=(16, 12), dpi=300)
gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.25)

# Panel A: Autokorelasi prcp
ax_prcp_hm = fig.add_subplot(gs[0, 0])
prcp_cols = [f'prcp_V{i}' for i in range(1, 31)]
corr_prcp = df[prcp_cols].corr()
sns.heatmap(corr_prcp, ax=ax_prcp_hm, cmap='Blues', vmin=-0.2, vmax=1.0, cbar_kws={'label': 'Korelasi Pearson (r)'})
ax_prcp_hm.set_title('(A) Matriks Korelasi Antarinterval: Presipitasi (prcp_V1–V30)', fontsize=11)
ax_prcp_hm.set_xticks(range(0, 30, 3))
ax_prcp_hm.set_xticklabels([f'V{i+1}' for i in range(0, 30, 3)], fontsize=8)
ax_prcp_hm.set_yticks(range(0, 30, 3))
ax_prcp_hm.set_yticklabels([f'V{i+1}' for i in range(0, 30, 3)], fontsize=8)

# Panel B: Autokorelasi tmax
ax_tmax_hm = fig.add_subplot(gs[0, 1])
tmax_cols = [f'tmax_V{i}' for i in range(1, 31)]
corr_tmax = df[tmax_cols].corr()
sns.heatmap(corr_tmax, ax=ax_tmax_hm, cmap='Reds', vmin=0.4, vmax=1.0, cbar_kws={'label': 'Korelasi Pearson (r)'})
ax_tmax_hm.set_title('(B) Matriks Korelasi Antarinterval: Suhu Maksimum (tmax_V1–V30)', fontsize=11)
ax_tmax_hm.set_xticks(range(0, 30, 3))
ax_tmax_hm.set_xticklabels([f'V{i+1}' for i in range(0, 30, 3)], fontsize=8)
ax_tmax_hm.set_yticks(range(0, 30, 3))
ax_tmax_hm.set_yticklabels([f'V{i+1}' for i in range(0, 30, 3)], fontsize=8)

# Panel C: Autokorelasi vp
ax_vp_hm = fig.add_subplot(gs[1, 0])
vp_cols = [f'vp_V{i}' for i in range(1, 31)]
corr_vp = df[vp_cols].corr()
sns.heatmap(corr_vp, ax=ax_vp_hm, cmap='Purples', vmin=0.0, vmax=1.0, cbar_kws={'label': 'Korelasi Pearson (r)'})
ax_vp_hm.set_title('(C) Matriks Korelasi Antarinterval: Tekanan Uap Air (vp_V1–V30)', fontsize=11)
ax_vp_hm.set_xticks(range(0, 30, 3))
ax_vp_hm.set_xticklabels([f'V{i+1}' for i in range(0, 30, 3)], fontsize=8)
ax_vp_hm.set_yticks(range(0, 30, 3))
ax_vp_hm.set_yticklabels([f'V{i+1}' for i in range(0, 30, 3)], fontsize=8)

# Panel D: Profil Penurunan Autokorelasi (Autocorrelation Decay)
ax_decay = fig.add_subplot(gs[1, 1])
lags = range(1, 11)

decay_data = {}
for w in ['prcp', 'srad', 'tmax', 'tmin', 'vp']:
    cols = [f'{w}_V{i}' for i in range(1, 31)]
    c_mat = df[cols].corr().values
    decay_curve = []
    for lag in lags:
        diag_vals = [c_mat[i, i + lag] for i in range(30 - lag)]
        decay_curve.append(np.mean(diag_vals))
    decay_data[w] = decay_curve

ax_decay.plot(lags, decay_data['tmin'], marker='o', color='#2a9d8f', linewidth=2, label='tmin (Mean Lag-1 = 0.88)')
ax_decay.plot(lags, decay_data['tmax'], marker='s', color='#d90429', linewidth=2, label='tmax (Mean Lag-1 = 0.88)')
ax_decay.plot(lags, decay_data['vp'], marker='^', color='#9d4edd', linewidth=2, label='vp (Mean Lag-1 = 0.75)')
ax_decay.plot(lags, decay_data['srad'], marker='d', color='#fb8500', linewidth=2, label='srad (Mean Lag-1 = 0.47)')
ax_decay.plot(lags, decay_data['prcp'], marker='v', color='#219ebc', linewidth=2, label='prcp (Mean Lag-1 = 0.25)')

ax_decay.set_title('(D) Peluruhan Autokorelasi Berdasarkan Jarak Lag Antarinterval', fontsize=11)
ax_decay.set_xlabel('Jarak Lag Interval (1 Lag = 10 Hari)', fontsize=10)
ax_decay.set_ylabel('Rata-rata Koefisien Korelasi Autoregresif', fontsize=10)
ax_decay.set_xticks(lags)
ax_decay.grid(True, linestyle='--', alpha=0.4)
ax_decay.set_ylim(-0.1, 1.0)
ax_decay.legend(loc='upper right', fontsize=8.5)

ax_decay.text(0.05, 0.15, 
              "Diagnostik Redundansi:\n"
              "• Suhu (tmax, tmin) memiliki autokorelasi masif (>0.80 s.d. Lag-5)\n"
              "• Menunjukkan multikolinearitas serial ekstrem (150 fitur redundant)\n"
              "• Presipitasi bersifat episodik (autokorelasi rendah, Lag-1 = 0.25)",
              transform=ax_decay.transAxes, ha='left', va='center', fontsize=8,
              bbox=dict(boxstyle='round,pad=0.35', facecolor='#f8f9fa', edgecolor='gray', alpha=0.95))

fig.suptitle('Analisis Ketergantungan Serial Temporal dan Redundansi Fitur Cuaca Daymet', fontsize=13, y=0.99)
plt.savefig(os.path.join(out_dir, 'eda_03_weather_autocorrelation_redundancy.png'), bbox_inches='tight')
plt.close()
print("Saved eda_03_weather_autocorrelation_redundancy.png")

# ==============================================================================
# GAMBAR 4: Evaluasi Skenario Pra-Tanam (V1–V6) vs Dalam-Musim (V7–V24) terhadap YIELD
# ==============================================================================
fig, axes = plt.subplots(2, 2, figsize=(15, 12), dpi=300)

palette_sys = {'Hybrid': '#023047', 'Landrace': '#e76f51'}

# Panel A: Komparasi Kapabilitas Eksplanatori Model Linear (R2)
ax_r2 = axes[0, 0]
r2_vals = [0.3879, 0.4667, 0.5065]
r2_labels = ['Pra-Tanam (At-Planting)\nV1–V6 (30 Fitur)', 
             'Dalam-Musim (In-Season)\nV7–V24 (90 Fitur)', 
             'Seluruh Periode Cuaca\nV1–V30 (150 Fitur)']
bars = ax_r2.bar(r2_labels, r2_vals, color=['#2a9d8f', '#219ebc', '#023047'], width=0.55, edgecolor='black', linewidth=0.8)
ax_r2.set_title('(A) Proporsi Variansi YIELD yang Dijelaskan (R² Linear Model)', fontsize=11)
ax_r2.set_ylabel('Nilai Koefisien Determinasi (R²)')
ax_r2.set_ylim(0, 0.65)
ax_r2.grid(True, linestyle='--', alpha=0.4, axis='y')

for bar in bars:
    h = bar.get_height()
    ax_r2.text(bar.get_x() + bar.get_width()/2., h + 0.015, f"{h*100:.2f}%\n(R²={h:.4f})", 
               ha='center', va='bottom', fontsize=9, fontweight='bold')

ax_r2.text(0.04, 0.82, 
           "Temuan Kunci Skenario Prediksi:\n"
           "• V1–V6 merebut 38.79% variansi panen\n"
           "• Setara ~76.6% dari kapasitas 150 fitur cuaca (50.65%)\n"
           "• Menjadi fondasi kuat prediksi pra-tanam",
           transform=ax_r2.transAxes, ha='left', va='top', fontsize=8.5,
           bbox=dict(boxstyle='round,pad=0.35', facecolor='#ffffff', edgecolor='gray', alpha=0.9))

# Panel B: Scatter Plot Presipitasi Pra-Tanam (V1-V6) vs YIELD
ax_sc_pre = axes[0, 1]
prcp_pre_tot = df[[f'prcp_V{i}' for i in range(1, 7)]].sum(axis=1) * 10
sns.scatterplot(x=prcp_pre_tot, y=df['YIELD'], hue=df['System'], palette=palette_sys, 
                alpha=0.35, s=18, ax=ax_sc_pre, edgecolor='none')
sns.regplot(x=prcp_pre_tot, y=df['YIELD'], scatter=False, ax=ax_sc_pre, color='black', 
            line_kws={'linewidth': 2.0, 'label': 'Tren Global (r = +0.48, ρ = +0.49)'})
ax_sc_pre.set_title('(B) Total Presipitasi 60 Hari Pra-Tanam (V1–V6) vs YIELD', fontsize=11)
ax_sc_pre.set_xlabel('Akumulasi Presipitasi Pra-Tanam V1–V6 (mm)')
ax_sc_pre.set_ylabel('Produktivitas Jagung YIELD (Mg ha⁻¹)')
ax_sc_pre.grid(True, linestyle='--', alpha=0.4)
ax_sc_pre.legend(loc='lower right', fontsize=8)

# Panel C: Scatter Plot Presipitasi Dalam-Musim (V7-V24) vs YIELD
ax_sc_in = axes[1, 0]
prcp_in_tot = df[[f'prcp_V{i}' for i in range(7, 25)]].sum(axis=1) * 10
sns.scatterplot(x=prcp_in_tot, y=df['YIELD'], hue=df['System'], palette=palette_sys, 
                alpha=0.35, s=18, ax=ax_sc_in, edgecolor='none')
sns.regplot(x=prcp_in_tot, y=df['YIELD'], scatter=False, ax=ax_sc_in, color='black', 
            line_kws={'linewidth': 2.0, 'label': 'Tren Global (r = -0.09, ρ = -0.16)'})
ax_sc_in.set_title('(C) Total Presipitasi 180 Hari Dalam-Musim (V7–V24) vs YIELD', fontsize=11)
ax_sc_in.set_xlabel('Akumulasi Presipitasi Dalam-Musim V7–V24 (mm)')
ax_sc_in.set_ylabel('Produktivitas Jagung YIELD (Mg ha⁻¹)')
ax_sc_in.grid(True, linestyle='--', alpha=0.4)
ax_sc_in.legend(loc='upper right', fontsize=8)

# Panel D: Strategi Rekomendasi Alur Prediksi Dual-Horizon
ax_rec = axes[1, 1]
ax_rec.axis('off')

rec_text = (
    "REKOMENDASI METODOLOGIS: STRATEGI PEMODELAN DUAL-HORIZON\n"
    "─────────────────────────────────────────────────────────────────\n\n"
    "1. SKENARIO UTAMA: MODEL PREDIKSI SAAT TANAM (AT-PLANTING FORECAST)\n"
    "   • Status Kelayakan: SANGAT CUKUP & LAYAK SEBAGAI BASELINE.\n"
    "   • Fitur Cuaca yang Diizinkan: HANYA V1–V6 (60 hari sebelum tanam).\n"
    "   • Informasi yang Ditangkap: Onset hujan musiman (soil profile recharge)\n"
    "     dan baseline termal lokasi (tmax, tmin, vp pra-tanam).\n"
    "   • Kapabilitas: Menjelaskan 38.79% variansi YIELD (76.6% dari full cuaca).\n\n"
    "2. KETERBATASAN UTAMA YANG HARUS DIPERTIMBANGKAN:\n"
    "   • Ketidakmampuan Memprediksi Syok Cuaca Ekstrem Dalam-Musim:\n"
    "     V1–V6 tidak dapat mengantisipasi anomali kekeringan saat fase kritis\n"
    "     (canícula) atau badai tropis/banjir pada fase pengisian biji.\n"
    "   • Confounding Elevasi & Sistem:\n"
    "     Korelasi suhu tinggi V1–V6 sebagian besar merupakan refleksi\n"
    "     dataran rendah (lokasi Hybrid) vs pegunungan dingin (Landrace).\n\n"
    "3. SKENARIO SEKUNDER: PEMANTAUAN DALAM-MUSIM (IN-SEASON MONITORING)\n"
    "   • Menggunakan V7–V24 secara inkremental untuk memperbarui estimasi panen\n"
    "     (update carrying capacity peternakan unggas secara berkala)."
)

ax_rec.text(0.03, 0.95, rec_text, transform=ax_rec.transAxes, ha='left', va='top', fontsize=9,
            family='monospace', bbox=dict(boxstyle='round,pad=0.6', facecolor='#f8f9fa', edgecolor='#023047', linewidth=1.2))

fig.suptitle('Evaluasi Kelayakan Prediksi Skenario Saat Tanam (At-Planting) vs Pemantauan Dalam-Musim', fontsize=13, y=0.99)
plt.savefig(os.path.join(out_dir, 'eda_03_preplanting_vs_inseason_evaluation.png'), bbox_inches='tight')
plt.close()
print("Saved eda_03_preplanting_vs_inseason_evaluation.png")

print("All 4 EDA 03 figures generated successfully!")
