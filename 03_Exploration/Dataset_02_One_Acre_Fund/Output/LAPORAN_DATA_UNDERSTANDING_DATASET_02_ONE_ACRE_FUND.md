# LAPORAN DATA UNDERSTANDING (EDISI REVISI AUDIT) — DATASET 2: ONE ACRE FUND
## Pemodelan Prediksi Hasil Panen Jagung untuk Mendukung Perencanaan Produksi Ayam Petelur di Komunitas ASA Indonesia

---

### Informasi Dokumen & Konteks Penelitian
- **Peneliti:** Mahasiswa Sarjana Terapan Sistem Informasi Bisnis (SIB), Jurusan Teknologi Informasi, Politeknik Negeri Malang
- **Dosen Pembimbing:** Pak Habibie Ed Dien
- **Judul Skripsi:** *PEMODELAN PREDIKSI JUMLAH AYAM PETELUR UNTUK SMART FARMING BERDASARKAN KETERSEDIAAN LAHAN JAGUNG UNTUK MENDUKUNG PERENCANAAN PRODUKSI DI KOMUNITAS ASA INDONESIA*
- **Identitas Dataset:** Dataset 2 — One Acre Fund MEL (*Monitoring, Evaluation, and Learning*) Maize Survey Data 2016–2022
- **File Sumber Data Mentah:** `02_Raw_Data/Dataset_02_One_Acre_Fund/One_Acre_Fund_MEL_maize_survey_data_2016-2022.csv`
- **Lokasi Penyimpanan Output:** `03_Exploration/Dataset_02_One_Acre_Fund/`
- **Status Dokumen:** **Revisi Terbatas Pasca-Audit (4 November 2026)**

---

## 1. Identitas Dataset dan Ringkasan Observasi

Dataset 2 merupakan data survei empiris pemantauan hasil panen jagung petani kecil (*smallholder farmers*) yang dikumpulkan oleh organisasi pertanian **One Acre Fund** melalui divisi *Monitoring, Evaluation, and Learning* (MEL).

| Atribut | Keterangan Rinci |
|---|---|
| **Nama Dataset** | One Acre Fund MEL Maize Survey Data 2016–2022 |
| **Kategori Dataset** | Dataset 2 (Data Empiris Lapangan Petani Kecil) |
| **Format File** | Comma-Separated Values (`.csv`), ukuran $\approx 5,64\text{ MB}$ |
| **Jumlah Baris (Observasi)** | **14.773 baris** |
| **Jumlah Kolom (Fitur)** | **53 kolom** (30 variabel numerik, 23 variabel kategorikal/boolean/tanggal) |
| **Periode Waktu Survei** | **2016 – 2022** (Rincian per tahun: 2016: 2.437; 2017: 1.094; 2018: 3.187; 2019: 4.333; 2020: 3.607; **2021: 0 / absen**; 2022: 115) |
| **Cakupan Wilayah Geografis** | **7 Negara Afrika Sub-Sahara:** Kenya (7.258; 49,13%), Tanzania (3.710; 25,11%), Rwanda (2.080; 14,08%), Zambia (861; 5,83%), Burundi (640; 4,33%), Nigeria (115; 0,78%), Uganda (109; 0,74%) |
| **Siklus Musim Tanam** | *First season* (13.882 baris; 93,97%) dan *Second season* (891 baris; 6,03%, seluruhnya berada di Rwanda) |
| **Unit Observasi (*Unit of Analysis*)** | **Satu plot budidaya jagung per musim panen (*maize field/plot*)** dari petani mitra One Acre Fund dengan koordinat spasial berbasis sentroid kluster desa (*village cluster centroid*) guna melindungi privasi petani. |

> [!NOTE]
> **Catatan Struktur Data Tahun 2021:**
> Pada kolom `year`, tidak ditemukan observasi untuk tahun 2021 (data mencakup 2016, 2017, 2018, 2019, 2020, dan 2022). Ketiadaan data tahun 2021 dicatat murni sebagai **fakta struktur dataset** dalam berkas yang tersedia. Karena tidak ada dokumentasi resmi dari penyelenggara survei di dalam repositori mengenai penyebab ketiadaan data tahun 2021, laporan ini **tidak membuat spekulasi atau kesimpulan sepihak (termasuk tidak mengaitkannya dengan dampak pandemi COVID-19)** tanpa adanya rujukan resmi.

