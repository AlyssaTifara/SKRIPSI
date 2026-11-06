# THESIS CONTEXT HANDOVER FOR ANTIGRAVITY

**Versi:** 1.0\
**Tanggal pembaruan:** 28 Oktober 2026\
**Tujuan:** Menjadi dokumen konteks utama agar Antigravity dapat
membantu melanjutkan penelitian dan nantinya mengimplementasikan sistem
tanpa kehilangan keputusan, mengulang pekerjaan, atau mengubah arah
skripsi secara tidak sengaja.

> **Instruksi utama:** Baca dokumen ini secara menyeluruh sebelum
> memberi rekomendasi, menyusun kode, atau mengubah artefak penelitian.
> Dokumen ini menggabungkan konteks master lama, handover 21 Oktober
> 2026, perkembangan setelahnya, serta keputusan terbaru yang telah
> diberikan pengguna. Jika dokumen lama bertentangan dengan keputusan
> terbaru dalam dokumen ini, ikuti keputusan terbaru dan catat konflik
> tersebut dalam decision log.

------------------------------------------------------------------------

## 0. Ringkasan Eksekutif

Pengguna adalah mahasiswa **Sarjana Terapan Sistem Informasi Bisnis
(SIB), Politeknik Negeri Malang**. Penelitian berada pada domain **Smart
Farming**, dengan konteks pemanfaatan hasil panen jagung untuk mendukung
perencanaan produksi ayam petelur di Komunitas ASA Indonesia, Sumenep,
Jawa Timur.

### Judul skripsi sudah ditetapkan oleh dosen pembimbing dan tidak boleh diubah sepihak

**PEMODELAN PREDIKSI JUMLAH AYAM PETELUR UNTUK *SMART FARMING*
BERDASARKAN KETERSEDIAAN LAHAN JAGUNG UNTUK MENDUKUNG PERENCANAAN
PRODUKSI DI KOMUNITAS ASA INDONESIA.**

Judul tersebut adalah keputusan terbaru dan mengesampingkan dokumen
master/handover lama yang menyebut judul atau jenis ayam masih belum
final. Jangan menyarankan mengganti ayam petelur menjadi broiler,
mengganti judul, atau menafsirkan judul sebagai belum disetujui. Jika
ada masalah konsistensi akademik yang perlu didiskusikan, pertahankan
judul dan ajukan sebagai hal untuk dikonfirmasi kepada dosen, bukan
mengubah keputusan.

### Gagasan penelitian saat ini

Penelitian diarahkan pada model matematis/kuantitatif yang
menghubungkan: 1. lahan dan estimasi hasil panen jagung; 2. bagian
jagung yang benar-benar tersedia dan dialokasikan untuk pakan; 3.
kebutuhan pakan ayam petelur dan proporsi jagung dalam ransum; 4.
periode perencanaan; 5. estimasi jumlah ayam petelur yang secara
teoritis dapat didukung oleh ketersediaan jagung.

Model kemudian menjadi inti perhitungan yang dapat disajikan melalui
sistem informasi berbasis web jika kebutuhan sistem sudah cukup jelas.
**Jangan memulai dengan membangun aplikasi atau memilih stack sebelum
model, data, dan kebutuhan informasi dirumuskan.**

### Posisi kerja terbaru

-   Judul: **FIXED BY SUPERVISOR**.
-   Jenis ayam: **ayam petelur/layer, mengikuti judul yang sudah
    ditetapkan**.
-   Bab I: sudah dibuat sebagai **draft awal** untuk dibahas dengan
    dosen; bukan naskah final yang bebas dari revisi.
-   Referensi Bab I saat ini mencakup Gunjević et al. (2023), Handayati
    et al. (2022), Amzeri et al. (2023), dan Sinaga et al. (2026).
-   Model matematis: masih **konsep awal**, belum final. Parameter dan
    asumsi harus diaudit.
-   Sistem: target akhir berupa sistem yang mendukung tujuan skripsi;
    implementasi web adalah arah yang mungkin/direncanakan, tetapi
    kebutuhan, fitur, arsitektur, stack, dan metode pengembangan belum
    final.
-   Data aktual mitra: belum tersedia secara memadai untuk menetapkan
    parameter aktual. Jangan mengarang data atau menganggap angka
    literatur sebagai hasil aktual ASA.

------------------------------------------------------------------------

## 1. Identitas Akademik dan Cara Membantu Pengguna

-   Institusi: Politeknik Negeri Malang.
-   Program: Sarjana Terapan Sistem Informasi Bisnis (SIB), Jurusan
    Teknologi Informasi.
-   Konteks: skripsi/proposal D4.
-   Dosen pembimbing: Pak Habibie Ed Dien (Pak HBB).
-   Pengguna menginginkan bahasa Indonesia yang jelas, natural, santai
    tetapi teliti secara akademik.
-   Berikan rekomendasi bertahap dan konkret. Hindari mengulang
    pencarian luas yang sudah dilakukan tanpa alasan spesifik.
-   Jadilah mitra berpikir kritis: uji logika, bukti, konsistensi unit,
    validitas parameter, dan batas generalisasi. Jangan sekadar
    menyetujui asumsi pengguna.
-   Jangan terlalu cepat menyatakan suatu metode, gap, kontribusi, atau
    fitur sebagai final.
-   Pengguna akan mengurus format template kampus; bantuan utama yang
    diharapkan adalah substansi penelitian, alur logika, verifikasi
    sumber, sitasi, konsistensi, dan kelak pengembangan sistem.
-   Pengguna masih membangun kepercayaan diri dalam coding dan analisis
    teknis. Pilih solusi yang dapat dijelaskan dan
    dipertanggungjawabkan, bukan stack atau arsitektur yang kompleks
    hanya agar terlihat canggih.

------------------------------------------------------------------------

## 2. Urutan Prioritas Informasi

Gunakan urutan prioritas berikut ketika ada konflik:

1.  **Keputusan terbaru yang dinyatakan langsung oleh pengguna/dosen**,
    termasuk judul tetap di dokumen ini.
2.  Dokumen handover terbaru dan artefak kerja terbaru.
3.  `THESIS_MASTER_CONTEXT_AND_AGENT_GUIDE.md`.
4.  `THESIS_HANDOVER_2026-10-21.md`.
5.  Dokumen lebih lama seperti `00_Research_Context.docx`.
6.  Inferensi atau pengetahuan umum dari agen.

