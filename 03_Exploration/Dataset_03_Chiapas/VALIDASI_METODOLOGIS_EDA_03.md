# LAPORAN VALIDASI METODOLOGIS DAN AUDIT KRITIS EDA TAHAP 3
## Evaluasi Ketat Terhadap Klaim Metrik $R^2$, Ketersediaan Temporal Fitur Cuaca Daymet, Risiko Kebocoran Data (Data Leakage), dan Batasan Inferensi Ilmiah
### Dataset: Multiyear Maize Management Dataset, Chiapas, Mexico (2012–2018)

---

## 1. Ringkasan Eksekutif Validasi

Laporan ini menyajikan hasil **validasi metodologis terarah** terhadap dokumen [EDA_03_WEATHER_TEMPORAL.md](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/EDA_03_WEATHER_TEMPORAL.md) dan skrip analisis pendukung [run_eda_03_weather_stats.py](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/run_eda_03_weather_stats.py). Validasi dilakukan secara objektif dengan memeriksa kode sumber, metadata repositori CIMMYT, dan publikasi acuan [Trevisan et al. (2022)](file:///C:/SKRIPSI/07_Documentation/01_Literature_Review/Multiyear%20Maize%20Management%20Dataset.pdf), tanpa mengulang kalkulasi atau mengubah data mentah.

### Hasil Audit Kritis Singkat:
1. **Nilai $R^2$ ($0{,}3879$, $0{,}4667$, $0{,}5065$):** Diperoleh dari model **Ordinary Least Squares (OLS) in-sample murni tanpa data split (tanpa train/test split atau cross-validation)**. Perbandingan ketiganya **TIDAK ADIL** karena membandingkan model berdimensi 30 vs 90 vs 150 prediktor; penambahan parameter pada OLS pasti menaikkan $R^2$ latih secara matematis.
2. **Klaim Rasio "76,58% Kapasitas Penjelasan Cuaca":** **TIDAK DIDUKUNG SECARA STATISTIK**. Pembagian sederhana $\frac{R^2_{\text{pre}}}{R^2_{\text{full}}}$ mengasumsikan variansi aditif independen, padahal fitur cuaca antar-periode mengalami autokorelasi serial dan multikolinearitas ekstrem ($r > 0{,}80$).
3. **Ketersediaan V1–V6 pada Waktu Keputusan:** **TERJADI PENCAMPURADUKAN KONSEP**. V1–V6 secara fisik tersedia jika prediksi dilakukan **tepat pada hari tanam (*at-planting day*)**, namun **BELUM TERSEDIA pada fase perencanaan pra-tanam (*pre-planting planning*)**, karena tanggal tanam aktual (`Planting`) belum terjadi dan belum diketahui.
4. **Klaim "Bebas Leakage 0%":** **OVERCLAIM / TIDAK TEPAT**. Klaim tersebut hanya mengecek urutan kronologis kasar (terjadi sebelum hari tanam), tetapi **mengabaikan risiko *anchor leakage* (bergantung pada tanggal tanam riil), *spatial leakage* (autokorelasi spasial grid Daymet 1 km antar-petak berdekatan), dan *temporal clustering leakage* (7 tahun observasi berulang)**.
5. **Pelabelan V25–V30 sebagai "Pascapanen":** **PERLU KUALIFIKASI / SEBAGIAN KELIRU**. Bagi jagung hibrida dataran rendah (siklus 110–130 hari), V25–V30 memang pascapanen. Namun bagi jagung ras lokal pegunungan (*Landrace*, sepertiga populasi dengan siklus 180–220 hari), V25–V28 adalah masa pematangan akhir dan pengeringan batang di lahan.
6. **Interpretasi Agronomis:** Penjelasan perancu suhu oleh elevasi **VALID DAN DIDUKUNG DATA**. Namun, penjelasan "pengisian air tanah (*subsoil recharge*)" dan "kelebihan air memicu penyakit jamur" adalah **hipotesis agronomis yang masuk akal namun tidak terukur langsung (*indirect inference*)** karena ketiadaan sensor lengas tanah atau data patologi tanaman.

---

## 2. Matriks Validasi Klaim Metodologis EDA Tahap 3

Tabel 1 merangkum evaluasi terhadap 6 fokus investigasi metodologis:

### Tabel 1: Matriks Pemeriksaan Klaim, Bukti Kode/Data, Status Validitas, dan Koreksi yang Diperlukan

| No. | Klaim / Fokus Pemeriksaan | Bukti Kode / Sumber Data Aktual | Status Validitas | Koreksi Metodologis & Batasan Ilmiah yang Benar |
|---:|---|---|:---:|---|
| 1 | **Asal-usul $R^2$ ($0{,}3879$, $0{,}4667$, $0{,}5065$) dan Keadilan Perbandingan** | Skrip `run_eda_03_weather_stats.py` L145–L160: Menggunakan `sklearn.linear_model.LinearRegression().fit(X, y).score(X, y)` pada seluruh $N = 4.585$ tanpa partisi data (`train_test_split` / K-Fold). | **PERLU KUALIFIKASI KETAT (In-Sample Bias)** | Angka tersebut adalah **in-sample goodness-of-fit latih**, bukan akurasi prediksi generalisasi. Perbandingan 30 vs 90 vs 150 fitur bias menguntungkan model berparameter lebih besar karena sifat matematis $R^2$ OLS yang monotonik non-menurun. |
| 2 | **Klaim "V1–V6 Menangkap 76,58% Kapasitas Cuaca Penuh"** | Dihitung dari rasio $\frac{0{,}3879}{0{,}5065} \times 100\% = 76{,}58\%$. Dinyatakan pada teks EDA 03 Bagian 6 & 7. | **TIDAK DIDUKUNG SECARA STATISTIK (Invalid Metric)** | Pembagian $R^2$ bukan metode dekomposisi variansi yang sah untuk prediktor multikolinear. Variansi V1–V6 bertumpuk (*collinear overlap*) dengan V7–V30 melalui baseline termal elevasi. Klaim harus direvisi menjadi: *"Korelasi in-sample model OLS 30 fitur V1–V6 mencapai 76,6% dari fit OLS 150 fitur, sebagian besar didorong oleh redundansi sinyal suhu."* |
| 3 | **Ketersediaan V1–V6 pada Waktu Keputusan Petani** | V1–V6 didefinisikan sebagai 60 hari sebelum kolom `Planting` (DOY). Di lapangan, `Planting` bervariasi dari DOY 91 hingga 242 ($s = 22{,}5\text{ hari}$). | **PERLU KUALIFIKASI KETAT (Conflated Horizons)** | Harus dibedakan tegas: (a) Jika prediksi pada **hari tanam aktual** ($H$), V1–V6 sudah lewat dan tersedia secara historis; (b) Jika prediksi pada **fase perencanaan pra-tanam** (misal 2 bulan sebelum tanam untuk beli bibit ternak), V1–V6 **BELUM TERSEDIA** karena tanggal tanam riil belum ditetapkan. |
| 4 | **Klaim "Risiko Data Leakage: 0% (Bebas Kebocoran Data)"** | Tabel 3 EDA 03 mencantumkan "0% Bebas Kebocoran Data" untuk V1–V6. | **TIDAK DIDUKUNG / OVERCLAIM (False Security)** | Nol persen kebocoran hanya berlaku untuk dimensi temporal kasar. Masih ada risiko kebocoran berat: *anchor leakage* (menggunakan tanggal tanam aktual ex-post), *spatial autocorrelation leakage* (grid Daymet 1 km yang dipakai bersama oleh petak bertetangga), dan *clustering multitahun*. |
| 5 | **Label Periode V25–V30 sebagai "Pascapanen"** | Judul Tabel 1, Gambar 1, dan teks EDA 03 melabeli V25–V30 sebagai "Akhir/Pascapanen (180 s.d. 239 hari)". Trevisan et al. (2022) menyatakan siklus jagung subsisten berlangsung berbulan-bulan melampaui musim normal. | **PERLU KUALIFIKASI (Sebagian Tidak Tepat)** | Jagung hibrida dataran rendah memang sudah panen di DAP 110–130. Namun untuk jagung Landrace pegunungan ($33{,}8\%$ populasi) dengan siklus 180–220 hari, V25–V28 adalah masa pengisian biji akhir dan pengeringan batang, bukan pascapanen. Label harus diganti menjadi "Periode 180–239 Hari Pascatanam". |
| 6 | **Dukungan Bukti Interpretasi Korelasi & Agronomi** | Teks EDA 03 menginterpretasikan mekanisme: *subsoil recharge* (V1–V6), penyakit jamur/pencucian hara (V7–V24), dan perancu elevasi pada suhu. | **VALID UNTUK PERANCU SUHU; PERLU KUALIFIKASI UNTUK MEKANISME TANAH/PENYAKIT** | Bukti perancu suhu oleh elevasi terbukti kuat secara kuantitatif melalui dekomposisi subgrup. Namun, penjelasan lengas tanah dan penyakit jamur adalah inferensi agronomis induktif tanpa variabel terukur langsung di dataset. |

---

## 3. Investigasi Detail 6 Parameter Validasi

### 3.1 Investigasi Poin 1: Asal-Usul Nilai $R^2$ ($0{,}3879$, $0{,}4667$, $0{,}5065$)
Pemeriksaan baris 145–160 pada [run_eda_03_weather_stats.py](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/run_eda_03_weather_stats.py) membuktikan implementasi kode berikut:
```python
from sklearn.linear_model import LinearRegression

# Only V1-V6 (30 features)
X_v1_v6 = df[[f'{w}_V{i}' for w in weather_types for i in range(1, 7)]]
reg_pre = LinearRegression().fit(X_v1_v6, df[target])
r2_pre = float(reg_pre.score(X_v1_v6, df[target]))  # Hasil: 0.3879

# Only V7-V24 (90 features)
X_v7_v24 = df[[f'{w}_V{i}' for w in weather_types for i in range(7, 25)]]
reg_in = LinearRegression().fit(X_v7_v24, df[target])
r2_in = float(reg_in.score(X_v7_v24, df[target]))  # Hasil: 0.4667

# Full V1-V30 (150 features)
X_full = df[[f'{w}_V{i}' for w in weather_types for i in range(1, 31)]]
reg_full = LinearRegression().fit(X_full, df[target])
r2_full = float(reg_full.score(X_full, df[target]))  # Hasil: 0.5065
```

**Temuan Metodologis Kritis:**
1. **Model:** Menggunakan regresi kuadrat terkecil biasa (*Ordinary Least Squares / OLS*) tanpa regularisasi penalti (seperti Ridge atau Lasso).
2. **Ketiadaan Validasi Silang (*No Validation Split*):** Seluruh $4.585$ baris digunakan untuk fitting sekaligus evaluasi. Nilai $R^2$ yang dilaporkan murni merupakan **koefisien determinasi sampel latih (*in-sample $R^2$*)**.
3. **Ketidakadilan Perbandingan (*Model Dimensionality Asymmetry*):**
   Dalam aljabar linier terapan, penambahan variabel penjelas ke dalam model OLS tanpa penalti secara matematis **pasti meningkatkan atau mempertahankan nilai $R^2$ sampel latih**:
   $$R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}$$
   Model V1–V30 memiliki $150$ parameter derajat kebebasan, dibandingkan $90$ parameter pada V7–V24, dan hanya $30$ parameter pada V1–V6.
   Meskipun nilai *Adjusted* $R^2$ untuk 150 fitur ($R^2_{\text{adj}} \approx 0{,}4899$) tidak jatuh terlalu jauh karena besarnya ukuran sampel ($N = 4.585$), keunggulan $R^2$ dari $0{,}3879$ ke $0{,}5065$ sebagian merupakan konsekuensi penambahan 120 dimensi parameter, bukan semata-mata kualitas informasi cuaca baru.

