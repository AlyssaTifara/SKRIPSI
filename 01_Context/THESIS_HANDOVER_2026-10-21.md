# THESIS HANDOVER — MASTER CONTEXT UPDATE
**Tanggal pembaruan:** 21 Oktober 2026  
**Tujuan:** Dokumen transfer agar chat baru dapat melanjutkan penelitian tanpa mengulang dari awal atau mengubah keputusan yang belum final.

## 1. Instruksi untuk chat baru
Baca dokumen ini sebagai konteks terbaru bersama `THESIS_MASTER_CONTEXT_AND_AGENT_GUIDE.md` dan `00_Research_Context.docx` (yang lebih lama/outdated dan tidak boleh dianggap lebih baru daripada keputusan di handover ini). Lanjutkan dari status terakhir; jangan mengulang pencarian luas yang sudah selesai, jangan mengarang data mitra, dan jangan mengunci judul/metode/teknologi sebelum argumen penelitian cukup kuat.

Bimbing pengguna secara bertahap dan langsung ke pekerjaan berikutnya. Jelaskan dengan bahasa Indonesia yang jelas dan santai, tetapi tetap teliti secara akademik. Pisahkan fakta dari sumber, hasil hitung, asumsi/skenario, dan hal yang belum dikonfirmasi.

## 2. Identitas dan konteks skripsi
- Pengguna adalah mahasiswa Sarjana Terapan Sistem Informasi Bisnis (SIB), Politeknik Negeri Malang.
- Arah proyek: Smart Farming — jagung — pemanfaatan hasil panen sebagai bahan pakan ayam, dalam konteks mitra yang bersinergi dengan bank sampah di Sumenep, Jawa Timur. Jangan mengarang profil atau kondisi operasional mitra yang belum disampaikan.
- Solusi akhir kemungkinan sistem berbasis web, tetapi bentuk sistem, kebutuhan, arsitektur, stack, fitur, metode pengembangan, dan judul belum final.
- Penelitian harus tetap kuat sebagai Sistem Informasi Bisnis: fokus pada kebutuhan informasi, perencanaan, pengambilan keputusan, estimasi, atau pengelolaan ketersediaan/pasokan—bukan berubah menjadi riset agronomi murni atau formulasi nutrisi unggas murni.
- ML bukan fokus utama. Jangan mengarahkan ke Hadoop, Spark, big data, atau kembali ke kandidat penyakit/NDVI/irigasi dari eksplorasi dataset lama kecuali ada bukti baru yang relevan.
- Data riil hasil panen/pakan/ayam dari mitra belum tersedia. Arahan dosen: model dikembangkan dahulu berdasarkan literatur, bukan dipaksakan fit ke data mitra yang belum ada.

## 3. Fakta operasional dan batasan yang diketahui
- Ada 3 petak jagung, masing-masing 5 m × 6 m = 30 m²; total area 90 m² = 0,009 ha.
- Hasil yang dihitung adalah bagian jagung yang dipanen untuk pakan, bukan batang/biomassa keseluruhan. Bentuk hasil yang tepat (pipilan kering, biji dengan kadar air tertentu, atau tongkol) perlu dinyatakan eksplisit; jangan mencampur bentuk hasil.
- Siklus jagung diperkirakan sekitar 3 bulan/~90 hari. Rencana konseptual: tiga petak ditanam dengan selisih waktu agar panen bisa tersedia tiap bulan. Istilah kandidat yang dicari di literatur: *staggered planting* / *sequential planting* / penanaman bertahap. Jadwal dan asumsi panen bulanan belum boleh dianggap final tanpa memeriksa sumber.
- Dosen pernah menyebut angka 200 g pakan/ayam/hari sebagai total ransum, bukan jagung murni. Angka ini tidak universal; bergantung jenis ayam, umur, fase produksi, dan sistem pemeliharaan.
- Fokus hitungan yang dipilih: berapa ekor ayam yang secara teoritis dapat didukung oleh hasil jagung dari petak tersebut. Broiler dan layer masih alternatif yang dibandingkan; jangan pilih salah satunya tanpa perbandingan kebutuhan dan argumen yang bisa dipertanggungjawabkan.
- Jika menghitung jagung untuk pakan lengkap, persentase jagung dalam complete feed harus dibedakan dari konsumsi total pakan per ekor per hari. Keduanya tidak boleh disamakan.

## 4. Tahap yang sudah dilakukan
- Eksplorasi dataset proxy sekitar 111 observasi dan 22 kolom: notebook 1 Data Understanding, notebook 2 Data Quality & EDA, notebook 3 Candidate Research Problems sudah dilakukan. Dataset ini hanya proxy/eksplorasi, bukan bukti operasional mitra.
- Sudah ada literatur awal mengenai hasil jagung, umur panen, serta parameter ransum broiler/layer.
- Sudah ada pembahasan bahwa kebutuhan utama sekarang bukan memperluas pencarian secara acak, tetapi menyusun *evidence matrix* dari paper yang telah dikumpulkan untuk menentukan parameter yang layak digunakan, keterbatasan, dan relevansi ke model.

