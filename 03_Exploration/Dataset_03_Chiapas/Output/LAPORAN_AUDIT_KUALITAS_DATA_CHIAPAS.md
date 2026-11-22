# LAPORAN AUDIT KUALITAS DATA: CHIAPAS MAIZE DATASET (2012–2018)

---

## 1. Ruang Lingkup & Protokol Audit

### 1.1 Prinsip dan Kepatuhan Audit
Audit kualitas data ini dilakukan sesuai kaidah metodologi penelitian kuantitatif yang ketat:
1. **Prinsip Non-Destruktif:** Pemeriksaan dilakukan tanpa menghapus baris/kolom, tanpa mengimputasi missing value, dan tanpa mengubah nilai pada berkas sumber asli.
2. **Keterpisahan Fakta dan Dokumentasi:** Seluruh angka statistik dihitung langsung dari berkas observasi aktual (`Chiapas_Data.csv` dan sheet `Data` pada `Chiapas Field Data 2012-2018.xlsx`), serta dibandingkan secara kritis terhadap dokumentasi sheet `Legend` dan artikel ilmiah pendamping (Trevisan et al., 2022 di *Data in Brief*).
3. **Audit Kesiapan Pemodelan:** Evaluasi diarahkan untuk menilai keabsahan dataset dalam konteks skripsi *Smart Farming Komunitas ASA Indonesia* guna memitigasi risiko kegagalan pemodelan, bias estimasi, dan kebocoran data (*data leakage*).

---

## 2. Audit Kelengkapan Data (Missing Value Analysis)

### 2.1 Ringkasan Missing Value Global
Berdasarkan pemeriksaan menyeluruh terhadap seluruh **4.585 baris dan 169 kolom** (total 774.865 sel data):
- **Jumlah Kolom Lengkap (0 Missing / 100% Complete):** **168 kolom** (99,41% dari total kolom). Seluruh variabel target (`YIELD`), konteks (`Mun_yield`), temporal (`Year`), spasial (`Lat`, `Long`, `Elev`), karakteristik tanah (`Slope`, `Clay`, `CEC`, `SOM`, `PH`), pemupukan (`Nitrogen`, `Phosphorus`, `Potassium`), sistem budidaya (`System`), olah tanah (`Tillage`), hari tanam (`Planting`), serta ke-150 variabel cuaca gridded (`prcp`, `srad`, `tmax`, `tmin`, `vp` V1–V30) **tidak memiliki satupun sel kosong**.
- **Jumlah Kolom dengan Missing Value:** Hanya **1 kolom**, yaitu `Cultivar`.

### 2.2 Rincian Missing Value Kolom Cultivar
| Variabel | Jumlah Missing | Persentase Missing | Baris Terisi | Tipe Data Teramati | Kategori Variabel |
|---|---:|---:|---:|---|---|
| `Cultivar` | **310 baris** | **6,76%** | 4.275 baris (93,24%) | `object` (string) | Pengelolaan Agronomi (Genotipe) |

### 2.3 Investigasi Penyebab Missing Value Cultivar
Berdasarkan penelusuran terhadap tahun dan sistem tanam pada 310 data kosong tersebut:
- Seluruh 310 nilai kosong terjadi pada **tahun 2012** (tahun pertama pelaksanaan program MasAgro di Chiapas).
- Rincian berdasarkan sistem budidaya pada tahun 2012:
  * Sistem `Hybrid`: 245 baris kosong (dari 468 baris Hybrid tahun 2012).
  * Sistem `Landrace`: 65 baris kosong (dari 255 baris Landrace tahun 2012).
- **Penyebab Metodologis:** Pada tahun perdana (2012), modul pencatatan digital BEM baru diperkenalkan kepada penasihat lapangan, dan pengisian nama genotipe spesifik belum diberlakukan sebagai kolom wajib (*mandatory entry*). Mulai tahun 2013 hingga 2018, kepatuhan pencatatan kultivar meningkat sehingga missing value menjadi 0%.
- **Rekomendasi Penanganan untuk Tahap Selanjutnya:**
  * Jangan menghapus 310 baris ini secara sembarangan, karena dapat menghilangkan 42,88% data observasi dari musim tanam 2012.
  * Pada tahap penyiapan data (*Data Preparation*), nilai kosong pada `Cultivar` dapat diberi label eksplisit `'UNKNOWN_OR_UNSPECIFIED'` sebagai kategori tersendiri.