---

## 2. Karakteristik Variabel dan Kamus Data

Ke-53 variabel dikelompokkan ke dalam 8 kategori fungsional pada berkas [`data_dictionary_one_acre_fund.csv`](file:///c:/SKRIPSI/03_Exploration/Dataset_02_One_Acre_Fund/output/tables/data_dictionary_one_acre_fund.csv). Status setiap variabel diverifikasi secara transparan antara yang didukung fakta dokumentasi dan yang masih berstatus interpretasi sementara:

### A. Rincian Kamus Data per Kategori
1. **Identitas & Spasial (6 kolom):** `country`, `iso`, `cz` (kode zona agroklimat), `strat` (strata sampling survei), `lon`, `lat`. *(Status: Terkonfirmasi)*.
2. **Waktu & Kalender Tanam (6 kolom):**
   - `year`, `season`, `plant_date`, `plant_doy` (hari dalam tahun, 1–365). *(Status: Terkonfirmasi)*.
   - `harvest_date`: Tanggal panen riil. *(Status: Terkonfirmasi; Risiko Fatal Data Leakage)*.
   - `plant_date_dev`: Deviasi tanggal tanam terhadap titik acuan referensi (rentang $-108$ s.d. $+97$ hari, median 0 hari). *(Status: **Belum Terverifikasi / Interpretasi Sementara**; formula dan titik acuan referensi belum memiliki dokumentasi resmi)*.
3. **Topografi & Karakteristik Tanah (7 kolom):**
   - `elev` (elevasi, mdpl), `twi` (Topographic Wetness Index), `soil_rzpawhc` (kapasitas retensi air perakaran, mm), `soil_clay` (liat, %), `soil_pH` (derajat keasaman, 4,7–7,0), `soil_ECEC` (kapasitas tukar kation efektif, cmol(+)/kg). *(Status: Terkonfirmasi)*.
   - `soil_orgC`: Karbon organik tanah (rentang 3,48 s.d. 39,45; mean 14,07). *(Status: **Belum Terverifikasi / Interpretasi Sementara**; interpretasi satuan $g/kg$ didasarkan pada rentang agronomis tanah mineral)*.
4. **Agroklimat & Cuaca (7 kolom):** `avg_season_gdd` (Growing Degree Days, °C-days), `avg_season_ai` (Aridity Index), `avg_season_tavg` (suhu musiman rata-rata, °C), `season_prec` (total curah hujan musim, mm), `season_prec_1..3` (curah hujan per fase pertumbuhan, mm). *(Status: Terkonfirmasi)*.
5. **Karakteristik Benih & Varietas (10 kolom):**
   - `hybrid` (biner True/False), `hyb_type` (tipe silangan), `hyb_yor` (tahun rilis), serta 6 toleransi penyakit tanaman: `hyb_tol_mln`, `hyb_tol_msv`, `hyb_tol_gls`, `hyb_tol_nclb`, `hyb_tol_rust`, `hyb_tol_ear_rot`. *(Status: Terkonfirmasi)*.
   - `hyb_mat`: Rating/kelompok kematangan varietas hibrida (rentang diskrit 0.5 s.d. 3.0; nilai: 0.5, 1.0, 1.5, 2.0, 2.5, 3.0; median 2.5). *(Status: **Belum Terverifikasi / Interpretasi Sementara**; skala kematangan ini diduga mengelompokkan umur panen varietas hibrida, namun belum memiliki buku kode (*codebook*) resmi dari One Acre Fund)*.
6. **Praktik Budidaya & Pemupukan (12 kolom):**
   - `pl_m2` (kepadatan populasi tanaman/m²), `row_spacing` (jarak baris, cm), `N_kg_ha` (pupuk Nitrogen, kg/ha), `P_kg_ha` (pupuk Fosfat, kg/ha), `K_kg_ha` (pupuk Kalium, kg/ha), `compost` (biner), `manure` (pupuk kandang), `fert_in_hole` (pemupukan di lubang tanam), `lime_kg_ha` (kapur pertanian), `weeding` (penyiangan), `pesticide` (aplikasi pestisida). *(Status: Terkonfirmasi)*.
   - `comp_kg_ha`: Dosis aplikasi kompos padat per hektar. *(Status: Terkonfirmasi dengan **Catatan Khusus Anomali Nilai Ekstrem** hingga $166.666,55\text{ kg/ha}$)*.
7. **Tekanan Biotik & Abiotik (4 kolom):** `pest` (hama ulat/penggerek), `disease` (penyakit), `water_excess` (genangan air), `striga` (gulma parasitik). *(Status: Terkonfirmasi; seluruhnya merupakan kejadian in-season)*.
8. **Target Prediksi (1 kolom):** `yield_kg_ha` (hasil panen jagung pipilan kering, kg/ha). *(Status: Terkonfirmasi)*.

---

## 3. Karakteristik Target Prediksi (`yield_kg_ha`)

Variabel target didefinisikan sebagai **bobot panen biji jagung pipilan kering per satuan hektar (`yield_kg_ha`)**.

```
    Min (0 kg/ha)          Q1 (1.744)       Median (2.714)    Mean (2.969)      Q3 (3.945)           Max (11.139 kg/ha)
         |---------------------|-------------------|---------------|----------------|------------------------|
   [Zero Yield (1,78%)]  [Produktivitas Rendah]    [Rerata Smallholder]    [Produktivitas Tinggi]   [Outlier Agroteknologi]
                                                                                                      (2,00%)
```

### Parameter Statistik Deskriptif Target
- **Jumlah Observasi Valid:** 14.773 baris (100% lengkap, **0 missing values**).
- **Rata-rata (Mean):** $2.969,06\text{ kg/ha}$ ($\approx 2,97\text{ ton/ha}$).
- **Median:** $2.713,87\text{ kg/ha}$.
- **Standar Deviasi:** $1.686,07\text{ kg/ha}$ (Koefisien Variasi = $56,79\%$).
- **Rentang Data (Range):** $0,00\text{ kg/ha}$ s.d. $11.139,13\text{ kg/ha}$.
- **Kuartil:** $Q_1 = 1.743,99\text{ kg/ha}$, $Q_3 = 3.945,22\text{ kg/ha}$, $\text{IQR} = 2.201,23\text{ kg/ha}$.
- **Bentuk Distribusi:** Skewness $= +0,8246$ (*moderate positive skewness*); Kurtosis $= +0,7831$ (*light leptokurtic*).
- **Nilai Negatif:** **0 baris** (tidak ditemukan nilai negatif fisik).
- **Ambang Batas Outlier IQR Atas:**
  $$\text{Upper Threshold} = Q_3 + 1,5 \times \text{IQR} = 3.945,22 + 1,5(2.201,23) = 7.247,07\text{ kg/ha}$$
  Terdapat **296 observasi (2,00%)** yang melampaui batas atas IQR. Nilai 7.000–11.000 kg/ha secara agronomis masih dapat dicapai pada varietas hibrida intensif di dataran tinggi Rwanda dan Kenya Barat.

> [!IMPORTANT]
> **Temuan Data Observasi Hasil Panen Nol (Zero Yield):**
> Sebanyak **263 observasi (1,78%)** tercatat bernilai `yield_kg_ha = 0`. Temuan ini merupakan **fakta empiris pencatatan data lapangan** di mana tidak ada hasil panen yang diperoleh pada plot survei terkait (Kenya: 144, Rwanda: 61, Tanzania: 58).
> **Batasan Interpretasi Akademik:** Dataset survei tidak menyediakan kolom atribusi penyebab kehilangan hasil per baris. Oleh karena itu, **penyebab spesifik dari nilai nol ini (apakah akibat kekeringan, serangan hama, genangan air, atau faktor operasional survei lainnya) tidak dapat dipastikan secara definitif tanpa bukti resmi**. Keputusan penanganan 263 observasi ini (apakah dipertahankan sebagai cerminan risiko puso atau dimodelkan bertahap via *hurdle model*) wajib dievaluasi pada tahap Data Preparation.

---

## 4. Temuan Kualitas Data (*Data Quality Audit*)

### A. Verifikasi Jumlah Kolom Tanpa Missing Values
Berdasarkan pemeriksaan komputasi pada seluruh 53 kolom:
- **Jumlah Kolom Tanpa Missing Values (100% Lengkap):** **20 kolom (37,74%)**
- **Jumlah Kolom dengan Missing Values (>0%):** **33 kolom (62,26%)**

**Daftar 20 Kolom yang 100% Lengkap Tanpa Missing Values:**
1. `year` (int64)
2. `country` (str)
3. `iso` (str)
4. `season` (str)
5. `cz` (int64)
6. `lon` (float64)
7. `lat` (float64)
8. `season_prec` (float64)
9. `season_prec_1` (float64)
10. `season_prec_2` (float64)
11. `season_prec_3` (float64)
12. `elev` (int64)
13. `twi` (float64)
14. `N_kg_ha` (float64)
15. `P_kg_ha` (float64)
16. `fert_in_hole` (bool)
17. `disease` (bool)
18. `pest` (bool)
19. `water_excess` (bool)
20. `yield_kg_ha` (float64)

### B. Distribusi Kolom Berdasarkan Tingkat Missingness
- **Lengkap (0% missing):** **20 kolom (37,74%)**.
- **Missing Rendah (<5%):** **3 kolom (5,66%)**: `avg_season_gdd`, `avg_season_ai`, `avg_season_tavg` (masing-masing 0,28%).
- **Missing Moderat (5–30%):** **6 kolom (11,32%)**: `hybrid` (8,33%), `lime_kg_ha` (9,01%), `strat` (17,13%), `plant_date` (24,33%), `plant_date_dev` (24,33%), `plant_doy` (24,33%), `K_kg_ha` (24,89%), `weeding` (25,76%).
- **Missing Tinggi (30–50%):** **19 kolom (35,85%)**: seluruh 5 variabel tanah `soil_*` (30,06%), `harvest_date` (30,38%), `pl_m2` (31,19%), `pesticide` (38,48%), `compost` (39,29%), `row_spacing` (42,88%), `hyb_mat` (47,95%), 6 toleransi penyakit hibrida (48,68%).
- **Missing Kritis (>50%):** **5 kolom (9,43%)**: `comp_kg_ha` (52,30%), `hyb_yor` (53,50%), `hyb_type` (82,52%), `striga` (82,91%), `manure` (**94,00%**). Kolom-kolom ini **tidak direkomendasikan** sebagai prediktor utama karena imputasi buatan akan mendistorsi pola data.

### C. Catatan Anomali Ekstrem pada `comp_kg_ha`
Pemeriksaan pada variabel aplikasi kompos padat (`comp_kg_ha`) menemukan karakteristik distribusi yang sangat tidak lazim:
- Observasi valid: 7.047 baris (52,30% missing).
- Sebanyak 5.482 dari 7.047 baris valid bernilai $0\text{ kg/ha}$ ($77,79\%$).
- Kuartil: $Q_1=0$, $Q_2=0$, $Q_3=0$, persentil 90: $6.000\text{ kg/ha}$, persentil 95: $12.000\text{ kg/ha}$.
- **Nilai Maksimum:** **$166.666,55\text{ kg/ha}$** ($\approx 166,7\text{ ton kompos/ha}$).
- Sebanyak 381 baris memiliki nilai $> 10.000\text{ kg/ha}$, 10 baris $> 50.000\text{ kg/ha}$, dan 1 baris mencapai $166.666,55\text{ kg/ha}$.

> [!WARNING]
> **Peringatan Metodologis Anomali `comp_kg_ha`:**
> Nilai $166.666,55\text{ kg/ha}$ merupakan **pencilan ekstrem (*extreme outlier*)** yang melampaui dosis wajar budidaya tanaman pangan. Namun, **tidak dapat langsung dipastikan bahwa nilai ini diakibatkan oleh kesalahan konversi satuan** karena belum tersedia bukti dokumentasi resmi terkait riwayat pencatatan enumerator survei. Nilai ini dicatat secara objektif sebagai **anomali data yang wajib diverifikasi dan diputuskan strategi penanganannya (apakah melalui winsorization/capping, trimming, atau perlakuan khusus) pada tahap Data Preparation**.

---

## 5. Temuan Utama Exploratory Data Analysis (EDA)

### A. Evaluasi Rinci Hubungan Variabel `hybrid` terhadap Yield
Tabel di bawah menyajikan komparasi hasil panen jagung berdasarkan adopsi benih hibrida secara transparan dengan filter yang konsisten:

| Kelompok Variabel `hybrid` | Definisi Filter Pandas | Jumlah Observasi ($N$) | Proporsi (%) | Mean (kg/ha) | Median (kg/ha) | Std (kg/ha) | Min (kg/ha) | Max (kg/ha) |
|---|---|---|---|---|---|---|---|---|
| **Benih Hibrida (`True`)** | `df['hybrid'] == True` | **10.734** | $72,66\%$ | **$3.185,65$** | **$2.934,37$** | 1.706,18 | 0,00 | 10.798,74 |
| **Bukan Hibrida (`False`)** | `df['hybrid'] == False` | **2.809** | $19,01\%$ | **$2.264,38$** | **$1.996,59$** | 1.461,53 | 0,00 | 11.139,13 |
| **Data Hilang (`NaN`)** | `df['hybrid'].isna()` | **1.230** | $8,33\%$ | **$2.688,21$** | **$2.350,44$** | 1.497,60 | 0,00 | 9.701,31 |
| **Total Keseluruhan** | Seluruh data ($N=14.773$) | **14.773** | $100,00\%$ | **$2.969,06$** | **$2.713,87$** | 1.686,07 | 0,00 | 11.139,13 |

*Interpretasi:*
- Petani yang menanam benih hibrida mencatatkan rata-rata hasil panen **$3.185,65\text{ kg/ha}$**, lebih tinggi **$+921,27\text{ kg/ha}$ ($+40,69\%$)** dibandingkan petani yang menanam benih non-hibrida/lokal (**$2.264,38\text{ kg/ha}$**).
- Nilai median benih hibrida ($2.934,37\text{ kg/ha}$) juga unggul $+46,97\%$ dibandingkan non-hibrida ($1.996,59\text{ kg/ha}$).
- Observasi dengan status `hybrid` yang hilang (*missing*, $N=1.230$) memiliki rata-rata di tengah-tengah ($2.688,21\text{ kg/ha}$).

### B. Variasi Hasil Panen Antar-Negara
- **Rwanda** memiliki median yield tertinggi ($3.277\text{ kg/ha}$, mean $3.417\text{ kg/ha}$), didukung oleh wilayah dataran tinggi dengan curah hujan teratur dan adopsi input yang intensif.
- **Kenya** ($2.765\text{ kg/ha}$) dan **Tanzania** ($2.689\text{ kg/ha}$) memiliki rentang sebaran terluas.
- **Burundi** ($1.663\text{ kg/ha}$) dan **Nigeria** ($1.639\text{ kg/ha}$) memiliki produktivitas terendah.

### C. Korelasi Variabel Numerik Utama terhadap Yield
- **Korelasi Positif Terkuat:** Pupuk Fosfat (`P_kg_ha`, $r = +0,180$), Elevasi (`elev`, $r = +0,179$), Kematangan Hibrida (`hyb_mat`, $r = +0,178$), Pupuk Nitrogen (`N_kg_ha`, $r = +0,159$), Bahan Organik Tanah (`soil_orgC`, $r = +0,151$), dan Kepadatan Tanaman (`pl_m2`, $r = +0,117$).
- **Korelasi Negatif Terkuat:** Suhu Rata-rata Musim (`avg_season_tavg`, $r = -0,186$) dan Kode Zona Agroklimat (`cz`, $r = -0,097$). Daerah dengan suhu yang terlalu panas memperpendek fase pengisian biji jagung.

---

## 6. Feature Relevance dan Evaluasi Skenario Fitur (Pre-Planting vs In-Season vs Post-Harvest)

Untuk kebutuhan **perencanaan produksi kapasitas pakan**, fitur diklasifikasikan secara ketat berdasarkan **waktu ketersediaan informasi (*chronological availability*)** saat model dijalankan:

| Skenario Ketersediaan | Daftar Variabel | Rekomendasi Pemodelan | Alasan Metodologis |
|---|---|---|---|
| **Tier 1: Pre-Planting (Sebelum Tanam)** | `elev`, `twi`, `lat`, `lon`, `soil_pH`, `soil_clay`, `soil_orgC`, `soil_ECEC`, `soil_rzpawhc`, `avg_season_gdd`, `avg_season_ai`, `avg_season_tavg`, `plant_doy`, `hybrid`, `hyb_mat` | **Sangat Direkomendasikan** untuk model perencanaan awal | Sepenuhnya bebas dari risiko data leakage. Karakteristik topografi, tanah, iklim makro/historis, jadwal rencana tanam, dan pilihan benih sudah diputuskan sebelum tanam. |
| **Tier 2: In-Season (Selama Pertumbuhan)** | `season_prec (1,2,3)`, `N_kg_ha`, `P_kg_ha`, `K_kg_ha`, `fert_in_hole`, `lime_kg_ha`, `comp_kg_ha`, `pl_m2`, `row_spacing`, `weeding`, `pesticide`, `pest`, `disease`, `water_excess`, `striga` | **Direkomendasikan Bersyarat** untuk pembaruan prediksi tengah musim | **PENEGASAN PENTING:** `pest`, `disease`, `water_excess`, dan `pesticide` **TIDAK BISA dimasukkan ke dalam model pre-planting** karena serangan hama/penyakit dan penyemprotan pestisida baru terjadi sepanjang masa tanam. |
| **Post-Harvest / Data Leakage Risks** | `harvest_date`, durasi tanam aktual (`harvest_date - plant_date`) | **WAJIB DIELIMINASI** | **Kebocoran Data Fatal.** Tanggal panen riil dan panjang musim panen hanya diketahui setelah panen selesai; tidak tersedia saat perencanaan pra-tanam. |
| **Identitas Administratif Lokal** | `iso` (redundan dengan `country`), `strat` (kode internal One Acre Fund), `cz` (kode zona Afrika) | **Dieliminasi** dari model generalisasi | Menghindari overfitting pada label administratif lokal yang tidak dapat digeneralisasi ke luar wilayah survei. |
| **Missingness Kritis (>50%)** | `manure`, `striga`, `hyb_type`, `hyb_yor`, `comp_kg_ha` | **Dieliminasi** dari prediktor utama | Mengurangi distorsi akibat imputasi berlebih pada kolom yang lebih dari separuh datanya kosong. |

---

## 7. Relevansi terhadap Konteks Penelitian (Sumenep & ASA Indonesia)

### A. Evaluasi Kesenjangan Agroklimat (Afrika Sub-Sahara vs Sumenep, Madura)
> [!WARNING]
> **Dataset 2 One Acre Fund TIDAK DAPAT dianggap mewakili kondisi agroklimat Kabupaten Sumenep secara langsung tanpa kalibrasi parameter lokal.**

1. **Topografi & Elevasi:** Lahan One Acre Fund berada di dataran tinggi pegunungan Afrika Timur (rata-rata $1.590\text{ mdpl}$), sedangkan lahan jagung di Sumenep berada di dataran rendah pesisir tropis ($0 - 100\text{ mdpl}$).
2. **Suhu Udara:** Suhu rata-rata survei One Acre Fund adalah $19,8^\circ\text{C}$ (sejuk), sedangkan Sumenep bersuhu panas tropis ($28 - 34^\circ\text{C}$). Laju respirasi dan kebutuhan air tanaman di Sumenep jauh lebih tinggi.
3. **Tanah & Keasaman:** Tanah survei Afrika didominasi tanah masam pelapukan lanjut (rerata pH 5,71), sedangkan Sumenep didominasi tanah mediteran berkapur dan grumosol dengan pH netral hingga agak basa (pH 6,5–7,8).
4. **Varietas Jagung:** Petani Afrika menggunakan hibrida komersial Afrika Timur (adopsi 72,7%), sedangkan petani Sumenep dominan menanam jagung lokal Madura (varietas Guluk-guluk, Kretek) yang berumur sangat genjah (70–80 hari) dengan produktivitas tipikal 2,0–3,5 ton/ha.

---

### B. Pemisahan Kerangka Konseptual Konversi Pakan Ayam dari Hasil Data Understanding

> [!IMPORTANT]
> **Pemisahan Ruang Lingkup Analisis:**
> 1. **Hasil Murni Data Understanding Dataset 2:** Terbatas pada pemahaman empiris terhadap struktur data, kualitas variabel, karakteristik target, dan perilaku budidaya jagung petani kecil di Afrika Sub-Sahara.
> 2. **Formulasi Konversi Pakan Ayam Petelur:** Merupakan **kerangka konseptual eksternal / model skenario perencanaan** yang dirancang khusus untuk konteks skripsi di Komunitas ASA Indonesia, **bukan kesimpulan atau temuan empiris yang dihasilkan oleh dataset One Acre Fund**.
> 3. **Validasi Parameter Peternakan:** Parameter konsumsi pakan harian layer ($110 - 120\text{ g/ekor/hari}$) dan proporsi jagung dalam formulasi ransum ($50\% - 55\%$) adalah **parameter teknis peternakan yang memerlukan rujukan literatur ilmiah tersendiri** (misal panduan manajemen galur *Hy-Line Brown* atau standar nutrisi ternak tropis), serta wajib dikonfirmasi langsung dengan kondisi peternakan riil mitra ASA Indonesia di Kabupaten Sumenep.

#### Formulasi Matematis Kerangka Perencanaan Konseptual:
1. **Estimasi Produksi Jagung Total ($P_{\text{jagung}}$):**
   $$P_{\text{jagung}} = L_{\text{lahan}}\text{ (ha)} \times \hat{Y}_{\text{prediksi}}\text{ (kg/ha)}$$
2. **Jagung Bersih untuk Pakan Ternak ($Q_{\text{pakan}}$):**
   $$Q_{\text{pakan}} = P_{\text{jagung}} \times (1 - \alpha_{\text{susut}}) \times (1 - \beta_{\text{jual}})$$
   *Keterangan:* $\alpha_{\text{susut}}$ adalah persentase susut pasca-panen (pipil dan pengeringan); $\beta_{\text{jual}}$ adalah persentase jagung yang dijual komersial atau dikonsumsi rumah tangga.
3. **Kebutuhan Pakan Jagung per Ekor Ayam Petelur ($K_{\text{tahunan}}$):**
   Berdasarkan rujukan literatur manajemen unggas komersial:
   - Konsumsi ransum harian layer fase layer/produksi ($FI$): $110 - 120\text{ gram/ekor/hari}$ (rata-rata $0,115\text{ kg/hari}$).
   - Proporsi jagung dalam formula ransum seimbang ($P_{\text{maize}}$): $50\% - 55\%$.
   - Kebutuhan harian: $k_{\text{harian}} = 0,115\text{ kg} \times 0,55 = 0,06325\text{ kg jagung/ekor/hari}$.
   - Kebutuhan jagung per ekor selama 1 tahun ($T = 365\text{ hari}$):
     $$K_{\text{tahunan}} = 0,06325 \times 365 \approx 23,09\text{ kg jagung/ekor/tahun}$$
4. **Kapasitas Dukung Populasi Ayam Petelur ($N_{\text{ayam}}$):**
   $$N_{\text{ayam}} = \left\lfloor \frac{Q_{\text{pakan}}}{K_{\text{tahunan}}} \right\rfloor$$

*Simulasi Kasus Skenario:*
Jika seorang peternak mitra mengalokasikan lahan $0,5\text{ ha}$ dengan estimasi yield $3.200\text{ kg/ha}$ (produksi $1.600\text{ kg}$), susut $8\%$, dan $75\%$ dialokasikan untuk pakan ayam mandiri ($Q_{\text{pakan}} = 1.104\text{ kg}$ jagung), maka kapasitas ayam petelur yang dapat didukung pakan jagungnya selama 1 tahun adalah:
$$N_{\text{ayam}} = \frac{1.104\text{ kg}}{23,09\text{ kg/ekor}} \approx 47 - 48\text{ ekor ayam petelur}.$$

### C. Parameter yang Wajib Dikonfirmasi dari Mitra ASA Indonesia
1. Luasan dan tipologi lahan jagung riil per peternak mitra di Sumenep (tegalan/pekarangan sempit $0,1 - 0,5\text{ ha}$).
2. Varietas jagung dominan (jagung lokal Madura Guluk-guluk/Kretek vs hibrida nasional BISI/Pioneer).
3. Catatan produktivitas ubinan historis di Sumenep (benchmark BPS Sumenep: 2,5–3,8 ton/ha).
4. Persentase riil hasil panen yang dialokasikan untuk pakan ayam mandiri vs dijual tunai.
5. Formulasi ransum pakan aktual (apakah membuat pakan campur sendiri / *self-mixing* berbasis konsentrat + jagung + dedak, atau pakan komersial utuh).

---

## 8. Kesimpulan Kelayakan Dataset 2 dan Rekomendasi

### Kesimpulan Kelayakan
1. **Status Kelayakan:** **LAYAK SEBAGAI DATASET BENCHMARK EMPIRIS DUNIA NYATA.**
2. Dataset 2 memiliki keunggulan pada **keaslian data lapangan**, **skala sampel memadai (14.773 baris)**, **keberagaman interaksi agronomi**, dan **kelengkapan variabel target 100%**.
3. Namun, Dataset 2 **tidak dapat digunakan sebagai representasi langsung agroklimat Sumenep** karena disparitas topografi dataran tinggi, suhu, jenis tanah, dan varietas benih.

### Rekomendasi Tahap Selanjutnya
1. **Perlakuan Fitur:** Terapkan filtrasi fitur pra-tanam (*pre-planting*) dan eliminasi fitur pasca-panen (`harvest_date`) untuk mencegah *data leakage*.
2. **Kombinasi dengan Data Kontekstual Mitra:** Gunakan elastisitas respon agronomi dari Dataset 2 (dosis N/P, kerapatan tanam, adopsi benih unggul) sebagai pembanding perilaku model, sementara parameter absolut disesuaikan dengan data lokal Sumenep.
3. **Data Preparation:** Lakukan penanganan anomali ekstrem `comp_kg_ha`, evaluasi imputasi regional pada fitur tanah, dan uji pemodelan bertahap (*hurdle model*) untuk mengakomodasi 263 observasi hasil panen nol ($1,78\%$).

---

## 9. Inventaris File yang Dihasilkan

Seluruh artefak hasil analisis Dataset 2 telah disimpan secara mandiri dan terstruktur di dalam direktori `03_Exploration/Dataset_02_One_Acre_Fund/`:

```
03_Exploration/Dataset_02_One_Acre_Fund/
├── 01_Data_Understanding_One_Acre_Fund.ipynb  # Notebook 1: Overview & Data Dictionary Terstruktur (Revisi)
├── 02_Data_Quality_EDA_One_Acre_Fund.ipynb    # Notebook 2: Audit Kualitas, Target, EDA, & Relevansi (Revisi)
└── output/
    ├── LAPORAN_DATA_UNDERSTANDING_DATASET_02_ONE_ACRE_FUND.md  # Laporan Markdown Sintesis Lengkap (Revisi)
    ├── figures/
    │   ├── fig01_yield_distribution.png          # Distribusi Target (Histogram, KDE, Boxplot, QQ-Plot)
    │   ├── fig02_yield_by_country.png            # Distribusi Yield antar 7 Negara
    │   ├── fig03_yield_by_year.png               # Tren Yield per Tahun Survei (2016-2022)
    │   ├── fig04_correlation_heatmap.png         # Matriks Korelasi Fitur Teratas
    │   ├── fig05_agronomic_factors_yield.png     # Hubungan Pupuk N, P, Populasi, Benih vs Yield
    │   ├── fig06_environmental_factors_yield.png # Hubungan Elevasi, Suhu, Hujan, pH Tanah vs Yield
    │   ├── fig07_missing_values_overview.png     # Bar Chart Persentase Missing Values
    │   └── fig08_biotic_stress_impact.png        # Dampak Hama, Penyakit, dan Genangan Air
    └── tables/
        ├── data_dictionary_one_acre_fund.csv     # Kamus Data Lengkap 53 Kolom (Revisi Status)
        ├── data_quality_summary.csv              # Ringkasan Kualitas Data Teknis
        ├── target_summary_by_country_year.csv    # Statistik Target Berdasarkan Negara & Tahun
        └── correlation_summary.csv               # Korelasi Pearson & Spearman dengan Target
```

---
*Laporan revisi ini disusun secara independen khusus untuk Dataset 2 One Acre Fund, dengan mempertahankan integritas data mentah dan tanpa mencampurkan data observasi dari Dataset 1.*