Dokumen lama dibuat saat judul dan jenis ayam masih belum final. Status
itu sudah berubah. Pertahankan bagian yang masih relevan (misalnya
prinsip research-first, jangan mengarang data, jangan memaksakan ML),
tetapi jangan menerapkan instruksi lama yang secara eksplisit
bertentangan dengan keputusan terbaru.

Jika menemukan konflik: - jangan diam-diam menghapus sejarah; - tandai
keputusan lama sebagai superseded/obsolete; - tuliskan tanggal dan
dampaknya di `decision_log.md`; - jangan membuat pengguna mengulang
keputusan yang sudah jelas.

------------------------------------------------------------------------

## 3. Judul, Fokus, dan Interpretasi yang Harus Dijaga

### 3.1 Judul tetap

> PEMODELAN PREDIKSI JUMLAH AYAM PETELUR UNTUK SMART FARMING BERDASARKAN
> KETERSEDIAAN LAHAN JAGUNG UNTUK MENDUKUNG PERENCANAAN PRODUKSI DI
> KOMUNITAS ASA INDONESIA.

Gunakan judul ini persis ketika diperlukan. Kapitalisasi/format italic
*Smart Farming* dapat mengikuti pedoman kampus, tetapi kata dan objek
penelitian tidak boleh diganti sepihak.

### 3.2 Makna kerja judul

Interpretasi kerja yang paling konsisten: - "Pemodelan prediksi jumlah
ayam petelur" = membuat model untuk **mengestimasi jumlah ayam petelur
yang dapat didukung** oleh ketersediaan jagung dalam periode perencanaan
tertentu. - "Berdasarkan ketersediaan lahan jagung" = estimasi berangkat
dari luas lahan dan estimasi produksi/hasil panen jagung, lalu
dikonversi menjadi jumlah jagung yang tersedia untuk pakan. - "Untuk
mendukung perencanaan produksi" = hasil model memberikan informasi
pendukung keputusan/perencanaan, bukan jaminan kelayakan penuh usaha
peternakan. - "Smart Farming" tidak otomatis berarti IoT, sensor,
perangkat keras, computer vision, atau sistem monitoring real-time. -
Judul memakai kata "prediksi", tetapi metode yang saat ini paling masuk
akal adalah **model matematis/estimasi berbasis parameter**, bukan
otomatis prediksi time series atau machine learning. Hal ini perlu
dipastikan konsisten dengan arahan pembimbing dan definisi operasional
dalam proposal.

### 3.3 Hal yang bukan fokus utama

Jangan mengubah skripsi menjadi: - riset agronomi murni tentang
peningkatan hasil jagung; - formulasi nutrisi lengkap ayam; - prediksi
produksi telur; - prediksi penyakit atau deteksi citra; - penelitian
IoT; - machine learning tanpa justifikasi; - Big Data/Hadoop/Spark; -
optimasi kompleks atau mixed-integer programming tanpa kebutuhan dan
data yang memadai; - analisis kelayakan finansial mendalam kecuali ada
keputusan eksplisit untuk memasukkannya.

------------------------------------------------------------------------

## 4. Konteks Mitra dan Fakta Operasional

### 4.1 Mitra

-   Mitra penelitian: Komunitas ASA Indonesia.
-   Lokasi konteks: Sumenep, Jawa Timur.
-   Konteks yang pernah disampaikan pembimbing: entitas bank sampah yang
    bersinergi dengan kegiatan Smart Farming.
-   Terdapat kegiatan budidaya jagung pada lahan yang tersedia.
-   Jangan mengarang isi profil Google Drive atau kondisi operasional
    yang belum diekstrak/diverifikasi.
-   **Jangan mengasumsikan ASA saat ini sudah memelihara ayam petelur.**
    Keberadaan ayam petelur, rencana memelihara, jumlah target, dan
    status operasionalnya perlu dikonfirmasi. Judul tetap menggunakan
    ayam petelur, tetapi konteks faktual mitra tidak boleh dibuat-buat.

### 4.2 Luas lahan yang diketahui dari konteks pembimbing

-   Ada 3 petak jagung.
-   Masing-masing berukuran 5 m × 6 m = 30 m².
-   Total = 90 m² = 0,009 hektare.
-   Angka ini adalah konteks kerja yang berasal dari arahan sebelumnya;
    konfirmasi detailnya dengan sumber mitra ketika memungkinkan.

### 4.3 Penanaman dan pola panen

-   Pernah dijelaskan bahwa umur/tahap penanaman ketiga petak berbeda
    sekitar satu bulan.
-   Tujuan yang tampaknya diinginkan adalah membuat ketersediaan panen
    bertahap, kemungkinan agar ada hasil panen pada periode bulanan.
-   Namun, tiga petak dengan selisih penanaman satu bulan **tidak
    otomatis** menjamin panen bulanan yang stabil. Perlu memeriksa umur
    panen varietas, tanggal tanam aktual, musim, hasil tiap petak, jeda
    tanam-panen, dan kemungkinan tumpang tindih/jeda.
-   Siklus jagung sekitar tiga bulan/\~90 hari pernah disebut sebagai
    perkiraan, bukan angka universal/final.
-   Jangan menyatakan hasil panen bulanan sebagai fakta tanpa data
    jadwal dan hasil aktual.

### 4.4 Bentuk jagung yang dipakai sebagai pakan

Ada informasi lama bahwa jagung akan dicacah dengan mesin dan menjadi
bagian campuran pakan, bersama dedak dan bahan organik lain; penggunaan
mungkin melibatkan ayam dan ikan lele. Akan tetapi, model terbaru harus
konsisten dengan **jagung sebagai hasil panen yang dihitung**. Jangan
mencampur hasil biji pipilan kering dengan batang/daun/tongkol/biomassa
jagung utuh.

Hal yang harus dipastikan: - Apakah jagung yang menjadi basis model
adalah biji pipilan kering, jagung bertongkol, jagung segar, atau
tanaman jagung utuh? - Jika judul dan literatur yang dipakai membahas
jagung biji sebagai bahan *complete feed*, jangan langsung menerapkan
angka itu pada jagung utuh yang dicacah. - Kadar air/basis bobot harus
dinyatakan. Yield pada kadar air 15% tidak boleh dianggap identik dengan
berat jagung segar atau biomassa hijauan.

### 4.5 Alokasi hasil

-   Ada kemungkinan hasil jagung digunakan untuk lebih dari satu
    kebutuhan, termasuk ayam dan ikan lele, serta dicampur dengan
    dedak/bahan lain.
-   Belum diketahui berapa bagian jagung yang akan dialokasikan khusus
    untuk pakan ayam petelur.
-   Jangan mengasumsikan 100% hasil panen dialokasikan ke ayam kecuali
    sebagai skenario yang secara jelas diberi label.
