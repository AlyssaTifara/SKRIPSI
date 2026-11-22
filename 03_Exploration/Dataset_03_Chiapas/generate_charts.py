import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_theme(style='whitegrid', font='sans-serif')
csv_path = r'C:\SKRIPSI\02_Raw_Data\Dataset_03_Chiapas\Chiapas_Data.csv'
out_dir = r'C:\SKRIPSI\03_Exploration\Dataset_03_Chiapas\Output'
os.makedirs(out_dir, exist_ok=True)
df = pd.read_csv(csv_path)

mean_yield = df['YIELD'].mean()
med_yield = df['YIELD'].median()
mean_mun = df['Mun_yield'].mean()

# Chart 1: Distribusi Yield vs Mun_yield
fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
sns.histplot(df['YIELD'], kde=True, color='#2b5c8f', stat='density', bins=35, label='Field YIELD (Target)', alpha=0.6, ax=ax)
sns.histplot(df['Mun_yield'], kde=True, color='#e26d5c', stat='density', bins=25, label='Mun_yield (Context)', alpha=0.5, ax=ax)
ax.axvline(mean_yield, color='#1d3557', linestyle='--', linewidth=2, label=f'Mean YIELD: {mean_yield:.2f} Mg/ha')
ax.axvline(med_yield, color='#457b9d', linestyle=':', linewidth=2, label=f'Median YIELD: {med_yield:.2f} Mg/ha')
ax.axvline(mean_mun, color='#e63946', linestyle='--', linewidth=2, label=f'Mean Mun_yield: {mean_mun:.2f} Mg/ha')
ax.set_title('Distribusi Produktivitas Jagung: Field YIELD vs Rata-rata Munisipal (Mun_yield)', fontsize=13, fontweight='bold', pad=12)
ax.set_xlabel('Hasil Panen Jagung (Mg ha⁻¹ atau Ton ha⁻¹)', fontsize=11)
ax.set_ylabel('Densitas', fontsize=11)
ax.legend(frameon=True, facecolor='white', loc='upper right')
plt.tight_layout()
plt.savefig(os.path.join(out_dir, 'distribusi_yield_chiapas.png'))
plt.close()
print('Generated distribusi_yield_chiapas.png')

# Chart 2: Missing Values Overview
fig, ax = plt.subplots(figsize=(9, 4.5), dpi=300)
bars = ax.barh(['168 Variabel Lainnya\n(Agronomi, Tanah, Cuaca)', 'Cultivar\n(Genotipe / Varietas)'], [0.0, 6.76], color=['#2a9d8f', '#e76f51'], height=0.45)
ax.set_xlim(0, 10)
ax.set_xlabel('Persentase Missing Value (%)', fontsize=11)
ax.set_title('Audit Kelengkapan Data: Persentase Missing Value per Variabel (N = 4.585)', fontsize=12, fontweight='bold', pad=12)
for bar in bars:
    w = bar.get_width()
    y = bar.get_y() + bar.get_height()/2
    if w > 0:
        ax.text(w + 0.2, y, f'{w:.2f}% (310 / 4.585 baris)', va='center', fontweight='bold', color='#e76f51')
    else:
        ax.text(0.2, y, '0.00% (Lengkap 100% / 0 baris kosong)', va='center', fontweight='bold', color='#2a9d8f')
plt.tight_layout()
plt.savefig(os.path.join(out_dir, 'missing_values_chiapas.png'))
plt.close()
print('Generated missing_values_chiapas.png')

# Chart 3: Distribusi Yield berdasarkan Sistem Budidaya (Hybrid vs Landrace)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), dpi=300)
sns.boxplot(x='System', y='YIELD', data=df, palette=['#3a86ff', '#ff006e'], ax=ax1, width=0.4)
ax1.set_title('Boxplot YIELD: Hybrid vs Landrace', fontsize=12, fontweight='bold')
ax1.set_xlabel('Sistem Budidaya', fontsize=11)
ax1.set_ylabel('Field YIELD (Mg ha⁻¹)', fontsize=11)

sns.kdeplot(data=df, x='YIELD', hue='System', common_norm=False, fill=True, palette=['#3a86ff', '#ff006e'], alpha=0.3, ax=ax2)
ax2.set_title('Distribusi Densitas YIELD per Sistem', fontsize=12, fontweight='bold')
ax2.set_xlabel('Field YIELD (Mg ha⁻¹)', fontsize=11)
ax2.set_ylabel('Densitas', fontsize=11)
plt.tight_layout()
plt.savefig(os.path.join(out_dir, 'distribusi_yield_by_system.png'))
plt.close()
print('Generated distribusi_yield_by_system.png')

# Chart 4: Observasi per Tahun dan Sistem
fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
df_counts = df.groupby(['Year', 'System']).size().unstack(fill_value=0)
df_counts.plot(kind='bar', stacked=True, color=['#3a86ff', '#ff006e'], ax=ax, edgecolor='white', width=0.6)
ax.set_title('Distribusi Jumlah Observasi Cropping Events per Tahun (2012–2018)', fontsize=12, fontweight='bold', pad=12)
ax.set_xlabel('Tahun Tanam', fontsize=11)
ax.set_ylabel('Jumlah Observasi', fontsize=11)
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
ax.legend(title='Sistem', frameon=True, facecolor='white')
for p in ax.patches:
    h = p.get_height()
    if h > 50:
        ax.annotate(str(int(h)), (p.get_x() + p.get_width() / 2., p.get_y() + h / 2.),
                    ha='center', va='center', color='white', fontweight='bold', fontsize=9)
totals = df_counts.sum(axis=1)
for i, total in enumerate(totals):
    ax.annotate(f'Total: {total}', (i, total + 15), ha='center', va='bottom', fontweight='bold', fontsize=9, color='#333333')
ax.set_ylim(0, 1150)
plt.tight_layout()
plt.savefig(os.path.join(out_dir, 'distribusi_observasi_per_tahun.png'))
plt.close()
print('Generated distribusi_observasi_per_tahun.png')