## 5. Literatur hasil jagung yang sudah diprioritaskan
### Sumber inti
1. **Amzeri et al. (2023)**, “Genotype by Environment Interaction on Early-Maturing and High-Yield Maize Hybrids,” DOI: 10.28991/HEF-2023-04-01-05. Multi-lokasi, termasuk Lenteng, Sumenep. Hasil yang pernah diekstrak: G4 sekitar 9,30 t/ha pada musim kering dan 8,92 t/ha pada musim hujan di Sumenep; rerata keseluruhan sekitar 8,71 t/ha; umur panen rata-rata sekitar 91,93 hari. Angka ini bergantung genotipe/lokasi/musim dan bukan prediksi otomatis hasil mitra.
2. **Handayati et al. (2022)**, “Increasing maize yield and farming benefit through integrated plant management in Madura Island East Java,” IOP Conference Series: Earth and Environmental Science. Konteks Pamekasan/Madura. Pernah diekstrak: hasil terbaik 6,35 t/ha dengan integrated plant management versus 1,22 t/ha pada praktik petani eksisting. Perbedaan ini menunjukkan hasil sangat dipengaruhi praktik budidaya.
### Sumber pendukung
3. **Wicaksana et al. (2022)**, “Selection of High Yield and Stable Maize Hybrids in Mega-Environments of Java Island, Indonesia,” Agronomy, DOI: 10.3390/agronomy12122923. Studi multi-lokasi di Jawa; panen sekitar 93 hari.
4. **Aristya & Samijan (2022)**, “The Yield Gap Maize under Intensive Cropping System in Central Java,” DOI: 10.18196/pt.v10i1.8789. Hasil aktual petani pernah diekstrak sekitar 5,57 t/ha; nilai potensi/model tidak boleh diperlakukan sebagai hasil aktual.

Konversi yang sudah dihitung: untuk satu petak 30 m², hasil t/ha × 3 = kg/petak; untuk seluruh 90 m², hasil t/ha × 9 = kg. Contoh angka yang pernah dihitung: 1,22 t/ha → 3,66 kg/petak dan 10,98 kg/90 m²; 6,35 t/ha → 19,05 kg/petak dan 57,15 kg total; 8,92–9,30 t/ha → 26,76–27,90 kg/petak dan 80,28–83,70 kg total. Angka terakhir hanya konversi bersyarat dari hasil percobaan, bukan estimasi pasti hasil mitra. Perlu cek basis kadar air dan apakah hasil sudah dikoreksi ke kadar air standar.

Untuk kematangan/panen, bedakan kematangan fisiologis (misalnya black layer, biji keras, kelobot mengering) dengan waktu panen dan pengeringan agar biji aman disimpan/digunakan. Kadar air saat penimbangan sangat memengaruhi estimasi kg biji.

## 6. Literatur pakan ayam dan verifikasi PDF terbaru
Pengguna telah menggunakan Consensus AI untuk mencari paper peer-reviewed 2022–2026 tentang persentase jagung dalam complete feed untuk broiler dan layer, dan menyatakan bahwa paper serta link dari Consensus/yang diberikan sebelumnya sudah benar. Jangan menganggap sumber Consensus keseluruhan salah hanya karena ada potensi ketidakcocokan file yang diunggah.

### Layer — Gunjević et al. (2023), sudah diperiksa dari PDF
Judul: “Effect of Maize Hybrid in Complete Feed on the Production Performance and Economic Considerations in Laying Hens.” Sustainability 2023, 15, 15748. DOI: 10.3390/su152215748.
- Tabel 2 mencantumkan maize 600 g/kg = 60% complete feed.
- Lohmann Brown; fase awal bertelur; studi dilakukan di Kroasia, sehingga bukan bukti langsung kondisi tropis Indonesia.
- Konsumsi complete feed yang dilaporkan abstrak: 119,7–123,1 g/hen/day.
- Hasil hitung sederhana 60% × konsumsi pakan = sekitar 71,82–73,86 g maize/hen/day, hanya untuk kondisi studi tersebut, bukan rekomendasi universal atau nilai final bagi model Sumenep.
- Nutrien terhitung diet pada Tabel 2: ME 11,51 MJ/kg; crude protein 16,91%; crude fat 5,55%; crude fiber 2,81%; starch 40,65%; lysine 0,88%; methionine 0,42%; Ca 3,8%; total P 0,6%; available P 0,43%; linolenic acid 3,16%.

