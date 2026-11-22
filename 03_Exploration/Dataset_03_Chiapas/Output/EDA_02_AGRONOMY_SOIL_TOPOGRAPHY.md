# LAPORAN EXPLORATORY DATA ANALYSIS (EDA) TAHAP 2
## Eksplorasi Univariat & Bivariat Fitur Agronomi, Sifat Tanah, dan Topografi serta Analisis Multikolinearitas dan Ketersediaan Temporal
### Dataset: Multiyear Maize Management Dataset, Chiapas, Mexico (2012–2018)

---

## 1. Identitas Dokumen & Ruang Lingkup Analisis

### 1.1 Konteks Skripsi & Relevansi Fitur Prediktor Non-Cuaca
Laporan ini merupakan dokumen resmi **Exploratory Data Analysis (EDA) Tahap 2** yang melanjutkan investigasi analitis terhadap dataset budidaya jagung di Chiapas, Meksiko ($N = 4.585$ observasi). Analisis ini berada dalam kerangka penelitian skripsi bertajuk:
> *"Pemodelan Prediksi Jumlah Ayam Petelur untuk Smart Farming Berdasarkan Ketersediaan Lahan Jagung untuk Mendukung Perencanaan Produksi di Komunitas ASA Indonesia"*.

Dalam arsitektur *decision support system* (DSS) perencanaan pakan mandiri Komunitas ASA, estimasi produktivitas jagung (`YIELD`, $\text{Mg ha}^{-1}$) per petak lahan menjadi variabel penentu kapasitas tampung ternak (*carrying capacity*). Setelah perilaku distribusi univariat variabel target `YIELD` dipetakan secara mendalam pada [EDA_01_TARGET_YIELD.md](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/EDA_01_TARGET_YIELD.md), EDA Tahap 2 ini berfokus penuh mengeksplorasi **12 fitur prediktor non-cuaca**, yang terdiri atas:
1. **Fitur Agronomi & Pengelolaan Budidaya (6 fitur):** Dosis pemupukan `Nitrogen`, `Phosphorus`, `Potassium`, tanggal tanam `Planting`, sistem budidaya `System`, dan praktik olah tanah `Tillage`.
2. **Fitur Sifat Tanah (4 fitur):** Kandungan liat `Clay`, kapasitas tukar kation `CEC`, bahan organik tanah `SOM`, dan derajat keasaman tanah `PH`.
3. **Fitur Topografi Lahan (2 fitur):** Elevasi lahan `Elev` dan kemiringan lereng `Slope`.

