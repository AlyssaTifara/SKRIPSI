import pandas as pd
import numpy as np
import json
import os

csv_path = r'C:\SKRIPSI\02_Raw_Data\Dataset_03_Chiapas\Chiapas_Data.csv'
legend_path = r'C:\SKRIPSI\02_Raw_Data\Dataset_03_Chiapas\legend_dump.json'
out_path = r'C:\SKRIPSI\03_Exploration\Dataset_03_Chiapas\Output\DATA_DICTIONARY_CHIAPAS.md'

df = pd.read_csv(csv_path)

with open(legend_path, 'r', encoding='utf-8') as f:
    legend_dump = json.load(f)

# Parse legend
header_idx = None
for i, d in enumerate(legend_dump):
    if len(d['values']) >= 3 and d['values'][1] == 'Variable' and d['values'][2] == 'Description':
        header_idx = i
        break

legend_dict = {}
for d in legend_dump[header_idx+1:]:
    vals = d['values']
    var = vals[1] if len(vals) > 1 else ''
    desc = vals[2] if len(vals) > 2 else ''
    unit = vals[3] if len(vals) > 3 else ''
    if var:
        legend_dict[var] = {'description': desc, 'unit': unit}

rows_md = []
for idx, col in enumerate(df.columns, start=1):
    leg = legend_dict.get(col, {'description': '-', 'unit': '-'})
    desc = leg['description']
    unit = leg['unit'] if leg['unit'] else '-'
    
    # Category and timing
    if col in ['Field_ID', 'Year']:
        cat = 'Identifikasi / Temporal'
        timing = 'Tersedia sebelum tanam (ID & Tahun)'
    elif col == 'YIELD':
        cat = 'Target Utama'
        timing = 'Target Observasi Lapangan (Pasca Panen)'
    elif col == 'Mun_yield':
        cat = 'Konteks Wilayah'
        timing = 'Statistik Regional Tahunan (SIAP)'
    elif col in ['Lat', 'Long', 'Elev']:
        cat = 'Geografis / Topografi'
        timing = 'Tersedia sebelum tanam'
    elif col in ['System', 'Cultivar', 'Tillage', 'Planting']:
        cat = 'Pengelolaan Agronomi'
        timing = 'Tersedia saat penanaman'
    elif col in ['Nitrogen', 'Phosphorus', 'Potassium']:
        cat = 'Pemupukan'
        timing = 'Rencana/Aplikasi pemupukan'
    elif col in ['Slope', 'Clay', 'CEC', 'SOM', 'PH']:
        cat = 'Karakteristik Tanah'
        timing = 'Tersedia sebelum tanam (Peta Tanah INEGI)'
    elif col.startswith('prcp_') or col.startswith('srad_') or col.startswith('tmax_') or col.startswith('tmin_') or col.startswith('vp_'):
        v_num = int(col.split('_V')[1])
        cat = 'Cuaca Gridded (Daymet)'
        if v_num <= 6:
            timing = f'Pre-planting (Hari -{(7-v_num)*10} s/d -{(6-v_num)*10+1})'
        elif v_num <= 24:
            timing = f'POTENSI LEAKAGE: In-season (Hari {(v_num-7)*10} s/d {(v_num-6)*10-1})'
        else:
            timing = f'POTENSI LEAKAGE: Post-season (Hari {(v_num-7)*10} s/d {(v_num-6)*10-1})'
    else:
        cat = 'Lainnya'
        timing = '-'

    n_miss = df[col].isnull().sum()
    pct_miss = (n_miss / len(df)) * 100.0
    dtype = str(df[col].dtype)
    
    if col in ['System', 'Cultivar', 'Tillage']:
        s = df[col].dropna()
        val_range = f'Kategori: {s.nunique()} unik (Modus: {s.mode().iloc[0]})'
    else:
        s = pd.to_numeric(df[col], errors='coerce')
        val_range = f'{s.min():.2f} s/d {s.max():.2f} (Mean: {s.mean():.2f})'
        
    rows_md.append(f'| {idx} | `{col}` | {cat} | {desc} | {unit} | `{dtype}` | {n_miss} ({pct_miss:.2f}%) | {val_range} | {timing} |')

