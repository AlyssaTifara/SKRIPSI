# AUDIT TRAIL EKSPERIMEN PEMODELAN PREDIKSI PRODUKTIVITAS JAGUNG
## Uji Komparasi Skenario A (Environment + System) vs Skenario B (Environment + System + Cultivar)
### Dataset: Chiapas Field Data 2012–2018 ($N = 4.585$ Observasi)

---

## 1. Status Workspace dan File Lama
- **Prinsip Integritas:** Tidak ada file lama pada repositori/workspace yang diubah atau dihapus. Seluruh direktori konteks (`01_Context`), data mentah (`02_Raw_Data`), eksplorasi (`03_Exploration`), dokumentasi (`07_Documentation`), dan arsip (`archive`) tetap utuh.
- **Folder Eksperimen Baru:** Seluruh artefak eksperimen baru diisolasi di `C:\SKRIPSI\05_Modeling\exp_cultivar_comparison\`.
- **Lingkungan Eksekusi:** Menggunakan virtual environment mandiri di `C:\SKRIPSI\.venv\` dengan versi:
  - Python: 3.14.0
  - pandas: 3.1.1
  - scikit-learn: 1.9.1
  - xgboost: 3.4.1
  - numpy: 2.5.5
  - openpyxl: 3.1.5

---

## 2. Verifikasi File Sumber & Struktur Kolom
- **File Sumber:** `C:\SKRIPSI\02_Raw_Data\Dataset_03_Chiapas\Chiapas Field Data 2012-2018.xlsx` (dan salinan CSV `Chiapas_Data.csv`).
- **Dimensi:** 4.585 baris dan 169 kolom.
- **Target `YIELD`:**
  - 0 missing value, 0 nilai non-finite, 0 nilai nol, 0 nilai negatif.
  - Rentang: $0{,}10$ hingga $9{,}80\text{ Mg ha}^{-1}$ (rata-rata $3{,}593$, standar deviasi $1{,}869$).
- **Distribusi Temporal `Year`:**
  - 2012: 723 baris
  - 2013: 479 baris
  - 2014: 376 baris
  - 2015: 424 baris (Tahun 2015 tetap dipertahankan utuh)
  - 2016: 816 baris
  - 2017: 960 baris
  - 2018: 807 baris
  - Total: 4.585 baris.

---

## 3. Pencegahan Kebocoran Data (Data Leakage Prevention)

### 3.1 Fitur yang Dikecualikan Secara Ketat
1. `Field_ID`: Pengenal administratif murni; dikeluarkan agar model tidak mempelajari indeks baris.
2. `Lat`, `Long`: Koordinat mengalami pembulatan (*spatial blurring*) oleh CIMMYT ke 2 desimal (~1,1 km), berisiko memicu *spatial memorization overfitting* dan tidak relevan untuk transfer lokasi ke luar Chiapas.
3. `Mun_yield`: Rata-rata munisipalitas SIAP yang baru dirilis pascapanen (*ex-post aggregation leakage*).
4. `Year`: Dikeluarkan dari prediktor langsung untuk mencegah keterikatan tren waktu kontinu yang tidak dapat digeneralisasi ke masa depan; `Year` difungsikan murni sebagai variabel partisi temporal.
5. `Nitrogen`, `Phosphorus`, `Potassium` (`NPK`): Dosis pemupukan riil terakumulasi hingga fase akhir vegetatif V4–V8 (*ex-post management leakage*).
6. `Planting`: Tanggal tanam aktual belum diketahui secara pasti pada horizon pra-tanam (*anchor leakage*).
7. `Tillage`: Dikeluarkan sesuai instruksi batas prediktor.

### 3.2 Fitur yang Digunakan
- **Fitur Lingkungan Biofisik Statis (6 Fitur):**
  - `Clay` (kandungan liat %)
  - `CEC` (kapasitas tukar kation tanah)
  - `SOM` (bahan organik tanah %)
  - `PH` (kemasaman tanah)
  - `Elev` (elevasi m dpl)
  - `Slope` (kemiringan lereng %)
- **Fitur Cuaca Pra-Tanam 60 Hari (5 Fitur Agregat dari Interval V1–V6):**
  - `rain_pre60d`: $10 \times \sum_{i=1}^6 \text{prcp\_V}_i$ (curah hujan kumulatif 60 hari sebelum tanam, mm).
  - `srad_mean_pre60d`: $\frac{1}{6} \sum_{i=1}^6 \text{srad\_V}_i$ (radiasi surya rata-rata harian, $\text{MJ m}^{-2}\text{ day}^{-1}$).
  - `tmax_mean_pre60d`: $\frac{1}{6} \sum_{i=1}^6 \text{tmax\_V}_i$ (suhu maksimum rata-rata harian, °C).
  - `tmin_mean_pre60d`: $\frac{1}{6} \sum_{i=1}^6 \text{tmin\_V}_i$ (suhu minimum rata-rata harian, °C).
  - `vp_mean_pre60d`: $\frac{1}{6} \sum_{i=1}^6 \text{vp\_V}_i$ (tekanan uap rata-rata harian, Pa).
- **Fitur Sistem Budidaya:**
  - `System`: Kategorikal (`Hybrid` vs `Landrace`), di-encode dengan `OneHotEncoder(handle_unknown='ignore', sparse_output=False)`.

### 3.3 Penanganan Khusus Fitur `Cultivar` (Hanya Skenario B)
- Nilai kosong (310 baris pada dataset asli) diimputasi dengan string `'UNKNOWN'`.
- Thresholding frekuensi: dihitung murni pada data training fold berjalan.
- Kategori dengan frekuensi $< 5$ pada training fold dipetakan ke `'RARE_OR_UNSEEN'`.
- Kategori pada test fold yang tidak termasuk dalam kategori sering ($\ge 5$) training fold dipetakan ke `'RARE_OR_UNSEEN'`.
- Transformasi dan pengodean fit strictly pada data training fold di dalam `scikit-learn Pipeline`.

---

## 4. Desain Validasi Temporal & Protokol Eksperimen
- **Skema Validasi:** *Expanding Window Temporal Validation* (4 Fold berurutan):
  - **Fold 1:** Train 2012–2014 ($N=1.578$), Test 2015 ($N=424$).
  - **Fold 2:** Train 2012–2015 ($N=2.002$), Test 2016 ($N=816$).
  - **Fold 3:** Train 2012–2016 ($N=2.818$), Test 2017 ($N=960$).
  - **Fold 4:** Train 2012–2017 ($N=3.778$), Test 2018 ($N=807$).
  - **Total Out-of-Fold Test Observations:** $3.007$ observasi ($424 + 816 + 960 + 807$).
  - **Overlap Check:** 0 observasi overlap antara train dan test pada setiap fold.

- **Baseline Pembanding:**
  - Prediksi rata-rata target training fold ($\hat{y} = \bar{y}_{\text{train}}$) dievaluasi pada test fold terkait.

- **Konfigurasi Algoritma:**
  - **Random Forest:** `RandomForestRegressor(n_estimators=300, min_samples_leaf=2, max_features=1.0, random_state=42, n_jobs=-1)`
  - **XGBoost:** `XGBRegressor(n_estimators=300, max_depth=4, learning_rate=0.05, subsample=0.8, colsample_bytree=0.8, objective='reg:squarederror', random_state=42, n_jobs=4, verbosity=0)`

- **Tata Kelola Status & Checkpoint:**
  - Status manifest: `PENDING`, `RUNNING`, `COMPLETED`, `FAILED`, `PAUSED`.
  - Checkpoint disimpan per fold secara atomik setelah fold selesai.
  - Jika terjadi kegagalan, hanya fold gagal yang diulang setelah perbaikan akar masalah.