### Broiler — nilai hasil Consensus perlu dipetakan ke paper/tabel
Sintesis Consensus yang sudah disalin pengguna memuat nilai berikut:
- Alqhtani et al. (2024), disebut DOI 10.37496/rbz5320230100, Ross 308: starter hari 0–10 51,6%; grower hari 11–24 58,5–58,8%; finisher hari 25–35 59,8–60,6% maize, basis as-fed.
- Teymouri et al. (2025), Veterinary Medicine and Science, Ross 308 finisher hari 25–42: 59,24% corn as-fed.
- Ahmad et al. (2024), Veterinary Quarterly, Ross 708 control: 566 g/kg (56,6%) as-fed pada studi penggantian sorgum.
- Mai (2023), studi QPM: normal maize pada diet finisher dilaporkan 52,1%, 39,07%, 26,05%, 13,03%, dan 0% sesuai level substitusi QPM.

### Layer — nilai tambahan dari sintesis Consensus
- van Eck et al. (2025 online / issue 2026), DOI 10.1016/j.psj.2025.106174, Dekalb White: jagung bervariasi menurut fase; sintesis Consensus menyebut rearing 0–5 minggu 448 atau 358 g/kg; 5–10 minggu 408 atau 373 g/kg; 10–17 minggu 429 atau 408 g/kg; pre-lay 17–20 minggu 342–400 g/kg; laying 20–28 minggu 353–392 g/kg; 28–44 minggu 231–421 g/kg; 44–110 minggu 251–367 g/kg. Tahun bibliografi final harus mengikuti metadata artikel/jurnal.
- Oluwabiyi et al. (2022): Hy-Line Brown grower 9–17 minggu 68,23% atau 64,57%; pre-lay 18–21 minggu 63,98% atau 60,83%.
- Novela et al. (2023): kontrol 60% yellow maize; diet substitusi 40% yellow maize + wheat bran.

Penting: angka-angka Consensus adalah *ekstraksi sekunder sementara* sampai setiap angka dipetakan ke artikel asli, tabel, fase ayam, satuan/basis as-fed atau lainnya, dan kondisi studi. Jangan langsung mengambil angka terbesar atau menyebutnya sebagai standar universal. Studi di luar Indonesia harus diberi batasan generalisasi.

### Dua PDF yang muncul dalam percakapan ini
1. `sustainability-15-15748.pdf`: sesuai dengan paper Gunjević et al. (2023) di atas.
2. `1806-9290-rbz-53-e20220108.pdf`: file yang benar-benar terunggah menunjukkan paper Sinhorini et al. (2024), “Blood addition and processing conditions: Improving protein content and digestibility value of hydrolyzed feather meal,” DOI 10.37496/rbz5320220108. Ini berbeda dari metadata Alqhtani yang dikutip Consensus (DOI yang disebut Consensus: 10.37496/rbz5320230100). Perlakukan ini sebagai **ketidakcocokan antara file PDF yang terunggah dan paper Alqhtani yang dirujuk**, bukan sebagai bukti bahwa semua sumber/link Consensus salah. Periksa link/metadata artikel Alqhtani secara spesifik saat diperlukan, tetapi tidak perlu membuka pencarian literatur luas dari nol.

## 7. Sumber panduan performa unggas (baseline resmi, bukan data lokal)
### Broiler Ross 308 AP Performance Objectives 2022
PDF resmi Aviagen: https://aa-intl.aviagen.com/assets/Tech_Center/Ross_Broiler/RossxRoss308AP-BroilerPerformanceObjectives2022-EN.pdf
- Konsumsi pakan kumulatif as-hatched: hari 35 = 3,268 g/ekor; hari 42 = 4,674 g/ekor; hari 56 = 7,884 g/ekor.
- Sasaran berbeda menurut jenis kelamin; tabel performa menunjukkan jantan hari 35 = 3,455 g dan hari 42 = 4,980 g; betina hari 35 = 3,082 g dan hari 42 = 4,369 g.
- Ini target performa breed, bukan data aktual peternak lokal.
### Hy-Line Brown Commercial Layers Performance Standards Guide
PDF resmi: https://www.hyline.com/filesimages/Hy-Line-Products/Hy-Line-Product-PDFs/Brown/BRN%20STD%20ENG.pdf
- Ringkasan konsumsi selama pemeliharaan 0–17 minggu sekitar 5,99 kg/ekor.
- Saat produksi: minggu 18 81–86 g/hari; minggu 19 86–92; minggu 20 91–98; minggu 21 96–103; minggu 22 101–108; minggu 23 104–112; minggu 24 107–114; minggu 25 108–116; minggu 26 109–117; minggu 27–100 110–118 g/hari.
- Ringkasan rata-rata harian minggu 19–100: 109,1–116,9 g/hari. Bedakan tabel awal produksi minggu 18 dari ringkasan minggu 19–100.