---

### 3.2 Investigasi Poin 2: Justifikasi Statistik Rasio "76,58% Kapasitas Penjelasan"
Laporan EDA 03 mengklaim:
$$\frac{R^2_{\text{pre}}}{R^2_{\text{full}}} = \frac{0{,}3879}{0{,}5065} = 76{,}584\% \approx 76{,}58\%$$
dan menafsirkannya sebagai *"informasi V1–V6 saja mampu menangkap 76,6% dari total kapasitas prediktif seluruh 150 variabel cuaca"*.

**Kelemahan Statistik:**
1. **Pelanggaran Asumsi Ortogonalitas:** Pembagian fraksi variansi $\frac{R^2_A}{R^2_B}$ hanya memiliki interpretasi probabilistik yang valid jika prediktor dalam himpunan $A$ dan himpunan $B \setminus A$ independen (ortogonal). Sebagaimana dibuktikan pada EDA 03 Tabel 2, suhu pada V1–V6 dan suhu pada V7–V30 memiliki korelasi serial $r > 0{,}80$.
2. **Kovariansi Tumpang Tindih (*Overlapping Information*):** Fitur V1–V6 dan V7–V30 menjelaskan variansi target yang **sama**, yaitu variansi yang terkait dengan gradien elevasi lokasi lahan.
3. **Kenaikan Marjinal Sebenarnya:** Jika model dasar V1–V6 ($R^2 = 0{,}3879$) diperluas dengan memasukkan seluruh 120 fitur pascatanam V7–V30, kenaikan variansi yang dijelaskan ($\Delta R^2$) hanyalah sebesar **$+0{,}1186$ ($11{,}86\%$)**.
4. **Koreksi Istilah:** Penggunaan istilah "kapasitas prediktif" harus diganti dengan **"derajat kecocokan sampel latih (*in-sample explained variance ratio*)"**, disertai catatan eksplisit mengenai multikolinearitas antar-himpunan.

