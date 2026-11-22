# Dataset Context — Chiapas Field Data 2012–2018

## 1. Identitas dataset

- **Nama dataset:** *Agronomic, soil and weather data from modules and extension areas in hub Chiapas, Mexico 2012–2018*.
- **Institusi pengelola:** International Maize and Wheat Improvement Center (CIMMYT).
- **Lokasi:** Negara bagian Chiapas, Meksiko.
- **Periode observasi:** tujuh musim tanam, 2012–2018.
- **Tanggal publikasi dataset di repositori:** 26 Oktober 2021 (versi repositori yang tercatat).
- **Jumlah observasi:** 4.585 cropping events.
- **Unit observasi:** satu baris merepresentasikan satu kejadian budidaya pada suatu field/lahan dalam satu tahun tanam; bukan satu petani unik.
- **Format sumber:** Excel, dengan sheet `Legend` dan `Data`.

## 2. Asal dan tujuan pengumpulan

Dataset dikembangkan dalam kegiatan *CIMMYT Knowledge/Innovation Hub* di Chiapas. Kegiatan ini melibatkan *innovation modules* (perbandingan praktik budidaya yang dilakukan berdampingan) dan *extension areas* (lahan petani tempat praktik yang diperkenalkan diterapkan atau didemonstrasikan). Konteksnya adalah perbaikan sistem produksi jagung lokal melalui pengujian dan penerapan praktik agronomi bersama petani dan pendamping lapangan.

Data agronomi dikumpulkan oleh farm advisors ketika melakukan kunjungan lapangan dan dicatat melalui **Bitacora Electrónica MasAgro (BEM)**, yaitu sistem logbook elektronik untuk pencatatan kegiatan budidaya. Dataset yang dibagikan merupakan subset variabel dari basis data BEM untuk wilayah Chiapas pada 2012–2018.

## 3. Sumber data dan metode perolehan

| Kelompok data | Sumber | Cara/peran dalam dataset |
|---|---|---|
| Data agronomi dan pengelolaan lahan | BEM / Bitacora Electrónica MasAgro | Dicatat oleh farm advisors melalui kunjungan lapangan; mencakup hasil/yield, varietas atau cultivar, sistem tanam, olah tanah, waktu tanam, dan pemupukan. |
| Data tanah dan topografi | INEGI (Instituto Nacional de Estadística y Geografía), Meksiko | Variabel spasial/lingkungan seperti kemiringan, tekstur atau kandungan liat, bahan organik tanah, kapasitas tukar kation (CEC), dan pH diperoleh dari dataset pemetaan terbuka INEGI dan dipadankan dengan field. |
| Data cuaca | DAYMET | Data cuaca berbasis grid diekstrak untuk lokasi field dan diringkas ke dalam 30 interval, masing-masing 10 hari. Menurut sheet Legend, rentang interval dimulai 60 hari sebelum tanam hingga 240 hari setelah tanam. Variabel yang tercantum pada workbook meliputi presipitasi, radiasi surya, suhu maksimum, suhu minimum, dan tekanan uap. |
| Rata-rata hasil tingkat munisipal | SIAP (Agri-food and Fisheries Information Service), sebagaimana dijelaskan dalam artikel data | Rata-rata hasil jagung pada tingkat munisipal sebagai konteks pembanding. |

**Catatan metodologis:** data agronomi merupakan catatan observasional dari lahan petani, bukan hasil eksperimen terkontrol yang seluruh perlakuannya diacak. Data tanah dan cuaca merupakan data sekunder yang dipasangkan berdasarkan lokasi dan periode. Karena itu, hubungan antarvariabel tidak otomatis dapat ditafsirkan sebagai hubungan sebab-akibat.

## 4. Paper/artikel terkait

Artikel data yang mendeskripsikan dataset ini adalah:

Trevisan, R. G., Martin, N. F., Fonteyne, S., Verhulst, N., Dorado Betancourt, H. A., Jiménez, D., & Gardeazabal, A. (2022). **Multiyear maize management dataset collected in Chiapas, Mexico.** *Data in Brief, 40*, 107837. https://doi.org/10.1016/j.dib.2022.107837

Artikel tersebut menjelaskan rancangan pengumpulan, sumber data agronomi/tanah/cuaca, dan karakteristik 4.585 observasi selama 2012–2018. Artikel ini merupakan artikel deskripsi dataset (*data paper*), bukan klaim bahwa seluruh variabel dalam dataset merupakan hasil eksperimen kausal.