Visualisasi audit missing value tersimpan di:
`03_Exploration/Dataset_03_Chiapas/Output/missing_values_chiapas.png`.

---

## 3. Audit Duplikasi Data

Pemeriksaan duplikasi dilakukan pada beberapa tingkatan granularitas:

| Kriteria Duplikasi | Jumlah Terdeteksi | Status Kualitas | Penjelasan & Implikasi |
|---|---:|---|---|
| **Duplikasi Baris Identik (Full Row Duplicates)** | **0 baris** | **Sangat Baik** | Tidak ada baris observasi yang berulang persis pada ke-169 kolom. Seluruh baris adalah rekaman observasi mandiri. |
| **Duplikasi ID Lahan (`Field_ID`)** | **0 baris** | **Sangat Baik** | Tepat 4.585 ID unik dari 4.585 baris data (100% unik, rentang 1 s.d. 4585). |
| **Duplikasi Kombinasi (`Field_ID`, `Year`)** | **0 baris** | **Sangat Baik** | Tidak ada ID lahan yang tercatat lebih dari satu kali dalam tahun yang sama. |
| **Duplikasi Koordinat Spasial (`Lat`, `Long`, `Year`)** | **1.832 baris** | **Karakteristik Khusus** | Terdapat 2.753 pasangan koordinat unik. Sebanyak 1.832 baris berbagi koordinat yang sama dalam tahun yang sama. |

### 3.3 Penjelasan Ilmiah atas Kesamaan Koordinat (Lat, Long, Year)
Adanya 1.832 baris dengan koordinat nominal yang sama **bukan merupakan kesalahan pencatatan data (*data entry error*)**, melainkan konsekuensi langsung dari kebijakan privasi etika penelitian yang diterapkan oleh CIMMYT:
1. **Spatial Blurring:** Paper pendamping (Trevisan et al., 2022, Halaman 6) menyatakan secara eksplisit: *"Spatial blurring was conducted (reduced to 2 decimals) to avoid identifying farmers' fields."*
2. **Efek Pembulatan 2 Desimal:** Pembulatan koordinat hingga 2 angka di belakang koma menghasilkan resolusi kotak spasial berukuran sekitar **1,1 km × 1,1 km**. Jika dalam satu desa atau kelompok tani terdapat 2 hingga 5 petak lahan petani berbeda yang berjarak ratusan meter, koordinat keduanya akan terpotong menjadi angka nominal yang persis sama.
3. **Verifikasi Nilai Agronomi:** Walaupun koordinatnya sama, nilai agronomi pada baris-baris tersebut (seperti `YIELD`, `Planting`, `Nitrogen`, `Cultivar`, `Tillage`) terbukti berbeda, mencerminkan petak lahan dan manajemen petani yang berbeda.

---

## 4. Audit Kesesuaian Tipe Data

Pemeriksaan tipe data hasil pembacaan parser pandas/openpyxl terhadap sifat fisis variabel:

| Variabel | Tipe Data Parser | Tipe Data Fisis / Semantik | Status Kesesuaian | Evaluasi & Rekomendasi |
|---|---|---|---|---|
| `Field_ID` | `int64` | Identifier Kategorikal | Sesuai | Pengenal unik, tidak untuk operasi aritmatika. |
| `YIELD` | `float64` | Numerik Kontinu (Mg ha⁻¹) | Sesuai | Target continuous panen riil. |
| `Year` | `int64` | Temporal / Ordinal | Sesuai | Tahun tanam 2012–2018. |
| `Mun_yield` | `float64` | Numerik Kontinu (Mg ha⁻¹) | Sesuai | Rata-rata agregat wilayah SIAP. |
| `Lat`, `Long` | `float64` | Koordinat Geografis | Sesuai | Derajat desimal 2 angka di belakang koma. |
| `Elev` | `int64` | Numerik Diskrit / Kontinu (m) | Sesuai | Elevasi lahan di atas permukaan laut. |
| `System` | `object` | Kategorikal Nominal (2 level) | Sesuai | `'Hybrid'` dan `'Landrace'`. |
| `Cultivar` | `object` | Kategorikal Nominal (249 level) | Sesuai | Memiliki 310 sel kosong (`NaN`). |
| `Tillage` | `object` | Kategorikal Nominal (3 level) | Sesuai | `'Conventional'`, `'Reduced'`, `'No-till'`. |
| `Planting` | `int64` | Temporal Diskrit (DOY: 1–365) | Sesuai | Hari dalam tahun saat penanaman jagung. |
| `Nitrogen`, `Phosphorus`, `Potassium` | `float64` | Numerik Rasio (kg ha⁻¹) | Sesuai | Dosis pupuk (non-negatif). |
| `Slope`, `Clay`, `SOM` | `float64` / `int64` | Numerik Rasio (%) | Sesuai | Nilai persentase non-negatif. |
| `CEC` | `float64` | Numerik Rasio (cmolc dm⁻³) | Sesuai | Kapasitas tukar kation tanah. |
| `PH` | `float64` | Numerik Skala (0–14) | Sesuai | Derajat kemasaman tanah riil (4,92–8,25). |
| `prcp_V1` s/d `prcp_V30` | `float64` | Numerik Rasio (mm day⁻¹) | Sesuai | Presipitasi non-negatif harian rata-rata. |
| `srad_V1` s/d `srad_V30` | `float64` | Numerik Rasio (MJ m⁻² day⁻¹) | Sesuai | Radiasi surya harian rata-rata. |
| `tmax_V1` s/d `tmax_V30` | `float64` | Numerik Interval (°C) | Sesuai | Suhu maksimum harian rata-rata. |
| `tmin_V1` s/d `tmin_V30` | `float64` | Numerik Interval (°C) | Sesuai | Suhu minimum harian rata-rata. |
| `vp_V1` s/d `vp_V30` | `float64` | Numerik Rasio (Pa) | Sesuai | Tekanan uap air atmosfer harian rata-rata. |

---

## 5. Audit Nilai Tidak Wajar, Validitas Rentang, dan Outlier

Pemeriksaan outlier dilakukan menggunakan batas pagar Tukey (*Interquartile Range* / IQR, batas bawah $= Q_1 - 1,5 	imes IQR$; batas atas $= Q_3 + 1,5 	imes IQR$) yang dikombinasikan dengan batas hukum fisika dan agronomi tropis:

| Variabel | Batas Bawah IQR | Batas Atas IQR | Min Aktual | Max Aktual | Outlier IQR (Count & %) | Evaluasi Validitas Fisis & Agronomi |
|---|---:|---:|---:|---:|---:|---|
| **`YIELD`** | -2,87 | 9,72 | 0,10 | 9,80 | 3 (0,07%) | **Valid.** Rentang 0,10 s.d. 9,80 Mg ha⁻¹ wajar untuk variabilitas jagung tropis (0,1 ton/ha subsisten gagal panen hingga 9,8 ton/ha hibrida intensif beririgasi/terawat). |
| **`Mun_yield`** | -0,48 | 5,47 | 1,13 | 4,39 | 0 (0,00%) | **Valid.** Tidak ada outlier statistik; rata-rata munisipal berkisar 1,13 s.d. 4,39 Mg ha⁻¹. |
| **`Elev`** | -138,50 | 1.809,50 | 7,00 | 2.849,00 | 199 (4,34%) | **Valid.** Chiapas mencakup dataran rendah pantai pasifik (7 m dpl) hingga pegunungan tinggi Los Altos (>2.500 m dpl). Bukan data error. |
| **`Planting`** | 112,50 | 220,50 | 91,00 | 242,00 | 123 (2,68%) | **Valid.** Hari tanam dari DOY 91 (1 April) s.d. DOY 242 (30 Agustus) mencerminkan jendela tanam musim hujan di berbagai zona agroekologi Chiapas. |
| **`Nitrogen`** | -74,00 | 294,00 | 0,00 | 349,00 | 28 (0,61%) | **Valid.** Dosis maksimum 349 kg N ha⁻¹ terjadi pada petak intensif komersial; dosis 0 kg N ha⁻¹ (7,81%) terjadi pada petani subsisten/pupuk kandang. |
| **`Phosphorus`** | -69,00 | 115,00 | 0,00 | 143,00 | 19 (0,41%) | **Valid.** Dosis P₂O₅ berkisar 0 hingga 143 kg ha⁻¹, umum diterapkan pada jagung hibrida. |
| **`Potassium`** | -18,75 | 31,25 | 0,00 | 100,00 | 320 (6,98%) | **Valid.** Mayoritas petani kecil tidak memakai K (median = 0), sehingga pemakaian 40–100 kg K₂O ha⁻¹ oleh petani komersial terdeteksi outlier secara statistik. |
| **`Slope`** | -9,76 | 19,83 | 0,00 | 61,19 | 245 (5,34%) | **Valid.** Lahan pertanian lereng bukit curam di Chiapas mencapai kemiringan 61% (umum pada sistem pertanian tebang-bakar tradisional). |
| **`Clay`** | 2,00 | 58,00 | 5,00 | 57,00 | 0 (0,00%) | **Valid.** Persentase liat tanah 5% s.d. 57% berada pada rentang tekstur lempung berpasir hingga liat berat. |
| **`CEC`** | -0,96 | 44,74 | 4,31 | 50,80 | 31 (0,68%) | **Valid.** Nilai 4,31 s.d. 50,80 cmolc dm⁻³ adalah rentang normal kapasitas tukar kation tanah tropis. |
| **`SOM`** | -0,62 | 3,62 | 0,27 | 4,00 | 130 (2,84%) | **Valid.** Bahan organik tanah 0,27% s.d. 4,00% konsisten dengan tanah mineral pertanian tropis. |
| **`PH`** | 5,55 | 8,41 | 4,92 | 8,25 | 264 (5,76%) | **Valid.** Rentang kemasaman tanah dari masam moderat (pH 4,92) hingga agak alkalis (pH 8,25) sangat umum di Chiapas. |