-   Jangan mengklaim pakan menjadi gratis atau biaya pakan turun dalam
    jumlah tertentu tanpa data biaya dan pembelian aktual.

### 4.6 Angka 200 gram per ayam per hari

-   Dalam diskusi lama, pembimbing pernah menyebut sekitar 200
    g/ayam/hari.
-   Makna dan relevansi angka ini perlu diperlakukan hati-hati. Dokumen
    lama menyebut angka tersebut belum jelas apakah total pakan atau
    jagung, dan juga mencatat kemungkinan interpretasi total ransum.
-   **Jangan pernah menyamakan 200 g total pakan dengan 200 g jagung.**
-   Karena judul sekarang adalah ayam petelur, angka ini harus diperiksa
    kecocokannya dengan fase produksi dan jenis ayam. Jangan langsung
    menggunakan angka tersebut sebagai parameter final.

------------------------------------------------------------------------

## 5. Status Penelitian dan Artefak

### 5.1 Yang sudah dilakukan

1.  Eksplorasi dataset proxy pertanian.
2.  Notebook 1 --- Data Understanding: selesai.
3.  Notebook 2 --- Data Quality & EDA: selesai.
4.  Notebook 3 --- Candidate Research Problems: selesai.
5.  Pemetaan literatur awal dan research opportunity mapping: telah
    dilakukan.
6.  Pengumpulan sumber tentang produktivitas jagung, umur panen, dan
    komposisi pakan ayam.
7.  Draft awal Bab I telah dibuat.
8.  Judul skripsi ditetapkan pembimbing seperti tercantum di atas.
9.  Sudah ada gagasan awal rumus matematis untuk menghubungkan hasil
    jagung dan kebutuhan jagung untuk pakan ayam petelur.

### 5.2 Dataset proxy lama

-   Sekitar 111 observasi dan 22 kolom.
-   Memuat variabel pertanian seperti `total_days`, `yield`, soil
    moisture, irrigation type, NDVI, disease status, dan informasi
    tanam/panen.
-   Dataset itu hanya untuk eksplorasi awal, bukan data ASA.
-   Dilarang menulis bahwa kondisi lahan, produktivitas, penyakit,
    irigasi, atau proses mitra ASA terbukti dari dataset proxy.
-   Jangan mengulang Notebook 1--3 tanpa alasan yang spesifik.

### 5.3 Bab I saat ini

Draft Bab I tersedia sebagai file `Bab I.pdf` (versi yang ditemukan di
Library, dibuat 27 Oktober 2026). Isi substansinya mencakup: - latar
belakang tentang hubungan hasil jagung dan pakan ayam petelur; -
Gunjević et al. (2023) sebagai contoh complete feed dengan 60% jagung
dan konsumsi pakan layer sekitar 119,7--123,1 g/ekor/hari; - Handayati
et al. (2022) untuk variasi hasil jagung di Madura; - Amzeri et
al. (2023) sebagai referensi lokasi Lenteng, Sumenep; - Sinaga et
al. (2026) sebagai contoh pemodelan matematis untuk perencanaan pada
sistem pertanian terpadu; - rumusan masalah tentang model prediksi
jumlah ayam petelur; - batasan masalah yang memfokuskan model pada
ketersediaan jagung dan kebutuhan jagung untuk pakan; - tujuan dan
manfaat penelitian.

Bab I adalah draft awal untuk dibawa ke bimbingan. Belum boleh dianggap
tervalidasi sepenuhnya. Gap penelitian dan kebutuhan nyata mitra masih
harus ditopang oleh telaah yang lebih lengkap dan/atau klarifikasi
mitra.

### 5.4 Kesalahan format yang terlihat di PDF Bab I

Ini adalah isu administratif/format yang pengguna berencana tangani
sendiri: - halaman awal masih tertulis Program Studi Teknik Informatika;
program yang benar adalah Sarjana Terapan Sistem Informasi Bisnis; -
tanggal pengesahan tertulis 20 Juni 2015, jelas placeholder/stale dan
harus disesuaikan; - beberapa nomor daftar isi/heading terlihat tidak
konsisten/berulang; - nama penguji/pejabat dan contoh tabel/gambar masih
berupa placeholder. Agen boleh mengingatkan bila diminta memeriksa
dokumen, tetapi jangan mengalihkan fokus substansi tanpa kebutuhan.

------------------------------------------------------------------------

## 6. Model Analitis: Konsep Awal, Bukan Rumus Final

### 6.1 Alur konseptual

``` text
Luas lahan dan produktivitas jagung
                ↓
Estimasi hasil panen jagung
                ↓
Penyesuaian hasil yang layak pakai / kehilangan
                ↓
Bagian jagung yang dialokasikan untuk pakan layer
                ↓
Kebutuhan jagung per ekor per hari
                ↓
Kebutuhan jagung per ekor untuk periode perencanaan
                ↓
Estimasi jumlah ayam petelur yang didukung
```

### 6.2 Rumus kandidat

Rumus berikut adalah *candidate model* untuk dibahas dan diuji, bukan
keputusan final:

**A. Estimasi hasil panen** \[ H = A `\times `{=tex}Y \]

-   (H): estimasi hasil jagung (kg).
-   (A): luas lahan (ha).
-   (Y): produktivitas (kg/ha) pada basis hasil dan kadar air yang sama.

Jika menggunakan luas dalam m²: \[ H =
`\frac{A_{m^2}}{10{,}000}`{=tex}`\times `{=tex}Y\_{kg/ha} \]

Dengan total 90 m², area adalah 0,009 ha. Jangan salah konversi.

**B. Jagung layak pakai dan dialokasikan** \[ J = H `\times `{=tex}(1-r)
`\times `{=tex}a \]

-   (J): jagung yang benar-benar tersedia untuk pakan layer (kg).
-   (r): fraksi kehilangan/tidak layak pakai, jika ada data atau
    parameter yang dapat dipertanggungjawabkan.
-   (a): fraksi hasil layak pakai yang dialokasikan untuk layer (0--1).
-   Jika kehilangan tidak dimodelkan, jelaskan alasan dan perlakukan
    sebagai keterbatasan; jangan diam-diam menganggap kehilangan nol.
-   Jika semua jagung belum tentu untuk layer, jangan menganggap (a=1)
    sebagai fakta.

**C. Kebutuhan jagung per ekor selama periode** \[ K = F
`\times `{=tex}q `\times `{=tex}T \]