### 1.2 Batasan Ruang Lingkup Ketat (Scope Boundaries)
Sesuai arahan metodologis dan pedoman integritas data:
- **Dataset Acuan:** Berkas [Chiapas_Data.csv](file:///C:/SKRIPSI/02_Raw_Data/Dataset_03_Chiapas/Chiapas_Data.csv) yang berstatus *read-only* tanpa modifikasi.
- **Memanfaatkan Hasil Audit Sebelumnya (Tanpa Repetisi):** Laporan ini berlandaskan temuan audit pada [EDA_01_TARGET_YIELD.md](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/EDA_01_TARGET_YIELD.md), [LAPORAN_VERIFIKASI_KRITIS_CHIAPAS.md](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/LAPORAN_VERIFIKASI_KRITIS_CHIAPAS.md), dan [DATA_DICTIONARY_CHIAPAS.md](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/DATA_DICTIONARY_CHIAPAS.md). **TIDAK ADA pengulangan audit kualitas data umum, missing values, duplikasi baris/kolom, atau eksplorasi ulang target YIELD secara mandiri**.
- **Larangan Ketat Pembersihan & Preprocessing (Zero Data Dropping):** Seluruh $4.585$ baris dipertahankan secara utuh. Tidak ada penghapusan data pencilan, transformasi variabel, normalisasi, imputasi, maupun *encoding* yang diterapkan pada berkas mentah.
- **Larangan Seleksi Fitur Final & Pemodelan:** Laporan ini murni bersifat diagnostik dan deskriptif. Tidak ada pemodelan prediktif (*machine learning*) atau eliminasi fitur permanen pada tahap ini.
- **Kepatuhan Keras Inferensi: Korelasi Bukan Sebab-Akibat:** Hubungan statistik asosiatif (koefisien Pearson dan Spearman) ditafsirkan semata-mata sebagai kovariansi matematis dalam data observasional lapangan, bukan hubungan kausal agronomis langsung. Seluruh interpretasi diverifikasi menggunakan data aktual dan dokumentasi resmi [DATASET_CONTEXT.md](file:///C:/SKRIPSI/02_Raw_Data/Dataset_03_Chiapas/DATASET_CONTEXT.md).

---

## 2. Klasifikasi Fitur Berdasarkan Waktu Ketersediaan Data (Temporal Availability)

Dalam perancangan model prediksi hasil panen untuk mendukung perencanaan operasional usaha tani dan peternakan (*feed supply planning*), salah satu kesalahan paling fatal dalam sains data pertanian adalah **kebocoran informasi masa depan (*look-ahead bias / data leakage*)**. Memasukkan fitur-fitur yang baru diketahui setelah tanaman tumbuh atau setelah panen ke dalam model prediksi sebelum tanam (*pre-planting forecast*) akan menciptakan ilusi akurasi semu di laboratorium yang tidak akan pernah bisa dioperasikan di lapangan.

Tabel 1 menyajikan klasifikasi temporal resmi seluruh 12 fitur prediktor non-cuaca dalam dataset Chiapas, membedakan secara tegas antara **fakta yang terverifikasi** (berdasarkan protokol pengumpulan data BEM CIMMYT dan artikel Trevisan et al., 2022) dan **asumsi operasional pemodelan**:

### Tabel 1: Klasifikasi Waktu Ketersediaan Fitur, Status Verifikasi, dan Risiko Data Leakage

| No. | Fitur Prediktor | Unit / Tipe | Waktu Ketersediaan Aktual di Lapangan | Status Verifikasi Metodologis | Dasar Fakta vs Asumsi Operasional | Implikasi & Risiko pada Model Prediksi Pra-Tanam |
|---:|---|:---:|:---:|:---:|---|---|
| 1 | **`Elev`** | $\text{m dpl}$<br>*(Numerik)* | **Sebelum Tanam**<br>*(Pre-planting)* | **FAKTA TERVERIFIKASI** | **Fakta:** Bersumber dari data elevasi spasial INEGI yang diekstrak berdasarkan titik koordinat geografis petak lahan. Sifat topografi ini statis permanen antar-tahun.<br>**Asumsi:** Koordinat petak diasumsikan akurat merepresentasikan seluruh hamparan lahan petani. | **Sangat Aman:** Bebas dari risiko *leakage*. Fitur topografi dapat langsung digunakan sebagai kovariat dasar dalam pemodelan pra-tanam. |
| 2 | **`Slope`** | $\%$<br>*(Numerik)* | **Sebelum Tanam**<br>*(Pre-planting)* | **FAKTA TERVERIFIKASI** | **Fakta:** Diekstrak dari peta topografi/elevasi digital INEGI. Nilai kelerengan lahan bersifat statis dan tidak dipengaruhi oleh musim tanam.<br>**Asumsi:** Kemiringan makro INEGI dianggap seragam di seluruh petak ubinan. | **Sangat Aman:** Bebas dari risiko *leakage*. Menjadi prediktor penting untuk potensi erosi dan limpasan air hujan. |
| 3 | **`Clay`** | $\%$<br>*(Numerik)* | **Sebelum Tanam**<br>*(Pre-planting)* | **FAKTA TERVERIFIKASI (Sumber Peta)**<br>*ASUMSI (Presisi Lapangan)* | **Fakta:** Diekstrak dari peta tanah terbuka skala tinjau INEGI, bukan hasil uji laboratorium tanah *in-situ* tahunan per petak. Secara administratif tersedia sebelum tanam.<br>**Asumsi:** Diasumsikan bahwa tekstur liat pada peta INEGI tidak mengalami perubahan drastis akibat sedimentasi lokal. | **Aman Secara Temporal:** Tersedia sebelum tanam karena bersumber dari basis data statis, namun memiliki keterbatasan resolusi spasial. |
| 4 | **`CEC`** | $\text{cmol}_{\text{c}}\text{ dm}^{-3}$<br>*(Numerik)* | **Sebelum Tanam**<br>*(Pre-planting)* | **FAKTA TERVERIFIKASI (Sumber Peta)**<br>*ASUMSI (Presisi Lapangan)* | **Fakta:** Diekstrak dari peta geospasial tanah INEGI. Bersifat statis pada repositori sekunder sebelum musim dimulai.<br>**Asumsi:** Diasumsikan kapasitas tukar kation peta regional berkorelasi memadai dengan horizon perakaran aktual. | **Aman Secara Temporal:** Bebas risiko *leakage*, tetapi memuat ketidakpastian pengukuran sekunder (*inherent measurement error*). |
| 5 | **`SOM`** | $\%$<br>*(Numerik)* | **Sebelum Tanam**<br>*(Pre-planting)* | **FAKTA TERVERIFIKASI (Sumber Peta)**<br>*ASUMSI (Presisi Lapangan)* | **Fakta:** Berasal dari layer pemetaan tanah INEGI.<br>**Asumsi:** Kandungan bahan organik peta regional diasumsikan mewakili kondisi petak, mengabaikan dinamika penambahan mulsa/residu tanaman riil oleh petani. | **Aman Secara Temporal:** Tersedia sebelum tanam sebagai data sekunder peta tanah regional. |
| 6 | **`PH`** | $-\log[\text{H}^+]$<br>*(Numerik)* | **Sebelum Tanam**<br>*(Pre-planting)* | **FAKTA TERVERIFIKASI (Sumber Peta)**<br>*ASUMSI (Presisi Lapangan)* | **Fakta:** Diekstrak dari dataset pemetaan tanah INEGI.<br>**Asumsi:** pH tanah peta statis diasumsikan tidak bergeser signifikan akibat riwayat aplikasi kapur pertanian atau pupuk pembentuk asam. | **Aman Secara Temporal:** Tersedia sebelum tanam, namun variabilitas riil perlakuan pengapuran lokal tidak terekam dalam layer ini. |
| 7 | **`System`** | `Hybrid` / `Landrace`<br>*(Kategori)* | **Sebelum Tanam / Saat Perencanaan** | **FAKTA TERVERIFIKASI (Keputusan)**<br>*ASUMSI (Pencatatan BEM)* | **Fakta:** Petani memutuskan menanam varietas hibrida unggul atau benih lokal (*criollo*) sebelum benih disemai.<br>**Asumsi:** Pencatatan oleh penyuluh (*farm advisor*) di logbook BEM diasumsikan sesuai dengan niat tanam awal petani tanpa pergantian benih darurat. | **Kondisional:** Aman digunakan pada model pra-tanam sebagai **variabel skenario budidaya** (misalnya simulasi: "berapa panen jika menanam Hybrid vs Landrace?"). |
| 8 | **`Tillage`** | `Conventional` / `Reduced` / `No-till`<br>*(Kategori)* | **Sebelum Tanam hingga Saat Tanam** | **FAKTA TERVERIFIKASI (Praktik)**<br>*ASUMSI (Pencatatan BEM)* | **Fakta:** Persiapan lahan (bajak, olah minimum, atau tanpa olah tanah) secara fisik dieksekusi sebelum benih dimasukkan ke tanah.<br>**Asumsi:** Jadwal pencatatan kunjungan penyuluh BEM diasumsikan merefleksikan praktik pengolahan tanah yang sebenarnya di petak tersebut. | **Aman / Skenario:** Dapat dijadikan variabel input perencanaan pra-tanam sesuai paket teknologi yang akan diterapkan petani. |
| 9 | **`Planting`** | $\text{DOY (Hari)}$<br>*(Numerik)* | **Saat Tanam**<br>*(At Planting)* | **FAKTA TERVERIFIKASI (Realisasi Aktual)**<br>❌ *BUKAN DATA PRA-TANAM* | **Fakta:** Kolom `Planting` mencatat **hari riil penanaman di lapangan** (*actual Day of Year*). Tanggal riil tanam sangat ditentukan oleh tibanya hujan awal musim (*rain onset*), ketersediaan benih, dan traktor/tenaga kerja.<br>**Asumsi Berbahaya:** Menganggap nilai `Planting` aktual sudah diketahui pasti sebelum tanam adalah **asumsi keliru**. | ⚠️ **WASPADA DATA LEAKAGE TINGKAT SEDANG:** Untuk prediksi pra-tanam murni, nilai `Planting` aktual **belum tersedia**. Model pra-tanam hanya dapat menggunakan *asumsi target jadwal tanam* atau *perkiraan klimatologis*. |
| 10 | **`Nitrogen`** | $\text{kg N ha}^{-1}$<br>*(Numerik)* | **Selama Pertumbuhan hingga Pascapanen**<br>*(Vegetatif V4–V8)* | **FAKTA TERVERIFIKASI (Total Akumulasi)**<br>❌ *BUKAN DATA PRA-TANAM* | **Fakta:** Menurut manual BEM CIMMYT, angka ini adalah **total akumulasi pupuk N yang selesai diaplikasikan sepanjang musim**. Pemupukan N jagung tropis dilakukan terbagi (*split*): sebagian saat tanam dan sebagian besar (susulan) pada fase vegetatif aktif V4–V8. Petani menyesuaikan pupuk susulan dengan kondisi curah hujan.<br>**Asumsi Berbahaya:** Menganggap dosis N aktual sudah tersedia sebelum tanam adalah **kesalahan agronomis**. | 🚨 **RISIKO DATA LEAKAGE TINGGI:** Dosis N riil yang diterima tanaman adalah hasil realisasi dinamis sepanjang musim. Hanya dapat digunakan pada model pra-tanam jika diposisikan sebagai **skenario dosis yang direncanakan (*prescribed dosage*)**, bukan realisasi aktual. |
| 11 | **`Phosphorus`** | $\text{kg P}_2\text{O}_5\text{ ha}^{-1}$<br>*(Numerik)* | **Saat Tanam hingga Pascapanen** | **FAKTA TERVERIFIKASI (Total Akumulasi)**<br>❌ *BUKAN DATA PRA-TANAM* | **Fakta:** Angka tercatat adalah total realisasi musiman. Meskipun pupuk fosfat sebagian besar diaplikasikan sebagai pupuk dasar saat tanam, pencatatan akhir di BEM direkap oleh penyuluh setelah musim berjalan. 41% petak tercatat bernilai 0 (tanpa pupuk P). | 🚨 **RISIKO DATA LEAKAGE SEDANG-TINGGI:** Sama seperti Nitrogen, jika digunakan untuk prediksi pra-tanam, nilai ini harus diperlakukan sebagai rencana intervensi (*management decision scenario*). |
| 12 | **`Potassium`** | $\text{kg K}_2\text{O ha}^{-1}$<br>*(Numerik)* | **Saat Tanam hingga Pascapanen** | **FAKTA TERVERIFIKASI (Total Akumulasi)**<br>❌ *BUKAN DATA PRA-TANAM* | **Fakta:** Angka tercatat adalah total aplikasi riil. 66% petak petani di Chiapas tidak mengaplikasikan K (nilai 0 kg/ha). Rekapitulasi dilakukan pada akhir siklus pencatatan logbook. | 🚨 **RISIKO DATA LEAKAGE SEDANG-TINGGI:** Harus diperlakukan sebagai skenario input budidaya terencana, bukan nilai faktual yang otomatis diketahui sebelum musim dimulai. |

> [!IMPORTANT]
> **Kesimpulan Metodologis Klasifikasi Temporal:**
> Fitur yang **benar-benar terverifikasi faktual tersedia sebelum tanam** secara objektif hanyalah fitur **topografi (`Elev`, `Slope`)** dan **sifat tanah peta sekunder (`Clay`, `CEC`, `SOM`, `PH`)**. Variabel manajemen budidaya (`System`, `Tillage`, `Planting`, `Nitrogen`, `Phosphorus`, `Potassium`) yang tercatat dalam dataset Chiapas adalah **realisasi historis (*ex-post observations*)**, bukan rencana awal (*ex-ante plans*). Dalam aplikasi praktis pada sistem informasi Smart Farming Komunitas ASA, variabel-variabel manajemen ini harus diperlakukan sebagai **fitur skenario intervensi yang dikendalikan oleh peternak/petani**, bukan fitur lingkungan yang diobservasi pasif.

---

## 3. Eksplorasi Univariat Fitur Agronomi, Sifat Tanah, dan Topografi

Visualisasi distribusi univariat komprehensif untuk seluruh fitur prediktor non-cuaca disajikan pada gambar resolusi tinggi berikut:

![Distribusi Univariat Fitur Agronomi](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/eda_02_agronomy_univariate.png)
*Gambar 1: Distribusi univariat fitur-fitur agronomi dataset Chiapas: (A1–A4) Boxplot dan Histogram/KDE untuk Nitrogen, Phosphorus, Potassium, dan Planting; (B1–B2) Distribusi frekuensi kategorikal System dan Tillage.*

![Distribusi Univariat Fitur Tanah & Topografi](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/eda_02_soil_topography_univariate.png)
*Gambar 2: Distribusi univariat fitur tanah dan topografi: (A1–A3) Kandungan liat (Clay), KTK tanah (CEC), dan Bahan Organik Tanah (SOM); (B1–B3) Derajat keasaman (pH), Elevasi (Elev), dan Kelerengan (Slope).*

### 3.1 Ringkasan Parameter Statistik Deskriptif 10 Fitur Numerik ($N = 4.585$)

Tabel 2 memuat hasil perhitungan parameter statistik pemusatan, penyebaran, bentuk distribusi, serta keberadaan nilai nol (*zero-inflation*) dari data aktual:

### Tabel 2: Statistik Deskriptif Komprehensif Fitur Numerik Prediktor

| Kelompok | Fitur Prediktor | Satuan | Mean ($\bar{X}$) | Std ($s$) | Min | Kuartil 1 ($Q_1$) | Median ($P_{50}$) | Kuartil 3 ($Q_3$) | Max | IQR | Rentang | CV (%) | Kemencengan ($\gamma_1$) | Kurtosis ($\gamma_2$) | Jumlah Nilai 0 | Persentase Nol (%) |
|---|---|:---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **Agronomi** | **`Nitrogen`** | $\text{kg N ha}^{-1}$ | 109,74 | 64,13 | 0,00 | 64,00 | 110,00 | 156,00 | 349,00 | 92,00 | 349,00 | 58,43% | +0,25 | -0,18 | 218 | 4,75% |
| **Agronomi** | **`Phosphorus`** | $\text{kg P}_2\text{O}_5\text{ ha}^{-1}$ | 23,88 | 26,71 | 0,00 | 0,00 | 23,00 | 46,00 | 143,00 | 46,00 | 143,00 | 111,87% | +0,93 | +0,51 | 1.882 | 41,05% |
| **Agronomi** | **`Potassium`** | $\text{kg K}_2\text{O ha}^{-1}$ | 9,30 | 17,74 | 0,00 | 0,00 | 0,00 | 12,50 | 100,00 | 12,50 | 100,00 | 190,83% | +1,98 | +3,52 | 3.025 | 65,98% |
| **Agronomi** | **`Planting`** | $\text{DOY}$ | 165,12 | 22,53 | 91,00 | 153,00 | 167,00 | 180,00 | 242,00 | 27,00 | 151,00 | 13,65% | -0,43 | +0,39 | 0 | 0,00% |
| **Tanah** | **`Clay`** | $\%$ | 30,15 | 10,12 | 5,00 | 23,00 | 28,00 | 37,00 | 57,00 | 14,00 | 52,00 | 33,55% | +0,46 | -0,38 | 0 | 0,00% |
| **Tanah** | **`CEC`** | $\text{cmol}_{\text{c}}\text{ dm}^{-3}$ | 22,74 | 7,42 | 4,31 | 16,18 | 21,12 | 27,60 | 50,80 | 11,42 | 46,49 | 32,64% | +0,62 | +0,24 | 0 | 0,00% |
| **Tanah** | **`SOM`** | $\%$ | 1,60 | 0,93 | 0,27 | 0,97 | 1,17 | 2,03 | 4,00 | 1,06 | 3,73 | 58,32% | +1,10 | +0,02 | 0 | 0,00% |
| **Tanah** | **`PH`** | unit | 6,81 | 0,71 | 4,92 | 6,62 | 6,79 | 7,34 | 8,25 | 0,71 | 3,33 | 10,44% | -0,42 | -0,11 | 0 | 0,00% |
| **Topografi** | **`Elev`** | $\text{m dpl}$ | 884,70 | 443,93 | 7,00 | 592,00 | 712,00 | 1079,00 | 2849,00 | 487,00 | 2842,00 | 50,18% | +1,06 | +0,62 | 0 | 0,00% |
| **Topografi** | **`Slope`** | $\%$ | 6,03 | 6,78 | 0,00 | 1,34 | 3,04 | 8,74 | 61,19 | 7,40 | 61,19 | 112,53% | +1,81 | +4,00 | 91 | 1,98% |

### 3.2 Sebaran Persentil Lengkap Fitur Numerik

Tabel 3 menyajikan profil persentil empiris untuk memetakan dispersi nonlinier dan ekor distribusi:

### Tabel 3: Sebaran Persentil Empiris Fitur Numerik ($P_1$ sampai $P_{99}$)

| Fitur Prediktor | $P_1$ (1%) | $P_5$ (5%) | $P_{10}$ (10%) | $P_{25}$ ($Q_1$) | $P_{50}$ (Median) | $P_{75}$ ($Q_3$) | $P_{90}$ (90%) | $P_{95}$ (95%) | $P_{99}$ (99%) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **`Nitrogen`** ($\text{kg ha}^{-1}$) | 0,00 | 1,00 | 32,00 | 64,00 | 110,00 | 156,00 | 196,00 | 223,00 | 275,00 |
| **`Phosphorus`** ($\text{kg ha}^{-1}$) | 0,00 | 0,00 | 0,00 | 0,00 | 23,00 | 46,00 | 59,50 | 69,00 | 115,00 |
| **`Potassium`** ($\text{kg ha}^{-1}$) | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 12,50 | 30,00 | 50,00 | 60,00 |
| **`Planting`** (DOY) | 121,00 | 131,00 | 136,00 | 153,00 | 167,00 | 180,00 | 192,00 | 199,00 | 215,00 |
| **`Clay`** (%) | 10,00 | 13,00 | 17,00 | 23,00 | 28,00 | 37,00 | 45,00 | 48,00 | 52,00 |
| **`CEC`** ($\text{cmol}_{\text{c}}\text{ dm}^{-3}$) | 9,99 | 12,04 | 13,85 | 16,18 | 21,12 | 27,60 | 34,22 | 36,97 | 45,00 |
| **`SOM`** (%) | 0,42 | 0,55 | 0,69 | 0,97 | 1,17 | 2,03 | 3,11 | 3,63 | 4,00 |
| **`PH`** (unit) | 5,09 | 5,50 | 5,79 | 6,62 | 6,79 | 7,34 | 7,72 | 7,92 | 8,11 |
| **`Elev`** ($\text{m dpl}$) | 23,00 | 466,00 | 526,00 | 592,00 | 712,00 | 1079,00 | 1572,00 | 1774,00 | 2165,00 |
| **`Slope`** (%) | 0,00 | 0,00 | 0,57 | 1,34 | 3,04 | 8,74 | 14,79 | 19,89 | 32,84 |

### 3.3 Karakteristik Penting Distribusi Fitur Lapangan

1. **Fenomena Ekses Nilai Nol (*Zero Inflation*) pada Pupuk Fosfat dan Kalium:**
   - **`Nitrogen`:** Hanya $218$ petak ($4{,}75\%$) yang tidak menerima pupuk nitrogen sama sekali. Median aplikasi $110\text{ kg N ha}^{-1}$ mencerminkan adopsi pupuk urea yang sangat luas.
   - **`Phosphorus`:** Sebanyak $1.882$ petak (**$41{,}05\%$**) tidak menerima pupuk fosfat ($0\text{ kg P}_2\text{O}_5\text{ ha}^{-1}$), sehingga nilai $Q_1$ jatuh pada angka 0.
   - **`Potassium`:** Mengalami *zero-inflation* yang masif, di mana $3.025$ petak (**$65{,}98\%$**) tidak diberi pupuk kalium ($0\text{ kg K}_2\text{O ha}^{-1}$). Akibatnya, nilai median populasi adalah $0{,}00$, dengan kemencengan positif tinggi ($\gamma_1 = +1{,}98$) dan kurtosis runcing ($\gamma_2 = +3{,}52$). Hal ini membuktikan bahwa petani jagung di Chiapas secara umum memprioritaskan alokasi modal pada pupuk Nitrogen dan mengabaikan Kalium.
2. **Karakteristik Temporal Hari Tanam (`Planting`):**
   - Rata-rata hari tanam jatuh pada DOY $165{,}12$ (sekitar 14 Juni), dengan median DOY $167$ (16 Juni).
   - Rentang tanam sangat lebar ($151\text{ hari}$), mulai dari DOY $91$ (awal April) hingga DOY $242$ (akhir Agustus). $80\%$ penanaman terkonsentrasi pada DOY $136$ hingga $192$ (pertengahan Mei hingga pertengahan Juli), yang bertepatan dengan mulainya musim hujan (*rainy season*).
3. **Karakteristik Geografis & Topografi:**
   - **`Elev`:** Menunjukkan kemencengan kanan yang nyata ($\gamma_1 = +1{,}06$). Median elevasi adalah $712\text{ m dpl}$, namun terdapat petak-petak dataran tinggi yang mencapai $2.849\text{ m dpl}$ di kawasan pegunungan Sierra Madre de Chiapas.
   - **`Slope`:** Mayoritas lahan relatif landai (median $3{,}04\%$), namun memiliki rentang ekstrem hingga $61{,}19\%$ ($\gamma_1 = +1{,}81, \gamma_2 = +4{,}00$). $91$ petak ($1{,}98\%$) berstatus datar sempurna ($0\%$). Lahan curam ($>10\%$) terkonsentrasi pada sistem pertanian subsisten tradisional.
4. **Karakteristik Sifat Tanah Peta Regional:**
   - **`PH`:** Cenderung mendekati netral hingga agak basa (rata-rata $6{,}81$, median $6{,}79$, rentang $4{,}92$ hingga $8{,}25$).
   - **`Clay` & `CEC`:** Liat rata-rata $30{,}15\%$ (tekstur lempung liat) dengan KTK rata-rata $22{,}74\text{ cmol}_{\text{c}}\text{ dm}^{-3}$, menunjukkan kapasitas penyangga hara yang tergolong sedang hingga baik.
   - **`SOM`:** Bahan organik tanah tergolong rendah hingga sedang (rata-rata $1{,}60\%$, median $1{,}17\%$, maksimum $4{,}00\%$).

---

## 4. Analisis Univariat Fitur Kategorikal (`System` & `Tillage`)

### 4.1 Distribusi dan Komposisi Frekuensi Kategorikal

Tabel 4 merangkum frekuensi dan proporsi dua variabel kategorikal utama:

### Tabel 4: Distribusi Frekuensi Fitur Kategorikal Budidaya ($N = 4.585$)

| Fitur Kategorikal | Kategori Nilai | Jumlah Observasi ($N$) | Proporsi Persentase (%) | Deskripsi Praktik Agronomi Lapangan |
|---|---|---:|---:|---|
| **`System`** | **`Hybrid`** | **3.034** | **66,17%** | Budidaya komersial/semi-komersial benih jagung hibrida unggul dengan input pupuk kimia sedang-tinggi. |
| | **`Landrace`** | **1.551** | **33,83%** | Budidaya subsisten jagung lokal (*criollo*) warisan adat, input pupuk minimal, sering di lereng berbukit. |
| **`Tillage`** | **`Conventional`** | **2.092** | **45,63%** | Olah tanah intensif (pembajakan konvensional dengan traktor atau hewan ternak). |
| | **`No-till`** | **1.634** | **35,64%** | Tanpa olah tanah (*zero tillage*); benih ditanam langsung pada tanah berpenutup mulsa residu. |
| | **`Reduced`** | **859** | **18,74%** | Olah tanah minimum (*strip tillage / minimum tillage*) untuk mengurangi gangguan struktur tanah. |

### 4.2 Tabulasi Silang Sistem Budidaya vs Praktik Olah Tanah (`System` $\times$ `Tillage`)

Tabel 5 memperlihatkan bagaimana praktik pengolahan tanah terdistribusi pada masing-masing sistem budidaya:

### Tabel 5: Matriks Kontingensi Tabulasi Silang `System` $\times$ `Tillage`

| Praktik Olah Tanah (`Tillage`) | Sistem Hybrid ($N = 3.034$) | % dalam Hybrid | Sistem Landrace ($N = 1.551$) | % dalam Landrace | Total Petak Populasi | % Total Populasi |
|---|---:|---:|---:|---:|---:|---:|
| **`Conventional`** | 1.306 | 43,05% | 786 | 50,68% | 2.092 | 45,63% |
| **`No-till`** | 1.072 | 35,33% | 562 | 36,23% | 1.634 | 35,64% |
| **`Reduced`** | 656 | 21,62% | 203 | 13,09% | 859 | 18,74% |
| **Total Kelompok** | **3.034** | **100,00%** | **1.551** | **100,00%** | **4.585** | **100,00%** |

> [!NOTE]
> Adopsi teknologi olah tanah konservasi (*No-till*) cukup merata di kedua sistem budidaya, mencakup **$35{,}33\%$ pada Hybrid** dan **$36{,}23\%$ pada Landrace**. Hal ini mencerminkan keberhasilan program diseminasi pertanian konservasi oleh CIMMYT di Chiapas. Namun, petani Landrace memiliki proporsi olah tanah konvensional yang lebih tinggi ($50{,}68\%$) dibandingkan petani Hybrid ($43{,}05\%$).

### 4.3 Kesenjangan Input Pemupukan Antar-Sistem Budidaya

Evaluasi data aktual membuktikan disparitas yang sangat tajam dalam adopsi pupuk kimia antara sistem Hybrid dan Landrace:
- **Petak Tanpa Pupuk Nitrogen:** Pada sistem Hybrid hanya **$1{,}91\%$** ($58$ petak), sedangkan pada Landrace melonjak menjadi **$10{,}32\%$** ($160$ petak).
- **Petak Tanpa Pupuk Fosfat:** Pada sistem Hybrid sebesar **$31{,}58\%$** ($958$ petak), sedangkan pada Landrace mencapai **$59{,}57\%$** ($924$ petak).
- **Petak Tanpa Pupuk Kalium:** Pada sistem Hybrid sebesar **$56{,}95\%$** ($1.728$ petak), sedangkan pada Landrace mendominasi hingga **$83{,}62\%$** ($1.297$ petak).

---

## 5. Analisis Bivariat Hubungan Masing-Masing Fitur dengan `YIELD`

Visualisasi bivariat mendalam disajikan pada Gambar 3 dan Gambar 4 berikut:

![Analisis Bivariat Fitur Agronomi vs YIELD](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/eda_02_agronomy_vs_yield_bivariate.png)
*Gambar 3: Scatter plot dan garis tren regresi fitur agronomi terhadap YIELD (A: Nitrogen, B: Phosphorus, C: Potassium, D: Planting DOY), dipisahkan berdasarkan Sistem Budidaya.*

![Analisis Bivariat Fitur Tanah & Topografi vs YIELD](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/eda_02_soil_topography_vs_yield_bivariate.png)
*Gambar 4: Scatter plot dan garis tren regresi fitur tanah dan topografi terhadap YIELD (A: Elevasi, B: Kelerengan, C: Kandungan Liat, D: KTK Tanah, E: Bahan Organik, F: Derajat Keasaman pH).*

### 5.1 Korelasi Parametrik (Pearson) dan Non-Parametrik (Spearman Rank)

Tabel 6 menyajikan kekuatan asosiasi linier dan monotonik antara 10 fitur numerik dengan `YIELD`, baik secara agregat global ($N = 4.585$) maupun terdekomposisi per sub-populasi sistem budidaya:

### Tabel 6: Matriks Koefisien Korelasi Fitur Numerik terhadap `YIELD`

| Fitur Prediktor | Koef. Pearson Global ($r$) | Nilai $p$ (Pearson) | Koef. Spearman Global ($\rho$) | Nilai $p$ (Spearman) | Spearman Subgrup Hybrid ($\rho_{\text{hyb}}$) | Spearman Subgrup Landrace ($\rho_{\text{land}}$) | Interpretasi Arah & Kekuatan Asosiasi |
|---|---:|:---:|---:|:---:|---:|---:|---|
| **`Elev`** | **-0,535** | $< 10^{-300}$ | **-0,533** | $< 10^{-300}$ | **-0,214** | **-0,221** | **Negatif Sedang-Kuat:** Semakin tinggi elevasi lahan, produktivitas panen menurun signifikan. |
| **`Nitrogen`** | **+0,508** | $< 10^{-299}$ | **+0,522** | $< 10^{-300}$ | **+0,338** | **+0,316** | **Positif Sedang-Kuat:** Dosis N berkorelasi positif paling kuat terhadap produktivitas jagung. |
| **`Planting`** | **+0,452** | $3{,}9 \times 10^{-230}$ | **+0,465** | $3{,}0 \times 10^{-245}$ | **+0,117** | **+0,378** | **Positif Sedang (Terkonfounding):** Korelasi global tinggi karena perbedaan waktu tanam Hybrid vs Landrace. |
| **`Slope`** | **-0,391** | $2{,}7 \times 10^{-167}$ | **-0,406** | $6{,}7 \times 10^{-182}$ | **-0,218** | **-0,361** | **Negatif Sedang:** Lahan terjal berasosiasi dengan penurunan tajam hasil panen. |
| **`Phosphorus`** | **+0,342** | $5{,}5 \times 10^{-126}$ | **+0,365** | $1{,}2 \times 10^{-144}$ | **+0,216** | **+0,094** | **Positif Lemah-Sedang:** Asosiasi positif lebih nyata pada Hybrid daripada Landrace. |
| **`Potassium`** | **+0,298** | $1{,}5 \times 10^{-94}$ | **+0,304** | $1{,}2 \times 10^{-98}$ | **+0,156** | **+0,130** | **Positif Lemah:** Asosiasi tereduksi akibat 66% petak tanpa pupuk K. |
| **`PH`** | **+0,091** | $6{,}5 \times 10^{-10}$ | **+0,081** | $3{,}4 \times 10^{-8}$ | **-0,001** | **+0,136** | **Sangat Lemah:** Tanah mendekati netral/basa sedikit lebih unggul pada Landrace. |
| **`Clay`** | **-0,068** | $3{,}5 \times 10^{-6}$ | **-0,080** | $6{,}0 \times 10^{-8}$ | **-0,029** | **+0,043** | **Sangat Lemah / Mendekati Nol:** Tekstur liat peta tidak menjelaskan variansi panen. |
| **`CEC`** | **-0,064** | $1{,}6 \times 10^{-5}$ | **-0,054** | $2{,}8 \times 10^{-4}$ | **-0,044** | **+0,111** | **Sangat Lemah / Mendekati Nol:** KTK peta regional tidak memiliki daya prediksi langsung. |
| **`SOM`** | **-0,047** | $1{,}4 \times 10^{-3}$ | **-0,016** | $0{,}272$ *(ns)* | **-0,061** | **+0,021** | **Tidak Signifikan (Spearman $p>0{,}05$):** Bahan organik peta tidak berkorelasi dengan hasil panen. |

*(Keterangan: ns = non-significant pada tingkat signifikansi $\alpha = 0{,}05$).*

### 5.2 Evaluasi Pola Nonlinier dan Kurva Respons Agroteknologi

Untuk mendeteksi pola nonlinier, dilakukan pencocokan model polinomial orde-1 (linier) versus orde-2 (kuadratik: $Y = ax^2 + bx + c$) serta analisis stratifikasi interval (*binned analysis*). Hasilnya terangkum pada Tabel 7:

### Tabel 7: Uji Diagnostik Kurva Nonlinier Kuadratik Fitur Numerik terhadap `YIELD`

| Fitur Prediktor | $R^2$ Linier | $R^2$ Kuadratik | Peningkatan $\Delta R^2$ | Koefisien Kuadratik ($a$) | Karakter Kurva Nonlinier Lapangan |
|---|---:|---:|---:|---:|---|
| **`Elev`** | 0,2863 | 0,2864 | +0,0001 | $-0{,}00000$ | **Ambang Batas Kritis (*Threshold Effect*):** Hasil optimal stabil di $400$–$600\text{ m dpl}$, lalu merosot drastis di atas $800\text{ m dpl}$. |
| **`Nitrogen`** | 0,2581 | 0,2589 | +0,0008 | $-0{,}00001$ | **Kenaikan Hasil Berkurang (*Diminishing Returns*):** Koefisien $a < 0$ mengonfirmasi kurva cembung ke atas (*concave downward*). |
| **`Planting`** | 0,2046 | 0,2237 | **+0,0191** | $-0{,}00034$ | **Kurva Cembung Kuadratik:** Panen optimal pada jendela DOY $160$–$180$, menurun tajam bila tanam terlalu awal ($<140$) atau telat ($>200$). |
| **`Slope`** | 0,1528 | 0,1779 | **+0,0251** | $+0{,}00391$ | **Penurunan Eksponensial Cepat lalu Mendatar:** Hasil anjlok dari $0$ ke $10\%$, kemudian mendatar (*plateau*) pada lahan $>15\%$. |
| **`Phosphorus`** | 0,1172 | 0,1334 | +0,0162 | $-0{,}00026$ | **Plateau Response:** Respons pupuk P meningkat tajam dari $0$ ke $46\text{ kg ha}^{-1}$, lalu mendatar pada dosis $>60\text{ kg ha}^{-1}$. |
| **`Potassium`** | 0,0890 | 0,1044 | +0,0154 | $-0{,}00059$ | **Plateau Response:** Peningkatan hasil hanya tampak saat berpindah dari 0 ke $>20\text{ kg ha}^{-1}$. |
| **`PH`** | 0,0082 | 0,0103 | +0,0021 | $+0{,}12874$ | **Kurva Cekung Lemah:** Lahan asam ($\text{pH} < 6{,}0$) memiliki panen lebih rendah daripada lahan netral/basa ($\text{pH} > 6{,}8$). |
| **`Clay`** | 0,0046 | 0,0066 | +0,0020 | $+0{,}00074$ | **Nonlinier Lemah:** Tidak memperlihatkan pola agronomis yang tegas. |
| **`CEC`** | 0,0041 | 0,0044 | +0,0003 | $+0{,}00046$ | **Linier Rata:** Tidak memperlihatkan dinamika kurva respons bermakna. |
| **`SOM`** | 0,0022 | 0,0028 | +0,0006 | $-0{,}07695$ | **Rata / Acak:** Variabilitas bahan organik regional tidak mampu membedakan panen tinggi vs rendah. |

### 5.3 Analisis Detail Fenomena Agroteknologi Lapangan

#### A. Hukum Kenaikan Hasil yang Semakin Berkurang pada Pemupukan Nitrogen
Stratifikasi dosis Nitrogen aktual memperlihatkan peningkatan hasil panen yang konsisten namun melambat:
- **Dosis $0\text{ kg N ha}^{-1}$ ($N = 218$):** Median hasil panen hanya **$1{,}80\text{ Mg ha}^{-1}$** (rata-rata $2{,}08\text{ Mg ha}^{-1}$).
- **Dosis $1$–$50\text{ kg N ha}^{-1}$ ($N = 711$):** Median hasil panen **$1{,}70\text{ Mg ha}^{-1}$** (rata-rata $2{,}22\text{ Mg ha}^{-1}$).
- **Dosis $51$–$100\text{ kg N ha}^{-1}$ ($N = 1.126$):** Median melonjak ke **$3{,}00\text{ Mg ha}^{-1}$** (rata-rata $3{,}08\text{ Mg ha}^{-1}$).
- **Dosis $101$–$150\text{ kg N ha}^{-1}$ ($N = 1.184$):** Median mencapai **$4{,}00\text{ Mg ha}^{-1}$** (rata-rata $3{,}81\text{ Mg ha}^{-1}$).
- **Dosis $151$–$200\text{ kg N ha}^{-1}$ ($N = 988$):** Median mencapai **$4{,}80\text{ Mg ha}^{-1}$** (rata-rata $4{,}64\text{ Mg ha}^{-1}$).
- **Dosis $>200\text{ kg N ha}^{-1}$ ($N = 358$):** Median mencapai puncak **$5{,}40\text{ Mg ha}^{-1}$** (rata-rata $5{,}28\text{ Mg ha}^{-1}$).
*Catatan Kritis:* Koefisien kuadratik bertanda negatif ($a = -0{,}00001$) mengindikasikan bahwa laju pertambahan hasil panen per tambahan kilogram pupuk N mulai mengalami deselerasi (*diminishing marginal returns*). Penambahan N di atas $180\text{ kg ha}^{-1}$ hanya memberikan kenaikan panen marjinal.

#### B. Zona Agroklimat Optimal Elevasi Lahan (*Elevation Sweet-Spot*)
Stratifikasi elevasi mengungkap hubungan nonlinier berbentuk lonceng asimetris:
- **Dataran Rendah Pesisir ($<400\text{ m dpl}$, $N = 146$):** Median hasil panen **$3{,}50\text{ Mg ha}^{-1}$** (rata-rata $3{,}24\text{ Mg ha}^{-1}$). Produktivitas sedikit tertekan oleh stres suhu panas ekstrem atau drainase buruk.
- **Zona Optimal / Sweet-Spot ($400$–$600\text{ m dpl}$, $N = 1.108$):** Median hasil panen mencapai puncak tertinggi **$5{,}00\text{ Mg ha}^{-1}$** (rata-rata $4{,}70\text{ Mg ha}^{-1}$). Wilayah ini merupakan pusat produksi jagung intensif Chiapas (kawasan lembah La Fraylesca).
- **Dataran Sedang ($600$–$800\text{ m dpl}$, $N = 1.439$):** Median hasil panen **$4{,}40\text{ Mg ha}^{-1}$** (rata-rata $4{,}33\text{ Mg ha}^{-1}$).
- **Peralihan ($800$–$1.000\text{ m dpl}$, $N = 639$):** Median hasil turun tajam ke **$3{,}50\text{ Mg ha}^{-1}$** (rata-rata $3{,}40\text{ Mg ha}^{-1}$).
- **Pegunungan Tinggi ($1.000$–$1.500\text{ m dpl}$, $N = 630$):** Median hasil merosot ke **$1{,}70\text{ Mg ha}^{-1}$** (rata-rata $2{,}04\text{ Mg ha}^{-1}$).
- **Pegunungan Sangat Tinggi ($>1.500\text{ m dpl}$, $N = 623$):** Median hasil hanya **$1{,}50\text{ Mg ha}^{-1}$** (rata-rata $1{,}78\text{ Mg ha}^{-1}$).
*Penyebab Lapangan:* Di atas $1.000\text{ m dpl}$, suhu udara malam hari yang dingin memperpanjang masa pengisian biji, radiasi efektif berkurang akibat tutupan awan pegunungan, aksesibilitas logistik pupuk terbatas, dan didominasi varietas lokal berdaya hasil rendah.

#### C. Pengaruh Kelerengan Terhadap Hasil Panen
- **Lahan Datar ($0$–$2\%$, $N = 1.762$):** Median hasil **$4{,}35\text{ Mg ha}^{-1}$** (rata-rata $4{,}29\text{ Mg ha}^{-1}$).
- **Lahan Landai ($2$–$5\%$, $N = 1.092$):** Median hasil **$4{,}00\text{ Mg ha}^{-1}$** (rata-rata $3{,}98\text{ Mg ha}^{-1}$).
- **Lahan Agak Curam ($5$–$10\%$, $N = 730$):** Median hasil anjlok ke **$2{,}70\text{ Mg ha}^{-1}$** (rata-rata $3{,}03\text{ Mg ha}^{-1}$).
- **Lahan Curam ($10$–$20\%$, $N = 761$):** Median hasil **$1{,}80\text{ Mg ha}^{-1}$** (rata-rata $2{,}39\text{ Mg ha}^{-1}$).
- **Lahan Sangat Curam ($>20\%$, $N = 240$):** Median hasil mendatar di angka rendah **$1{,}68\text{ Mg ha}^{-1}$** (rata-rata $2{,}19\text{ Mg ha}^{-1}$).
*Penyebab Lapangan:* Penurunan drastis terjadi saat kelerengan melampaui $5\%$, yang memicu kehilangan lapisan tanah atas (*topsoil loss*) akibat erosi dan mempercepat aliran air permukaan (*surface runoff*).

#### D. Ilusi Korelasi Tanggal Tanam (`Planting`) Akibat Confounding
Secara global, korelasi Spearman antara `Planting` dan `YIELD` bertanda positif sedang ($\rho = +0{,}465$). Petak yang ditanam lebih lambat (akhir Juni hingga Juli) seolah-olah menghasilkan panen jauh lebih tinggi.
Namun, ketika diuji secara terpisah pada masing-masing sistem:
- Pada sistem **Hybrid**, korelasinya melemah drastis menjadi **$\rho_{\text{hyb}} = +0{,}117$** (hampir tidak berkorelasi).
- Rata-rata tanam petani Hybrid adalah DOY $173{,}26$ (akhir Juni), sedangkan petani Landrace menanam jauh lebih awal pada DOY $149{,}21$ (akhir Mei).
*Kesimpulan Kritis:* Korelasi global $+0{,}465$ adalah **korelasi semu akibat perancu (*confounded by System*)**. Petani Landrace di pegunungan terpaksa menanam lebih awal menyambut hujan pertama di dataran tinggi, dan kebetulan produktivitas Landrace memang rendah ($1{,}92\text{ Mg ha}^{-1}$). Sementara itu, petani Hybrid di lembah yang subur menanam belakangan dan memperoleh panen tinggi ($4{,}45\text{ Mg ha}^{-1}$).

---

## 6. Evaluasi Perbedaan Antarkelompok Fitur Kategorikal terhadap `YIELD`

Visualisasi perbandingan distribusi antarkelompok disajikan pada Gambar 5:

![Perbandingan Kelompok Kategorikal terhadap YIELD](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/eda_02_categorical_yield_comparisons.png)
*Gambar 5: Evaluasi kelompok kategorikal terhadap YIELD: (A) Violin plot System; (B) Violin plot Tillage global; (C) Interaksi silang System × Tillage; (D) Proporsi petak tanpa pupuk per sistem.*

### 6.1 Uji Signifikansi Komparasi Sistem Budidaya (`System`)

Perbedaan produktivitas antara sistem Hybrid dan Landrace diuji secara parametrik dan non-parametrik:
- **Parameter Hybrid ($N = 3.034$):** Rata-rata $\bar{Y} = 4{,}45\text{ Mg ha}^{-1}$, Standar Deviasi $s = 1{,}61$, Median $= 4{,}60$, $\text{IQR} = 2{,}00$, Rentang $= 0{,}10$–$9{,}80\text{ Mg ha}^{-1}$.
- **Parameter Landrace ($N = 1.551$):** Rata-rata $\bar{Y} = 1{,}92\text{ Mg ha}^{-1}$, Standar Deviasi $s = 1{,}03$, Median $= 1{,}65$, $\text{IQR} = 1{,}30$, Rentang $= 0{,}10$–$6{,}10\text{ Mg ha}^{-1}$.
- **Uji Beda Rata-rata (Welch's Two-Sample t-Test):**
  $$t = 64{,}45 \quad (df = 4.312{,}3; \quad p < 10^{-300})$$
- **Uji Beda Distribusi Peringkat (Mann-Whitney U Test):**
  $$U = 4.214.390 \quad (p < 10^{-300})$$

Kedua uji statistik mengonfirmasi bahwa perbedaan produktivitas antar-sistem budidaya sangat signifikan secara statistik ($p < 0{,}001$), dengan *effect size* yang sangat masif ($\Delta \bar{Y} = +2{,}53\text{ Mg ha}^{-1}$ keunggulan rata-rata pada varietas Hybrid).

### 6.2 Uji Signifikansi Komparasi Praktik Olah Tanah Global (`Tillage`)

Perbandingan produktivitas pada tiga kelompok olah tanah agregat:
- **`Conventional` ($N = 2.092$):** Rata-rata $3{,}50\text{ Mg ha}^{-1}$ ($s = 1{,}91$, Median $3{,}50$, $\text{IQR} = 3{,}40$).
- **`Reduced` ($N = 859$):** Rata-rata $3{,}71\text{ Mg ha}^{-1}$ ($s = 1{,}81$, Median $4{,}00$, $\text{IQR} = 3{,}00$).
- **`No-till` ($N = 1.634$):** Rata-rata $3{,}65\text{ Mg ha}^{-1}$ ($s = 1{,}84$, Median $3{,}50$, $\text{IQR} = 2{,}80$).
- **Uji ANOVA Satu Arah (One-Way ANOVA):**
  $$F = 5{,}01 \quad (p = 0{,}0067)$$
- **Uji Kruskal-Wallis Non-Parametrik:**
  $$H = 8{,}68 \quad (df = 2; \quad p = 0{,}0130)$$

Secara global, terdapat perbedaan kecil yang signifikan antar-kategori olah tanah ($p < 0{,}05$), di mana olah tanah minimum (*Reduced*) dan tanpa olah tanah (*No-till*) mencatat rata-rata hasil sedikit lebih tinggi daripada olah tanah konvensional.

### 6.3 Interaksi Kritis `System` $\times$ `Tillage`: Pembalikan Efektivitas Olah Tanah (Simpson's Paradox Agroteknologi)

Ketika praktik olah tanah dianalisis secara terstratifikasi di dalam masing-masing sistem budidaya, ditemukan **fenomena interaksi agronomis yang sangat kontras** sebagaimana dirangkum pada Tabel 8:

### Tabel 8: Analisis Interaksi `System` $\times$ `Tillage` terhadap Produktivitas Jagung

| Sistem Budidaya | Praktik Olah Tanah | Jumlah Petak ($N$) | Mean YIELD ($\text{Mg ha}^{-1}$) | Std ($s$) | Median YIELD | IQR | Uji Signifikansi Sub-Sistem |
|---|---|---:|---:|---:|---:|---:|---|
| **`Hybrid`** | **`Conventional`** | **1.306** | **4,54** | 1,55 | **4,90** | 2,00 | **ANOVA:** $F = 6{,}53$ ($p = 0{,}0015$)<br>**Kruskal-Wallis:** $H = 17{,}11$ ($p = 0{,}0002$) |
| | **`No-till`** | 1.072 | 4,44 | 1,65 | 4,50 | 2,20 | *Pola:* $\text{Conventional} > \text{No-till} > \text{Reduced}$ |
| | **`Reduced`** | 656 | 4,26 | 1,63 | 4,50 | 2,15 | |
| **`Landrace`** | **`No-till`** | **562** | **2,15** | 1,10 | **2,00** | 1,49 | **ANOVA:** $F = 23{,}17$ ($p = 1{,}1 \times 10^{-10}$)<br>**Kruskal-Wallis:** $H = 51{,}50$ ($p = 6{,}6 \times 10^{-12}$) |
| | **`Reduced`** | 203 | 1,91 | 0,97 | 1,60 | 1,25 | *Pola Terbalik:* $\text{No-till} > \text{Reduced} > \text{Conventional}$ |
| | **`Conventional`** | 786 | 1,77 | 0,95 | 1,50 | 1,15 | |

> [!WARNING]
> **Pembalikan Efektivitas Olah Tanah (*Interaction / Moderation Effect*):**
> 1. Pada **Sistem Hybrid (Lahan Datar Lembah Subur):** Pembajakan konvensional menghasilkan panen tertinggi (median $4{,}90\text{ Mg ha}^{-1}$ vs No-till $4{,}50\text{ Mg ha}^{-1}$). Di lahan dataran dengan mekanisasi penuh, aerasi tanah dan pembalikan gulma oleh bajak memfasilitasi penyerapan pupuk kimia intensif.
> 2. Pada **Sistem Landrace (Lahan Pegunungan Terjal):** Terjadi pembalikan total. Tanpa olah tanah (**`No-till`**) menghasilkan produktivitas **tertinggi secara signifikan** (median $2{,}00\text{ Mg ha}^{-1}$, rata-rata $2{,}15\text{ Mg ha}^{-1}$), sedangkan olah tanah konvensional menghasilkan panen terendah (median $1{,}50\text{ Mg ha}^{-1}$, rata-rata $1{,}77\text{ Mg ha}^{-1}$).
> 3. **Rasionalitas Lapangan:** Petani tradisional Landrace menanam di lereng bukit curam. Membajak tanah di lereng curam merusak agregat tanah, memicu erosi hebat, dan menguras kelembaban tanah. Sistem *No-till* menjaga mulsa organik penutup tanah, menahan lengas air hujan, dan mencegah hanyutnya lapisan perakaran, sehingga memberikan keunggulan produktivitas riil sebesar $+21{,}5\%$ dibandingkan pembajakan konvensional di perbukitan.

---

## 7. Pemeriksaan Potensi Multikolinearitas Antar-Fitur Numerik

Visualisasi pemeriksaan multikolinearitas disajikan pada Gambar 6:

![Pemeriksaan Multikolinearitas dan VIF](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/eda_02_multicollinearity_and_vif.png)
*Gambar 6: Diagnostik multikolinearitas fitur numerik: (A) Matriks Korelasi Rank Spearman; (B) Matriks Korelasi Linear Pearson; (C) Bar Chart Variance Inflation Factor (VIF).*

### 7.1 Matriks Korelasi Bivariat Antar-Fitur Numerik

Tabel 9 memuat nilai koefisien korelasi linear Pearson ($r$, segitiga atas) dan korelasi rank Spearman ($\rho$, segitiga bawah) antar seluruh 10 fitur prediktor numerik:

### Tabel 9: Matriks Korelasi Antar-Fitur Prediktor Numerik

| Fitur | `Nitrogen` | `Phosphorus` | `Potassium` | `Planting` | `Clay` | `CEC` | `SOM` | `PH` | `Elev` | `Slope` |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **`Nitrogen`** | $1{,}000$ | $+0{,}390$ | $+0{,}251$ | $+0{,}303$ | $-0{,}037$ | $-0{,}036$ | $-0{,}018$ | $+0{,}046$ | $-0{,}271$ | $-0{,}300$ |
| **`Phosphorus`** | $+0{,}404$ | $1{,}000$ | $+0{,}397$ | $+0{,}248$ | $+0{,}018$ | $+0{,}019$ | $+0{,}017$ | $+0{,}046$ | $-0{,}231$ | $-0{,}203$ |
| **`Potassium`** | $+0{,}250$ | $+0{,}478$ | $1{,}000$ | $+0{,}271$ | $+0{,}001$ | $-0{,}002$ | $-0{,}010$ | $+0{,}028$ | $-0{,}228$ | $-0{,}196$ |
| **`Planting`** | $+0{,}327$ | $+0{,}289$ | $+0{,}291$ | $1{,}000$ | $-0{,}050$ | $-0{,}048$ | $-0{,}025$ | $+0{,}033$ | $-0{,}481$ | $-0{,}336$ |
| **`Clay`** | $-0{,}049$ | $+0{,}017$ | $-0{,}001$ | $-0{,}049$ | $1{,}000$ | $+0{,}621$ | $+0{,}245$ | $+0{,}225$ | $+0{,}124$ | $+0{,}057$ |
| **`CEC`** | $-0{,}046$ | $+0{,}013$ | $-0{,}001$ | $-0{,}053$ | $+0{,}606$ | $1{,}000$ | $+0{,}468$ | $+0{,}474$ | $+0{,}059$ | $+0{,}002$ |
| **`SOM`** | $-0{,}017$ | $+0{,}012$ | $-0{,}007$ | $-0{,}024$ | $+0{,}273$ | $+0{,}567$ | $1{,}000$ | $+0{,}266$ | $+0{,}101$ | $+0{,}058$ |
| **`PH`** | $+0{,}054$ | $+0{,}042$ | $+0{,}021$ | $+0{,}037$ | $+0{,}269$ | $+0{,}549$ | $+0{,}251$ | $1{,}000$ | $-0{,}089$ | $-0{,}070$ |
| **`Elev`** | $-0{,}292$ | $-0{,}247$ | $-0{,}235$ | $-0{,}434$ | $+0{,}128$ | $+0{,}063$ | $+0{,}103$ | $-0{,}089$ | $1{,}000$ | $+0{,}338$ |
| **`Slope`** | $-0{,}315$ | $-0{,}215$ | $-0{,}198$ | $-0{,}311$ | $+0{,}060$ | $+0{,}001$ | $+0{,}048$ | $-0{,}075$ | $+0{,}376$ | $1{,}000$ |

*(Catatan: Nilai di atas diagonal utama adalah korelasi Pearson $r$; nilai di bawah diagonal utama adalah korelasi Spearman Rank $\rho$).*

### 7.2 Analisis Korelasi Berpasangan Tertinggi (*Pairwise Collinearity*)

Pasangan fitur yang menunjukkan korelasi terkuat dalam dataset adalah:
1. **`Clay` vs `CEC` ($r = +0{,}621, \rho = +0{,}606$):** Korelasi alami geokimia tanah. Fraksi liat bermuatan negatif merupakan penyusun utama kapasitas tukar kation tanah.
2. **`CEC` vs `SOM` ($r = +0{,}468, \rho = +0{,}567$):** Koloid humus bahan organik menyumbangkan gugus karboksil dan fenol yang meningkatkan KTK tanah.
3. **`CEC` vs `PH` ($r = +0{,}474, \rho = +0{,}549$):** Tanah netral/basa umumnya didominasi kation basa ($\text{Ca}^{2+}, \text{Mg}^{2+}, \text{K}^+$), mempertahankan KTK efektif lebih tinggi.
4. **`Planting` vs `Elev` ($r = -0{,}481, \rho = -0{,}434$):** Petak dataran tinggi ditanam lebih awal (DOY lebih rendah) mengikuti siklus hujan pegunungan.
5. **`Phosphorus` vs `Potassium` ($r = +0{,}397, \rho = +0{,}478$):** Ko-aplikasi pupuk majemuk NPK atau paket subsidi pemupukan berimbang.
6. **`Elev` vs `Slope` ($r = +0{,}338, \rho = +0{,}376$):** Karakteristik fisiografis di mana wilayah dataran tinggi Chiapas memiliki morfologi perbukitan curam.

Tidak ada satu pun pasangan variabel prediktor yang memiliki koefisien korelasi $|r| \ge 0{,}70$ atau $|\rho| \ge 0{,}70$.

### 7.3 Hasil Perhitungan Variance Inflation Factor (VIF)

Tabel 10 menyajikan nilai VIF empiris untuk seluruh 10 fitur numerik:

### Tabel 10: Hasil Diagnostik Variance Inflation Factor (VIF)

| Peringkat | Fitur Prediktor Numerik | Nilai VIF Aktual | Ambang Waspada Konservatif | Batas Kritis Multikolinearitas | Status Diagnostik & Rekomendasi |
|---:|---|---:|:---:|:---:|---|
| 1 | **`CEC`** | **3,639** | $< 5{,}0$ | $< 10{,}0$ | **Sangat Aman (Bebas Masalah):** VIF tertinggi akibat kovariansi alami dengan `Clay`, `SOM`, dan `PH`. |
| 2 | **`Clay`** | **2,497** | $< 5{,}0$ | $< 10{,}0$ | **Sangat Aman:** Mengalami inflasi variansi sedang akibat asosiasi dengan `CEC`. |
| 3 | **`PH`** | **1,857** | $< 5{,}0$ | $< 10{,}0$ | **Sangat Aman:** Inflasi variansi minimal. |
| 4 | **`Planting`** | **1,463** | $< 5{,}0$ | $< 10{,}0$ | **Sangat Aman:** Kovariansi dengan elevasi tidak memicu instabilitas numerik. |
| 5 | **`Elev`** | **1,457** | $< 5{,}0$ | $< 10{,}0$ | **Sangat Aman:** Bebas dari kolinearitas parah. |
| 6 | **`SOM`** | **1,443** | $< 5{,}0$ | $< 10{,}0$ | **Sangat Aman:** Bebas dari kolinearitas parah. |
| 7 | **`Phosphorus`** | **1,364** | $< 5{,}0$ | $< 10{,}0$ | **Sangat Aman:** Kovariansi dengan N dan K tergolong rendah. |
| 8 | **`Slope`** | **1,330** | $< 5{,}0$ | $< 10{,}0$ | **Sangat Aman:** Bebas dari kolinearitas parah. |
| 9 | **`Nitrogen`** | **1,311** | $< 5{,}0$ | $< 10{,}0$ | **Sangat Aman:** Bebas dari kolinearitas parah. |
| 10 | **`Potassium`** | **1,256** | $< 5{,}0$ | $< 10{,}0$ | **Sangat Aman:** Bebas dari kolinearitas parah. |

> [!NOTE]
> **Kesimpulan Multikolinearitas:**
> Seluruh nilai VIF berada di bawah **$3{,}7$**, jauh di bawah batas toleransi konservatif $5{,}0$ dan batas bahaya $10{,}0$. Hal ini membuktikan secara matematis bahwa **tidak ada masalah multikolinearitas berbahaya (*no severe multicollinearity*)** pada 10 fitur numerik non-cuaca. Seluruh fitur dapat dipertahankan untuk pertimbangan pemodelan berikutnya tanpa kekhawatiran terjadinya ledakan standar eror regresi (*variance inflation*).

---

## 8. Interpretasi Kritis: Fakta Terverifikasi, Keterbatasan Bukti, dan Penolakan Spekulasi Kausal

Bagian ini menegaskan batasan inferensi ilmiah dari temuan EDA Tahap 2 untuk mencegah penarikan kesimpulan yang melampaui data aktual:

### 8.1 Fakta Terverifikasi yang Terbukti dari Data Aktual
1. **Asosiasi Dominan:** Dua fitur non-cuaca yang memiliki kovariansi terbesar dengan variasi hasil panen jagung adalah **`Elev`** ($\rho = -0{,}533$) dan **`Nitrogen`** ($\rho = +0{,}522$).
2. **Disparitas Sistem Budidaya:** Terdapat perbedaan hasil panen riil sebesar $+2{,}53\text{ Mg ha}^{-1}$ antara sistem Hybrid (median $4{,}60\text{ Mg ha}^{-1}$) dan Landrace (median $1{,}65\text{ Mg ha}^{-1}$). Disparitas ini disertai oleh perbedaan drastis dalam elevasi (Hybrid di dataran rendah $701\text{ m dpl}$, Landrace di pegunungan $1.244\text{ m dpl}$) dan input pupuk N (Hybrid $128\text{ kg ha}^{-1}$, Landrace $73\text{ kg ha}^{-1}$).
3. **Efek Pembalikan Olah Tanah (Interaksi):** Keunggulan praktik olah tanah bergantung pada sistem budidaya dan kondisi biofisik lahan. Di dataran rendah dengan sistem Hybrid, olah tanah konvensional lebih unggul; sebaliknya di perbukitan terjal pegunungan dengan sistem Landrace, sistem tanpa olah tanah (**No-till**) terbukti menghasilkan panen tertinggi ($+21{,}5\%$).
4. **Ortogonalitas Geokimia Tanah Regional:** Variabel tanah INEGI (`Clay`, `CEC`, `SOM`, `PH`) memiliki korelasi yang sangat mendekati nol dengan variasi panen lapangan ($|\rho| < 0{,}09$).

### 8.2 Keterbatasan Bukti Lapangan & Bahaya Asumsi Kausal
1. **Jangan Menyimpulkan Bahwa Benih Hybrid Secara Mandiri Menyebabkan Kenaikan Panen:**
   Keunggulan produksi sistem Hybrid tidak dapat diklaim semata-mata sebagai efek genetik benih. Petak Hybrid berada di dataran rendah yang subur, menerima pupuk nitrogen dan fosfat $2\times$ lebih banyak, dan dikelola petani komersial. Ada bias seleksi lahan (*selection bias*) dan faktor perancu (*confounding factors*) yang masif.
2. **Keterbatasan Kualitas Data Tanah Sekunder (INEGI):**
   Rendahnya korelasi variabel tanah dengan YIELD kemungkinan besar bukan berarti kesuburan tanah tidak berpengaruh terhadap jagung, melainkan karena data tanah bersumber dari **peta poligon berskala tinjau regional dari INEGI**, bukan hasil uji laboratorium tanah *in-situ* dari masing-masing petak petani pada musim tersebut. Keterbatasan resolusi spasial dan temporal data peta sekunder ini mereduksi daya prediksinya.
3. **Jangan Mengasumsikan Pemupukan Terjadi Sekaligus Sebelum Tanam:**
   Data dosis Nitrogen, Fosfat, dan Kalium adalah **akumulasi riil pascapanen**, bukan aplikasi tunggal pra-tanam. Mengasumsikan pupuk ini dapat langsung dimasukkan ke model prediksi sebelum tanam tanpa memperlakukannya sebagai skenario rekomendasi akan menimbulkan galat logika penerapan sistem di dunia nyata.

---

## 9. Rekomendasi Langkah Analisis Berikutnya yang Paling Tepat

Berdasarkan hasil temuan univariat, bivariat, interaksi agronomis, dan analisis ketersediaan temporal pada Tahap 1 dan 2, rekomendasi langkah berikutnya yang paling tepat dan esensial bagi penelitian prediksi hasil panen jagung skripsi ini adalah:

> [!TIP]
> ### Rekomendasi Langkah Selanjutnya:
> **EDA TAHAP 3 — Eksplorasi Temporal Dinamis 150 Variabel Cuaca Daymet (Presipitasi, Radiasi Surya, Suhu Maksimum/Minimum, Tekanan Uap dalam 30 Interval 10-Harian) dan Formulasi Jendela Prediksi Pra-Tanam vs Dalam-Musim**
> 
> **Fokus & Agenda Utama EDA Tahap 3:**
> 1. **Pemetaan Siklus Temporal Cuaca Daymet:** Menganalisis lintasan temporal dinamika iklim harian yang diringkas dalam 30 interval 10-harian (`prcp_V1`–`V30`, `srad_V1`–`V30`, `tmax_V1`–`V30`, `tmin_V1`–`V30`, `vp_V1`–`V30`), mulai dari 60 hari sebelum tanam (V1–V6) hingga 240 hari setelah tanam (V7–V30).
> 2. **Identifikasi Fase Fenologi Kritis Tanaman Jagung:** Mengidentifikasi interval cuaca mana yang memiliki korelasi bivariat terkuat terhadap `YIELD`, khususnya pada fase pembungaan/penyerbukan (*silking/tasseling*, sekitar interval V12–V16) dan fase pengisian biji (*grain filling*, V17–V22).
> 3. **Pemisahan Jendela Prediksi Bebas Data Leakage (*Pre-Planting Feature Window*):** Mengisolasi variabel cuaca sebelum tanam (interval V1–V6) untuk model prediksi sebelum tanam (*ex-ante*), serta merancang opsi agregasi kumulatif cuaca jika model difungsikan untuk pemantauan dalam-musim (*in-season monitoring*).
> 4. **Penanganan Dimensi Tinggi & Multikolinearitas Deret Waktu:** Mengingat terdapat 150 variabel cuaca dengan autokorelasi serial yang sangat tinggi, EDA Tahap 3 harus merancang strategi reduksi dimensi (misalnya ringkasan fitur statistik per fase pertumbuhan: total curah hujan vegetatif vs generatif, rata-rata suhu puncak penyerbukan, dsb.) guna mempersiapkan tahap *data preparation*.

---

## 10. Indeks Berkas Laporan & Visualisasi Terkait

Seluruh berkas visualisasi pendukung resolusi tinggi ($300\text{ DPI}$) telah tersimpan pada repositori lokal dan dapat diakses langsung melalui tautan berikut:

1. [EDA_02_AGRONOMY_SOIL_TOPOGRAPHY.md](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/EDA_02_AGRONOMY_SOIL_TOPOGRAPHY.md): Laporan lengkap EDA Tahap 2 Fitur Agronomi, Tanah, dan Topografi.
2. [eda_02_agronomy_univariate.png](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/eda_02_agronomy_univariate.png): Visualisasi distribusi univariat fitur-fitur agronomi (Nitrogen, Phosphorus, Potassium, Planting, System, Tillage).
3. [eda_02_soil_topography_univariate.png](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/eda_02_soil_topography_univariate.png): Visualisasi distribusi univariat fitur tanah dan topografi (Clay, CEC, SOM, PH, Elev, Slope).
4. [eda_02_agronomy_vs_yield_bivariate.png](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/eda_02_agronomy_vs_yield_bivariate.png): Scatter plot dan garis tren bivariat fitur agronomi terhadap target YIELD dengan stratifikasi sistem.
5. [eda_02_soil_topography_vs_yield_bivariate.png](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/eda_02_soil_topography_vs_yield_bivariate.png): Scatter plot dan garis tren bivariat fitur tanah dan topografi terhadap target YIELD.
6. [eda_02_categorical_yield_comparisons.png](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/eda_02_categorical_yield_comparisons.png): Evaluasi perbandingan kelompok kategorikal (System, Tillage, interaksi System × Tillage, dan proporsi zero fertilizer).
7. [eda_02_multicollinearity_and_vif.png](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/eda_02_multicollinearity_and_vif.png): Diagnostik multikolinearitas (Heatmap korelasi Spearman, Pearson, dan bar chart Variance Inflation Factor).
8. [generate_eda_02_charts.py](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/generate_eda_02_charts.py): Skrip Python otomatisasi untuk menghasilkan seluruh grafik visualisasi resolusi tinggi di atas.
9. [run_detailed_eda_02_stats.py](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/run_detailed_eda_02_stats.py): Skrip kalkulasi statistik lengkap, korelasi, uji hipotesis, dan VIF.
10. [eda_02_stats_summary.json](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/eda_02_stats_summary.json): Berkas rekaman numerik JSON berisi seluruh output komputasi statistik presisi tinggi.
11. [EDA_01_TARGET_YIELD.md](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/EDA_01_TARGET_YIELD.md): Laporan acuan resmi EDA Tahap 1 Variabel Target YIELD.