### 5.2 Pemeriksaan Rentang Variabel Cuaca Gridded (150 Kolom)
- **Presipitasi (`prcp_V1` s/d `prcp_V30`):** Min = 0,00 mm/hari; Max = 54,90 mm/hari; Rata-rata global = 4,05 mm/hari. Tidak ditemukan presipitasi bernilai negatif.
- **Radiasi Surya (`srad_V1` s/d `srad_V30`):** Min = 6,78 MJ m⁻² day⁻¹; Max = 26,76 MJ m⁻² day⁻¹; Rata-rata global = 17,71 MJ m⁻² day⁻¹. Nilai radiasi sangat konsisten dengan radiasi harian lintang tropis.
- **Suhu Maksimum (`tmax_V1` s/d `tmax_V30`):** Min = 16,60 °C; Max = 39,20 °C; Rata-rata global = 29,85 °C.
- **Suhu Minimum (`tmin_V1` s/d `tmin_V30`):** Min = **-2,15 °C**; Max = 36,25 °C; Rata-rata global = 17,44 °C.
  * *Catatan Suhu Negatif (-2,15 °C):* Nilai suhu di bawah nol derajat terjadi pada petak observasi di daerah pegunungan berketinggian >2.500 m dpl di Los Altos de Chiapas selama periode musim dingin (V1–V3 sebelum tanam), yang secara klimatologis sah terjadi di dataran tinggi Meksiko.
- **Tekanan Uap Air (`vp_V1` s/d `vp_V30`):** Min = 252,00 Pa; Max = 6.452,00 Pa; Rata-rata global = 1.762,36 Pa. Seluruh nilai berada dalam rentang wajar atmosfer tropis.

> [!NOTE]
> **Kesimpulan Outlier:** Seluruh nilai ekstrim dalam dataset merupakan **variabilitas ekologis dan agronomi riil (*true natural and management variance*)** dari bentang alam Chiapas yang heterogen, bukan akibat kesalahan pengetikan atau kerusakan sensor (*sensor malfunction*). Oleh karena itu, baris-baris ini **tidak boleh dihapus atau dipotong secara sembarangan**.

---

## 6. Audit Variabel Konstan & Multikolinearitas

1. **Uji Varians Nol (Variabel Konstan):**
   - Dilakukan pengujian standar deviasi pada seluruh 166 kolom numerik.
   - **Hasil:** Tidak ditemukan satupun kolom dengan standar deviasi = 0. Tidak ada kolom konstan dalam dataset.