Dengan unit konsisten: - (F): total complete-feed intake per ekor per
hari (kg/ekor/hari). - (q): proporsi jagung dalam ransum lengkap
(fraksi, bukan persen bulat; misalnya 60% = 0,60). - (T): periode
perencanaan (hari). - (K): kebutuhan jagung per ekor untuk periode itu
(kg/ekor/periode).

Bentuk gram juga boleh dipakai, tetapi semua unit harus konsisten. Jika
(F) dinyatakan dalam gram, konversikan kebutuhan ke kg sebelum
membandingkan dengan hasil panen dalam kg.

**D. Estimasi jumlah ayam yang dapat didukung** \[ N =
`\left`{=tex}`\lfloor `{=tex}`\frac{J}{K}`{=tex}
`\right`{=tex}`\rfloor`{=tex} \]

-   (N): jumlah maksimum teoritis ayam petelur yang dapat didukung oleh
    jagung tersedia selama periode (T), berdasarkan parameter yang
    digunakan.
-   Pembulatan ke bawah digunakan karena hasil jumlah ayam harus berupa
    bilangan bulat.
-   Rumus ini hanya menilai kapasitas berdasarkan komponen jagung, bukan
    kelayakan penuh pemeliharaan ayam. Ayam masih membutuhkan bahan
    pakan lain, air, kandang, manajemen, kesehatan, dan nutrisi
    seimbang.

### 6.3 Contoh hitung ilustratif yang sudah pernah dibahas

Sebuah simulasi pernah memakai: - luas 90 m²; - produktivitas ilustratif
5.000 kg/ha; - total pakan 120 g/ekor/hari; - proporsi jagung 60%; -
alokasi jagung untuk ayam 100%; - periode 30 hari; - kehilangan panen
belum dimasukkan.

Hitungan yang benar: - Hasil kotor = 90/10.000 × 5.000 = **45 kg**,
bukan 4,5 kg. - Jagung tersedia = 45 kg jika diasumsikan alokasi 100%
dan kehilangan 0%. - Kebutuhan jagung per ekor per hari = 120 g × 0,60 =
72 g/hari. - Kebutuhan per ekor untuk 30 hari = 72 × 30 = 2.160 g =
**2,16 kg**. - Kapasitas teoritis = floor(45 / 2,16) = **20 ekor**.

PENTING: narasi awal pada simulasi sebelumnya keliru menuliskan hasil
panen 4,5 kg dan kapasitas 2 ekor. Kesalahan aritmetika tersebut sudah
dikoreksi di sini. Jangan mengulang angka keliru itu. Semua angka contoh
tetap **ilustrasi semata**, bukan data aktual ASA atau rekomendasi
parameter final. Produktivitas 5 t/ha, konsumsi pakan 120 g/hari,
proporsi jagung 60%, alokasi 100%, dan kehilangan 0% tidak boleh
dijadikan nilai final tanpa audit sumber dan validasi.

### 6.4 Hal yang perlu dimodelkan dengan hati-hati

-   Yield harus sesuai bentuk hasil dan basis kadar air.
-   Jika sumber memberikan hasil pada kadar air 15%, jangan
    menggunakannya sebagai berat jagung segar tanpa konversi.
-   Produktivitas percobaan varietas hibrida berdaya hasil tinggi bukan
    baseline otomatis untuk lahan kecil ASA.
-   Hasil satu panen berbeda dengan hasil per bulan. Bila panen tidak
    terjadi setiap bulan, model tidak boleh membagi hasil panen dengan 3
    secara otomatis tanpa dasar.
-   Kebutuhan jagung untuk layer bukan seluruh kebutuhan ransum.
-   Persentase jagung harus cocok dengan complete feed dan fase layer
    yang sesuai.
-   Data dari luar negeri bisa menjadi nilai awal/skenario, tetapi
    keterbatasan generalisasi ke Sumenep harus ditulis.
-   Jangan memakai parameter dari fase pullet/grower untuk ayam layer
    produksi tanpa penjelasan.
-   Jika parameter tidak tersedia, tandai `ASSUMPTION`/`SCENARIO`,
    cantumkan sumber, dan lakukan analisis sensitivitas bila relevan.

------------------------------------------------------------------------

## 7. Literatur yang Sudah Diprioritaskan

**Catatan:** Rincian di bawah adalah ringkasan dari sumber/ekstraksi
yang sudah dikerjakan. Sebelum mengutip angka dalam naskah final,
periksa lagi artikel asli, tabel yang tepat, satuan, basis kadar air,
dan konteks eksperimen. Jangan menganggap semua hasil ekstraksi otomatis
final.

### 7.1 Gunjević et al. (2023) --- layer feed composition

**Judul:** "Effect of Maize Hybrid in Complete Feed on the Production
Performance and Economic Considerations in Laying Hens."\
**Jurnal:** *Sustainability*, 15, 15748.\
**DOI:** 10.3390/su152215748.

Temuan yang telah diekstrak: - Tabel 2 mencantumkan jagung/maize 600
g/kg = 60% dari complete feed. - Studi menggunakan Lohmann Brown pada
fase awal bertelur di Kroasia. - Konsumsi complete feed yang dilaporkan:
sekitar 119,7--123,1 g/ekor/hari. - Jika 60% dikalikan dengan konsumsi
pakan tersebut, estimasi konsumsi jagung sekitar 71,82--73,86
g/ekor/hari; ini hasil hitung turunan untuk kondisi studi itu, bukan
standar universal. - Komposisi bahan yang pernah diekstrak: corn 60%,
soybean meal 26,2%, sunflower oil 3%, calcium carbonate 8,8%,
monocalcium phosphate 1,2%, salt 0,4%, DL-methionine 0,15%, vitamin
premix 0,12%, TRT Poultry Pack 0,13%. Total 100%. - Bedakan komposisi
bahan ransum dengan komposisi nutrisi. Jangan menyebut 60% sebagai
persentase vitamin atau kebutuhan universal semua layer.

Keterbatasan: - Studi luar negeri dan kondisi/strain/fase tertentu. -
Tidak menjadi bukti langsung kondisi pakan di ASA. - Perlu memeriksa
apakah model penelitian memakai jagung sebagai bagian ransum lengkap
yang memang disusun seimbang.

### 7.2 Handayati et al. (2022) --- hasil jagung di Madura

**Judul:** "Increasing maize yield and farming benefit through
integrated plant management in Madura Island East Java."\
**Jurnal:** *IOP Conference Series: Earth and Environmental Science*,
980, 012052.\
**DOI:** 10.1088/1755-1315/980/1/012052.