---

### 3.3 Investigasi Poin 3: Ketersediaan Temporal V1–V6 pada Waktu Keputusan
Di dalam berkas dataset, variabel V1–V6 adalah rata-rata 10-harian yang dihitung mundur dari kolom `Planting`:
$$\text{Interval V6} = [\text{Planting} - 10 \text{ s.d. } \text{Planting} - 1], \quad \dots, \quad \text{Interval V1} = [\text{Planting} - 60 \text{ s.d. } \text{Planting} - 51]$$

**Pemisahan Dua Skenario Keputusan Nyata:**
1. **Skenario A: Prediksi pada Hari Tanam (*At-Planting Day Prediction*):**
   - Waktu: Petani berdiri di lahan pada hari tanam riil (misal 15 Juni).
   - Status: Hari tanam `Planting` sudah pasti. Enam puluh hari kalender sebelumnya (16 April s.d. 14 Juni) sudah lewat di dunia nyata.
   - Ketersediaan: **Secara fisik telah terjadi**. Namun, secara teknis operasional, data Daymet adalah produk data sekunder historis yang dirilis tahunan (bukan data sensor stasiun cuaca *real-time*).
2. **Skenario B: Prediksi Perencanaan Pra-Tanam (*Pre-Planting Planning Decision*):**
   - Waktu: Peternak Komunitas ASA memutuskan kapasitas kandang ayam petelur pada bulan Februari/Maret (2–3 bulan sebelum tanam).
   - Status: Petani **BELUM TAHU** pada hari ke berapa (`Planting` DOY) benih akan ditanam, karena tanggal tanam di Chiapas sangat bergantung pada datangnya hujan pertama (*rain onset*, rentang DOY 91–242).
   - Ketersediaan: **BELUM TERSEDIA**. Jendela 60 hari V1–V6 tidak dapat dipotong secara kalender karena titik jangkar akhirnya (`Planting`) belum ada.

