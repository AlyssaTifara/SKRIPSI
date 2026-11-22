# LAPORAN VERIFIKASI KRITIS: CHIAPAS MAIZE DATASET (2012–2018)
## Investigasi Mandiri Berkas Excel Asli, Paper Trevisan et al. (2022), dan Kelayakan Pemodelan Smart Farming Komunitas ASA

---

## 1. Konteks dan Tujuan Verifikasi Kritis

Laporan ini disusun sebagai dokumen verifikasi tingkat lanjut (*critical verification audit*) yang mengevaluasi secara ketat berkas asli `Chiapas Field Data 2012-2018.xlsx` (sheet `Data` dan `Legend`), berkas publikasi ilmiah pendamping [Trevisan et al. (2022) di *Data in Brief*](file:///C:/SKRIPSI/07_Documentation/01_Literature_Review/Multiyear%20Maize%20Management%20Dataset.pdf), serta laporan audit sebelumnya.

Audit ini menanggapi 4 isu mendasar:
1. **Diskrepansi Statistik Yield:** Mengapa paper melaporkan rata-rata 6 Mg ha⁻¹ dan rentang 0,1–10,0 Mg ha⁻¹, sedangkan komputasi data aktual menunjukkan rata-rata 3,59 Mg ha⁻¹.
2. **Verifikasi Missing Values:** Memverifikasi klaim 168 kolom lengkap dan 310 nilai kosong pada `Cultivar` setelah normalisasi berbagai bentuk karakter kosong.
3. **Prediction-Time Feasibility & Data Leakage:** Mengkaji ketersediaan variabel secara temporal (sebelum tanam, saat tanam, dan menjelang panen) serta mengevaluasi potensi kebocoran data (*lookahead leakage*) pada variabel cuaca V1–V30, pupuk NPK, dan `Mun_yield`.
4. **Local Calibration Feasibility:** Mengkaji secara teoritis dan metodologis batasan kalibrasi model pada 3 petak demoplot Komunitas ASA di Sumenep, Madura.

> [!IMPORTANT]
> **Prinsip Audit:** Audit ini dilakukan secara non-destruktif tanpa mengubah berkas sumber data (`.xlsx` maupun `.csv`) dan tanpa menjalankan *training/fitting* pemodelan *machine learning*.

---

## 2. Tabel Perbandingan Angka Hasil Komputasi Data Aktual vs Paper Trevisan et al. (2022)

Pemeriksaan komparatif dilakukan dengan membandingkan hasil kalkulasi langsung pada 4.585 baris data berkas Excel asli terhadap Table 2 dan teks narasi publikasi Trevisan et al. (2022).

### 2.1 Perbandingan Komprehensif Seluruh Variabel Numerik (Table 2 Paper vs Data Aktual)

| Variabel | Unit | Mean (Data) | Mean (Paper) | SD (Data) | SD (Paper) | P0 Min (Data) | P0 (Paper) | P25 Q1 (Data) | P25 (Paper) | P50 Med (Data) | P50 (Paper) | P75 Q3 (Data) | P75 (Paper) | P100 Max (Data) | P100 (Paper) | Status Kesesuaian |
|---|:---:|---:|:---:|---:|:---:|---:|:---:|---:|:---:|---:|:---:|---:|:---:|---:|:---:|---|
| **YIELD** | **Mg ha⁻¹** | **3,59** | **6** | **1,87** | **1,9** | **0,10** | **0,1** | **1,85** | **1,9** | **3,60** | **6** | **5,00** | **5,0** | **9,80** | **9,8** | **DISKREPANSI PADA MEAN & P50** |
| **Elevation** | m dpl | 884,70 | 884 | 443,93 | 443 | 7,00 | 7 | 592,00 | 592 | 712,00 | 712 | 1079,00 | 1079 | 2849,00 | 2849 | **100% Identik** |
| **Slope** | % | 6,03 | 6,0 | 6,78 | 6,8 | 0,00 | 0 | 1,34 | 1,3 | 3,04 | 3,0 | 8,74 | 8,7 | 61,19 | 61,2 | **100% Identik** |
| **Clay** | % | 30,15 | 30 | 10,12 | 10 | 5,00 | 5 | 23,00 | 23 | 28,00 | 28 | 37,00 | 37 | 57,00 | 57 | **100% Identik** |
| **CEC** | cmolc dm⁻³ | 22,74 | 22,7 | 7,42 | 7,4 | 4,31 | 4,3 | 16,18 | 16,2 | 21,12 | 21,1 | 27,60 | 27,6 | 50,80 | 50,8 | **100% Identik** |
| **SOM** | % | 1,60 | 1,6 | 0,93 | 0,9 | 0,27 | 0,3 | 0,97 | 1,0 | 1,17 | 1,2 | 2,03 | 2,0 | 4,00 | 4,0 | **100% Identik** |
| **pH** | - | 6,81 | 6,8 | 0,71 | 0,7 | 4,92 | 4,9 | 6,62 | 6,6 | 6,79 | 6,8 | 7,34 | 7,3 | 8,25 | 8,3 | **100% Identik** |
| **Planting** | DOY | 165,12 | 165 | 22,53 | 22 | 91,00 | 91 | 153,00 | 153 | 167,00 | 167 | 180,00 | 180 | 242,00 | 242 | **100% Identik** |
| **Nitrogen** | kg N ha⁻¹ | 109,74 | 109 | 64,13 | 64 | 0,00 | 0 | 64,00 | 64 | 110,00 | 110 | 156,00 | 156 | 349,00 | 349 | **100% Identik** |
| **Phosphorus** | kg P₂O₅ ha⁻¹ | 23,88 | 23 | 26,71 | 26 | 0,00 | 0 | 0,00 | 0 | 23,00 | 23 | 46,00 | 46 | 143,00 | 143 | **100% Identik** |
| **Potassium** | kg K₂O ha⁻¹ | 9,30 | 9 | 17,74 | 17 | 0,00 | 0 | 0,00 | 0 | 0,00 | 0 | 12,50 | 12 | 100,00 | 100 | **100% Identik** |
| **Precipitation** | mm day⁻¹ | 4,05 | 4,05 | 4,86 | 4,86 | 0,00 | 0 | 0,00 | 0 | 2,10 | 2,1 | 6,80 | 6,8 | 54,90 | 54,9 | **100% Identik** (pooled 30 V) |
| **Solar Radiation** | MJ m⁻² day⁻¹ | 17,71 | 17,7 | 2,83 | 2,8 | 6,78 | 6,8 | 15,55 | 15,6 | 17,36 | 17,4 | 19,55 | 19,5 | 26,76 | 26,8 | **100% Identik** (pooled 30 V) |
| **Max Temperature** | °C | 29,85 | 29,8 | 2,51 | 2,5 | 16,60 | 16,6 | 28,40 | 28,4 | 30,15 | 30,2 | 31,50 | 31,5 | 39,20 | 39,2 | **100% Identik** (pooled 30 V) |
| **Min Temperature** | °C | 17,44 | 17,4 | 1,02 | 1,0 | -2,15 | -2,1 | 15,50 | 15,5 | 18,00 | 18,0 | 19,70 | 19,7 | 36,25 | 36,2 | **100% Identik** (pooled 30 V) |
| **Vapor Pressure** | Pa | 1762,36 | 1761 | 628,44 | 628 | 252,00 | 252 | 1336,00 | 1336 | 1900,00 | 1900 | 2240,00 | 2240 | 6452,00 | 6452 | **100% Identik** (pooled 30 V) |

### 2.2 Rincian Khusus Statistik Variabel YIELD

| Parameter Metrik | Nilai Aktual Komputasi | Nilai Dilaporkan Paper | Selisih / Deviasi | Status Validitas |
|---|---:|---:|---:|---|
| **Jumlah Baris Valid** | 4.585 | 4.585 | 0 | 100% Lengkap |
| **Jumlah Missing Value** | 0 | 0 | 0 | Tidak ada sel kosong |
| **Jumlah Nilai Nol (`0`)** | 0 | 0 | 0 | Tidak ada gagal panen total absolut |
| **Minimum ($P_0$)** | 0,1000 Mg ha⁻¹ | 0,1 Mg ha⁻¹ | 0,00 | Identik |
| **Maksimum ($P_{100}$)** | 9,8000 Mg ha⁻¹ | 9,8 Mg ha⁻¹ (Tabel) / 10,0 (Teks) | 0,00 / -0,20 | Identik di Tabel, dibulatkan di teks |
| **Mean (Rata-rata)** | **3,5926 Mg ha⁻¹** | **6 Mg ha⁻¹** | **-2,4074 Mg ha⁻¹ (-40,1%)** | **Diskrepansi Mayor** |
| **Median ($P_{50}$)** | **3,6000 Mg ha⁻¹** | **6 Mg ha⁻¹** | **-2,4000 Mg ha⁻¹ (-40,0%)** | **Diskrepansi Mayor** |
| **Kuartil 1 ($P_{25}$)** | 1,8500 Mg ha⁻¹ | 1,9 Mg ha⁻¹ | -0,05 | Identik (pembulatan 1 desimal) |
| **Kuartil 3 ($P_{75}$)** | 5,0000 Mg ha⁻¹ | 5,0 Mg ha⁻¹ | 0,00 | Identik |
| **Standar Deviasi ($s$)** | 1,8686 Mg ha⁻¹ | 1,9 Mg ha⁻¹ | -0,03 | Identik (pembulatan 1 desimal) |
| **Interquartile Range (IQR)** | 3,1500 Mg ha⁻¹ | 3,1 Mg ha⁻¹ | +0,05 | Konsisten |

---

## 3. Bukti Perhitungan Ilmiah dan Rekonstruksi Diskrepansi

Penetapan bahwa nilai pada paper mengalami kesalahan ketik/tata letak (*typographical truncation*) didasarkan pada **tujuh pilar bukti matematis, statistik, dan forensik dokumen** berikut:

### Bukti 1: Pelanggaran Aksioma Monotonisitas Statistik Terurut (*Ordered Statistics Contradiction*)
Secara fundamental dalam teori statistika, persentil dari suatu variabel acak wajib memenuhi urutan monoton tidak-turun:
$$P_0 \le P_{25} \le P_{50} \le P_{75} \le P_{100}$$

Pada Table 2 publikasi Trevisan et al. (2022), baris *Yield* tercetak:
$$P_{25} = 1,9 \quad \longrightarrow \quad \mathbf{P_{50} = 6} \quad \longrightarrow \quad P_{75} = 5,0$$

Pernyataan $P_{50} = 6$ ketika $P_{75} = 5,0$ menghasilkan kontradiksi:
$$6 \le 5,0 \quad \text{(SECARA AKSIOMATIK MUSTAHIL)}$$
Nilai tengah (median) dari 4.585 data tidak mungkin lebih besar daripada batas 75% data terendah. Fakta ini membuktikan anomali cetak internal pada Table 2 tanpa memerlukan data eksternal.

### Bukti 2: Kontradiksi Batas Atas Rata-rata Tertimbang Subgrup (*Subgroup Weighted Mean Bound*)
Pada Section 1 (Halaman 3 paragraf 4), Trevisan et al. menuliskan fakta agronomi hasil panen:
> *"The yields follow the same pattern, with most observations in the range of 1.6 to 3.0 Mg ha⁻¹ for the Landrace system and 4.2 to 5.3 Mg ha⁻¹ in the Hybrid system."*

Proporsi observasi aktual dalam dataset:
- Sistem `Hybrid`: $N = 3.034$ lahan (proporsi $w_H = 66,17\%$, rata-rata aktual = $4,45$ Mg ha⁻¹).
- Sistem `Landrace`: $N = 1.551$ lahan (proporsi $w_L = 33,83\%$, rata-rata aktual = $1,92$ Mg ha⁻¹).

Jika kita asumsikan skenario batas atas paling ekstrem (seluruh lahan Landrace menghasilkan nilai tertinggi 3,0 Mg ha⁻¹ dan seluruh lahan Hybrid menghasilkan nilai tertinggi 5,3 Mg ha⁻¹):
$$\text{Batas Atas Maksimum Teoretis} = (0,3383 \times 3,0) + (0,6617 \times 5,3) = 1,0149 + 3,5070 = \mathbf{4,5219 \text{ Mg ha⁻¹}}$$

Rata-rata global sebesar **6,0 Mg ha⁻¹** melanggar batas atas teoretis tertinggi yang dimungkinkan oleh deskripsi agronomi penulis sendiri. Rata-rata tertimbang aktual dari data riil adalah:
$$\bar{Y} = (0,3383 \times 1,9236) + (0,6617 \times 4,4457) = 0,6508 + 2,9417 = \mathbf{3,5925 \text{ Mg ha⁻¹}}$$

### Bukti 3: Pola Pemotongan Karakter (*Truncation Signature*) `"3.6"` $\rightarrow$ `"6"`
Perhatikan nilai hasil komputasi pada berkas asli:
- Rata-rata aktual: $3,5926 \text{ Mg ha⁻¹} \approx \mathbf{3,6}$ (pembulatan 1 desimal).
- Median aktual ($P_{50}$): $3,6000 \text{ Mg ha⁻¹} = \mathbf{3,6}$.

Di Table 2 paper:
- Kolom *Mean* tertulis: **`6`**
- Kolom *P50* tertulis: **`6`**

Kedua parameter yang bernilai numerik identik `3.6` mengalami pemotongan karakter awalan `"3."` secara simultan, menyisakan angka desimal `"6"`. Sebaliknya, 15 baris variabel lainnya di Table 2 tercetak dengan presisi 1 desimal yang sempurna.

### Bukti 4: Alur Sitasi Teks Terhadap Tabel (*Citation Trail*)
Teks narasi pada Section 1 Halaman 3 berbunyi:
> *"The yield ranged from 0.1 to 10.0 Mg ha⁻¹, with 75% of the values lower than 5.0 Mg ha⁻¹ and an average of 6 Mg ha⁻¹ (Table 2)."*

Frasa rujukan `(Table 2)` menegaskan bahwa penulis menyalin angka rata-rata `6` langsung dari Table 2 saat menyusun draf naskah, bukan menghitungnya dari formula terpisah.

---

### Bukti 5: Verifikasi Missing-Value dan Koreksi Distribusi Missing Cultivar

Pemeriksaan komprehensif dilakukan dengan menormalisasi seluruh kemungkinan nilai kosong:
- Objek kosong: `None`, `np.nan`, `pd.NA`.
- String kosong & spasi: `""`, `" "`, `"   "`.
- Karakter sentinel: `"NA"`, `"N/A"`, `"nan"`, `"null"`, `"none"`, `"-"`, `"."`, `"#N/A"`, `"?"`.

#### Hasil Pemindaian Menyeluruh (169 Kolom $\times$ 4.585 Baris)
- **168 Kolom Lengkap (100% / 0 Missing):** Termasuk target `YIELD`, koordinat `Lat`/`Long`, elevasi, jenis tanah, dosis NPK, seluruh 150 variabel cuaca gridded (V1–V30), dan waktu tanam `Planting`.
- **1 Kolom Memiliki Missing Value:** Kolom `Cultivar` memiliki **tepat 310 sel kosong (6,76%)**.

#### Koreksi Fakta atas Laporan Audit Sebelumnya
Laporan audit sebelumnya menyebutkan bahwa 310 data kosong Cultivar terjadi hanya pada tahun 2012 (245 baris Hybrid dan 65 baris Landrace). **Pernyataan tersebut terbukti keliru setelah diverifikasi langsung ke berkas Excel mentah.**

Fakta sebaran aktual missing `Cultivar`:
1. **100% Nilai Kosong Berada pada Sistem Hybrid:** Seluruh 310 baris missing cultivar berpasangan dengan `System == 'Hybrid'`. Pada sistem `Landrace`, seluruh baris (1.551 baris) terisi nama varietas lokal (`CRIOLLO`, `CRIOLLO BLANCO`, dll).
2. **Nilai Kosong Terjadi di Setiap Tahun (2012–2018):**
   * 2012: 230 baris (36,68% dari Hybrid 2012)
   * 2013: 11 baris (2,31% dari Hybrid 2013)
   * 2014: 23 baris (12,71% dari Hybrid 2014)
   * 2015: 14 baris (3,54% dari Hybrid 2015)
   * 2016: 15 baris (4,05% dari Hybrid 2016)
   * 2017: 9 baris (1,60% dari Hybrid 2017)
   * 2018: 8 baris (1,89% dari Hybrid 2018)
   * **Total: 310 baris**

---

### Bukti 6: Evaluasi Waktu Prediksi dan Potensi Kebocoran Data (Data Leakage)

Pemeriksaan terhadap sheet `Legend` menegaskan bahwa variabel cuaca DAYMET diagregasikan ke dalam 30 jendela 10-harian:
- $V_1$ s/d $V_6$: 60 hari sebelum tanam (-60 s/d 0 DAP).
- $V_7$ s/d $V_{30}$: 240 hari setelah tanam (1 s/d 240 DAP).

#### Matriks Ketersediaan Fitur Berdasarkan Waktu Eksekusi Prediksi

| Variabel | Tahap Perencanaan (Day -60 s/d -30) | Tahap Hari Tanam (Day 0) | Tahap Vegetatif (30–40 DAP) | Tahap Panen (Ex-Post) | Potensi & Jenis Kebocoran Data (Data Leakage) |
|---|:---:|:---:|:---:|:---:|---|
| `Lat`, `Long`, `Elev`, `Slope` | Tersedia | Tersedia | Tersedia | Tersedia | **Aman.** Properti geografis statis. |
| `Clay`, `CEC`, `SOM`, `PH` | Tersedia | Tersedia | Tersedia | Tersedia | **Aman.** Berasal dari peta tanah/uji lab awal. |
| `System`, `Cultivar`, `Tillage` | Rencana | Pasti | Pasti | Pasti | **Aman.** Parameter keputusan petani. |
| `Planting` (DOY) | Estimasi | Pasti | Pasti | Pasti | Rentan bias pada tahap perencanaan jika awal hujan bergeser. |
| `Nitrogen`, `Phosphorus`, `Potassium` | Dosis Rencana | Dosis Dasar | Dosis Susulan | Total Riil | **LEAKAGE MANAJEMEN:** Dataset BEM mencatat total kumulatif satu musim, bukan pemupukan bertahap (*split*). |
| `Mun_yield` | Tidak Ada | Tidak Ada | Tidak Ada | Tersedia | **LEAKAGE TEMPORAL KRITIS ($r = 0,639$):** Sensus SIAP dirilis pasca-panen tahun berjalan. |
| Cuaca DAYMET $V_1$–$V_3$ | Sebagian Ada | Tersedia | Tersedia | Tersedia | **Aman pada Day 0.** Pada Day -60 belum terjadi. |
| Cuaca DAYMET $V_4$–$V_6$ | **BELUM TERJADI** | Tersedia | Tersedia | Tersedia | **LEAKAGE PRA-TANAM:** Mengasumsikan V4–V6 tersedia saat perencanaan (-60 hari) adalah kebocoran waktu. |
| Cuaca DAYMET $V_7$–$V_{16}$ | **BELUM TERJADI** | **BELUM TERJADI** | Sebagian Ada | Tersedia | **LEAKAGE MASIF:** Memasukkan cuaca in-season riil saat tanam menyebabkan overfitting retrospektif. |
| Cuaca DAYMET $V_{17}$–$V_{30}$ | **BELUM TERJADI** | **BELUM TERJADI** | **BELUM TERJADI** | Tersedia | **LEAKAGE MASIF:** Fase pengisian akhir dan pengeringan panen. |

---

### Bukti 7: Batasan Formal Kalibrasi Model Lokal pada Tiga Petak ASA ($N = 3$)

Komunitas ASA memiliki 3 petak demoplot jagung di Sumenep, Madura. Evaluasi statistik matematis terhadap $N = 3$:
1. **Derajat Kebebasan ($df$):** Dengan $N = 3$, derajat kebebasan hanya $df = 3 - 1 = 2$. Nilai kritis $t$-Student untuk selang kepercayaan 95% adalah $t_{0.025, 2} = 4,303$.
2. **Ketidakseimbangan Dimensi ($p \gg N$):** Dataset memiliki 168 fitur. Mengestimasi model regresi atau pohon keputusan dengan $p = 168$ dan $N = 3$ menghasilkan sistem *underdetermined* tak terbatas.
3. **Pemisahan Tiga Tingkatan Metodologi:**
   * **Validasi Eksternal (*Zero-Shot Evaluation*): LAYAK.** Menguji langsung model proxy Chiapas pada data 3 petak ASA tanpa mengubah bobot. Berfungsi sebagai studi kasus kualitatif / *sanity check* komparatif.
   * **Kalibrasi Parameter (*Scalar Bias Correction*): HANYA HEURISTIK.** Menghitung pergeseran rata-rata aditif tunggal ($\Delta = \frac{1}{3}\sum (y_i - \hat{y}_i)$) atau pengali rasio ($\alpha = \bar{y}_{ASA} / \bar{y}_{proxy}$). Tidak memiliki kekuatan inferensi statistik karena interval keyakinan sangat lebar ($\pm 2,48 \times s$).
   * **Retraining / Fine-Tuning Machine Learning: MUTLAK DILARANG SECARA METODOLOGIS.** Model pohon (Random Forest, XGBoost) hanya memerlukan 2 titik pemisahan (*splits*) untuk menghafal 100% data ($R^2 = 1,0$ pada train set), memicu keruntuhan generalisasi total (*catastrophic overfitting*).

---

## 4. Kesimpulan Akademis dan Metodologis

1. **Nilai Acuan Hasil Panen Resmi:** Karakteristik produktivitas jagung Chiapas pada naskah skripsi Bab 3 dan Bab 4 wajib merujuk pada angka hasil komputasi data aktual:
   $$\text{Mean} = \mathbf{3,59 \text{ Mg ha⁻¹}}, \quad \text{Median} = \mathbf{3,60 \text{ Mg ha⁻¹}}, \quad \text{Rentang} = \mathbf{0,10 \text{ s.d. } 9,80 \text{ Mg ha⁻¹}}$$
   Pernyataan pada publikasi Trevisan et al. (2022) yang menyebutkan rata-rata 6 Mg ha⁻¹ dan median 6 terbukti merupakan cacat tipografi (*typographical truncation*) dari angka asli 3,6 Mg ha⁻¹.
2. **Kualitas dan Integritas Berkas:** Dataset memiliki tingkat kelengkapan yang luar biasa tinggi (168 dari 169 kolom terisi 100%). Ke-310 data kosong pada `Cultivar` murni terjadi pada sistem `Hybrid` dan tidak boleh dihapus, melainkan dikelompokkan ke dalam kategori `'UNKNOWN_OR_UNSPECIFIED'`. Berkas CSV dan Excel 100% identik tanpa kehilangan data.
3. **Pencegahan Kebocoran Data (Data Leakage):** Model prediksi untuk perencanaan pakan di Komunitas ASA tidak boleh menggunakan variabel agregat wilayah tahun berjalan (`Mun_yield`) maupun variabel cuaca pasca-tanam ($V_7$–$V_{30}$) observasi riil tanpa prakiraan cuaca musiman.
4. **Posisi Data Tiga Petak ASA:** Data dari 3 petak lahan ASA difungsikan secara eksklusif sebagai **studi kasus validasi eksternal ilustratif**, bukan untuk melatih ulang (*retraining*) atau melakukan *fine-tuning* algoritma machine learning.

---

## 5. Hal yang Masih Belum Dapat Dipastikan (Uncertainties & Open Questions)

Meskipun integritas numerik dataset telah terbukti secara tuntas, terdapat sejumlah faktor eksternal dan domain-spesifik yang **tidak dapat dipastikan hanya dari data internal berkas Excel**:

1. **Penyebab Spesifik Terpotongnya Angka di Elsevier:**
   Tidak dapat dipastikan dengan dokumen yang ada apakah pemotongan `"3."` pada nilai `3.6` di Table 2 terjadi akibat skrip otomasi tabel (misal regex di R/Python yang memotong digit awal), penyusutan lebar kolom saat typesetting LaTeX oleh penerbit Elsevier, atau kesalahan pengetikan manual saat transfer naskah final.
2. **Alasan Ketiadaan Nama Varietas Hibrida pada 310 Petak:**
   Tidak terdokumentasi apakah ketiadaan nama varietas hibrida disebabkan oleh petani yang membeli benih curah/oplosan tanpa label resmi, ataukah penyuluh lapangan MasAgro lalai menanyakan seri komersial varietas tersebut saat entri BEM.
3. **Jadwal dan Tanggal Rilis Resmi Sensus Tahunan SIAP:**
   Tidak ada rekaman tanggal spesifik kapan angka rata-rata munisipalitas (`Mun_yield`) per tahun diterbitkan oleh pemerintah Meksiko (apakah dirilis pada bulan Desember tahun berjalan, atau kuartal pertama tahun berikutnya). Hal ini mempengaruhi ketepatan batasan jeda waktu (*latency*) jika `Mun_yield` historis hendak digunakan.
4. **Protokol Kadar Air Panen Standar vs Kadar Air Lapangan:**
   Sheet `Legend` menuliskan satuan panen sebagai `Mg ha-1`, namun tidak merinci apakah timbangan panen telah dikonversi ke kadar air standar perdagangan (14% basis kering) ataukah berupa bobot panen pipil basah saat pemetikan manual yang tertunda hingga 175–240 DAP.
5. **Tingkat Transferabilitas Hubungan Fitur Chiapas ke Tanah Madura:**
   Secara pedologi dan iklim, Chiapas didominasi tanah vulkanik/lempung pegunungan dan iklim tropis basah dataran tinggi Meksiko, sedangkan Sumenep (Madura) didominasi tanah berkapur/inseptisol/vertisol dengan pola iklim musiman kering (*dry tropical*). Deviasi respons pemupukan NPK dan varietas lokal Madura terhadap hasil panen tidak dapat dipastikan tanpa uji agronomi lapangan multi-musim di Madura.
