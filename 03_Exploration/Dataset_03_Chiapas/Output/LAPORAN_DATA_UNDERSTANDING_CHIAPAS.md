# LAPORAN DATA UNDERSTANDING: CHIAPAS MAIZE DATASET (2012–2018)

---

## 1. Identitas Dokumen & Konteks Penelitian

### 1.1 Konteks Skripsi
- **Judul Skripsi:** *Pemodelan Prediksi Jumlah Ayam Petelur untuk Smart Farming Berdasarkan Ketersediaan Lahan Jagung untuk Mendukung Perencanaan Produksi di Komunitas ASA Indonesia.*
- **Program Studi:** Sarjana Terapan Sistem Informasi Bisnis.
- **Domain:** Smart Farming & Decision Support Systems (DSS) untuk Perencanaan Produksi Peternakan dan Pertanian.
- **Peran Dataset:** Dataset utama ini digunakan untuk membangun komponen pemodelan produktivitas jagung (*maize yield prediction*). Hasil prediksi yield per petak lahan nantinya menjadi input estimasi ketersediaan pakan jagung guna menghitung daya tampung kapasitas populasi ayam petelur di mitra Komunitas ASA.
- **Batasan Konteks Penting:** Dataset Chiapas **bukan data ayam petelur** dan **bukan data lokal ASA**. Dataset ini berfungsi sebagai *benchmark / proxy dataset* agronomi skala besar yang kaya variabel (manajemen budidaya, tanah, dan cuaca terstruktur) untuk mempelajari arsitektur model estimasi hasil jagung sebelum dilakukan kalibrasi pada petak riil mitra ASA.