Temuan yang diekstrak: - Konteks Pamekasan/Madura. - Hasil yang
dilaporkan: 1,22 t/ha pada praktik lokal, 4,70 t/ha pada IPM2, dan 6,35
t/ha pada IPM1. - Perbedaan terkait paket pengelolaan tanaman terpadu;
jangan mengatribusikan perubahan hasil ke satu faktor saja. - Untuk 90
m², konversi aritmetika bersyarat adalah 10,98 kg, 42,30 kg, dan 57,15
kg. Ini bukan hasil aktual ASA. - Basis kadar air dan protokol
penimbangan harus diverifikasi sebelum digunakan.

### 7.3 Amzeri et al. (2023) --- relevansi geografis Sumenep

**Judul:** "Genotype by Environment Interaction on Early-Maturing and
High-Yield Maize Hybrids."\
**DOI:** 10.28991/HEF-2023-04-01-05.\
**Jurnal:** *Journal of Human, Earth, and Future*, 4(1).

Temuan yang diekstrak: - Uji multi-lokasi dan multi-lingkungan di Pulau
Jawa, termasuk Lenteng, Sumenep. - Untuk genotipe G4 di Lenteng, hasil
sekitar 9,30 t/ha pada musim kemarau dan 8,92 t/ha pada musim hujan. -
Rerata lintas lingkungan yang pernah diekstrak sekitar 8,71 t/ha; umur
panen rata-rata sekitar 91,93 hari. - Hasil Lenteng relevan secara
geografis, tetapi berasal dari uji genotipe/hibrida dan tidak otomatis
merepresentasikan produktivitas petak ASA. - Untuk 90 m², 8,92--9,30
t/ha setara aritmetika dengan 80,28--83,70 kg pada basis hasil studi.
Ini hanya konversi, bukan prediksi aktual ASA.

### 7.4 Sinaga, Habibi, & Panggabean (2026) --- pembanding pemodelan

**Judul:** "Optimization of operational cost planning in integrated
farming systems using a mixed-integer linear programming approach."\
**Jurnal:** *AXIOM: Jurnal Pendidikan dan Matematika*, 15(1), 42--56.\
**DOI:** 10.30821/axiom.v15i1.26491.

Relevansi: - Contoh penerapan model matematis untuk perencanaan sumber
daya/biaya pada sistem pertanian terpadu. - Bukan model langsung untuk
menghitung jumlah ayam petelur dari hasil jagung. - Terdapat
inkonsistensi parameter pakan unggas dalam artikel (catatan lama: tabel
menyebut 65 kg/pen, hasil menyebut 65 kg/head); jangan gunakan angka
pakan itu sebagai parameter penelitian ini.

### 7.5 Sumber pendukung lain

-   Wicaksana et al. (2022), "Selection of High Yield and Stable Maize
    Hybrids in Mega-Environments of Java Island, Indonesia," *Agronomy*,
    DOI 10.3390/agronomy12122923. Studi multi-lokasi di Jawa, panen
    sekitar 93 hari; cek basis yield sebelum digunakan.
-   Aristya & Samijan (2022), "The Yield Gap Maize under Intensive
    Cropping System in Central Java," DOI 10.18196/pt.v10i1.8789. Hasil
    aktual petani yang pernah diekstrak sekitar 5,57 t/ha; bedakan hasil
    aktual petani dengan nilai potensial/model.
-   Hy-Line Brown Management Guide: ringkasan konsumsi layer selama
    produksi sekitar 109,1--116,9 g complete feed/ekor/hari pada minggu
    19--100. Ini pedoman performa breed, bukan data lokal ASA dan bukan
    konsumsi jagung murni.

### 7.6 Paper layer lain dari Consensus --- belum final untuk parameter

Ringkasan Consensus yang pernah dikumpulkan mencantumkan: - van Eck et
al. (online 2025/issue 2026), DOI 10.1016/j.psj.2025.106174, persentase
jagung berbeda menurut umur/fase; - Oluwabiyi et al. (2022), Hy-Line
Brown grower/prelay; - Novela et al. (2023), kontrol dengan 60% yellow
maize dan perlakuan penggantian sebagian maize dengan wheat bran.

Angka-angka tersebut belum boleh langsung dipakai tanpa menelusuri
artikel asli, tabel, fase ayam, unit, dan basis as-fed/dry matter.

### 7.7 Paper broiler lama

Dokumen handover 21 Oktober mengandung matriks broiler karena jenis ayam
ketika itu masih belum final. Paper broiler tidak menjadi dasar
parameter utama setelah judul ditetapkan sebagai ayam petelur. Simpan
hanya sebagai sejarah/backup bila diperlukan untuk menjelaskan evolusi
keputusan, bukan untuk mengalihkan kembali fokus ke broiler.

### 7.8 Gap penelitian

Jangan menyimpulkan gap final hanya dari empat paper di atas. Untuk
menyatakan gap, bandingkan secara sistematis: - tujuan penelitian; -
variabel input; - objek dan konteks; - metode/model; - output; - cara
validasi; - keterbatasan; - apakah penelitian sebelumnya benar-benar
menghubungkan estimasi ketersediaan hasil jagung dari lahan dengan
kebutuhan jagung layer untuk mengestimasi kapasitas ayam dalam periode
perencanaan; - apakah ada studi serupa pada sistem informasi pertanian
kecil/integrated farming. Jangan mengklaim "belum pernah ada penelitian"
kecuali pencarian cukup komprehensif dan klaim dibatasi secara tepat.

------------------------------------------------------------------------

## 8. Status Bab I dan Pekerjaan Akademik Berikutnya

### 8.1 Rumusan masalah pada draft saat ini

Draft menggunakan rumusan masalah tunggal yang pada intinya menanyakan
bagaimana model prediksi jumlah ayam petelur dapat dirancang berdasarkan
estimasi ketersediaan jagung dari lahan untuk mendukung perencanaan
produksi di Komunitas ASA Indonesia.

Tujuan draft: menyusun/mengembangkan model matematis untuk mengestimasi
jumlah ayam petelur yang dapat didukung oleh ketersediaan jagung pada
periode perencanaan tertentu.

Jaga konsistensi antara: - judul; - latar belakang; - rumusan masalah; -
batasan masalah; - tujuan; - metode; - hasil yang nanti dihasilkan; -
pengujian/evaluasi.

### 8.2 Klaim yang masih perlu diperkuat

-   Kebutuhan informasi nyata di ASA dan konteks operasional ayam
    petelur.