## 8. Arah kerja dan langkah berikutnya — JANGAN lompat ke judul
Langkah paling tepat sekarang adalah **membangun matriks bukti/parameter dari sumber yang sudah terkumpul**, bukan mencari ratusan paper baru atau langsung menentukan kapasitas ayam final.

### Tahap A — matriks literatur jagung
Untuk Amzeri, Handayati, Wicaksana, Aristya/Samijan: ekstrak dan catat (1) varietas/genotipe, (2) lokasi dan musim, (3) perlakuan/budidaya, (4) hasil dan unit, (5) kadar air/basis bobot, (6) umur panen, (7) apakah angka hasil merupakan rata-rata, perlakuan terbaik, aktual petani, atau potensi model, dan (8) keterbatasan penerapan pada 90 m² di mitra.

### Tahap B — matriks parameter pakan
Untuk broiler dan layer: paper/tahun/DOI, strain, fase umur/produksi, persentase maize dalam complete feed, basis as-fed atau dry matter, konsumsi total pakan (g/ekor/hari atau kumulatif), lokasi/kondisi, tabel/halaman sumber, serta keterbatasan. Pastikan persentase maize dan konsumsi complete feed berasal dari diet/fase yang sama sebelum dikalikan.

### Tahap C — bandingkan skenario broiler vs layer
Hitung kebutuhan jagung per ekor per hari/per siklus hanya bila input yang cocok tersedia. Bandingkan: kebutuhan jagung, durasi pemeliharaan, hasil panen dari tiga petak, frekuensi panen, dan ketidakpastian. Pilih baseline berdasarkan kecocokan dengan tujuan operasional dan kekuatan data, bukan karena satu jenis ayam tampak paling menguntungkan dari satu angka.

### Tahap D — model panen dan dukungan pakan
Gunakan skenario hasil rendah/tengah/tinggi yang ditelusuri ke sumber. Pisahkan kehilangan pascapanen, pengeringan, penyimpanan, dan jumlah yang benar-benar dialokasikan untuk pakan bila data/parameter tersedia. Buat neraca sederhana: hasil jagung layak pakai per panen → bagian yang masuk ransum → kebutuhan jagung ayam → estimasi ekor yang bisa didukung. Nyatakan asumsi dan sensitivitas.

### Tahap E — jadwal panen bulanan
Cari dan verifikasi istilah serta bukti tentang staggered/sequential planting, umur varietas, dan jadwal tanam yang memungkinkan panen bulanan. Jangan menganggap tiga petak yang ditanam beda bulan otomatis memberi hasil bulanan stabil tanpa memperhitungkan umur panen, musim, varietas, dan kemungkinan jeda/overlap.

### Tahap F — problem SIB dan desain sistem
Setelah model parameter dan kebutuhan mitra makin jelas, rumuskan problem informasi/keputusan yang nyata (misalnya perencanaan tanam-panen dan proyeksi kecukupan jagung untuk pakan hanya jika relevan dengan bukti mitra). Baru petakan kebutuhan pengguna, input-output, aturan/perhitungan, evaluasi, dan metode pengembangan. Judul tetap belakangan.

## 9. Keputusan dan larangan mengasumsikan
- Belum final: broiler atau layer; persentase jagung final; yield baseline final; istilah/metode jadwal tanam final; bentuk hasil jagung dan kadar air; model sistem, metode, stack, judul.
- Jangan memperlakukan 8,9–9,3 t/ha sebagai hasil yang pasti di petak mitra.
- Jangan menyamakan jagung dalam complete feed dengan seluruh pakan ayam.
- Jangan menyebut data proxy sebagai data mitra.
- Jangan menyebut studi luar negeri sebagai bukti langsung kondisi tropis Indonesia.
- Jangan menyatakan PDF Alqhtani telah diverifikasi dari file yang salah; ketidakcocokan PDF perlu diselesaikan dengan mencocokkan DOI/link yang benar.

## 10. Kalimat pembuka untuk chat baru
“Gunakan `THESIS_HANDOVER_2026-10-21.md` sebagai konteks terbaru, bersama `THESIS_MASTER_CONTEXT_AND_AGENT_GUIDE.md`. Kita sedang mengembangkan model literatur untuk mengestimasi hasil panen biji jagung dari tiga petak (total 90 m²) dan kecukupannya sebagai bahan pakan ayam, dengan target konseptual panen bulanan melalui penanaman bertahap. Literatur yield utama sudah diprioritaskan; Consensus sudah mengumpulkan paper persentase maize untuk broiler/layer. Langkah berikutnya adalah membuat matriks bukti dan parameter yang terverifikasi, lalu membandingkan skenario broiler vs layer—bukan mencari literatur dari nol atau menentukan judul sekarang. Jaga semua keputusan yang belum final tetap conditional, bedakan sumber/hasil hitung/asumsi, dan jangan mengarang data mitra.”
