# LAPORAN EXPLORATORY DATA ANALYSIS (EDA) TAHAP 3
## Eksplorasi Temporal Dinamis 150 Variabel Cuaca Daymet, Struktur Autokorelasi, dan Evaluasi Skenario Prediksi Saat Tanam (At-Planting) vs Pemantauan Dalam-Musim
### Dataset: Multiyear Maize Management Dataset, Chiapas, Mexico (2012–2018)

---

## 1. Identitas Dokumen & Ruang Lingkup Analisis

### 1.1 Konteks Skripsi & Relevansi Fitur Cuaca Daymet
Laporan ini merupakan dokumen resmi **Exploratory Data Analysis (EDA) Tahap 3** yang melanjutkan rangkaian investigasi empiris pada dataset budidaya jagung di Chiapas, Meksiko ($N = 4.585$ observasi). Analisis ini dilaksanakan dalam konteks penelitian skripsi:
> *"Pemodelan Prediksi Jumlah Ayam Petelur untuk Smart Farming Berdasarkan Ketersediaan Lahan Jagung untuk Mendukung Perencanaan Produksi di Komunitas ASA Indonesia"*.

Setelah karakteristik distribusi variabel target `YIELD` dipetakan pada [EDA_01_TARGET_YIELD.md](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/EDA_01_TARGET_YIELD.md) dan prediktor non-cuaca (agronomi, tanah, topografi) dieksplorasi pada [EDA_02_AGRONOMY_SOIL_TOPOGRAPHY.md](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/EDA_02_AGRONOMY_SOIL_TOPOGRAPHY.md), EDA Tahap 3 ini berfokus penuh mengeksplorasi **150 variabel cuaca resolusi grid 1 km dari Daymet** (Thornton et al., 2016; Trevisan et al., 2022). Variabel-variabel tersebut terdiri atas 5 parameter cuaca yang diagregasikan ke dalam 30 interval sepuluh-harian:
1. **`prcp_V1`–`prcp_V30`:** Presipitasi rata-rata harian ($\text{mm hari}^{-1}$).
2. **`srad_V1`–`srad_V30`:** Radiasi surya rata-rata harian ($\text{MJ m}^{-2}\text{ hari}^{-1}$).
3. **`tmax_V1`–`tmax_V30`:** Suhu maksimum rata-rata ($^\circ\text{C}$).
4. **`tmin_V1`–`tmin_V30`:** Suhu minimum rata-rata ($^\circ\text{C}$).
5. **`vp_V1`–`vp_V30`:** Tekanan uap air rata-rata ($\text{Pa}$).