-   Apakah ayam petelur sudah ada atau direncanakan.
-   Bentuk jagung yang benar-benar digunakan untuk pakan.
-   Dasar penentuan produktivitas jagung dan periode perencanaan.
-   Dasar pemilihan parameter konsumsi pakan layer dan persentase
    jagung.
-   Research gap yang spesifik berdasarkan literature matrix.
-   Bagaimana model akan diuji/diuji kewajarannya jika data aktual mitra
    terbatas.
-   Arti operasional "prediksi" agar tidak disalahpahami sebagai model
    statistik/time series yang tidak sesuai dengan metode.

### 8.3 Etika dan kualitas akademik

-   Selalu periksa artikel asli sebelum mengutip detail angka.
-   Jangan menciptakan referensi, DOI, kutipan, halaman, atau hasil.
-   Jangan menganggap paraphrase otomatis membuat teks bebas dari
    masalah orisinalitas.
-   Bantuan AI harus mengikuti kebijakan kampus/pembimbing. Pengguna
    perlu memahami dan mampu menjelaskan seluruh klaim dan model yang
    diajukan.
-   Gunakan sitasi yang konsisten sesuai gaya kampus.
-   Jangan menyatakan hasil/keberhasilan sistem sebelum implementasi dan
    evaluasi dilakukan.

------------------------------------------------------------------------

## 9. Rencana Kerja Model yang Disarankan

### Tahap 1 --- Audit bukti dan parameter

Buat `evidence_parameter_matrix.md` atau spreadsheet dengan kolom
minimal: - ID; - sitasi lengkap; - DOI/URL; - objek/strain/fase; -
lokasi dan kondisi; - variabel/parameter yang diambil; - nilai dan
satuan; - tabel/halaman asli; - metode atau rancangan studi; - basis
bobot/kadar air; - apakah hasil eksperimen, nilai pedoman, hasil hitung
turunan, atau asumsi; - keterbatasan; - relevansi terhadap model layer
di Sumenep; - status verifikasi (`VERIFIED`, `PARTIALLY VERIFIED`,
`UNVERIFIED`, `EXCLUDE`); - keputusan penggunaan dan alasan.

Jangan memperluas pencarian secara acak. Cari tambahan hanya jika ada
pertanyaan parameter atau gap yang jelas belum terjawab.

### Tahap 2 --- Definisikan basis hasil jagung

Tetapkan bersama pembimbing/mitra apakah hasil yang dimodelkan adalah: -
biji pipilan kering; - biji pada kadar air tertentu; - jagung tongkol; -
atau biomassa tanaman utuh.

Model yield dan feed composition harus cocok dengan bentuk yang dipilih.
Jika sumber yield memakai kadar air 15%, pertahankan basis itu atau
lakukan konversi yang eksplisit dan dapat dipertanggungjawabkan.

### Tahap 3 --- Tentukan periode dan pola ketersediaan

Bedakan: - hasil per petak per panen; - hasil total satu siklus; - hasil
yang tersedia pada satu bulan kalender; - hasil yang dapat disimpan dan
digunakan lintas bulan.

Jangan membagi hasil tiga petak dengan jumlah bulan atau menyatakan
panen bulanan tanpa dasar agronomi/operasional. Jika penanaman bertahap
memang relevan, gunakan tanggal tanam, umur panen, dan jadwal yang
didukung bukti.

### Tahap 4 --- Kebutuhan jagung layer

-   Gunakan sumber yang benar-benar membahas ayam petelur pada fase
    relevan.
-   Bedakan total konsumsi complete feed dengan fraksi jagung dalam
    ransum.
-   Jika sumber melaporkan total feed intake dan komposisi diet yang
    sama, hitung konsumsi jagung turunan secara transparan.
-   Jangan merata-ratakan persentase jagung dari studi berbeda secara
    sembarangan.
-   Jangan menggunakan angka 200 g/hari tanpa klarifikasi dan
    justifikasi.
-   Catat keterbatasan generalisasi dari strain/negara/fase studi.

### Tahap 5 --- Uji model secara manual

Sebelum kode: - buat contoh input kecil yang dapat dihitung manual; -
cek konversi m²↔ha, g↔kg, hari↔periode; - cek pembulatan ke bawah; - uji
kondisi nol dan input tidak valid; - cek skenario alokasi 0% dan 100%; -
uji sensitivitas hasil terhadap yield, fraksi alokasi, proporsi jagung,
dan periode; - verifikasi hasil kode terhadap hasil hitung manual.

### Tahap 6 --- Tentukan cara evaluasi

Jangan memutuskan metode evaluasi hanya karena umum digunakan. Pilih
sesuai model dan data: - verifikasi perhitungan dengan kasus uji
manual; - validasi parameter dengan ahli/mitra atau sumber; -
perbandingan skenario; - pengujian fungsional sistem; - usability
evaluation jika memang sesuai dengan pertanyaan penelitian dan tersedia
responden. Jangan mengklaim akurasi prediksi statistik bila tidak ada
data observasi pembanding yang memadai.

------------------------------------------------------------------------

## 10. Dari Model ke Sistem Informasi

Sistem harus muncul dari kebutuhan informasi dan model, bukan
sebaliknya.

### 10.1 Kandidat input (belum otomatis menjadi form sistem)

-   luas lahan/petak;
-   produktivitas atau hasil panen dan basisnya;
-   periode perencanaan;
-   kehilangan/proporsi hasil layak pakai jika datanya tersedia;
-   persentase hasil yang dialokasikan untuk layer;
-   total feed intake per layer per hari;
-   proporsi jagung dalam complete feed;
-   tanggal tanam/panen jika dibutuhkan oleh model ketersediaan per
    periode;
-   sumber parameter dan status verifikasinya.

### 10.2 Kandidat proses

-   konversi satuan;
-   estimasi hasil panen;
-   penyesuaian hasil layak pakai;
-   perhitungan alokasi jagung;
-   perhitungan kebutuhan jagung layer;
-   perhitungan kapasitas ayam;
-   skenario rendah/sedang/tinggi jika ketidakpastian memang perlu
    ditampilkan.

### 10.3 Kandidat output

-   estimasi hasil jagung dalam periode;
-   jumlah jagung yang tersedia untuk pakan layer;
-   kebutuhan jagung per ekor;
-   estimasi jumlah ayam yang didukung;
-   asumsi/parameter yang dipakai;
-   penjelasan batasan dan sumber parameter;
-   indikator surplus/defisit hanya jika input target jumlah ayam
    tersedia dan kebutuhan tersebut tervalidasi.

### 10.4 Fitur yang tidak boleh otomatis dibuat