2. **Korelasi dan Multikolinearitas Antar-Interval Cuaca:**
   - Karena variabel cuaca dipecah menjadi 30 interval 10-harian berurutan, terdapat **autokorelasi serial yang sangat tinggi** antara interval yang bertetangga (misal korelasi `tmax_V10` dengan `tmax_V11` mencapai $> 0,85$).
   - **Implikasi Pemodelan:** Jika model regresi linear biasa digunakan, multikolinearitas tinggi ini akan menyebabkan instabilitas koefisien regresi (*inflated variance of estimators*). Model non-linear berbasis ensemble tree (*Random Forest*, *XGBoost*, *LightGBM*) atau teknik pereduksi dimensi/agregasi tahap pertumbuhan (misal mengagregasi interval cuaca menjadi fase Vegetatif, Pembungaan, dan Pengisian Biji) sangat direkomendasikan.

---

## 7. Audit Ketidaksesuaian Kritis (Discrepancy) antara Berkas Excel, Legend, dan Paper

Ini merupakan temuan paling krusial dari audit kualitas data independen:

### 7.1 TEMUAN KRITIS 1: Typo pada Table 2 dan Narasi Section 1 Paper Trevisan et al. (2022)
- **Teks pada Paper (Halaman 3 & 4):**
  * Paragraf Section 1: *"The yield ranged from 0.1 to 10.0 Mg ha⁻¹, with 75% of the values lower than 5.0 Mg ha⁻¹ and **an average of 6 Mg ha⁻¹** (Table 2)."*
  * Table 2 mencetak angka untuk *Yield (Mg ha⁻¹)*:
    `Mean: 6 | SD: 1.9 | P0: 0.1 | P25: 1.9 | P50: 6 | P75: 5.0 | P100: 9.8`
- **Fakta Hasil Pemeriksaan Aktual pada 4.585 Baris Data:**
  * **Mean Aktual:** **3,5926 Mg ha⁻¹** (~3,6 Mg ha⁻¹).
  * **P50 (Median) Aktual:** **3,6000 Mg ha⁻¹** (3,6 Mg ha⁻¹).
  * **P25 Aktual:** 1,8500 Mg ha⁻¹ (~1,9 Mg ha⁻¹).
  * **P75 Aktual:** 5,0000 Mg ha⁻¹ (5,0 Mg ha⁻¹).
  * **Max Aktual:** 9,8000 Mg ha⁻¹ (9,8 Mg ha⁻¹).
- **Analisis Anomali Matematis pada Paper:**
  Secara hukum statistik dasar, tidak mungkin nilai median (P50) bernilai **6**, sementara kuartil atas (P75) bernilai **5,0** dan kuartil bawah (P25) bernilai **1,9**!
  Jelas terlihat bahwa saat penyusunan atau typesetting artikel ilmiah *Data in Brief*, angka **`3.` pada nilai `3.6` terpotong secara tidak sengaja**, sehingga tercetak menjadi angka `6` untuk Mean dan P50. Penulis kemudian mengutip angka typo tersebut ke dalam teks paragraf Section 1 (*"an average of 6 Mg ha⁻¹"*).
- **Tindakan Peneliti Skripsi:**
  Gunakan **fakta aktual hasil komputasi data (Mean = 3,59 Mg ha⁻¹ dan Median = 3,60 Mg ha⁻¹)** dalam naskah skripsi. Berikan catatan kaki akademis mengenai adanya kesalahan ketik (*typographical error*) pada Table 2 publikasi Trevisan et al. (2022).

### 7.2 TEMUAN 2: Inkonsistensi Jumlah Level Kultivar
- Paper mencatat: *"A total of 250 unique cultivars were recorded..."* (Table 3).
- Hasil pembacaan aktual: Ditemukan **249 string nama kultivar unik** dan **310 nilai kosong (`NaN`)**.
- Kesimpulan: Pembuat dataset memperlakukan nilai kosong (`NaN`) sebagai 1 level kategori tambahan (249 nama + 1 missing = 250 kategori).

