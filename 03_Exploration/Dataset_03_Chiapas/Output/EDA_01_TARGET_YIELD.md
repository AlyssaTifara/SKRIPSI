# LAPORAN EXPLORATORY DATA ANALYSIS (EDA) TAHAP 1
## Analisis Univariat Mendalam Variabel Target `YIELD` (Produktivitas Jagung)
### Dataset: Multiyear Maize Management Dataset, Chiapas, Mexico (2012–2018)

---

## 1. Identitas Dokumen & Ruang Lingkup Analisis

### 1.1 Konteks Skripsi & Relevansi Variabel Target
Laporan ini merupakan dokumen resmi **Exploratory Data Analysis (EDA) Tahap 1** yang berfokus penuh dan mendalam pada variabel target utama: **`YIELD`** (produktivitas tanaman jagung dalam satuan metrik ton per hektar atau $\text{Mg ha}^{-1}$).

Dalam kerangka penelitian skripsi bertajuk *"Pemodelan Prediksi Jumlah Ayam Petelur untuk Smart Farming Berdasarkan Ketersediaan Lahan Jagung untuk Mendukung Perencanaan Produksi di Komunitas ASA Indonesia"*, variabel `YIELD` memegang peranan arsitektural yang sangat vital:
1. **Fondasi Estimasi Ketersediaan Pakan Mandiri:** Model *machine learning* yang akan dibangun bertugas memprediksi hasil panen jagung per petak lahan berdasarkan profil agroklimat dan manajemen budidaya.
2. **Kalkulasi Kapasitas Tampung Ternak:** Nilai prediksi `YIELD` dikonversikan menjadi total biomassa biji jagung pipil kering panen yang siap dijadikan bahan baku pakan utama (energi karbohidrat ~50–60% dalam formulasi pakan unggas petelur). Hasil tersebut menentukan batas daya dukung (*carrying capacity*) populasi ayam petelur yang dapat dipelihara secara berkelanjutan oleh peternak mitra Komunitas ASA tanpa risiko defisit pakan mendadak.
3. **Eksplorasi Perilaku Variabel Target:** Memahami karakteristik intrinsik distribusi `YIELD`—seperti pemusatan data, rentang variabilitas, keberadaan sub-populasi, bentuk kemencengan, dan perilaku nilai-nilai ekstrem—merupakan prasyarat mutlak sebelum melangkah ke pemodelan statistik atau pemilihan algoritma prediktif.