### 1.2 Batasan Ruang Lingkup Ketat (Scope Boundaries)
- **Dataset Acuan:** Berkas [Chiapas_Data.csv](file:///C:/SKRIPSI/02_Raw_Data/Dataset_03_Chiapas/Chiapas_Data.csv) yang berstatus *read-only*.
- **Tanpa Pengulangan Audit Sebelumnya:** Tidak ada repetisi audit kualitas data, pemetaan missing values, pemeriksaan duplikasi, eksplorasi ulang target YIELD, atau eksplorasi fitur non-cuaca yang telah tuntas di Tahap 1 dan 2.
- **Pencegahan Kebocoran Informasi (Strict Temporal Demarcation):** Analisis membedakan secara tegas dan ketat tiga periode waktu:
  - **`V1`–`V6` (Hari -60 s.d. -1 relatif terhadap tanam):** Cuaca historis 60 hari sebelum tanam (*antecedent / pre-planting weather*).
  - **`V7`–`V24` (Hari 0 s.d. 179 setelah tanam / DAP 0–179):** Cuaca selama 180 hari musim pertumbuhan aktif (*in-season growing period*).
  - **`V25`–`V30` (Hari 180 s.d. 239 setelah tanam / DAP 180–239):** Periode pengeringan akhir, pascapanen bagi dataran rendah, atau pematangan akhir bagi dataran tinggi.
- **Larangan Metodologis:** Tidak melakukan seleksi fitur final, tidak ada pembersihan/penghapusan data (*zero data dropping*), tidak ada rekayasa fitur (*preprocessing/scaling/encoding*), dan tidak membangun model prediktif *machine learning*.
- **Kepatuhan Inferensi Kausal:** Tidak menarik kesimpulan sebab-akibat dari koefisien korelasi asosiatif.

---

## 2. Verifikasi Ilmiah: Pemetaan Interval terhadap Fenologi Tanaman Jagung

> [!WARNING]
> ### Hasil Verifikasi Kritis Metodologis Fenologi
> **JANGAN MENETAPKAN INTERVAL TERTENTU (MISALNYA V12–V16 SEBAGAI PEMBUNGAAN ATAU V17–V22 SEBAGAI PENGISIAN BIJI) SECARA SERAGAM UNTUK SELURUH DATASET TANPA BUKTI TERVERIFIKASI.**

Berdasarkan artikel data resmi [Trevisan et al. (2022)](file:///C:/SKRIPSI/07_Documentation/01_Literature_Review/Multiyear%20Maize%20Management%20Dataset.pdf) dan prinsip agroklimatologi tropis, klaim pemetaan interval kalender seragam ke fase fenologi jagung di Chiapas **secara ilmiah tidak dapat dipertanggungjawabkan**, atas alasan-alasan faktual berikut:

1. **Pernyataan Eksplisit Penulis Dataset:**
   Trevisan et al. (2022, hlm. 6) secara tertulis menyatakan:
   > *"The weather data were organized according to the planting dates, starting 60 days before planting and running up to 240 days after planting, thus creating 30 new features for each variable, **extending beyond the growing season and not representing only the conditions in which plants were growing**."*
   Penulis dataset sengaja membuat jendela tetap 240 hari pascatanam untuk menyeragamkan dimensi fitur, bukan karena seluruh tanaman hidup selama 240 hari.

2. **Heterogenitas Termal Ekstrem Akibat Gradien Elevasi:**
   Dalam fisiologi tanaman jagung (*Zea mays L.*), laju perkembangan fenologi dikendalikan oleh **waktu termal (*thermal time*) atau akumulasi satuan panas (*Growing Degree Days / GDD*)**, bukan hari kalender:
   $$\text{GDD} = \sum \left( \frac{T_{\text{max}} + T_{\text{min}}}{2} - T_{\text{base}} \right), \quad T_{\text{base}} = 10^\circ\text{C}$$
   - Dataset Chiapas mencakup variasi elevasi dari **$7\text{ m}$ hingga $2.849\text{ m dpl}$**.
   - **Di Dataran Rendah ($<600\text{ m dpl}$, Suhu Rata-rata $\sim 28^\circ\text{C}$, Mayoritas Hybrid):** Akumulasi GDD harian sangat cepat ($\sim 18\text{ GDD/hari}$). Tanaman jagung hibrida mencapai inisiasi pembungaan (*silking/tasseling*) pada **DAP 50–60 (Interval V11–V12)**, dan mencapai masak fisiologis (*black layer*) pada **DAP 110–125 (Interval V17–V19)**. Bagi kelompok ini, interval **V20–V30 terjadi setelah panen selesai (*post-harvest*)**.
   - **Di Dataran Tinggi Pegunungan ($>1.500\text{ m dpl}$, Suhu Rata-rata $\sim 15^\circ\text{C}$, Mayoritas Landrace):** Akumulasi GDD harian sangat lambat ($\sim 5\text{–}7\text{ GDD/hari}$). Jagung ras lokal memerlukan waktu hingga **DAP 80–105 (Interval V15–V17) hanya untuk mencapai pembungaan**, dan siklus hidupnya berlangsung **180 hingga 220 hari (Interval V24–V28)** sebelum dapat dipanen.

3. **Pergeseran Tanggal Tanam (*Planting Date Spread*):**
   Tanggal tanam aktual bervariasi selebar $151\text{ hari}$ (DOY $91$ hingga $242$). Tanaman yang ditanam pada bulan April mengalami rezim radiasi dan suhu yang berbeda dibandingkan tanaman yang ditanam pada akhir Juli.

**Kesimpulan:** Menganggap interval kalender 10-harian tertentu merepresentasikan fase biologis seragam bagi seluruh $4.585$ petak adalah simplifikasi keliru. Analisis cuaca pada dataset ini harus diperlakukan sebagai **deret waktu agroklimat relatif terhadap titik awal tanam**, bukan penanda fenologi absolut.

---

## 3. Distribusi dan Dinamika Temporal 5 Variabel Cuaca Daymet (V1 s.d. V30)

Visualisasi lintasan temporal rata-rata dan rentang sebaran interkuartil ($Q_1$–$Q_3$) untuk kelima variabel cuaca disajikan pada Gambar 1:

![Profil Temporal Dinamika Cuaca](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/eda_03_weather_temporal_trajectories.png)
*Gambar 1: Profil dinamika temporal 5 variabel cuaca Daymet (V1–V30, N = 4.585). Zona abu-abu (V1–V6): Pra-Tanam; Zona biru muda (V7–V24): Dalam-Musim Pertumbuhan; Zona kuning (V25–V30): Akhir/Pascapanen.*

### 3.1 Pola Dinamika Musiman Tiap Variabel Cuaca

Tabel 1 menyajikan perbandingan statistik agregat kelima variabel cuaca pada tiga periode waktu:

### Tabel 1: Ringkasan Karakteristik Cuaca Berdasarkan Tiga Zona Waktu

| Parameter Cuaca | Satuan | Periode Pra-Tanam (V1–V6)<br>[-60 s.d. -1 hari] | Periode Dalam-Musim (V7–V24)<br>[0 s.d. 179 hari DAP] | Periode Akhir/Pascapanen (V25–V30)<br>[180 s.d. 239 hari DAP] | Dinamika Pola Temporal Lapangan |
|---|:---:|---:|---:|---:|---|
| **Presipitasi (`prcp`)** | $\text{mm hari}^{-1}$ | $3{,}75 \pm 2{,}37$ | **$5{,}38 \pm 2{,}24$** | $0{,}34 \pm 0{,}76$ | Meningkat bertahap sejak V4 menyambut musim hujan, memuncak pada V8–V18 ($5$–$7\text{ mm/hari}$), lalu anjlok mendekati 0 pada V25–V30. |
| **Total Presipitasi** | $\text{mm}$ (akumulasi) | **$225{,}15\text{ mm}$** | **$968{,}27\text{ mm}$** | $20{,}13\text{ mm}$ | Akumulasi pra-tanam ($225\text{ mm}$) cukup untuk membasahi profil tanah. Akumulasi dalam-musim ($968\text{ mm}$) sangat melimpah. |
| **Radiasi Surya (`srad`)** | $\text{MJ m}^{-2}\text{ hari}^{-1}$ | **$20{,}71 \pm 1{,}78$** | $17{,}16 \pm 1{,}28$ | $16{,}40 \pm 1{,}89$ | Tinggi pada pra-tanam (akhir musim kemarau yang cerah), lalu menurun pada dalam-musim akibat tingginya tutupan awan hujan tropis. |
| **Suhu Maksimum (`tmax`)** | $^\circ\text{C}$ | **$31{,}33 \pm 3{,}46$** | $29{,}78 \pm 3{,}19$ | $28{,}58 \pm 3{,}52$ | Tertinggi saat pra-tanam (puncak panas musim kering Chiapas), stabil hangat saat musim hujan, dan menurun saat musim gugur/dingin. |
| **Suhu Minimum (`tmin`)** | $^\circ\text{C}$ | $18{,}12 \pm 3{,}20$ | **$17{,}93 \pm 2{,}96$** | $15{,}27 \pm 3{,}41$ | Cenderung stabil hangat sepanjang musim tanam, lalu anjlok pada V25–V30 memasuki musim dingin Chiapas. |
| **Tekanan Uap Air (`vp`)** | $\text{Pa}$ | $1.220{,}75 \pm 267$ | **$2.058{,}09 \pm 284$** | $1.416{,}75 \pm 356$ | Melonjak tajam hampir $2\times$ lipat saat tanam (V7) mengonfirmasi pergeseran tegas dari udara kering ke masa monsun basah. |

---

## 4. Struktur Autokorelasi dan Redundansi Informasi Antarinterval

Visualisasi matriks korelasi antarinterval dan kurva peluruhan autokorelasi disajikan pada Gambar 2:

![Struktur Autokorelasi Cuaca](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/eda_03_weather_autocorrelation_redundancy.png)
*Gambar 2: Pemeriksaan ketergantungan serial temporal dan redundansi data cuaca Daymet: (A) Heatmap presipitasi; (B) Heatmap suhu maksimum; (C) Heatmap tekanan uap; (D) Kurva peluruhan autokorelasi (Lag-1 hingga Lag-10).*

### 4.1 Tingkat Ketergantungan Serial Temporal (Lag Autocorrelation)

Tabel 2 memuat parameter autokorelasi antarinterval sepuluh-harian untuk kelima variabel cuaca:

### Tabel 2: Rangkuman Metrik Autokorelasi Serial Fitur Cuaca Daymet

| Variabel Cuaca | Rata-rata Lag-1 ($r_{t, t+1}$) | Rentang Lag-1 (Min – Max) | Rata-rata Lag-2 ($r_{t, t+2}$) | Rata-rata Seluruh Matriks ($r_{\text{all}}$) | Derajat Redundansi Informasi & Implikasi Pemodelan |
|---|:---:|:---:|:---:|:---:|---|
| **`tmin`** | **0,881** | $0{,}638$ – $0{,}982$ | **0,843** | **0,802** | **Redundansi Ekstrem:** Hampir identik antarinterval berdekatan. Menjelaskan baseline termal lokasi, bukan dinamika cuaca dinamis. |
| **`tmax`** | **0,878** | $0{,}815$ – $0{,}947$ | **0,844** | **0,793** | **Redundansi Ekstrem:** Blok korelasi sangat masif ($r > 0{,}80$ bertahan hingga Lag-5 atau 50 hari). Multikolinearitas serial parah jika dipakai mentah. |
| **`vp`** | **0,753** | $0{,}376$ – $0{,}959$ | **0,632** | $0{,}388$ | **Redundansi Tinggi:** Kelembaban udara menunjukkan persistensi musiman yang kuat, terutama selama fase monsun basah (V7–V24). |
| **`srad`** | **0,473** | $0{,}278$ – $0{,}818$ | **0,289** | $0{,}141$ | **Redundansi Sedang:** Radiasi berfluktuasi sedang seiring dinamika tutupan awan harian. |
| **`prcp`** | **0,251** | $0{,}004$ – $0{,}503$ | **0,185** | **0,015** | **Redundansi Sangat Rendah (Episodik):** Presipitasi bersifat stokastik dan sporadis; hujan 10 hari ini tidak menjamin hujan 10 hari ke depan. |

> [!IMPORTANT]
> **Temuan Kunci Redundansi Cuaca:**
> Ke-30 interval untuk `tmax` dan `tmin` memiliki korelasi rata-rata lintas interval sebesar **$r \approx 0{,}80$**. Memasukkan seluruh 150 variabel cuaca mentah ke dalam model regresi linier secara langsung akan memicu **multikolinearitas serial kolosal**. Variabel suhu dan kelembaban Daymet tidak membawa 30 sinyal independen, melainkan satu sinyal iklim makro yang berulang.

---

## 5. Analisis Bivariat Hubungan Variabel Cuaca dengan `YIELD`

Visualisasi lintasan koefisien korelasi rank Spearman ($\rho$) terhadap `YIELD` di sepanjang 30 interval disajikan pada Gambar 3:

![Korelasi Cuaca vs YIELD](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/eda_03_weather_yield_correlations.png)
*Gambar 3: Lintasan korelasi Spearman (ρ) 5 parameter cuaca terhadap YIELD dari V1 hingga V30: (A–E) Perbandingan korelasi Global, Hybrid, dan Landrace; (F) Nilai korelasi absolut maksimum per zona temporal.*

### 5.1 Traktori Korelasi Tiap Variabel Cuaca Sepanjang Siklus Tanam

1. **Presipitasi (`prcp`): Perubahan Arah dari Positif ke Negatif**
   - **Pada Pra-Tanam (V1–V6):** Korelasi bertanda **positif kuat**, memuncak pada V4 ($\rho = +0{,}44$) dan V5 ($\rho = +0{,}42$). Hujan sebelum tanam menyediakan cadangan air profil tanah (*subsoil moisture recharge*) yang menjamin perkecambahan serempak.
   - **Pada Dalam-Musim (V7–V24):** Korelasi anjlok drastis mendekati nol, bahkan berbalik arah menjadi **negatif lemah** ($\rho = -0{,}16$ pada total presipitasi dalam-musim). Di daerah tropis Chiapas dengan curah hujan musiman $>900\text{ mm}$, air bukan lagi faktor pembatas utama. Kelebihan hujan justru berasosiasi dengan berkurangnya radiasi surya, pencucian hara, dan genangan air.
   - **Pada Periode Akhir (V25–V30):** Korelasi bertanda **negatif sedang** ($\rho = -0{,}34$). Hujan di akhir musim mengganggu proses pengeringan tongkol jagung (*dry-down*) dan memicu pembusukan biji.

2. **Suhu (`tmax` & `tmin`) dan Tekanan Uap (`vp`): Ilusi Asosiasi Kuat Akibat Perancu Elevasi**
   - Secara agregat global, `tmax`, `tmin`, dan `vp` menunjukkan korelasi positif tinggi yang persisten di seluruh interval ($\rho \approx +0{,}45$ hingga $+0{,}58$).
   - **Dekonvolusi Perancu (*Confounding Bias*):** Ketika dianalisis secara terstratifikasi di dalam masing-masing sub-populasi sistem:
     - Korelasi `tmax` pada sistem **Hybrid anjlok ke $\rho \approx +0{,}17$**, dan pada **Landrace anjlok ke $\rho \approx +0{,}14$**.
     - Penurunan korelasi dari $+0{,}47$ menjadi $+0{,}15$ membuktikan bahwa korelasi suhu global yang tinggi **bukan bukti bahwa jagung menyukai cuaca panas ekstrem**, melainkan mencerminkan fakta bahwa petak-petak berpanen tinggi (Hybrid) berlokasi di dataran rendah yang hangat, sedangkan petak-petak berpanen rendah (Landrace) berada di pegunungan tinggi yang dingin.

3. **Radiasi Surya (`srad`): Cermin Terbalik dari Presipitasi**
   - Radiasi surya berkorelasi negatif sedang pada pra-tanam hingga dalam-musim ($\rho \approx -0{,}47$). Mengapa? Karena radiasi tinggi terjadi pada hari-hari tanpa awan (musim kemarau/defisit air), sedangkan radiasi rendah bertepatan dengan hari-hari hujan lebat.

---

## 6. Evaluasi Skenario Prediksi Saat Tanam (*At-Planting*) vs Pemantauan Dalam-Musim (*In-Season*)

Visualisasi evaluasi komparasi kedua skenario disajikan pada Gambar 4:

![Evaluasi Skenario Prediksi Cuaca](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/eda_03_preplanting_vs_inseason_evaluation.png)
*Gambar 4: Evaluasi skenario prediksi: (A) Komparasi R² variansi panen terjelaskan; (B) Presipitasi pra-tanam vs YIELD; (C) Presipitasi dalam-musim vs YIELD; (D) Ringkasan arsitektur rekomendasi alur prediksi dual-horizon.*

### 6.1 Uji Daya Eksplanasi Model Linier: V1–V6 vs V7–V24 vs V1–V30

Untuk mengukur kapasitas informasi yang terkandung tanpa melakukan pemodelan final, dilakukan uji regresi multivariat dasar antar himpunan fitur cuaca:
- **Hanya Cuaca Pra-Tanam V1–V6 (30 Fitur):** Mampu menjelaskan **$R^2 = 0{,}3879$ (38,79% variansi `YIELD`)**.
- **Hanya Cuaca Dalam-Musim V7–V24 (90 Fitur):** Mampu menjelaskan **$R^2 = 0{,}4667$ (46,67% variansi `YIELD`)**.
- **Seluruh 150 Variabel Cuaca V1–V30:** Mampu menjelaskan **$R^2 = 0{,}5065$ (50,65% variansi `YIELD`)**.

Tabel 3 membandingkan nilai korelasi fitur ringkasan agregat periode cuaca terhadap hasil panen:

### Tabel 3: Perbandingan Asosiasi Fitur Agregat Cuaca Pra-Tanam vs Dalam-Musim

| Fitur Ringkasan Agregat Cuaca | Rata-rata | Median | Pearson ($r$) | Spearman ($\rho$) | Spearman Subgrup Hybrid | Spearman Subgrup Landrace |
|---|---:|---:|:---:|:---:|:---:|:---:|
| **Total Presipitasi Pra-Tanam (`tot_prcp_pre`, V1–V6)** | $225{,}15\text{ mm}$ | $242{,}00\text{ mm}$ | **+0,479** | **+0,492** | **+0,201** | **+0,391** |
| **Total Presipitasi Dalam-Musim (`tot_prcp_in`, V7–V24)** | $968{,}27\text{ mm}$ | $930{,}00\text{ mm}$ | **-0,087** | **-0,164** | **-0,058** | **-0,180** |
| **Total Presipitasi Akhir (`tot_prcp_late`, V25–V30)** | $20{,}13\text{ mm}$ | $2{,}00\text{ mm}$ | **-0,346** | **-0,342** | **-0,259** | **-0,314** |
| **Rata-rata T-Maks Pra-Tanam (`avg_tmax_pre`, V1–V6)** | $31{,}33^\circ\text{C}$ | $31{,}82^\circ\text{C}$ | **+0,453** | **+0,456** | **+0,231** | **+0,145** |
| **Rata-rata T-Maks Dalam-Musim (`avg_tmax_in`, V7–V24)** | $29{,}78^\circ\text{C}$ | $30{,}37^\circ\text{C}$ | **+0,479** | **+0,468** | **+0,173** | **+0,144** |
| **Rata-rata T-Min Pra-Tanam (`avg_tmin_pre`, V1–V6)** | $18{,}12^\circ\text{C}$ | $19{,}17^\circ\text{C}$ | **+0,528** | **+0,515** | **+0,202** | **+0,257** |
| **Rata-rata T-Min Dalam-Musim (`avg_tmin_in`, V7–V24)** | $17{,}93^\circ\text{C}$ | $18{,}48^\circ\text{C}$ | **+0,467** | **+0,449** | **+0,171** | **+0,180** |

---

## 7. Rekomendasi Kelayakan Data Cuaca V1–V6 untuk Skenario Prediksi Saat Tanam (*At-Planting*)

Menjawab pertanyaan mendasar penelitian: **Apakah data cuaca V1–V6 cukup informatif untuk skenario prediksi saat tanam?**

> [!TIP]
> ### KESIMPULAN REKOMENDASI METODOLOGIS
> **YA, DATA CUACA V1–V6 SANGAT CUKUP DAN LAYAK DIGUNAKAN SEBAGAI FONDASI UTAMA MODEL PREDIKSI SAAT TANAM (*AT-PLANTING FORECAST*).**
> 
> **Bukti Empiris Kelayakan:**
> 1. **Daya Eksplanasi Tinggi:** Informasi V1–V6 saja (30 fitur) telah mampu menangkap **$38{,}79\%$ variansi `YIELD`**, yang setara dengan **$76{,}6\%$ dari total kapasitas prediktif seluruh 150 variabel cuaca ($50{,}65\%$)**.
> 2. **Menangkap Dua Sinyal Agroklimat Kunci Sekaligus:**
>    - **Sinyal Kesiapan Air Lahan:** Presipitasi V1–V6 merekam tibanya awal musim hujan (*rain onset*) dan pengisian lengas tanah awal yang sangat krusial bagi keberhasilan fase vegetatif awal jagung.
>    - **Sinyal Karakteristik Termal Lokasi:** Suhu dan tekanan uap air V1–V6 secara efektif berfungsi sebagai proksi spasial iklim mikro lahan yang membedakan potensi biometrik dataran rendah dan dataran tinggi.

---

### Keterbatasan Kritis yang Wajib Dipertimbangkan dalam Pemodelan

Meskipun V1–V6 layak, peneliti wajib mempertimbangkan 4 keterbatasan fundamental berikut sebelum melangkah ke tahap persiapan data (*data preparation*):

1. **Kebutaan terhadap Syok Cuaca Ekstrem Dalam-Musim (*Look-Ahead Blindness*):**
   Model berbasis V1–V6 secara inheren tidak mampu melihat anomali cuaca yang terjadi setelah hari penanaman, seperti:
   - Kejadian kekeringan mendadak di tengah musim hujan (*mid-summer drought / canícula*).
   - Badai tropis atau banjir genangan yang merusak pertanaman saat pembungaan atau pengisian biji.
   *Implikasi Komunitas ASA:* Prediksi sebelum tanam harus diposisikan sebagai **estimasi batas daya dukung dasar (*baseline carrying capacity*)**, bukan jaminan mutlak pasokan pakan bebas risiko iklim.

2. **Perancu Kuat Antara Suhu Cuaca, Elevasi, dan Sistem Budidaya:**
   Tingginya korelasi suhu V1–V6 sebagian besar merupakan cerminan tidak langsung dari elevasi lahan dan sistem budidaya (`Hybrid` di dataran rendah hangat vs `Landrace` di pegunungan dingin). Jika model linier memasukkan `Elev`, `System`, dan `tmax_V1` secara bersamaan tanpa regularisasi, akan terjadi perebutan bobot koefisien akibat multikolinearitas.

3. **Multikolinearitas Serial Antar-Interval V1–V6:**
   Enam interval V1–V6 untuk suhu maksimum (`tmax_V1` s.d. `tmax_V6`) memiliki autokorelasi $r > 0{,}85$. Menggunakan ke-30 fitur mentah V1–V6 secara parsial sangat tidak efisien. **Sangat disarankan melakukan rekayasa fitur (*feature aggregation*)** pada tahap persiapan data, seperti merangkumnya menjadi:
   - Total presipitasi pra-tanam ($\sum \text{prcp}_{V1-V6} \times 10$).
   - Rata-rata suhu maksimum dan minimum pra-tanam.
   - Anomali kelembaban udara pra-tanam.

4. **Arsitektur Pemodelan Dual-Horizon yang Direkomendasikan:**
   Untuk kebutuhan sistem pendukung keputusan *Smart Farming* Komunitas ASA yang adaptif:
   - **Model Horizon 1 (Saat Tanam / At-Planting):** Memadukan fitur statis topografi (`Elev`, `Slope`), sifat tanah (`Clay`, `CEC`, `SOM`, `PH`), rencana budidaya (`System`, `Tillage`, rencana `N/P/K`), dan **cuaca pra-tanam V1–V6** untuk menyusun rencana kuota populasi ayam petelur awal.
   - **Model Horizon 2 (Pemantauan Dinamis / In-Season Update):** Memanfaatkan cuaca aktual berjalan (V7–V24) secara berkala (misalnya pada pertengahan musim tanam) untuk merevisi angka estimasi hasil panen dan menyesuaikan stok cadangan pakan peternak sebelum panen tiba.

---

## 8. Indeks Berkas Laporan & Visualisasi Terkait

Seluruh berkas visualisasi pendukung resolusi tinggi ($300\text{ DPI}$) telah tersimpan di direktori output resmi dan dapat diakses langsung melalui tautan berikut:

1. [EDA_03_WEATHER_TEMPORAL.md](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/EDA_03_WEATHER_TEMPORAL.md): Laporan lengkap EDA Tahap 3 Variabel Cuaca Daymet.
2. [eda_03_weather_temporal_trajectories.png](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/eda_03_weather_temporal_trajectories.png): Visualisasi profil dinamika temporal 5 parameter cuaca (V1–V30) dengan batas zona pra-tanam, dalam-musim, dan akhir.
3. [eda_03_weather_yield_correlations.png](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/eda_03_weather_yield_correlations.png): Visualisasi lintasan koefisien korelasi Spearman 150 variabel cuaca terhadap YIELD serta dekomposisi per sistem budidaya.
4. [eda_03_weather_autocorrelation_redundancy.png](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/eda_03_weather_autocorrelation_redundancy.png): Heatmap autokorelasi serial dan profil peluruhan ketergantungan antarinterval untuk mendeteksi redundansi data cuaca.
5. [eda_03_preplanting_vs_inseason_evaluation.png](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/eda_03_preplanting_vs_inseason_evaluation.png): Visualisasi komparasi kapabilitas prediktif skenario pra-tanam (V1–V6) vs dalam-musim (V7–V24) serta rekomendasi arsitektur dual-horizon.
6. [generate_eda_03_charts.py](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/generate_eda_03_charts.py): Skrip Python otomatisasi pembuatan seluruh visualisasi EDA Tahap 3.
7. [run_eda_03_weather_stats.py](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/run_eda_03_weather_stats.py): Skrip Python komputasi statistik temporal, autokorelasi, korelasi YIELD, dan metrik agregasi cuaca.
8. [eda_03_weather_stats_summary.json](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/eda_03_weather_stats_summary.json): Berkas rekaman numerik JSON berisi seluruh hasil komputasi statistik cuaca presisi tinggi.
9. [EDA_01_TARGET_YIELD.md](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/EDA_01_TARGET_YIELD.md): Laporan resmi acuan EDA Tahap 1 Variabel Target YIELD.
10. [EDA_02_AGRONOMY_SOIL_TOPOGRAPHY.md](file:///C:/SKRIPSI/03_Exploration/Dataset_03_Chiapas/Output/EDA_02_AGRONOMY_SOIL_TOPOGRAPHY.md): Laporan resmi acuan EDA Tahap 2 Fitur Agronomi, Tanah, dan Topografi.