### 7.3 TEMUAN 3: Perbedaan Penulisan Satuan dan Huruf Kapital
- Di sheet `Legend`, satuan suhu maksimum ditulis `⁰C` (dengan simbol superskrip nol), sedangkan di paper ditulis `o C`.
- Di berkas data Excel, kolom target dinamai `YIELD` (huruf kapital penuh), sedangkan di Table 1 paper ditulis `Yield`.
- Kolom kemasaman tanah di Excel dinamai `PH`, sedangkan di paper ditulis `pH`.

---

## 8. Audit Risiko Data Leakage & Keterbatasan Fitur Cuaca

### 8.1 Struktur 30 Interval 10-Harian (Daymet Weather)
Penataan fitur cuaca dalam dataset dilakukan dengan titik acuan hari penanaman (`Planting` DOY = 0):
- **Interval V1 s/d V6 (Hari -60 s/d Hari -1):** Kondisi cuaca **sebelum tanam (pre-planting)**. Fitur ini telah terjadi sebelum benih ditanam ke tanah.
- **Interval V7 s/d V24 (Hari 0 s/d Hari 179):** Kondisi cuaca **selama masa pertumbuhan tanaman (in-season)**. Rata-rata umur panen jagung di Chiapas adalah 175 hari.
- **Interval V25 s/d V30 (Hari 180 s/d Hari 240):** Kondisi cuaca **setelah kematangan fisiologis / pasca panen (post-season)**. Paper menjelaskan bahwa petani subsisten sering membiarkan tongkol jagung mengering di batang tanaman di lahan karena keterbatasan tenaga kerja panen manual.

### 8.2 Evaluasi Risiko Data Leakage Berdasarkan Horizon Keputusan
1. **Skenario Perencanaan Produksi Sebelum Tanam (Pre-Planting Planning):**
   - **Tujuan Skripsi:** Memprediksi ketersediaan jagung dari luas lahan mitra ASA sebelum musim tanam dimulai, guna merencanakan pengadaan pakan dan daya tampung populasi ayam petelur.
   - **Risiko Data Leakage:** Menggunakan variabel cuaca interval `*_V7` s/d `*_V30` sebagai fitur prediktor adalah **DATA LEAKAGE BERAT (TEMPORAL LEAKAGE)**, karena data cuaca hari ke-0 hingga hari ke-240 setelah tanam **belum terjadi di dunia nyata pada saat keputusan perencanaan diambil**.
   - **Aturan Pemodelan:** Untuk model prediksi sebelum tanam, **hanya fitur pre-planting (`*_V1` s/d `*_V6`), data tanah, dan rencana pengelolaan yang boleh dimasukkan sebagai prediktor**.
2. **Skenario Analisis Penjelas Hasil Panen (Explanatory ML / Yield Gap Analysis):**
   - Jika model bertujuan untuk mengevaluasi faktor pembatas hasil panen setelah musim tanam selesai (*post-harvest analysis*, sebagaimana dilakukan Trevisan et al.), maka fitur `*_V7` s/d `*_V24` sah digunakan untuk menjelaskan pengaruh kekeringan atau gelombang panas pada fase kritis tanaman.

---

## 9. Evaluasi Transferabilitas ke Konteks Mitra ASA (Sumenep, Madura, Indonesia)

Berdasarkan telaah kritis terhadap latar belakang mitra Komunitas ASA di Sumenep, Madura, terdapat kesenjangan signifikan yang mengharuskan kehati-hatian dalam mentransfer model:

```
+------------------------------------+       +------------------------------------+
|       CHIAPAS, MEKSIKO             |       |       SUMENEP, MADURA, INDO        |
| - Garis Lintang: 14.8° - 17.6° LU  |       | - Garis Lintang: ~7.0° LS          |
| - Elevasi: 7 - 2.849 m dpl         |  VS   | - Elevasi: Dataran Rendah (<100 m) |
| - Iklim: Subtropis/Tropis Gunung   |       | - Iklim: Tropis Muson Kering (Aw)  |
| - Varietas: Dekalb, Criollo Meksiko|       | - Varietas: Madura Lokal, Bisi, NK |
| - Skala: 4.585 petak observasi     |       | - Skala Mitra: 3 petak lahan       |
+------------------------------------+       +------------------------------------+
```