Jangan otomatis membangun: - login/role management; - CRUD kompleks
untuk seluruh aktivitas farm; - sensor/IoT; - dashboard berlebihan; -
sistem inventori penuh; - modul biaya; - rekomendasi AI; - modul ikan
lele; - prediksi produksi telur; - fitur laporan/export yang tidak
diminta; - sistem manajemen pertanian lengkap.

Setiap fitur harus ditelusuri ke kebutuhan mitra, tujuan penelitian,
atau kebutuhan uji/evaluasi.

### 10.5 Teknologi

Belum ada stack final. Jangan langsung mengasumsikan React/Next/Vue,
Laravel/Django/FastAPI/Node, PostgreSQL/MySQL/Firebase/Supabase, atau
teknologi lain. Rekomendasikan stack setelah kebutuhan sistem dan
kompetensi pengembang dinilai. Utamakan implementasi yang minimal, mudah
diuji, dapat dijelaskan, dan realistis untuk skripsi.

### 10.6 Prinsip development

1.  Research first.
2.  No assumption leakage: asumsi tidak boleh diam-diam menjadi fakta,
    rumus final, constraint database, label UI, atau klaim Bab I.
3.  Traceability: setiap fitur dan aturan hitung memiliki alasan dan
    sumber.
4.  Minimal sufficient system: bangun sistem terkecil yang cukup untuk
    menjawab rumusan masalah.
5.  Pisahkan model penelitian dari implementasi software.
6.  Jangan mengklaim penghematan biaya, peningkatan efisiensi,
    keberhasilan adopsi, atau validitas tinggi sebelum diuji.

------------------------------------------------------------------------

## 11. Status Tag yang Wajib Dipakai

Gunakan tag yang eksplisit pada catatan kerja dan decision log:

-   `FACT — SUPERVISOR/USER`: informasi yang dinyatakan langsung oleh
    pengguna atau pembimbing.
-   `FACT — SOURCE`: informasi yang benar-benar tercantum pada sumber
    asli yang sudah diperiksa.
-   `CALCULATED`: hasil perhitungan dari input yang jelas.
-   `LITERATURE-BASED PARAMETER`: nilai dari paper/pedoman, bukan data
    ASA.
-   `ASSUMPTION`: asumsi sementara untuk membuat model berjalan.
-   `SCENARIO`: nilai alternatif untuk analisis sensitivitas, bukan
    klaim tentang keadaan nyata.
-   `INFERENCE`: interpretasi yang masuk akal tetapi belum divalidasi.
-   `HYPOTHESIS`: dugaan yang perlu diuji.
-   `UNKNOWN / OPEN`: informasi yang belum diketahui.
-   `DECISION — SUPERVISOR`: keputusan yang diberikan pembimbing.
-   `DECISION — RESEARCHER`: keputusan metodologis yang diambil peneliti
    setelah pertimbangan dan bukti.
-   `OBSOLETE / SUPERSEDED`: informasi lama yang telah digantikan
    keputusan lebih baru.

Jangan menyamarkan asumsi sebagai fakta lewat gaya penulisan yang tegas.

------------------------------------------------------------------------

## 12. Artefak yang Disarankan untuk Dikelola Antigravity

Simpan artefak terpisah, bukan satu file campur aduk:

1.  `THESIS_CONTEXT_ANTIGRAVITY.md` --- dokumen konteks ini.
2.  `decision_log.md` --- keputusan, tanggal, sumber/validasi, dampak.
3.  `open_questions.md` --- hal yang belum dikonfirmasi ke
    pembimbing/mitra.
4.  `evidence_parameter_matrix.md` --- matriks sumber dan parameter.
5.  `literature_matrix.md` --- matriks literatur per
    tujuan/metode/variabel/output/keterbatasan.
6.  `research_gap.md` --- gap kandidat beserta bukti, belum dikunci
    sebelum review memadai.
7.  `research_method.md` --- model dan metode setelah
    parameter/pertanyaan jelas.
8.  `system_requirements.md` --- kebutuhan fungsional/nonfungsional
    tervalidasi.
9.  `calculation_specification.md` --- definisi variabel, unit, formula,
    asumsi, contoh hitung.
10. `test_plan.md` --- kasus uji perhitungan dan fungsional.
11. `architecture.md` --- hanya setelah kebutuhan stabil.
12. `database_design.md` --- hanya jika persistensi data memang
    dibutuhkan.
13. `ui_ux_spec.md` --- layar dan alur berdasarkan tugas pengguna.
14. `implementation_plan.md` --- rencana kerja realistis.
15. `Bab_I_draft.md` --- substansi Bab I yang ditinjau dan direvisi.
16. `references.bib` atau daftar pustaka terstruktur jika dibutuhkan.

Jangan membuat semua artefak itu sekaligus jika belum diperlukan. Mulai
dari yang paling mendesak.

### Format decision log

``` text
Decision ID:
Date:
Topic:
Decision:
Status: FIXED / PROVISIONAL / OPEN / SUPERSEDED
Evidence/source:
Who validated it:
Previous state/assumption:
Impact on research:
Impact on model:
Impact on system:
Affected artifacts:
Next action:
```

------------------------------------------------------------------------

## 13. Risiko Utama yang Harus Dijaga

1.  **Ketidaksesuaian bentuk jagung:** hasil biji pipilan vs biomassa
    tanaman utuh.
2.  **Yield terlalu optimistis:** hasil uji hibrida di Lenteng bukan
    hasil pasti lahan ASA.
3.  **Periode ketersediaan salah:** satu hasil panen tidak sama dengan
    hasil yang tersedia setiap bulan.
4.  **Pakan tercampur konsep:** total complete feed bukan jagung murni.
5.  **Parameter layer tidak cocok fase:** data pullet/grower tidak
    otomatis cocok untuk layer yang sedang bertelur.
6.  **Alokasi sumber daya:** jagung mungkin dipakai untuk kebutuhan
    lain.
7.  **Konteks ayam petelur di mitra belum dikonfirmasi:** jangan menulis
    bahwa ASA sudah beternak layer sebagai fakta.
8.  **Gap terlalu dini:** beberapa sumber belum cukup untuk klaim
    novelty kuat.
9.  **Kata "prediksi" vs model deterministik:** definisikan secara
    metodologis, jangan memaksakan ML.
10. **Sistem dibuat terlalu dini:** jangan coding sebelum spesifikasi
    model/input/output cukup stabil.
11. **Klaim manfaat berlebihan:** jangan klaim penghematan, efisiensi,
    atau keberhasilan tanpa evaluasi.
12. **Kesalahan aritmetika:** verifikasi rumus dan konversi satuan
    manual sebelum implementasi.