> [!IMPORTANT]
> Untuk skripsi Komunitas ASA, jika model ditujukan untuk perencanaan sebelum musim tanam dimulai, model tidak bisa menggunakan V1–V6 mentah berbasis tanggal tanam riil. Model harus menggunakan **jendela iklim berbasis kalender tetap (misal cuaca bulan Maret–April)** atau mengasumsikan rencana tanggal tanam target.

---

### 3.4 Investigasi Poin 4: Audit Komprehensif Risiko Kebocoran Data (*Data Leakage*)
Laporan EDA 03 mencantumkan label *"Risiko Data Leakage: 0% (Bebas Kebocoran Data)"* pada Tabel 3 untuk V1–V6. Label ini memberikan rasa aman palsu (*false sense of security*).

Tabel 2 memetakan spektrum risiko kebocoran data yang sebenarnya ada pada dataset ini:

### Tabel 2: Taksonomi Risiko Kebocoran Data pada Fitur Cuaca Daymet Chiapas

| Jenis Data Leakage | Status pada Fitur V1–V6 | Mekanisme Terjadinya & Bukti Lapangan | Dampak terhadap Validitas Model Skripsi |
|---|:---:|---|---|
| **1. Temporal Look-Ahead Leakage (Urutan Kejadian Kasar)** | **Aman** | Secara urutan waktu, cuaca V1–V6 terjadi sebelum hari tanam ($DAP < 0$). | Memenuhi kaidah dasar bahwa cuaca terjadi sebelum tanaman tumbuh. |
| **2. Target Anchor Leakage (Jangkar Tanggal Tanam Aktual)** | ⚠️ **BERISIKO** | Jendela V1–V6 dipotong mundur dari tanggal tanam aktual (`Planting`). Padahal tanggal tanam aktual baru terwujud setelah petani mengamati cuaca dan hujan riil. Menggunakan tanggal tanam riil untuk memotong V1–V6 pada perencanaan awal membocorkan informasi realisasi tanam masa depan. | Model tidak dapat dieksekusi sebelum tanggal tanam riil diketahui. |
| **3. Spatial Autocorrelation Leakage (Kebocoran Spasial Grid)** | 🚨 **RISIKO TINGGI** | Data cuaca Daymet memiliki resolusi grid $1\text{ km} \times 1\text{ km}$. Petak-petak ubinan yang berdekatan di satu desa/kecamatan menggunakan nilai piksel cuaca yang identik. Jika pembagian data latih/uji (*data splitting*) dilakukan secara acak (*random shuffle*), data uji akan berisi nilai cuaca yang identik dengan data latih, memicu overestimasi akurasi drastis. | Memerlukan validasi silang berbasis kelompok spasial (*spatial group K-fold*) atau berbasis munisipalitas. |
| **4. Multiyear Group Leakage (Kebocoran Klaster Tahun)** | 🚨 **RISIKO TINGGI** | Dataset berisi observasi selama 7 tahun (2012–2018). Efek iklim makro tahunan (misal tahun El Niño 2015) merata di seluruh wilayah. *Random splitting* akan membocorkan tren iklim tahunan ke data uji. | Memerlukan pengujian *Leave-One-Year-Out* (misal latih 2012–2017, uji pada 2018). |
| **5. Preprocessing / Aggregation Leakage** | **Belum Terjadi** | Belum ada normalisasi, imputasi, atau pemilihan fitur yang dilakukan pada data mentah. | Harus dijaga agar standarisasi fitur nantinya dihitung hanya dari lipatan latih (*train fold*). |