### 1.2 Identitas Paper Pendamping & Sumber Data
- **Judul Artikel:** *Multiyear Maize Management Dataset collected in Chiapas, Mexico.*
- **Jurnal:** *Data in Brief*, Volume 40, Februari 2022, Halaman 107837.
- **DOI:** [https://doi.org/10.1016/j.dib.2022.107837](https://doi.org/10.1016/j.dib.2022.107837)
- **Penulis:** Rodrigo G. Trevisan, Nicolas F. Martin, Simon Fonteyne, Nele Verhulst (Corresponding Author: n.verhulst@cgiar.org), Hugo A. Dorado Betancourt, Daniel Jimenez, dan Andrea Gardeazabal.
- **Institusi Peneliti:**
  1. Department of Crop Sciences, University of Illinois at Urbana-Champaign, USA.
  2. International Maize and Wheat Improvement Center (CIMMYT), Texcoco, Mexico.
  3. International Center for Tropical Agriculture (CIAT), Cali, Colombia.
  4. Universidad Icesi, Cali, Colombia.
- **Penyedia Repositori:** CIMMYT Research Data & Software Repository Network (Dataverse).
- **Persistent Identifier (Handle):** [https://hdl.handle.net/11529/10548624](https://hdl.handle.net/11529/10548624)
- **Lisensi Publikasi:** Creative Commons Attribution (CC BY 4.0).

---

## 2. Ringkasan Eksekutif & Struktur Berkas

Pemeriksaan aktual telah dilakukan langsung terhadap berkas Excel sumber dan naskah publikasi ilmiah pendamping. Rincian verifikasi struktur data adalah sebagai berikut:

| Parameter Pemeriksaan | Status / Nilai Aktual | Catatan Verifikasi |
|---|---|---|
| **Berkas Sumber Asli** | `Chiapas Field Data 2012-2018.xlsx` | Ukuran berkas: 5.149.464 bytes (~5,15 MB), terletak di folder `02_Raw_Data/Dataset_03_Chiapas/`. Berkas asli dipertahankan apa adanya tanpa perubahan (*read-only*). |
| **Identifikasi Sheet** | 2 Sheet: `Legend` dan `Data` | Sheet 1 (`Legend`) berisi dokumentasi/kamus variabel; Sheet 2 (`Data`) berisi observasi lapangan riil. |
| **Jumlah Baris Aktual** | 4.585 Baris Observasi | Total 4.586 baris dalam sheet (1 baris header + 4.585 baris data observasi *cropping events*). |
| **Jumlah Kolom Aktual** | 169 Kolom Variabel | Terdiri dari 19 variabel identifikasi, target, agronomi, tanah, dan 150 variabel cuaca gridded harian 10-hari. |
| **Berkas Salinan CSV** | `Chiapas_Data.csv` | Ukuran berkas: 4.985.377 bytes (~4,98 MB). Dibuat untuk memfasilitasi pembacaan komputasional berkecepatan tinggi. |
| **Verifikasi Integritas Ekspor** | 100% Identik (0 Mismatch) | Audit sel-per-sel (*cell-by-cell matching*) menunjukkan 4.585 baris dan 169 kolom tepat sama antara berkas Excel sheet `Data` dan CSV. |

> [!IMPORTANT]
> **Peringatan Struktur Sheet:** Jangan menganggap sheet pertama sebagai data observasi. Sheet pertama (`Legend`) adalah metadata dokumentasi kamus variabel (dimensi A1:D183), sedangkan data observasi aktual berada pada sheet kedua (`Data`).

---

## 3. Verifikasi Sumber & Metodologi Pengumpulan Data (Berdasarkan Paper)

Berdasarkan naskah *Data in Brief* (Trevisan et al., 2022), data dikumpulkan melalui inisiatif *CIMMYT Knowledge Hub* di Negara Bagian Chiapas, Meksiko bagian selatan, selama 7 musim tanam berturut-turut (2012–2018). Sistem pertanian jagung di wilayah ini didominasi oleh pertanian tadah hujan (*rainfed*) dengan topografi beragam, mencakup dataran pesisir hingga pegunungan tinggi Sierra Madre de Chiapas.

### 3.1 Integrasi Empat Sumber Data
Data yang tersusun dalam berkas merupakan hasil integrasi dari 4 sumber independen:
1. **Data Praktik Agronomi dan Hasil Lapangan (BEM - CIMMYT):**
   - Dikumpulkan secara rutin oleh penasihat lapangan (*farm advisors*) selama kunjungan inspeksi berkala.
   - Pencatatan menggunakan aplikasi buku lapangan digital in-house: **Bitácora Electrónica MasAgro (BEM)**. Sistem BEM dilengkapi validasi logika batas nilai (*entry constraints*), geo-referensi, dan kemampuan sinkronisasi offline-online.
   - Data mencakup: tanggal tanam (`Planting`), kultivar/genotipe (`Cultivar`), sistem budidaya (`System`), metode olah tanah (`Tillage`), pemupukan N, P₂O₅, K₂O (`Nitrogen`, `Phosphorus`, `Potassium`), dan hasil panen aktual (`YIELD`).
   - Plot observasi mencakup dua kategori lahan: *innovation modules* (petak perbandingan praktik konvensional vs praktik perbaikan) dan *extension areas* (lahan adopsi petani).
2. **Data Sifat Fisik dan Kimia Tanah (INEGI & SRTM):**
   - Sifat fungsional tanah diekstrak dari peta poligon digital berskala 1:250.000 terbitan *National Institute of Statistics and Geography* (INEGI, Delerce 2018).
   - Atribut tanah yang diekstrak meliputi fraksi liat (`Clay`), kapasitas tukar kation (`CEC`), bahan organik tanah (`SOM`), dan kemasaman tanah (`PH`).
   - Elevasi (`Elev`) dan kelerengan (`Slope`) diturunkan dari data model elevasi digital *Shuttle Radar Topography Mission* (SRTM 90m, Jarvis et al., 2008).
3. **Data Cuaca Gridded Harian (Daymet v3):**
   - Diperoleh dari dataset *Daymet: Daily Surface Weather Data on a 1-km Grid for North America* (Thornton et al., 2016).
   - Koordinat titik setiap lahan dioverlay pada grid raster 1 km untuk mengekstrak data presipitasi (`prcp`), radiasi surya (`srad`), suhu maksimum (`tmax`), suhu minimum (`tmin`), dan tekanan uap air (`vp`).
   - Nilai harian diagregasikan ke dalam rata-rata interval 10-harian, yang ditata relatif terhadap tanggal tanam aktual masing-masing petak (mulai dari 60 hari sebelum tanam hingga 240 hari setelah tanam, menghasilkan 30 fitur interval V1–V30).
4. **Data Rata-rata Hasil Munisipal (SIAP):**
   - Rata-rata hasil jagung tingkat munisipal (`Mun_yield`) diperoleh dari data statistik publik *Servicio de Información Agroalimentaria y Pesquera* (SIAP, 2020) sebagai konteks agregat produktivitas wilayah.

### 3.2 Unit Observasi dan Definisi Target Panen
- **Unit Observasi:** Satu baris merepresentasikan **satu kejadian budidaya (*cropping event*) pada satu petak lahan (*parcel/field*) dalam satu tahun tanam tertentu**, dengan luas petak rata-rata < 5 hektar. Dataset ini tidak mewakili satu petani unik; satu petani bisa mengelola petak yang berbeda atau petak yang sama pada tahun yang berbeda.
- **Definisi Target Hasil (`YIELD`):**
  - Satuan: **Mg ha⁻¹** (*Megagrams per hectare*, setara dengan **metrik ton per hektar / ton ha⁻¹**). Konversi ke kg/ha adalah dikalikan 1.000 (1 Mg ha⁻¹ = 1.000 kg/ha).
  - Metode Pengukuran Lapangan: Diukur langsung oleh penasihat lapangan dengan cara memanen sampel ubinan seluas 5 m x 1,5 m (mencakup lebar 2 baris tanaman jagung) pada **5 titik representatif** di setiap petak plot.
  - Standardisasi Kadar Air: Kadar air biji jagung hasil panen diukur dan **disesuaikan secara baku ke kadar air 14%** (*moisture content adjusted to 14%*).
  - Pengecualian Subsisten: Khusus untuk petani subsisten tradisional di daerah pegunungan (Ocosingo dan Los Altos), panen dilakukan bertahap selama beberapa bulan untuk konsumsi harian keluarga, sehingga nilai `YIELD` pada area ekstensi tersebut merupakan estimasi hasil yang dilaporkan oleh petani.

---

## 4. Taksonomi dan Deskripsi 169 Variabel

Sebanyak 169 variabel dalam dataset dikelompokkan ke dalam 6 kelompok fungsional:

```
Total 169 Variabel
├── 1. Identifikasi & Temporal (2) : Field_ID, Year
├── 2. Variabel Target & Konteks (2) : YIELD (Target), Mun_yield (Konteks Makro)
├── 3. Spasial & Topografi (3)      : Lat, Long, Elev
├── 4. Pengelolaan Agronomi (7)     : System, Cultivar, Tillage, Planting, Nitrogen, Phosphorus, Potassium
├── 5. Karakteristik Tanah (5)      : Slope, Clay, CEC, SOM, PH
└── 6. Cuaca Gridded Daymet (150)   : 5 Parameter x 30 Interval 10-Harian (prcp, srad, tmax, tmin, vp)
```

### Rincian Kelompok Variabel Non-Cuaca (19 Variabel Pertama)
| No. | Nama Kolom | Tipe Data Parser | Satuan | Deskripsi Berdasarkan Legend & Paper |
|---:|---|---|---|---|
| 1 | `Field_ID` | `int64` | - | Pengenal unik numerik untuk setiap baris kejadian budidaya (*cropping event*). |
| 2 | `YIELD` | `float64` | Mg ha⁻¹ | Hasil panen biji jagung aktual di tingkat petak (*field maize yield*), kadar air 14%. |
| 3 | `Year` | `int64` | Tahun | Tahun musim tanam kejadian budidaya (2012–2018). |
| 4 | `Mun_yield` | `float64` | Mg ha⁻¹ | Rata-rata produktivitas jagung di tingkat munisipal dari statistik SIAP. |
| 5 | `Lat` | `float64` | Derajat desimal | Koordinat lintang (*latitude*), dikaburkan menjadi 2 desimal demi privasi. |
| 6 | `Long` | `float64` | Derajat desimal | Koordinat bujur (*longitude*), dikaburkan menjadi 2 desimal demi privasi. |
| 7 | `Elev` | `int64` / `float64` | m dpl | Ketinggian tempat lahan dari permukaan laut (*elevation*). |
| 8 | `System` | `object` (string) | Kategori | Sistem budidaya: `Hybrid` (intensif komersial) atau `Landrace` (subsisten varietas lokal). |
| 9 | `Cultivar` | `object` (string) | Kategori | Nama kultivar / genotipe benih jagung yang ditanam (249 nama unik terdata). |
| 10 | `Tillage` | `object` (string) | Kategori | Praktik olah tanah: `Conventional`, `Reduced`, atau `No-till`. |
| 11 | `Planting` | `int64` | DOY | Hari penanaman dalam tahun (*Day of Year*, 1 s.d. 365/366). |
| 12 | `Nitrogen` | `float64` | kg N ha⁻¹ | Dosis pupuk Nitrogen yang ditambahkan per hektar. |
| 13 | `Phosphorus` | `float64` | kg P₂O₅ ha⁻¹ | Dosis pupuk Fosfor yang ditambahkan per hektar. |
| 14 | `Potassium` | `float64` | kg K₂O ha⁻¹ | Dosis pupuk Kalium yang ditambahkan per hektar. |
| 15 | `Slope` | `float64` | % | Kemiringan lereng lahan (*field slope*). |
| 16 | `Clay` | `int64` | % | Kandungan fraksi liat tanah dari peta INEGI. |
| 17 | `CEC` | `float64` | cmolc dm⁻³ | Kapasitas Tukar Kation (*Cation Exchange Capacity*). |
| 18 | `SOM` | `float64` | % | Kandungan bahan organik tanah (*Soil Organic Matter*). |
| 19 | `PH` | `float64` | Skala pH | Derajat kemasaman tanah (*soil pH*). |

---

## 5. Cuplikan 5 Baris Data Observasi Aktual

Berikut adalah 5 baris pertama data observasi yang dibaca secara langsung dari sheet `Data` / berkas `Chiapas_Data.csv` (menampilkan 14 kolom representatif):

| Field_ID | YIELD (Mg/ha) | Year | Mun_yield | Elev (m) | System | Cultivar | Tillage | Planting (DOY) | Nitrogen (kg/ha) | Slope (%) | PH | prcp_V1 (mm/d) | tmax_V1 (°C) |
|---:|---:|---:|---:|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| 1 | 5.0 | 2012 | 2.659 | 534 | Hybrid | *NaN* | Conventional | 177 | 156.00 | 0.48 | 7.28 | 0.0 | 32.65 |
| 2 | 2.3 | 2012 | 3.140 | 895 | Hybrid | *NaN* | Reduced | 183 | 123.00 | 2.09 | 8.01 | 0.0 | 31.85 |
| 3 | 2.7 | 2012 | 3.140 | 895 | Hybrid | *NaN* | Reduced | 189 | 62.86 | 2.09 | 8.01 | 0.8 | 29.90 |
| 4 | 4.0 | 2012 | 2.934 | 422 | Hybrid | *NaN* | Conventional | 154 | 133.00 | 0.00 | 6.80 | 0.9 | 36.05 |
| 5 | 5.1 | 2012 | 2.934 | 422 | Hybrid | *NaN* | Conventional | 177 | 156.00 | 0.00 | 6.80 | 0.0 | 37.00 |

*Catatan:* Pada baris 1 s.d. 5, variabel `Cultivar` bernilai kosong (*NaN*), yang merupakan salah satu dari 310 observasi tanpa catatan kultivar spesifik pada awal program MasAgro tahun 2012.

---

## 6. Analisis Distribusi Temporal & Observasi per Tahun

Sebaran jumlah observasi per tahun mencakup rentang 2012 hingga 2018 dengan rincian sebagai berikut:

| Tahun Tanam | Jumlah Observasi | Persentase | Sistem Hybrid | Sistem Landrace | Catatan Operasional |
|---:|---:|---:|---:|---:|---|
| **2012** | 723 | 15,77% | 468 | 255 | Tahun awal program ekspansi MasAgro di Chiapas. |
| **2013** | 479 | 10,45% | 344 | 135 | Penurunan jumlah petak modul yang dipantau. |
| **2014** | 376 | 8,20% | 275 | 101 | Titik terendah observasi karena pergantian personil lapangan. |
| **2015** | 424 | 9,25% | 295 | 129 | Peningkatan bertahap pendampingan petani. |
| **2016** | 816 | 17,80% | 518 | 298 | Peningkatan besar luas area ekstensi MasAgro. |
| **2017** | 960 | 20,94% | 599 | 361 | Puncak observasi tahunan tertinggi dalam dataset. |
| **2018** | 807 | 17,60% | 535 | 272 | Tahun akhir pemantauan program kemitraan. |
| **Total** | **4.585** | **100,00%** | **3.034 (66,17%)** | **1.551 (33,83%)** | Rasio Hybrid terhadap Landrace stabil (~2:1) setiap tahun. |

Visualisasi distribusi observasi tahunan disajikan pada gambar:
`03_Exploration/Dataset_03_Chiapas/Output/distribusi_observasi_per_tahun.png`.

---

## 7. Analisis ID Lahan & Struktur Observasi Spasial

### 7.1 Karakteristik Field_ID
- Jumlah nilai unik `Field_ID` adalah tepat **4.585** dari total 4.585 baris data (100% unik).
- Nilai `Field_ID` berurutan dari 1 sampai dengan 4585.
- **Temuan Struktur Data:** Tidak ditemukan perulangan `Field_ID` pada tahun yang berbeda. Hal ini menunjukkan bahwa sistem BEM menghasilkan ID baru untuk setiap kejadian budidaya (*cropping event*). Akibatnya, dataset ini harus diperlakukan secara statistik sebagai **cross-sectional pooled data**, bukan panel data berulang (*repeated measurements on identical tracked IDs*).

### 7.2 Koordinat Spasial dan Spatial Blurring
- Koordinat lintang (`Lat`) berkisar antara 14,83° hingga 17,60° LU; bujur (`Long`) berkisar antara -94,00° hingga -91,24° BB.
- Ditemukan sebanyak **2.753 pasangan koordinat unik**.
- Sebanyak 1.832 observasi berbagi koordinat (Lat, Long, Year) yang sama dengan baris lain.
- **Penjelasan Paper:** Sesuai etika perlindungan privasi subjek manusia (halaman 6 paper), peneliti melakukan *spatial blurring* dengan memotong ketelitian koordinat menjadi **2 angka di belakang koma** (~1,1 km resolusi spasial). Hal ini dilakukan agar lahan milik petani perorangan tidak dapat diidentifikasi secara presisi. Oleh karena itu, petak-petak lahan yang berada dalam satu desa, kelompok tani, atau modul demonstrasi yang berdekatan akan memiliki koordinat nominal yang identik.

---

## 8. Karakteristik Sistem Pertanian & Pengelolaan Budidaya

### 8.1 Dikotomi Sistem Budidaya: Hybrid vs Landrace
Dataset ini mencerminkan dualisme pertanian tropis yang sangat tegas di Chiapas:
1. **Sistem Hibrida (`Hybrid`, N = 3.034 / 66,17%):**
   - Berlokasi di wilayah lembah barat-tengah Chiapas (Frailesca, Centro, Fronteriza).
   - Petani semi-komersial skala menengah, menggunakan mekanisasi pertanian dan input pupuk anorganik yang memadai.
   - Varietas benih hibrida unggul (misal Dekalb 390, Pioneer P4082W).
   - Produktivitas tinggi: rata-rata hasil **4,45 Mg ha⁻¹**, median **4,60 Mg ha⁻¹**, dan maksimum mencapai **9,80 Mg ha⁻¹**.
2. **Sistem Varietas Lokal / Jagung Tradisional (`Landrace`, N = 1.551 / 33,83%):**
   - Berlokasi di wilayah utara dan pegunungan timur (Los Altos, Ocosingo, Selva).
   - Petani gurem skala kecil subsisten (*self-consumption*), bergantung pada tenaga kerja manual dan input rendah/pupuk kandang.
   - Varietas lokal turun-temurun (*Criollo* putih, kuning, merah).
   - Produktivitas rendah: rata-rata hasil **1,92 Mg ha⁻¹**, median **1,65 Mg ha⁻¹**, dan kuartil bawah **1,20 Mg ha⁻¹**.

Visualisasi perbandingan produktivitas disajikan pada gambar:
`03_Exploration/Dataset_03_Chiapas/Output/distribusi_yield_by_system.png`.

### 8.2 Praktik Pengolahan Tanah (Tillage)
- **Conventional Tillage (Olah Tanah Konvensional):** 2.092 observasi (45,63%). Rata-rata yield: 3,50 Mg ha⁻¹.
- **No-Till (Tanpa Olah Tanah / TOT):** 1.634 observasi (35,64%). Rata-rata yield: 3,65 Mg ha⁻¹. Merupakan praktik pertanian konservasi yang diperkenalkan oleh CIMMYT.
- **Reduced Tillage (Olah Tanah Minimum):** 859 observasi (18,74%). Rata-rata yield: 3,71 Mg ha⁻¹.
- *Catatan:* Perbedaan yield antar metode olah tanah relatif kecil dibandingkan efek sistem varietas (Hybrid vs Landrace).

### 8.3 Keragaman Kultivar (Genotipe)
- Terdapat 249 nama kultivar unik yang teridentifikasi, ditambah 310 data tanpa nama kultivar (*missing* 6,76%).
- Dominasi kultivar:
  1. `CRIOLLO` (varietas lokal umum tak terdefinisi): 629 petak (13,72%)
  2. `P4082W` (hibrida putih Pioneer): 420 petak (9,16%)
  3. `CRIOLLO AMARILLO` (jagung lokal kuning): 404 petak (8,81%)
  4. `NaN` (tidak tercatat): 310 petak (6,76%)
  5. `OTRA (ESPECIFIQUE)` (opsi form yang tidak dirinci): 299 petak (6,52%)
  6. `DEKALB 390` (hibrida Monsanto/Bayer): 283 petak (6,17%)
  7. `CRIOLLO BLANCO` (jagung lokal putih): 276 petak (6,02%)
  8. `DEKALB 7500`: 248 petak (5,41%)

### 8.4 Praktik Pemupukan (Dosis N, P₂O₅, K₂O)
- **Nitrogen (`Nitrogen`):** Rata-rata 109,10 kg N ha⁻¹ (SD: 63,99; Median: 110,0 kg N ha⁻¹; Rentang: 0 s.d. 349,0 kg N ha⁻¹). Terdapat 358 petak (7,81%) bernilai 0, yang dijelaskan oleh paper bahwa petani tidak melaporkan aplikasi atau mengandalkan kotoran ternak (pupuk kandang).
- **Fosfor (`Phosphorus`):** Rata-rata 22,81 kg P₂O₅ ha⁻¹ (SD: 25,72; Median: 23,0 kg ha⁻¹). Sebanyak 1.328 petak (28,96%) bernilai 0 (petani tidak memberikan pupuk fosfor).
- **Kalium (`Potassium`):** Rata-rata 9,30 kg K₂O ha⁻¹ (SD: 16,68; Median: 0,0 kg ha⁻¹). Sebanyak 2.746 petak (59,89%) bernilai 0 (mayoritas petani kecil di Chiapas tidak mengaplikasikan pupuk kalium).

### 8.5 Waktu Tanam (Planting DOY)
- Penanaman dimulai paling awal pada DOY 91 (1 April) dan paling lambat pada DOY 242 (30 Agustus).
- Rata-rata hari tanam adalah DOY 165 (14 Juni), dengan median DOY 167 (16 Juni) dan kuartil (P25–P75) berada pada DOY 153 s.d. 180 (2 Juni s.d. 29 Juni). Hal ini bertepatan dengan dimulainya musim hujan utama (*rainy season*) di Chiapas.

---

## 9. Statistik Deskriptif Variabel Numerik Kunci

Tabel ringkasan statistik deskriptif untuk variabel-variabel agronomi, edafis, dan target utama:

| Variabel | Satuan | Mean | Std Dev | Min (P0) | P25 | Median (P50) | P75 | Max (P100) | IQR | Nilai Nol (%) |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **`YIELD`** | Mg ha⁻¹ | **3,59** | 1,87 | 0,10 | 1,85 | **3,60** | 5,00 | 9,80 | 3,15 | 0,00% |
| **`Mun_yield`** | Mg ha⁻¹ | **2,61** | 0,95 | 1,13 | 1,75 | **2,66** | 3,24 | 4,39 | 1,49 | 0,00% |
| **`Elev`** | m dpl | 884,00 | 443,00 | 7,00 | 592,00 | 712,00 | 1079,00 | 2849,00 | 487,00 | 0,00% |
| **`Planting`** | DOY | 165,34 | 21,79 | 91,00 | 153,00 | 167,00 | 180,00 | 242,00 | 27,00 | 0,00% |
| **`Nitrogen`** | kg N ha⁻¹ | 109,10 | 63,99 | 0,00 | 64,00 | 110,00 | 156,00 | 349,00 | 92,00 | 7,81% |
| **`Phosphorus`** | kg P₂O₅ ha⁻¹ | 22,81 | 25,72 | 0,00 | 0,00 | 23,00 | 46,00 | 143,00 | 46,00 | 28,96% |
| **`Potassium`** | kg K₂O ha⁻¹ | 9,30 | 16,68 | 0,00 | 0,00 | 0,00 | 12,00 | 100,00 | 12,00 | 59,89% |
| **`Slope`** | % | 6,03 | 6,76 | 0,00 | 1,28 | 3,02 | 8,71 | 61,19 | 7,43 | 2,75% |
| **`Clay`** | % | 30,11 | 9,93 | 5,00 | 23,00 | 28,00 | 37,00 | 57,00 | 14,00 | 0,00% |
| **`CEC`** | cmolc dm⁻³ | 22,72 | 7,40 | 4,31 | 16,21 | 21,11 | 27,62 | 50,80 | 11,41 | 0,00% |
| **`SOM`** | % | 1,60 | 0,87 | 0,27 | 1,00 | 1,21 | 2,04 | 4,00 | 1,04 | 0,00% |
| **`PH`** | pH | 6,80 | 0,69 | 4,92 | 6,62 | 6,80 | 7,28 | 8,25 | 0,66 | 0,00% |

Visualisasi perbandingan distribusi `YIELD` dan `Mun_yield` disajikan pada gambar:
`03_Exploration/Dataset_03_Chiapas/Output/distribusi_yield_chiapas.png`.

---

## 10. Evaluasi Kesesuaian Penelitian Skripsi (Research Compatibility)

### 10.1 Relevansi terhadap Rantai Logika Skripsi
Skripsi ini berorientasi pada Sistem Informasi Bisnis dan Smart Farming:
$$\text{Luas Lahan Jagung Mitra ASA (ha)} \times \text{Prediksi Produktivitas Jagung (ton/ha)} \longrightarrow \text{Total Ketersediaan Jagung (kg)}$$
$$\text{Total Ketersediaan Jagung (kg)} \div \text{Konsumsi Jagung per Ekor Ayam (g/hari)} \longrightarrow \text{Kapasitas Daya Tampung Ayam Petelur (Ekor)}$$

Dataset Chiapas berkontribusi secara langsung pada mata rantai pertama: **komponen permodelan produktivitas jagung (*maize yield prediction*)**. Dataset ini memberikan landasan empiris mengenai bagaimana variabel iklim, kondisi tanah, dosis pupuk, dan pemilihan varietas mempengaruhi hasil panen jagung per hektar.

### 10.2 Kontribusi Konkret terhadap Naskah Skripsi
1. **Penyusunan Bab 1 (Pendahuluan):**
   - Menjelaskan urgensi estimasi produktivitas panen jagung sebagai faktor pembatas utama dalam perencanaan kapasitas peternakan ayam petelur mandiri (*integrated crop-livestock smart farming*).
   - Menunjukkan bahwa variabilitas hasil jagung sangat dipengaruhi oleh cuaca dan pengelolaan (pada dataset Chiapas berfluktuasi dari 0,1 hingga 9,8 ton/ha).
2. **Penyusunan Bab 2 (Tinjauan Pustaka):**
   - Menjadi rujukan ilmiah utama (*prior literature*) mengenai pemodelan hasil jagung berbasis data observasional berskala besar (merujuk pada Trevisan et al., 2022 di *Data in Brief*).
   - Mengelompokkan faktor penentu yield berdasarkan interaksi Genotipe × Lingkungan × Pengelolaan ($G \times E \times M$).
3. **Penyusunan Bab 3 (Metodologi Penelitian):**
   - Berfungsi sebagai **dataset benchmark/eksplorasi** untuk merancang skema fitur, arsitektur pemodelan, dan analisis risiko *data leakage* sebelum diimplementasikan pada data petak riil mitra ASA di Sumenep.
   - Memberikan protokol standardisasi target panen (penyesuaian kadar air biji 14% dan konversi Mg/ha ke ton/ha).

---

## 11. Kesimpulan Tahap Data Understanding
1. Berkas Excel sumber dan salinan CSV berada dalam kondisi prima, utuh, dan terverifikasi 100% konsisten pada seluruh 4.585 baris dan 169 kolom.
2. Dataset menyajikan pemisahan yang jelas antara varietas Hibrida komersial dan Landrace tradisional, yang menjadi faktor pembeda produktivitas paling dominan.
3. Variabel target panen lapangan yang sah adalah `YIELD` (Mg ha⁻¹), bukan `Mun_yield`.
4. Fitur cuaca tersusun dalam 30 interval 10-harian yang memerlukan pemilihan hati-hati agar tidak menimbulkan *data leakage* pada model perencanaan sebelum tanam.