content = f"""# DATA DICTIONARY — CHIAPAS MAIZE DATASET (2012–2018)

## 1. Ringkasan Dataset
- **Nama Dataset:** Multiyear Maize Management Dataset collected in Chiapas, Mexico (2012–2018)
- **Sumber Data:** CIMMYT Knowledge Hub Chiapas, BEM (Bitácora Electrónica MasAgro), INEGI, Daymet, SIAP
- **Publikasi Pendamping:** Trevisan, R. G., Martin, N. F., Fonteyne, S., Verhulst, N., Dorado Betancourt, H. A., Jiménez, D., & Gardeazabal, A. (2022). *Data in Brief*, 40, 107837. https://doi.org/10.1016/j.dib.2022.107837
- **Persistent Identifier (Handle):** https://hdl.handle.net/11529/10548624
- **Jumlah Observasi:** 4.585 baris *cropping events*
- **Jumlah Variabel:** 169 kolom (19 variabel agronomi/lingkungan/target + 150 variabel cuaca temporal)
- **Status Missing Value:** Lengkap 100% pada 168 kolom; hanya variabel `Cultivar` yang memiliki nilai kosong sebanyak 310 baris (6,76%).

---

## 2. Struktur Interval Cuaca (Daymet Gridded Weather V1 – V30)
Dataset cuaca ditransformasikan ke dalam 30 interval 10-harian yang dihitung relatif terhadap tanggal tanam (`Planting` DOY):
- **Interval V1 – V6 (6 interval = 60 hari):** Periode **Sebelum Tanam (Pre-planting)** dari hari ke -60 hingga hari ke -1 sebelum tanam. Fitur ini aman digunakan untuk peramalan yield sebelum tanam (*pre-season forecasting*).
- **Interval V7 – V24 (18 interval = 180 hari):** Periode **Selama Pertumbuhan (In-season)** dari hari ke 0 hingga hari ke 179 setelah tanam. Rata-rata durasi musim tanam jagung adalah 175 hari. Fitur ini **berpotensi menimbulkan data leakage** jika model ditujukan untuk perencanaan tanam awal, karena nilainya belum terjadi pada saat keputusan tanam diambil.
- **Interval V25 – V30 (6 interval = 60 hari):** Periode **Pasca Kematangan Fisiologis / Pasca Panen (Post-season)** dari hari ke 180 hingga hari ke 240 setelah tanam. Fitur ini merefleksikan kondisi cuaca saat jagung dibiarkan mengering di lahan sebelum panen manual.

Lima parameter cuaca harian yang dirata-ratakan dalam setiap interval 10-hari:
1. `prcp_V1` s/d `prcp_V30`: Presipitasi rata-rata harian (satuan: mm day⁻¹).
2. `srad_V1` s/d `srad_V30`: Radiasi surya rata-rata harian (satuan: MJ m⁻² day⁻¹).
3. `tmax_V1` s/d `tmax_V30`: Suhu maksimum rata-rata (satuan: °C).
4. `tmin_V1` s/d `tmin_V30`: Suhu minimum rata-rata (satuan: °C).
5. `vp_V1` s/d `vp_V30`: Tekanan uap air rata-rata (satuan: Pa).

---

## 3. Tabel Kamus Data Lengkap (169 Variabel)

| No. | Nama Kolom | Kategori | Deskripsi (Berdasarkan Legend / Paper) | Satuan Asli | Tipe Data | Missing Values | Rentang / Karakteristik Nilai | Status Ketersediaan & Risiko Leakage |
|---:|---|---|---|---|---|---|---|---|
""" + '\n'.join(rows_md) + """

---

## 4. Panduan Penggunaan Kamus Data untuk Penelitian Skripsi
1. **Pemilihan Variabel Target:**
   - Gunakan `YIELD` (Mg ha⁻¹ = ton ha⁻¹) sebagai target estimasi produktivitas lahan riil.
   - Jangan gunakan `Mun_yield` sebagai target. `Mun_yield` adalah statistik agregat tingkat munisipal dari SIAP yang hanya berfungsi sebagai pembanding makro atau kovariat regional.
2. **Pemisahan Prediktor Berdasarkan Waktu Keputusan (Decision Horizon):**
   - **Model Perencanaan Sebelum Tanam (Pre-Planting Planning):** Gunakan fitur geografi (`Elev`), karakteristik tanah (`Slope`, `Clay`, `CEC`, `SOM`, `PH`), rencana budidaya (`System`, `Tillage`, `Planting`, `Nitrogen`, `Phosphorus`, `Potassium`), dan cuaca historis pra-tanam (`*_V1` s/d `*_V6`). Hindari `*_V7` s/d `*_V30` untuk mencegah data leakage.
   - **Model Evaluasi Hasil / Explanatory Machine Learning (Post-Harvest):** Seluruh variabel cuaca `*_V1` s/d `*_V24` dapat diikutsertakan untuk mengidentifikasi pembatas hasil (*yield gap analysis*).
3. **Kebutuhan Kalibrasi Lokal ASA Indonesia:**
   - Variabel agronomi seperti `System` (Hybrid vs Landrace) dan dosis pupuk N-P-K harus dipetakan terhadap praktik budidaya lokal jagung Madura di Komunitas ASA.
"""

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Generated DATA_DICTIONARY_CHIAPAS.md successfully!')