---

### 3.5 Investigasi Poin 5: Validitas Label Periode V25–V30
Laporan EDA 03 melabeli interval V25–V30 (DAP 180 s.d. 239) sebagai *"Akhir/Pascapanen"*.

**Bukti Ketidaktepatan:**
1. **Jagung Sistem Hybrid ($N = 3.034$, $66{,}2\%$ populasi):** Varietas hibrida komersial di dataran rendah ($<700\text{ m dpl}$) mencapai kematangan fisiologis pada DAP 110–125 dan dipanen pada DAP 120–140. Bagi kelompok ini, interval V15–V30 (DAP 140–239) memang berlangsung setelah tanaman dipanen.
2. **Jagung Sistem Landrace ($N = 1.551$, $33{,}8\%$ populasi):** Varietas lokal di pegunungan tinggi ($>1.500\text{ m dpl}$) memiliki masa vegetatif dan pengisian biji yang sangat lambat akibat suhu dingin. Siklus hidupnya mencapai **180 hingga 220 hari**.
   - Interval V25 (DAP 180–189): Masa akhir translokasi pati ke biji.
   - Interval V26–V28 (DAP 190–219): Masa pengeringan alami tongkol di batang (*in-field dry-down*).
   - Interval V29–V30 (DAP 220–239): Panen bertahap oleh petani subsisten.