## 5. Repositori dan identifikasi sumber

- **Repositori:** CIMMYT Research Data & Software Repository Network.
- **Judul rekaman dataset:** *Agronomic, soil and weather data from modules and extension areas in hub Chiapas, Mexico 2012–2018*.
- **Persistent identifier dataset:** https://hdl.handle.net/11529/10548624
- **Halaman repositori:** https://data.cimmyt.org/dataset.xhtml?persistentId=hdl%3A11529%2F10548624
- **Versi file yang digunakan:** workbook `Chiapas Field Data 2012-2018.xlsx` yang diberikan untuk pemrosesan ini. Rekaman repositori menyebut file Excel dengan pembaruan koordinat latitude dan longitude pada April 2022. Jangan menganggap versi file lain identik tanpa membandingkan checksum atau isi datanya.

## 6. Struktur file hasil penyiapan

- `Chiapas_Original.xlsx`: file sumber Excel. File ini dipertahankan apa adanya dan tidak ditulis ulang.
- `Chiapas_Data.csv`: salinan nilai dari sheet `Data`, tanpa kolom indeks tambahan. Urutan kolom dan observasi mengikuti workbook.
- `DATASET_CONTEXT.md`: dokumen konteks sumber, lokasi, periode, metode pengumpulan, dan paper terkait.
- `DATA_DICTIONARY.md`: definisi 169 kolom berdasarkan sheet `Legend`, dilengkapi tipe data hasil pembacaan dan jumlah nilai kosong pada file ini.

## 7. Ringkasan pemeriksaan file

Hasil pemeriksaan terhadap sheet `Data` pada workbook yang diberikan:

- **Baris observasi:** 4.585.
- **Kolom:** 169.
- **Cakupan tahun:** 2012–2018.
- **Field_ID kosong:** 0.
- **Field_ID duplikat:** 0.
- **Baris duplikat identik:** 0.
- **Nilai kosong yang teridentifikasi:** terdapat pada kolom `Cultivar` (310 nilai kosong); kolom lain tidak memiliki nilai kosong pada pembacaan workbook ini.

Ringkasan tersebut merupakan pemeriksaan struktur dan kelengkapan dasar, bukan validasi menyeluruh atas kebenaran pengukuran, konsistensi satuan, ketepatan koordinat, atau kualitas pencatatan lapangan.

## 8. Catatan penggunaan dan batasan interpretasi

1. Dataset berfokus pada **budidaya jagung di Chiapas, Meksiko**. Karakteristik iklim, tanah, varietas, sistem pertanian, dan praktik pengelolaannya tidak otomatis mewakili wilayah atau komoditas lain.
2. Satu `Field_ID` merupakan pengenal field pada file ini. Jangan langsung mengasumsikan bahwa setiap baris adalah petani yang berbeda atau bahwa observasi antar-tahun independen.
3. Variabel cuaca `*_V1` sampai `*_V30` merupakan urutan interval waktu 10-harian. Untuk pemodelan temporal, pastikan arah dan titik acuan interval dipahami; jangan menafsirkan nomor V sebagai bulan.
4. Sebagian variabel cuaca mencerminkan kondisi setelah tanam. Jika tujuan model adalah prediksi sebelum tanam, fitur pascatanam berpotensi menimbulkan *data leakage* dan tidak boleh digunakan sebagai prediktor yang seolah-olah telah tersedia pada saat prediksi.
5. `YIELD` adalah hasil jagung pada tingkat field dengan satuan Mg ha-1 (setara ton/ha), sedangkan `Mun_yield` adalah rata-rata hasil tingkat munisipal. Keduanya bukan variabel target yang sama.
6. Nilai kosong pada `Cultivar` harus dipertahankan sebagai missing value atau ditangani secara eksplisit pada tahap preprocessing; jangan otomatis menganggapnya sebagai kategori tertentu.
7. Dataset bersifat observasional dan berasal dari konteks intervensi/demonstrasi serta area ekstensi. Seleksi lokasi dan praktik yang dicatat dapat membatasi generalisasi hasil model.

---
Dokumen ini disusun dari keterangan pada sheet `Legend` dalam workbook dan metadata repositori serta artikel data yang dirujuk di atas. Jika terdapat perbedaan, definisi kolom pada workbook sumber dipertahankan sebagai acuan langsung untuk file ini.