### 1.2 Batasan Ruang Lingkup Ketat (Scope Boundaries)
Sesuai arahan metodologis dan pedoman integritas data:
- **Dataset Acuan:** Berkas [Chiapas_Data.csv](file:///C:/SKRIPSI/02_Raw_Data/Dataset_03_Chiapas/Chiapas_Data.csv) yang bersumber langsung dari [Chiapas Field Data 2012-2018.xlsx](file:///C:/SKRIPSI/02_Raw_Data/Dataset_03_Chiapas/Chiapas%20Field%20Data%202012-2018.xlsx). Berkas mentah dipertahankan apa adanya (*read-only*) dan tidak diubah sedikit pun.
- **Memanfaatkan Audit Sebelumnya (Tanpa Repetisi):** Laporan ini memanfaatkan hasil temuan dari [LAPORAN_VERIFIKASI_KRITIS_CHIAPAS.md](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/LAPORAN_VERIFIKASI_KRITIS_CHIAPAS.md), [LAPORAN_DATA_UNDERSTANDING_CHIAPAS.md](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/LAPORAN_DATA_UNDERSTANDING_CHIAPAS.md), [LAPORAN_AUDIT_KUALITAS_DATA_CHIAPAS.md](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/LAPORAN_AUDIT_KUALITAS_DATA_CHIAPAS.md), dan [DATA_DICTIONARY_CHIAPAS.md](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/DATA_DICTIONARY_CHIAPAS.md). Sesuai instruksi, **TIDAK ADA pengulangan audit kualitas data umum, analisis missing values, atau pemeriksaan duplikasi baris/kolom**.
- **Batasan Eksplorasi Tahap 1:** Tahap ini dibatasi secara ketat pada **analisis statistik deskriptif dan visualisasi univariat serta dekomposisi subgrup terhadap `YIELD`**, tanpa melakukan analisis korelasi multivariat, rekayasa fitur (*feature engineering*), seleksi fitur (*feature selection*), pembersihan/penghapusan data (*data dropping/imputation*), transformasi distribusi, atau pemodelan (*machine learning*).
- **Integritas Observasi:** Seluruh identifikasi indikasi nilai ekstrem (outlier) dilakukan secara diagnostik **tanpa menghapus satu baris pun data aktual**.

---

## 2. Statistik Deskriptif Komprehensif Target `YIELD`

Variabel `YIELD` merepresentasikan hasil biji jagung pipil kering (*dry grain yield*) yang dipanen dari petak ubinan baku ($5\text{ m} \times 1{,}5\text{ m}$ pada 5 titik representatif) dan telah distandarisasi ke kadar air 14% (*moisture content adjusted to 14%*).

### 2.1 Ringkasan Parameter Statistik Deskriptif Keseluruhan ($N = 4.585$)

Tabel berikut menyajikan parameter statistik pemusatan, penyebaran, dan bentuk distribusi dari data aktual:

| Parameter Statistik | Simbol / Notasi | Nilai Komputasi Aktual | Satuan | Keterangan Matematis & Interpretasi Deskriptif |
|---|:---:|---:|:---:|---|
| **Jumlah Observasi (Count)** | $N$ | **4.585** | petak | Jumlah total baris valid tanpa ada satu pun nilai kosong (*zero missing*). |
| **Nilai Minimum** | $P_0 / \text{Min}$ | **0,1000** | $\text{Mg ha}^{-1}$ | Panen terendah tercatat (setara 100 kg/ha); tidak ada panen nol mutlak. |
| **Kuartil 1 (25th Percentile)** | $Q_1 / P_{25}$ | **1,8500** | $\text{Mg ha}^{-1}$ | 25% petak lahan menghasilkan $\le 1{,}85\text{ Mg ha}^{-1}$. |
| **Median (50th Percentile)** | $\text{Med} / P_{50}$ | **3,6000** | $\text{Mg ha}^{-1}$ | Titik tengah pembagi populasi; 50% data berada di atas dan di bawah $3{,}60$. |
| **Rata-rata Aritmatika (Mean)** | $\bar{Y}$ | **3,5926** | $\text{Mg ha}^{-1}$ | Nilai ekspektasi agregat ($3.592{,}56\text{ kg ha}^{-1}$); selaras dengan median. |
| **Kuartil 3 (75th Percentile)** | $Q_3 / P_{75}$ | **5,0000** | $\text{Mg ha}^{-1}$ | 75% petak lahan menghasilkan $\le 5{,}00\text{ Mg ha}^{-1}$. |
| **Nilai Maksimum** | $P_{100} / \text{Max}$ | **9,8000** | $\text{Mg ha}^{-1}$ | Panen tertinggi tercatat (setara 9.800 kg/ha); dicapai oleh varietas hibrida. |
| **Jangkauan Antar-Kuartil (IQR)** | $\text{IQR}$ | **3,1500** | $\text{Mg ha}^{-1}$ | Rentang sebaran 50% data inti ($Q_3 - Q_1 = 5{,}00 - 1{,}85$). |
| **Rentang Total (Range)** | $R$ | **9,7000** | $\text{Mg ha}^{-1}$ | Selisih nilai maksimum dan minimum ($\text{Max} - \text{Min} = 9{,}80 - 0{,}10$). |
| **Standar Deviasi Sampel** | $s$ | **1,8686** | $\text{Mg ha}^{-1}$ | Dispersi sebaran data di sekitar rata-rata aritmatika. |
| **Varians Sampel** | $s^2$ | **3,4915** | $\text{Mg}^2\text{ ha}^{-2}$ | Kuadrat deviasi standar populasi sampel. |
| **Koefisien Variasi (CV)** | $\text{CV}$ | **52,01%** | % | Variabilitas relatif yang sangat tinggi ($s / \bar{Y} \times 100\%$). |
| **Kemencengan (Skewness)** | $\gamma_1$ | **+0,1836** | - | Kemencengan positif sangat lemah (*near-symmetric* secara agregat). |
| **Kurtosis (Excess Kurtosis)** | $\gamma_2$ | **-0,7709** | - | Distribusi *platykurtic* (ekor lebih tipis dan puncak lebih datar dari kurva normal). |

> [!NOTE]
> **Konsistensi Audit:** Angka-angka di atas identik 100% dengan hasil audit independen pada [LAPORAN_VERIFIKASI_KRITIS_CHIAPAS.md](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/LAPORAN_VERIFIKASI_KRITIS_CHIAPAS.md#L48-L62), menegaskan kembali bahwa rata-rata aktual populasi data adalah **$3{,}59\text{ Mg ha}^{-1}$** dan median aktual adalah **$3{,}60\text{ Mg ha}^{-1}$** (mengoreksi kesalahan ketik angka 6 pada tabel paper publikasi Trevisan et al., 2022).

### 2.2 Sebaran Persentil Lengkap

Untuk memahami gradasi densitas data di sepanjang rentang $0{,}1$ hingga $9{,}8\text{ Mg ha}^{-1}$, berikut adalah tabel persentil empiris:

| Persentil | Nilai ($\text{Mg ha}^{-1}$) | Nilai Ekuivalen ($\text{kg ha}^{-1}$) | Interpretasi Lapangan |
|---|---:|---:|---|
| **$P_1$ (1%)** | 0,4000 | 400 | Batas bawah 1% lahan dengan produktivitas marjinal/tertekan parah. |
| **$P_5$ (5%)** | 0,8678 | 868 | 5% lahan menghasilkan kurang dari 0,87 ton/ha. |
| **$P_{10}$ (10%)** | 1,2000 | 1.200 | Batas desil pertama. |
| **$P_{25}$ ($Q_1$)** | 1,8500 | 1.850 | Kuartil bawah; batas pemisah kuadran produksi subsisten rendah. |
| **$P_{50}$ (Median)** | 3,6000 | 3.600 | Median populasi agregat. |
| **$P_{75}$ ($Q_3$)** | 5,0000 | 5.000 | Kuartil atas; awal kelompok produksi komersial tinggi. |
| **$P_{90}$ (90%)** | 6,0000 | 6.000 | Batas desil teratas; 10% petak lahan menghasilkan $\ge 6{,}00\text{ Mg ha}^{-1}$. |
| **$P_{95}$ (95%)** | 6,5000 | 6.500 | Kelompok elit 5% lahan berproduktivitas istimewa. |
| **$P_{99}$ (99%)** | 7,9580 | 7.958 | Batas 1% lahan teratas di Negara Bagian Chiapas. |

---

## 3. Analisis Visualisasi Bentuk Distribusi Target `YIELD`

Visualisasi distribusi keseluruhan disajikan pada gambar resolusi tinggi berikut:

![Distribusi Keseluruhan YIELD](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/eda_01_yield_distribusi_overall.png)
*Gambar 1: (A) Boxplot distribusi YIELD dengan garis pemusatan data dan pagar Tukey. (B) Histogram dan kurva Kernel Density Estimation (KDE) YIELD (N = 4.585).*

### 3.1 Evaluasi Bentuk Kurva dan Ilusi Normalitas Semu
1. **Kemencengan Rendah (+0,1836) Bukan Pertanda Distribusi Normal:**
   Secara sepintas, nilai *skewness* $+0{,}1836$ dan kedekatan nilai rata-rata ($3{,}59$) dengan median ($3{,}60$) sering kali disalahartikan sebagai bukti bahwa target berdistribusi normal (simetris Gaussian). Namun, inspeksi visual pada Gambar 1B secara tegas membantah asumsi tersebut.
2. **Karakter Platykurtic dan Indikasi Bimodalitas:**
   Nilai *excess kurtosis* bertanda negatif yang substansial ($\gamma_2 = -0{,}7709$) mengonfirmasi bahwa puncak kurva densitas tidak runcing, melainkan melebar rata (*flat-topped*). Terdapat lekukan (*valley*) di sekitar rentang $2{,}8$–$3{,}4\text{ Mg ha}^{-1}$ yang memisahkan dua puncak frekuensi (*bimodal distribution*):
   - **Puncak Pertama (Mode Rendah):** Berada pada rentang frekuensi sekitar **$1{,}5$ hingga $2{,}0\text{ Mg ha}^{-1}$**.
   - **Puncak Kedua (Mode Tinggi):** Berada pada rentang frekuensi sekitar **$4{,}5$ hingga $5{,}2\text{ Mg ha}^{-1}$**.
3. **Penyebab Struktural Bimodalitas:**
   Bimodalitas ini bukan disebabkan oleh anomali instrumen pencatatan data, melainkan mencerminkan adanya **dua populasi riil yang berbeda secara biologis dan agronomis di lapangan**, yaitu pembedaan sistem budidaya (`Hybrid` versus `Landrace`).

---

## 4. Analisis Distribusi `YIELD` Berdasarkan Sistem Budidaya (`System`)

Dalam dataset Chiapas, variabel kategorikal `System` mencatat dua pendekatan budidaya jagung yang sangat kontras di Meksiko:
- **`Hybrid` ($N = 3.034$, 66,17%):** Penanaman benih jagung hibrida komersial unggul (misalnya varietas DEKALB, Pioneer, Syngenta) yang dipadukan dengan pemupukan sintetis intensif, kepadatan tanam tinggi, dan umumnya berada di lahan dataran atau lembah yang subur.
- **`Landrace` ($N = 1.551$, 33,83%):** Penanaman jagung varietas lokal (*criollo*) warisan turun-temurun oleh petani pribumi/subsisten, dengan input pupuk kimia minimal atau tanpa pupuk, di lahan berlereng curam (*sloping hillsides*).

Visualisasi dekomposisi bimodalitas berdasarkan sistem disajikan pada gambar berikut:

![Distribusi YIELD berdasarkan Sistem](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/eda_01_yield_by_system.png)
*Gambar 2: (A) Boxplot komparatif produktivitas jagung sistem Hybrid vs Landrace. (B) Dekomposisi kurva densitas KDE yang memperlihatkan pemisahan tegas dua puncak populasi.*

### 4.1 Tabel Komparasi Statistik Deskriptif: Hybrid vs Landrace

| Parameter Statistik | Sistem `Hybrid` | Sistem `Landrace` | Perbedaan ($\Delta = \text{H} - \text{L}$) | Rasio ($\text{H} / \text{L}$) |
|---|---:|---:|---:|---:|
| **Jumlah Observasi ($N$)** | **3.034** (66,17%) | **1.551** (33,83%) | +1.483 petak | 1,96x |
| **Rata-rata ($\bar{Y}$)** | **4,4457 Mg ha⁻¹** | **1,9236 Mg ha⁻¹** | **+2,5221 Mg ha⁻¹** | **2,31x** |
| **Standar Deviasi ($s$)** | **1,6083 Mg ha⁻¹** | **1,0260 Mg ha⁻¹** | +0,5823 Mg ha⁻¹ | 1,57x |
| **Median ($P_{50}$)** | **4,6000 Mg ha⁻¹** | **1,6500 Mg ha⁻¹** | **+2,9500 Mg ha⁻¹** | **2,79x** |
| **Minimum ($P_0$)** | 0,1000 Mg ha⁻¹ | 0,1000 Mg ha⁻¹ | 0,0000 | 1,00x |
| **Maksimum ($P_{100}$)** | **9,8000 Mg ha⁻¹** | **6,1000 Mg ha⁻¹** | **+3,7000 Mg ha⁻¹** | **1,61x** |
| **Kuartil 1 ($Q_1$)** | 3,5000 Mg ha⁻¹ | 1,2000 Mg ha⁻¹ | +2,3000 Mg ha⁻¹ | 2,92x |
| **Kuartil 3 ($Q_3$)** | 5,5000 Mg ha⁻¹ | 2,5000 Mg ha⁻¹ | +3,0000 Mg ha⁻¹ | 2,20x |
| **IQR ($Q_3 - Q_1$)** | 2,0000 Mg ha⁻¹ | 1,3000 Mg ha⁻¹ | +0,7000 Mg ha⁻¹ | 1,54x |
| **Koefisien Variasi (CV)** | **36,18%** | **53,34%** | -17,16% | 0,68x |
| **Kemencengan (Skewness)** | **-0,1980** | **+0,8369** | -1,0349 | - |
| **Kurtosis** | **+0,0363** | **+0,3001** | -0,2638 | - |

### 4.2 Analisis Pola Distribusi dan Pemaknaan Agronomis Non-Kausal
1. **Dekomposisi Sempurna Distribusi Bimodal:**
   Kurva KDE pada Gambar 2B membuktikan bahwa dua puncak pada distribusi agregat sepenuhnya terpisah ketika dipecah berdasarkan `System`:
   - Sub-populasi **Landrace** membentuk kurva condong ke kanan (*positively skewed*, $\gamma_1 = +0{,}84$) dengan median $1{,}65\text{ Mg ha}^{-1}$ dan rata-rata $1{,}92\text{ Mg ha}^{-1}$. Mayoritas besar (75%) petak Landrace menghasilkan panen di bawah $2{,}50\text{ Mg ha}^{-1}$.
   - Sub-populasi **Hybrid** membentuk kurva yang relatif simetris dengan kemencengan negatif sangat tipis ($\gamma_1 = -0{,}20$) dengan median $4{,}60\text{ Mg ha}^{-1}$ dan rata-rata $4{,}45\text{ Mg ha}^{-1}$. Separuh petak Hybrid berada pada rentang stabil $3{,}50$ hingga $5{,}50\text{ Mg ha}^{-1}$.
2. **Kesenjangan Produktivitas Absolut vs Relatif:**
   Secara rata-rata, lahan ber-sistem Hybrid menghasilkan produktivitas $2{,}31\text{ kali lipat}$ lebih tinggi ($4{,}45$ vs $1{,}92\text{ Mg ha}^{-1}$) dibandingkan lahan Landrace. 
   Namun, dari perspektif variabilitas relatif, sistem **Landrace memiliki fluktuasi hasil yang jauh lebih bergejolak ($\text{CV} = 53{,}34\%$)** dibandingkan sistem Hybrid ($\text{CV} = 36{,}18\%$). Ketidakstabilan hasil pada Landrace mengindikasikan bahwa pertanian subsisten sangat rentan terhadap variasi iklim mikro lokal dan kualitas lahan marjinal.
3. **Peringatan Interpretasi Agronomis Hati-Hati (Non-Kausalitas):**
   > [!IMPORTANT]
   > **Batasan Kausalitas:** Kita **TIDAK BOLEH** menyimpulkan secara gegabah bahwa sekadar "mengganti benih lokal dengan benih hibrida akan serta-merta meningkatkan hasil sebesar $2{,}52\text{ Mg ha}^{-1}$". 
   > 
   > Secara agronomis dan spasial, petak-petak `Hybrid` dan `Landrace` berada pada ekosistem biofisik dan manajemen yang berbeda secara sistematis (*confounding factors*):
   > - Lahan Hybrid umumnya berlokasi di elevasi lebih rendah ($500$–$800\text{ m dpl}$) dengan topografi datar hingga landai.
   > - Lahan Hybrid menerima asupan pupuk nitrogen sintetis rata-rata jauh lebih tinggi ($130$–$180\text{ kg N ha}^{-1}$) serta aplikasi herbisida/pestisida intensif.
   > - Sebaliknya, lahan Landrace banyak berlokasi di dataran tinggi pegunungan Sierra Madre ($> 1.200\text{ m dpl}$), kelerengan curam ($> 15\%$), serta minim pemupukan kimia.
   > 
   > Oleh karena itu, disparitas hasil panen ini merupakan **asosiasi fenotipik teramati (*observed phenotypic association*)** dari paket agronomi terpadu dan seleksi lahan, bukan pembuktian dampak kausal tunggal dari jenis benih semata.

---

## 5. Analisis Distribusi `YIELD` Berdasarkan Tahun Tanam (`Year`)

Dataset mencakup rentang waktu 7 musim tanam berturut-turut (2012–2018). Distribusi hasil panen tahunan disajikan pada gambar berikut:

![Distribusi YIELD berdasarkan Tahun](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/eda_01_yield_by_year.png)
*Gambar 3: (A) Boxplot produktivitas YIELD per tahun tanam (2012–2018) dengan garis tren rata-rata tahunan. (B) Dinamika pergeseran komposisi sampel (Hybrid vs Landrace) per tahun.*

### 5.1 Tabel Statistik Deskriptif `YIELD` Lintas Tahun (2012–2018)

| Tahun (`Year`) | Jumlah Sampel ($N$) | Proporsi Sampel (%) | Rata-rata ($\bar{Y}$) | Median ($\text{Med}$) | Standar Deviasi ($s$) | Min | Max | Kuartil 1 ($Q_1$) | Kuartil 3 ($Q_3$) | IQR | Skewness | CV (%) |
|:---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **2012** | 723 | 15,77% | **4,4948** | 4,5000 | 1,2754 | 0,52 | 9,00 | 3,8850 | 5,3000 | 1,4150 | -0,2057 | 28,37% |
| **2013** | 479 | 10,45% | **3,6033** | 3,9500 | 1,7675 | 0,50 | 8,40 | 1,8000 | 5,0000 | 3,2000 | +0,0166 | 49,05% |
| **2014** | 376 | 8,20% | **2,6960** | 1,9000 | 1,8511 | 0,10 | 7,50 | 1,2000 | 4,0375 | 2,8375 | +0,7501 | 68,66% |
| **2015** | 424 | 9,25% | **3,7495** | 3,5000 | 1,6825 | 0,10 | 8,05 | 2,8000 | 4,9000 | 2,1000 | +0,0839 | 44,87% |
| **2016** | 816 | 17,80% | **3,1071** | 3,0000 | 1,9464 | 0,20 | 9,50 | 1,3500 | 4,8000 | 3,4500 | +0,5577 | 62,64% |
| **2017** | 960 | 20,94% | **3,8094** | 3,8500 | 1,9526 | 0,10 | 9,80 | 2,0000 | 5,4000 | 3,4000 | +0,2000 | 51,26% |
| **2018** | 807 | 17,60% | **3,3460** | 3,0000 | 1,9044 | 0,10 | 9,80 | 1,7000 | 4,6800 | 2,9800 | +0,5077 | 56,91% |

### 5.2 Pembongkaran Fenomena Pergeseran Komposisi Sampel (*Sampling Composition Shift*)
Pemeriksaan tren rata-rata tahunan sepintas memperlihatkan penurunan tajam:
- Tahun 2012 mencatat rata-rata tertinggi sebesar **$4,49\text{ Mg ha}^{-1}$**.
- Tahun 2014 anjlok ke titik terendah sebesar **$2,70\text{ Mg ha}^{-1}$** (penurunan $-39{,}9\%$).
- Tahun 2016 kembali mengalami tekanan rata-rata rendah di angka **$3,11\text{ Mg ha}^{-1}$**.

Namun, investigasi mendalam terhadap komposisi sampel (Gambar 3B) mengungkap fakta kritis:
1. **Fluktuasi Komposisi Hybrid vs Landrace:**
   - Pada **2012**, dataset didominasi secara masif oleh sistem **Hybrid ($86{,}7\%$)**, dengan hanya $13{,}3\%$ Landrace.
   - Pada **2013**, observasi hampir murni **Hybrid ($99{,}4\%$)**, hanya 3 petak Landrace ($0{,}6\%$).
   - Mulai **2014**, CIMMYT memperluas program pendataan ke wilayah pegunungan adat subsisten. Akibatnya, proporsi Landrace melompat menjadi **$51{,}9\%$ pada 2014**, **$54{,}7\%$ pada 2016**, **$41{,}5\%$ pada 2017**, dan **$47{,}6\%$ pada 2018**.
2. **Karakteristik Simpson's Paradox:**
   Ketika proporsi petak Landrace (yang secara inheren memiliki produktivitas sekitar $1{,}9\text{ Mg ha}^{-1}$) melonjak hingga separuh dari total observasi tahunan, rata-rata agregat tahun tersebut secara mekanis akan tertarik ke bawah, **meskipun produktivitas lahan Hybrid pada tahun tersebut sebenarnya tidak turun drastis**.

### 5.3 Dekomposisi Interaksi Tahun vs Sistem (`Year` $\times$ `System`)
Untuk membuktikan temuan di atas, dilakukan dekomposisi cross-tabulation antara tahun dan sistem budidaya yang divisualisasikan pada gambar berikut:

![Interaksi Tahun dan Sistem](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/eda_01_yield_interaction_year_system.png)
*Gambar 4: Distribusi produktivitas jagung yang didekomposisi per sistem budidaya untuk setiap tahun tanam (2012–2018).*

Berikut adalah tabel rincian statistik interaksi `Year` $\times$ `System`:

| Tahun | Sistem | Jumlah Petak ($N$) | Proporsi (%) | Rata-rata ($\text{Mg ha}^{-1}$) | Median ($\text{Mg ha}^{-1}$) | Std Dev ($\text{Mg ha}^{-1}$) | Min | Max | IQR |
|:---:|:---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **2012** | **Hybrid** | 627 | 86,72% | 4,7068 | 4,8000 | 1,1920 | 0,52 | 9,00 | 1,5000 |
| | **Landrace** | 96 | 13,28% | 3,1106 | 3,0100 | 0,8763 | 0,80 | 5,50 | 1,3000 |
| **2013** | **Hybrid** | 476 | 99,37% | 3,6103 | 3,9600 | 1,7708 | 0,50 | 8,40 | 3,2200 |
| | **Landrace** | 3 | 0,63% | 2,5000 | 2,4000 | 0,2646 | 2,30 | 2,80 | 0,2500 |
| **2014** | **Hybrid** | 181 | 48,14% | 3,9533 | 4,0900 | 1,8277 | 0,10 | 7,50 | 3,0000 |
| | **Landrace** | 195 | 51,86% | 1,5289 | 1,4500 | 0,8248 | 0,28 | 5,80 | 0,8500 |
| **2015** | **Hybrid** | 395 | 93,16% | 3,9394 | 3,8000 | 1,5608 | 0,10 | 8,05 | 2,1000 |
| | **Landrace** | 29 | 6,84% | 1,1628 | 0,7500 | 1,0236 | 0,10 | 4,10 | 1,1000 |
| **2016** | **Hybrid** | 370 | 45,34% | 4,7593 | 5,0000 | 1,5095 | 1,00 | 9,50 | 1,9000 |
| | **Landrace** | 446 | 54,66% | 1,7364 | 1,5000 | 0,9469 | 0,20 | 5,80 | 0,9000 |
| **2017** | **Hybrid** | 562 | 58,54% | 5,0658 | 5,0500 | 1,4236 | 0,70 | 9,80 | 1,8000 |
| | **Landrace** | 398 | 41,46% | 2,0352 | 1,9000 | 0,9777 | 0,10 | 6,10 | 1,3000 |
| **2018** | **Hybrid** | 423 | 52,42% | 4,5842 | 4,5000 | 1,6485 | 0,30 | 9,80 | 2,3000 |
| | **Landrace** | 384 | 47,58% | 1,9821 | 1,8000 | 1,0389 | 0,10 | 5,30 | 1,3000 |

### 5.4 Implikasi Agronomis Terhadap Variasi Antar-Tahun
1. **Bukti Ketahanan Hybrid di Tahun 2016:**
   Pada tingkat agregat, tahun 2016 terlihat lesu dengan rata-rata $3{,}11\text{ Mg ha}^{-1}$. Namun dekomposisi interaksi membuktikan bahwa **rata-rata sistem Hybrid di tahun 2016 justru sangat tinggi ($4{,}76\text{ Mg ha}^{-1}$)**, lebih tinggi daripada tahun 2013, 2014, dan 2015. Kerendahan rata-rata 2016 semata-mata diakibatkan oleh masuknya 446 sampel petak Landrace ($54{,}66\%$) yang rata-ratanya hanya $1{,}74\text{ Mg ha}^{-1}$.
2. **Tahun 2013 Sebagai Anomali Penurunan Kinerja Hybrid:**
   Berbeda dengan 2016, tahun **2013 adalah tahun di mana produktivitas Hybrid benar-benar mengalami kontraksi riil**. Meskipun $99{,}4\%$ sampel adalah Hybrid, rata-ratanya hanya mencapai $3{,}61\text{ Mg ha}^{-1}$ (jauh di bawah rata-rata Hybrid 2012 sebesar $4{,}71$ atau 2017 sebesar $5{,}07$). Hal ini mengindikasikan adanya faktor eksternal regional (seperti anomali iklim, pola curah hujan yang tidak merata, atau serangan organisme pengganggu tanaman/OPT) yang menekan pertumbuhan jagung pada tahun tersebut, yang memerlukan verifikasi data cuaca pada tahap eksplorasi selanjutnya.
3. **Puncak Produktivitas 2017:**
   Tahun 2017 merupakan musim tanam paling produktif dalam catatan dataset: Hybrid mencapai rata-rata tertingginya sepanjang sejarah pendataan ($5{,}07\text{ Mg ha}^{-1}$ dengan median $5{,}05\text{ Mg ha}^{-1}$) dan Landrace juga mengalami pemulihan ke rata-rata di atas $2{,}00\text{ Mg ha}^{-1}$.

---

## 6. Identifikasi Indikasi Outlier Tanpa Penghapusan Data

Pemeriksaan outlier dilakukan menggunakan dua pendekatan formal: **Aturan Pagar Tukey (*Tukey's Fences*)** berbasis interkuartil dan **Aturan Tiga Sigma ($3\sigma$)** berbasis mean dan deviasi standar.

Visualisasi identifikasi outlier dikaitkan dengan faktor elevasi lahan disajikan pada gambar berikut:

![Profil Outlier YIELD](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/eda_01_yield_outliers_profile.png)
*Gambar 5: Identifikasi sebaran nilai ekstrem (outlier) YIELD terhadap elevasi lahan (Elev) per sistem budidaya, menunjukkan variabilitas riil di lapangan.*

### 6.1 Deteksi Formal Outlier Tingkat Keseluruhan Data ($N = 4.585$)

1. **Metode Pagar Tukey (1,5 $\times$ IQR):**
   - Jangkauan Antar-Kuartil: $\text{IQR} = Q_3 - Q_1 = 5{,}0000 - 1{,}8500 = 3{,}1500\text{ Mg ha}^{-1}$.
   - Pagar Bawah (*Lower Fence*): $\text{LF} = Q_1 - 1{,}5 \times \text{IQR} = 1{,}8500 - (1{,}5 \times 3{,}1500) = \mathbf{-2{,}8750\text{ Mg ha}^{-1}}$.
     - Karena nilai minimum aktual adalah $0{,}1000\text{ Mg ha}^{-1}$, maka **tidak ada observasi ($0$ petak / $0{,}00\%$) yang berada di bawah batas bawah Tukey**.
   - Pagar Atas (*Upper Fence*): $\text{UF} = Q_3 + 1{,}5 \times \text{IQR} = 5{,}0000 + (1{,}5 \times 3{,}1500) = \mathbf{9{,}7250\text{ Mg ha}^{-1}}$.
     - Terdapat **3 observasi ($0{,}065\%$)** yang nilainya melampaui pagar atas ($> 9{,}725\text{ Mg ha}^{-1}$), ketiganya bernilai tepat **$9{,}80\text{ Mg ha}^{-1}$**.

2. **Metode Tiga Sigma ($\mu \pm 3\sigma$):**
   - Batas Bawah: $3{,}5926 - (3 \times 1{,}8686) = -2{,}0132\text{ Mg ha}^{-1}$ ($0$ observasi / $0{,}00\%$).
   - Batas Atas: $3{,}5926 + (3 \times 1{,}8686) = \mathbf{9{,}1982\text{ Mg ha}^{-1}}$.
   - Terdapat **9 observasi ($0{,}196\%$)** dengan nilai panen $> 9{,}20\text{ Mg ha}^{-1}$ (nilai: 9,2; 9,2; 9,5; 9,5; 9,6; 9,7; 9,8; 9,8; 9,8).

### 6.2 Deteksi Outlier Berdasarkan Sub-Populasi Sistem Budidaya (*Within-System Outliers*)

Mengingat sifat bimodal dari data, deteksi outlier dalam masing-masing sistem budidaya memberikan gambaran agronomis yang jauh lebih akurat:

| Parameter Deteksi Subgrup | Sub-Populasi `Hybrid` ($N = 3.034$) | Sub-Populasi `Landrace` ($N = 1.551$) |
|---|---:|---:|
| **Kuartil Bawah ($Q_1$)** | 3,5000 Mg ha⁻¹ | 1,2000 Mg ha⁻¹ |
| **Kuartil Atas ($Q_3$)** | 5,5000 Mg ha⁻¹ | 2,5000 Mg ha⁻¹ |
| **Rentang Interkuartil ($\text{IQR}$)** | 2,0000 Mg ha⁻¹ | 1,3000 Mg ha⁻¹ |
| **Pagar Bawah ($\text{LF} = Q_1 - 1{,}5\text{IQR}$)** | **0,5000 Mg ha⁻¹** | **-0,7500 Mg ha⁻¹** |
| **Pagar Atas ($\text{UF} = Q_3 + 1{,}5\text{IQR}$)** | **8,5000 Mg ha⁻¹** | **4,4500 Mg ha⁻¹** |
| **Outlier Bawah Terdeteksi ($< \text{LF}$)** | **8 petak (0,26%)** | **0 petak (0,00%)** |
| **Outlier Atas Terdeteksi ($> \text{UF}$)** | **19 petak (0,63%)** | **25 petak (1,61%)** |
| **Total Outlier Subgrup** | **27 petak (0,89%)** | **25 petak (1,61%)** |

### 6.3 Profil Agronomis Lahan Ekstrem

Pemeriksaan baris data individual pada kedua ujung ekstrem menyingkap dinamika biologis dan teknis yang penting:

#### A. Tiga Petak Tertinggi Populasi Global ($YIELD = 9{,}80\text{ Mg ha}^{-1}$)
1. **Baris 2855 (Field_ID 2856):** Tahun 2017, Sistem Hybrid, Kultivar `DEKALB 395`, Elevasi 602 m dpl, Pemupukan N: 226,5 kg/ha, P₂O₅: 23,0 kg/ha, K₂O: 30,0 kg/ha.
2. **Baris 3031 (Field_ID 3032):** Tahun 2017, Sistem Hybrid, Kultivar `DEKALB 390`, Elevasi 637 m dpl, Pemupukan N: 212,3 kg/ha, P₂O₅: 46,0 kg/ha, K₂O: 30,0 kg/ha.
3. **Baris 4055 (Field_ID 4056):** Tahun 2018, Sistem Hybrid, Kultivar `DEKALB 7500`, Elevasi 583 m dpl, Pemupukan N: 168,8 kg/ha, P₂O₅: 46,0 kg/ha, K₂O: 0,0 kg/ha.
*Profil:* Seluruh hasil puncak diproduksi oleh benih hibrida komersial unggul generasi mutakhir pada elevasi dataran sedang ($580$–$640\text{ m dpl}$) dengan dosis nitrogen sangat intensif ($> 165\text{ kg N ha}^{-1}$).

#### B. Delapan Petak Hybrid dengan Hasil Ekstrem Rendah / Gagal Panen ($YIELD < 0{,}50\text{ Mg ha}^{-1}$)
- Contoh: Baris 1716, 1719, 1756 (Tahun 2015, Kultivar `DEKALB 395`, Elevasi 560–573 m dpl, Pemupukan N: 119 kg/ha, P₂O₅: 69 kg/ha, K₂O: 60 kg/ha, tetapi hasil panen hanya **$0{,}10$–$0{,}20\text{ Mg ha}^{-1}$**).
*Profil:* Lahan-lahan ini menerima paket input pupuk kimia lengkap dan menggunakan benih hibrida unggul, namun panennya hampir gagal total. Fenomena ini mencerminkan kejadian bencana agronomis lokal yang tak terelakkan di lapangan, seperti serangan hama penggerek batang, penyakit bulai (*downy mildew*), banjir lokal, atau kekeringan parah tepat saat fase pembungaan (*silking/tasseling*).

#### C. Dua Puluh Lima Petak Landrace Berkinerja Tinggi ($YIELD > 4{,}45\text{ Mg ha}^{-1}$, Maksimum $6{,}10\text{ Mg ha}^{-1}$)
- Contoh: Petak-petak di pegunungan dengan kultivar lokal `CRIOLLO` yang mampu mencapai $5{,}0$ hingga $6{,}1\text{ Mg ha}^{-1}$.
*Profil:* Merepresentasikan fenomena *positive deviance* di kalangan petani tradisional. Petani-petani ini kemungkinan memiliki kearifan lokal dalam pemanfaatan bahan organik, penanaman pada lembah pegunungan mikro yang sangat subur, atau pengairan mata air alami.

### 6.4 Landasan Metodologis Penolakan Penghapusan Outlier (Zero Dropping Policy)
Sesuai prinsip kehati-hatian statistik dan integritas sains data pertanian, **TIDAK ADA OUTLIER YANG DIHAPUS DARI DATASET**, atas pertimbangan ilmiah berikut:
1. **Plausibilitas Biologis (*Biological Plausibility*):**
   Rentang panen $0{,}1$ hingga $9{,}8\text{ Mg ha}^{-1}$ sepenuhnya valid secara agronomi untuk tanaman jagung tropis (*Zea mays L.*). Di lingkungan tropis basah dengan radiasi tinggi, potensi genetik varietas hibrida modern mampu mencapai $10$–$12\text{ Mg ha}^{-1}$, sedangkan kondisi marjinal tadah hujan dapat menekan hasil mendekati nol. Tidak ada nilai negatif atau nilai mustahil (seperti $> 25\text{ Mg ha}^{-1}$) yang mengindikasikan galat ketik (*typo entry*).
2. **Pencegahan Bias Optimis (*Sunny-Day Bias*):**
   Jika petak-petak berpanen rendah ($< 0{,}5\text{ Mg ha}^{-1}$) dihapus atas nama "pembersihan outlier", model *machine learning* yang dilatih akan memiliki ilusi optimis palsu bahwa budidaya jagung selalu menghasilkan panen sedang-tinggi. Hal ini akan sangat berisiko fatal jika diimplementasikan pada DSS peternak Komunitas ASA, karena peternak akan melebih-lebihkan pasokan pakan dan berpotensi mengalami krisis pakan mendadak saat terjadi gangguan iklim.
3. **Pembelajaran Resiliensi Model:**
   Titik-titik ekstrem menyediakan variasi pembelajaran krusial bagi algoritma untuk mengenali kombinasi kondisi cuaca dan tanah yang berisiko memicu gagal panen serta kondisi yang memungkinkan produktivitas puncak.

---

## 7. Interpretasi Kritis: Apa yang Dapat dan Belum Dapat Disimpulkan

Untuk menjaga integritas ilmiah, bagian ini menegaskan secara eksplisit batasan inferensi dari analisis univariat tahap 1 ini:

### 7.1 Hal-Hal yang DAPAT Disimpulkan Secara Pasti
1. **Statistik Riil Dataset:** Nilai rata-rata target `YIELD` populasi aktual adalah **$3{,}59\text{ Mg ha}^{-1}$** dan median aktual adalah **$3{,}60\text{ Mg ha}^{-1}$** dengan rentang $0{,}10$ hingga $9{,}80\text{ Mg ha}^{-1}$.
2. **Bimodalitas Alamiah:** Distribusi `YIELD` tidak berdistribusi normal, melainkan bimodal, yang secara struktural dipicu oleh keberadaan dua sistem budidaya yang berbeda secara mendasar (`Hybrid` vs `Landrace`).
3. **Perbedaan Produktivitas Teramati antar Sistem:** Lahan bersistem Hybrid mencatat produktivitas median teramati $4{,}60\text{ Mg ha}^{-1}$ (rata-rata $4{,}45\text{ Mg ha}^{-1}$), sedangkan sistem Landrace mencatat median $1{,}65\text{ Mg ha}^{-1}$ (rata-rata $1{,}92\text{ Mg ha}^{-1}$).
4. **Fluktuasi Tahunan Terdistorsi Sampling:** Variasi rata-rata panen antar-tahun (terendah 2014 sebesar $2{,}70\text{ Mg ha}^{-1}$, tertinggi 2012 sebesar $4{,}49\text{ Mg ha}^{-1}$) sangat dipengaruhi oleh pergeseran komposisi sampel observasi yang dikumpulkan CIMMYT, bukan semata-mata cerminan perbedaan kualitas iklim antar-tahun.
5. **Validitas Seluruh Observasi:** Tidak ada pencilan yang diakibatkan oleh eror transmisi data atau kesalahan input; seluruh rentang nilai mencerminkan variabilitas biologis riil pertanian tropis sehingga seluruh 4.585 baris wajib dipertahankan.

### 7.2 Hal-Hal yang BELUM DAPAT Disimpulkan pada Tahap Ini
1. **Belum Dapat Membuktikan Hubungan Sebab-Akibat Benih:** Kita belum dapat menyimpulkan bahwa keunggulan sistem Hybrid semata-mata disebabkan oleh potensi genetik benih hibrida, karena terdapat bias seleksi (*selection bias*) dan perancu (*confounding factors*) berupa perbedaan elevasi lahan, kelerengan, serta tingkat pemupukan N, P, dan K.
2. **Belum Dapat Memetakan Pengaruh Iklim/Cuaca:** Penurunan kinerja sistem Hybrid pada tahun 2013 belum dapat dipastikan penyebab cuacanya, karena 150 variabel cuaca harian Daymet (V1–V30 untuk presipitasi, radiasi, suhu maksimum/minimum, dan tekanan uap) belum dianalisis secara temporal pada tahap ini.
3. **Belum Dapat Mengidentifikasi Fitur Prediktor Dominan:** Kita belum dapat mengetahui variabel tanah (Clay, CEC, SOM, pH) atau variabel topografi (Slope, Elev) mana yang memiliki kekuatan asosiasi paling kuat terhadap variabilitas `YIELD`.
4. **Belum Dapat Menentukan Arsitektur Model Prediksi:** Belum dapat diputuskan algoritma pemodelan terbaik (apakah regresi linier terregularisasi, model berbasis pohon seperti Random Forest/XGBoost, atau neural network) sebelum struktur korelasi multivariat dan multikolinearitas antar fitur diperiksa.

---

## 8. Rekomendasi Satu Langkah Analisis Berikutnya

Sebagai kelanjutan logis dan terstruktur dari investigasi univariat target ini, langkah berikutnya yang direkomendasikan adalah:

> [!TIP]
> ### Rekomendasi Langkah Selanjutnya:
> **EDA TAHAP 2 — Eksplorasi Fitur Prediktor Agronomi, Tanah, dan Topografi serta Analisis Bivariat Hubungan Fitur terhadap `YIELD`**
> 
> **Fokus Utama EDA Tahap 2:**
> 1. Menganalisis sebaran univariat fitur-fitur prediktor non-cuaca (dosis pupuk `Nitrogen`, `Phosphorus`, `Potassium`, tanggal tanam `Planting`, serta sifat tanah `Clay`, `CEC`, `SOM`, `PH`, dan topografi `Elev`, `Slope`).
> 2. Melakukan analisis bivariat antara masing-masing fitur prediktor tersebut terhadap target `YIELD` (analisis scatter plot, kurva tren loess, dan boxplot per strata pemupukan/elevasi).
> 3. Memeriksa korelasi dan potensi multikolinearitas antar fitur manajemen dan tanah guna mempersiapkan pertimbangan pemilihan fitur (*feature selection*) pada tahap persiapan data (*data preparation*).

---

## 9. Indeks Berkas Laporan & Visualisasi Terkait

Semua berkas visualisasi pendukung resolusi tinggi telah disimpan di folder output resmi dan dapat diakses melalui tautan berikut:

1. [EDA_01_TARGET_YIELD.md](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/EDA_01_TARGET_YIELD.md): Laporan lengkap EDA Tahap 1 Variabel Target YIELD.
2. [eda_01_yield_distribusi_overall.png](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/eda_01_yield_distribusi_overall.png): Visualisasi Boxplot dan Histogram/KDE target YIELD keseluruhan data.
3. [eda_01_yield_by_system.png](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/eda_01_yield_by_system.png): Visualisasi komparatif dan dekomposisi bimodalitas YIELD sistem Hybrid vs Landrace.
4. [eda_01_yield_by_year.png](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/eda_01_yield_by_year.png): Visualisasi fluktuasi rata-rata YIELD per tahun tanam (2012–2018) dan komposisi sampel.
5. [eda_01_yield_interaction_year_system.png](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/eda_01_yield_interaction_year_system.png): Visualisasi dekomposisi interaksi tahun tanam dan sistem budidaya.
6. [eda_01_yield_outliers_profile.png](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/eda_01_yield_outliers_profile.png): Visualisasi profil outlier YIELD terhadap elevasi lahan dan variabilitas biologis riil.
7. [generate_eda_01_charts.py](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/generate_eda_01_charts.py): Skrip otomatisasi Python untuk replikasi seluruh grafik di atas.