3. **Koreksi:** Menyamaratakan seluruh V25–V30 sebagai "pascapanen" adalah kesalahan agregasi yang bias pada sistem Hybrid. Terminologi yang tepat adalah **"Periode Musim Lanjut / Pascatanam Lanjut (DAP 180–239)"**.

---

### 3.6 Investigasi Poin 6: Verifikasi Fakta vs Asumsi pada Penjelasan Agronomis

Tabel 3 membedakan secara ketat antara temuan yang didukung data langsung dengan hipotesis agronomis induktif:

### Tabel 3: Klasifikasi Derajat Bukti terhadap Interpretasi Agronomis EDA Tahap 3

| Penjelasan / Interpretasi Fenomena | Status Dukungan Bukti | Rincian Bukti Data vs Batasan Fakta Terverifikasi |
|---|:---:|---|
| **Suhu (tmax, tmin) dan Kelembaban (vp) Terkonfounding Kuat oleh Elevasi** | **TERBUKTI FAKTUAL (Data-Grounded)** | **Fakta Kuat:** Korelasi global $tmax$ sebesar $+0{,}47$ runtuh menjadi $+0{,}17$ pada Hybrid dan $+0{,}14$ pada Landrace. Elevasi berkorelasi negatif kuat dengan suhu ($r \approx -0{,}85$) dan berkorelasi negatif dengan hasil panen ($\rho = -0{,}53$). Variabel cuaca suhu merefleksikan ketinggian tempat, bukan respons fisiologis murni terhadap panas. |
| **Presipitasi V1–V6 Berfungsi sebagai Pengisian Lengas Tanah (*Subsoil Moisture Recharge*)** | **HIPOTESIS AGRONOMIS MASUK AKAL (Indirect Inference)** | **Fakta:** Korelasi positif presipitasi pra-tanam terbukti nyata secara matematis ($\rho = +0{,}49$).<br>**Batasan:** Dataset Daymet tidak mengukur kadar air tanah (*soil water content*). Mekanisme "pengisian profil lengas tanah" adalah inferensi dari literatur agronomi tropis, bukan variabel terukur di dataset. |
| **Presipitasi Dalam-Musim (V7–V24) Negatif Akibat Penyakit Jamur dan Pencucian Hara** | **SPEKULASI AGRONOMIS (Plausible, but Unverified)** | **Fakta:** Total curah hujan dalam-musim memang melimpah ($968\text{ mm}$) dan berkorelasi negatif lemah ($\rho = -0{,}16$).<br>**Batasan:** Tidak ada data insidensi penyakit tanaman (seperti hawar daun *Helminthosporium* atau karat daun) maupun data analisis pencucian nitrogen di berkas Chiapas. Korelasi negatif ini juga sebagian merupakan cerminan bahwa wilayah pegunungan berhujan lebat memiliki hasil panen rendah. |
| **Presipitasi Akhir (V25–V30) Negatif Akibat Mengganggu Pengeringan Biji** | **HIPOTESIS MASUK AKAL (Indirect Inference)** | **Fakta:** Korelasi presipitasi akhir bertanda negatif sedang ($\rho = -0{,}34$).<br>**Batasan:** Merupakan fenomena umum panen jagung tropis di mana hujan saat panen memicu busuk tongkol, namun tingkat kerusakan biji tidak terekam dalam kolom dataset. |

---

## 4. Rekomendasi Keputusan Metodologis untuk Diskusi dengan Dosen Pembimbing