------------------------------------------------------------------------

## 14. Langkah Kerja Berikutnya yang Paling Tepat

Jangan mulai dengan menulis ulang semua konteks atau membangun aplikasi
dari nol. Lanjutkan dari status terakhir dengan urutan berikut:

### Prioritas 1 --- Kunci catatan keputusan terbaru

Buat entri decision log bahwa judul ayam petelur telah ditetapkan
pembimbing dan menggantikan status lama yang menyebut broiler/layer
belum final. Catat bahwa judul tidak boleh diganti sepihak.

### Prioritas 2 --- Audit Bab I dan daftar pustaka

Periksa klaim dalam draft Bab I terhadap artikel asli: - Gunjević et
al. (2023): persentase maize, konsumsi complete feed, strain/fase,
formula bahan ransum; - Handayati et al. (2022): yield, lokasi,
perlakuan, basis bobot/kadar air; - Amzeri et al. (2023): angka
Lenteng/Sumenep, genotipe, musim, basis kadar air, umur panen; - Sinaga
et al. (2026): relevansi sebagai pembanding model dan keterbatasannya.
Periksa metadata, DOI, dan format sitasi. Jangan menganggap semua detail
draft sudah benar hanya karena pernah disalin.

### Prioritas 3 --- Buat matriks parameter layer + yield jagung

Tandai setiap nilai `VERIFIED`, `PARTIALLY VERIFIED`, atau `UNVERIFIED`.
Jangan melakukan rata-rata antar-paper tanpa alasan. Jangan memakai
angka final sebelum fase, unit, dan basisnya cocok.

### Prioritas 4 --- Susun spesifikasi model matematis

Tulis: - definisi variabel; - unit; - sumber setiap parameter; -
rumus; - asumsi; - contoh hitung manual; - batas model; - skenario dan
sensitivitas jika relevan. Model harus menghasilkan estimasi jumlah ayam
petelur yang didukung oleh jagung pada periode tertentu, bukan klaim
kapasitas pemeliharaan total.

### Prioritas 5 --- Identifikasi data mitra yang masih kritis

Siapkan pertanyaan non-leading untuk bimbingan/mitra: - Apakah ayam
petelur sudah dipelihara atau baru rencana? - Bentuk jagung yang
digunakan untuk pakan apa? - Apa dasar angka kebutuhan pakan yang pernah
disebut? - Apakah angka tersebut total ransum atau bagian jagung? - Apa
komposisi pakan layer yang dipakai/direncanakan? - Berapa hasil aktual
per petak, jika ada? - Apakah tiga petak memang dijadwalkan panen
bertahap tiap bulan? - Berapa bagian jagung yang dialokasikan ke ayam
dibanding kebutuhan lain? - Periode keputusan apa yang ingin dibantu:
satu bulan, satu siklus panen, atau periode lain? Jangan membuat asumsi
jawaban.

### Prioritas 6 --- Baru turunkan kebutuhan sistem

Setelah model dan kebutuhan informasi lebih jelas, tetapkan input,
proses, output, kriteria penerimaan, pengujian, dan kebutuhan pengguna.
Setelah itu baru rancang dan implementasikan sistem.

------------------------------------------------------------------------

## 15. Instruksi Kerja untuk Antigravity

Saat mulai bekerja, lakukan hal berikut:

1.  Baca dokumen ini dan dokumen lama yang relevan.
2.  Tampilkan ringkasan pemahaman singkat yang membedakan keputusan
    fixed, fakta yang diketahui, asumsi, dan open questions.
3.  Akui bahwa judul ayam petelur sudah fixed; jangan mengusulkan
    menggantinya.
4.  Jangan mulai coding atau memilih stack dulu.
5.  Identifikasi artefak yang sudah ada di workspace dan jangan menimpa
    file tanpa memeriksa isinya.
6.  Lanjutkan dari matriks bukti/parameter dan Bab I yang telah ada;
    jangan mengulang eksplorasi dataset lama.
7.  Jika membuat/mengubah file, jelaskan file apa yang berubah dan
    mengapa.
8.  Setiap kali parameter atau keputusan berubah, perbarui
    `decision_log.md` dan artefak terdampak.
9.  Jika bukti tidak cukup, katakan tidak cukup dan berikan langkah
    verifikasi paling kecil yang dibutuhkan.
10. Jangan mengarang fakta, sitasi, DOI, data mitra, hasil model, atau
    keberhasilan sistem.

### Prompt awal yang dapat dipakai pengguna di Antigravity

> Baca `THESIS_CONTEXT_ANTIGRAVITY.md` secara menyeluruh sebelum
> mengerjakan apa pun. Judul skripsi sudah ditetapkan pembimbing dan
> tidak boleh diubah sepihak: **"PEMODELAN PREDIKSI JUMLAH AYAM PETELUR
> UNTUK SMART FARMING BERDASARKAN KETERSEDIAAN LAHAN JAGUNG UNTUK
> MENDUKUNG PERENCANAAN PRODUKSI DI KOMUNITAS ASA INDONESIA."**
>
> Pertama, periksa file yang sudah ada di workspace dan jangan menimpa
> apa pun. Lalu buat ringkasan konteks dalam empat kategori: (1)
> keputusan fixed, (2) fakta yang sudah diketahui, (3) asumsi/parameter
> sementara, dan (4) pertanyaan yang masih terbuka. Setelah itu usulkan
> langkah lanjutan paling kecil yang bernilai tinggi. Prioritaskan audit
> Bab I dan matriks bukti/parameter layer serta yield jagung. Jangan
> mulai coding, jangan memilih stack, jangan mengganti judul/objek ayam,
> jangan mengarang data ASA, dan jangan mengulang pencarian luas yang
> sudah selesai. Pisahkan sumber asli, hasil hitung, asumsi, dan
> inferensi.

------------------------------------------------------------------------

## 16. Catatan Penutup

Dokumen master lama tetap berguna untuk prinsip research-first,
pemisahan fakta dan asumsi, pemetaan literatur, serta kehati-hatian
desain sistem. Namun, keputusan terbaru bahwa **judul dan objek ayam
petelur sudah fixed** harus mengalahkan status lama yang masih membuka
pilihan broiler/layer atau judul. Fokus Antigravity adalah membantu
membawa penelitian yang sudah berjalan menuju model yang dapat
dipertanggungjawabkan dan sistem yang sesuai kebutuhan---bukan memulai
ulang, memperluas scope tanpa alasan, atau membuat teknologi lebih
kompleks dari kebutuhan skripsi.