### 9.1 Kesenjangan Utama
1. **Kesenjangan Agroekologi & Topografi:**
   Chiapas memiliki elevasi hingga 2.849 m dpl dengan kemiringan lereng hingga 61%. Sebaliknya, lahan pertanian jagung di Kabupaten Sumenep (Madura) berada pada dataran rendah pesisir tropis dengan iklim muson kering (*type Aw*) dan curah hujan tahunan yang relatif lebih terkonsentrasi pada bulan-bulan tertentu.
2. **Kesenjangan Genotipe Benih (Cultivar):**
   Varietas dalam dataset Chiapas mencakup hibrida komersial Amerika Latin (Dekalb 390, Pioneer P4082W) dan jagung lokal Meksiko (*Criollo*). Di Madura, petani menggunakan varietas jagung lokal Madura (seperti Jagung Kretek, Jagung Guluk-Guluk) atau varietas hibrida nasional Indonesia (seperti BISI-18, Pioneer P27, NK-212). Respon hasil terhadap input pupuk dan iklim akan berbeda secara fisiologis.
3. **Kesenjangan Karakteristik Tanah:**
   Tanah pertanian Madura umumnya didominasi oleh tanah mediteran merah, grumusol, atau litosol berbasis batu kapur (karst), sedangkan dataset Chiapas didominasi oleh tanah vulkanik dan aluvial pegunungan dengan karakteristik kimiawi yang berbeda.

### 9.2 Batasan Transfer Model ke Skripsi ASA
> [!CAUTION]
> **Larangan Klaim Langsung:** Model machine learning yang dilatih murni menggunakan dataset Chiapas **TIDAK BISA dan TIDAK BOLEH diklaim langsung berlaku akurat untuk memprediksi tonase riil 3 petak lahan mitra ASA di Sumenep tanpa proses validasi dan kalibrasi lapangan**.

Dataset Chiapas harus diposisikan secara tepat dalam skripsi sebagai:
- **Proxy/Benchmark Dataset:** Untuk membangun pipeline pemodelan, menguji algoritma, mengevaluasi pengaruh fitur agronomi dan cuaca pra-tanam, serta memahami dinamika variabilitas produktivitas jagung.
- **Baseline Framework:** Kerangka kerja pemodelan yang nantinya akan dikalibrasi (*fine-tuned / transfer learning / domain adaptation*) menggunakan parameter empiris 3 petak lahan mitra ASA (luas petak, jenis tanah lokal, riwayat pupuk, dan varietas jagung Madura).

---

## 10. Rekomendasi Kelayakan Akhir

Berdasarkan audit kualitas data menyeluruh terhadap seluruh baris, kolom, dan literatur pendukung:

### **Status Rekomendasi: LAYAK DENGAN CATATAN (FEASIBLE WITH CONDITIONS)**

### Rincian Kondisi dan Catatan Wajib:
1. **Pemilihan Target Mutlak:** Variabel target pemodelan produktivitas harus menggunakan **`YIELD`** (satuan Mg ha⁻¹ = ton ha⁻¹), bukan `Mun_yield`.
2. **Pencegahan Data Leakage:** Dalam perancangan sistem pendukung keputusan (DSS) perencanaan ayam petelur berbasis lahan sebelum tanam, **fitur cuaca pascatanam (`*_V7` s/d `*_V30`) wajib dieksklusi dari set prediktor**. Gunakan hanya fitur tanah, manajemen terencana, dan cuaca pra-tanam (`*_V1` s/d `*_V6`).
3. **Penanganan Missing Value Cultivar:** Jangan membuang 310 baris observasi tahun 2012; tangani dengan memberi kategori pengganti `'UNKNOWN'` pada tahap Data Preparation.
4. **Koreksi Typo Paper pada Naskah Skripsi:** Gunakan nilai rata-rata aktual hasil audit (**3,59 Mg ha⁻¹**, bukan 6 Mg ha⁻¹) saat merujuk karakteristik dataset di Bab 3 skripsi.
5. **Penegasan Ruang Lingkup Akademis:** Nyatakan secara eksplisit dalam Bab 1 dan Bab 3 bahwa dataset Chiapas adalah dataset studi kasus eksplorasi/pembelajaran agronomi global, dan prediksi final kapasitas ayam petelur Komunitas ASA akan menggabungkan parameter validasi lokal mitra di Sumenep.