Sebelum melangkah ke tahap penyiapan data (*Data Preparation*) dan pemodelan (*Modeling*), terdapat **5 keputusan metodologis mendasar** yang harus dikonsultasikan dan disepakati bersama dosen pembimbing:

> [!TIP]
> ### 5 Agenda Keputusan Metodologis Bersama Dosen Pembimbing:
> 
> 1. **Penetapan Waktu Keputusan Model Prediksi (*Prediction Horizon / Decision Gate*):**
>    - *Opsi A (Prediksi Hari Tanam / At-Planting Day):* Model dijalankan pada hari tanam aktual. Fitur cuaca V1–V6 dan tanggal tanam aktual `Planting` sah digunakan.
>    - *Opsi B (Prediksi Pra-Musim Murni / Ex-Ante Planning):* Model dijalankan 1–2 bulan sebelum tanam untuk perencanaan ayam petelur Komunitas ASA. Fitur V1–V6 harus diganti dengan **fitur iklim kalender tetap (misal ringkasan cuaca bulan Maret–April)** dan tanggal tanam diganti dengan **asumsi skenario target tanam**.
> 
> 2. **Strategi Pemilihan Fitur Cuaca (Mengatasi Multikolinearitas 150 Variabel):**
>    - Karena autokorelasi suhu lintas-interval mencapai $r > 0{,}80$, dilarang memasukkan ke-150 variabel mentah ke model linier tanpa regularisasi.
>    - Disarankan mengonsultasikan penggunaan **rekayasa fitur agregat (Feature Engineering)**: merangkum 30 interval menjadi 4–6 parameter bermakna agronomis (total presipitasi pra-tanam, total presipitasi dalam-musim, akumulasi satuan panas GDD, dan frekuensi hari kering berturut-turut).
> 
> 3. **Protokol Validasi Silang Bebas Kebocoran Spasial-Temporal (*Data Splitting Strategy*):**
>    - Menolak pembagian data acak sederhana (*random shuffle split*).
>    - Mengusulkan skema **GroupKFold berbasis Munisipalitas/Spasial** atau **Temporal Split (Train 2012–2016, Test 2017–2018)** untuk menguji kemampuan model melakukan generalisasi ke lokasi baru atau tahun iklim baru.
> 
> 4. **Penanganan Variabel Perancu (*Confounding Control*):**
>    - Menyepakati apakah sistem budidaya (`Hybrid` vs `Landrace`) akan dimodelkan dalam **satu model tunggal dengan fitur interaksi** atau **dua model terpisah (Stratified Models)**, mengingat karakteristik agroklimat dan kurva respons pupuk keduanya sangat berbeda.
> 
> 5. **Penggunaan Fitur Cuaca Dalam-Musim (V7–V24):**
>    - Menyetujui arsitektur **Dual-Horizon**: Model 1 (Pra-Tanam) untuk alokasi populasi ternak awal, dan Model 2 (Pascatanam Berjalan) untuk revisi stok pakan saat fase pembungaan/pengisian biji telah selesai.

---

## 5. Indeks Berkas Terkait

1. [VALIDASI_METODOLOGIS_EDA_03.md](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/VALIDASI_METODOLOGIS_EDA_03.md): Laporan resmi validasi metodologis EDA Tahap 3.
2. [EDA_03_WEATHER_TEMPORAL.md](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/EDA_03_WEATHER_TEMPORAL.md): Laporan acuan EDA Tahap 3 yang diaudit.
3. [run_eda_03_weather_stats.py](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/run_eda_03_weather_stats.py): Skrip kode analisis perhitungan statistik dan regresi OLS.
4. [generate_eda_03_charts.py](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/generate_eda_03_charts.py): Skrip otomatisasi visualisasi cuaca.
5. [Multiyear Maize Management Dataset.pdf](file:///C:/SKRIPSI/07_Documentation/01_Literature_Review/Multiyear%20Maize%20Management%20Dataset.pdf): Makalah sumber data resmi (Trevisan et al., 2022).
