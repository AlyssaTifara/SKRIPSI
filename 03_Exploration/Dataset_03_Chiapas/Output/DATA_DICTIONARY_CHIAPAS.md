# DATA DICTIONARY — CHIAPAS MAIZE DATASET (2012–2018)

## 1. Ringkasan Dataset
- **Nama Dataset:** Multiyear Maize Management Dataset collected in Chiapas, Mexico (2012–2018)
- **Sumber Data:** CIMMYT Knowledge Hub Chiapas, BEM (Bitácora Electrónica MasAgro), INEGI, Daymet, SIAP
- **Publikasi Pendamping:** Trevisan, R. G., Martin, N. F., Fonteyne, S., Verhulst, N., Dorado Betancourt, H. A., Jiménez, D., & Gardeazabal, A. (2022). *Data in Brief*, 40, 107837. https://doi.org/10.1016/j.dib.2022.107837
- **Persistent Identifier (Handle):** https://hdl.handle.net/11529/10548624
- **Jumlah Observasi:** 4.585 baris *cropping events*
- **Jumlah Variabel:** 169 kolom (19 variabel agronomi/lingkungan/target + 150 variabel cuaca temporal)
- **Status Missing Value:** Lengkap 100% pada 168 kolom; hanya variabel `Cultivar` yang memiliki nilai kosong sebanyak 310 baris (6,76%).

---

## 2. Struktur Interval Cuaca (Daymet Gridded Weather V1 – V30)
Dataset cuaca ditransformasikan ke dalam 30 interval 10-harian yang dihitung relatif terhadap tanggal tanam (`Planting` DOY):
- **Interval V1 – V6 (6 interval = 60 hari):** Periode **Sebelum Tanam (Pre-planting)** dari hari ke -60 hingga hari ke -1 sebelum tanam. Fitur ini aman digunakan untuk peramalan yield sebelum tanam (*pre-season forecasting*).
- **Interval V7 – V24 (18 interval = 180 hari):** Periode **Selama Pertumbuhan (In-season)** dari hari ke 0 hingga hari ke 179 setelah tanam. Rata-rata durasi musim tanam jagung adalah 175 hari. Fitur ini **berpotensi menimbulkan data leakage** jika model ditujukan untuk perencanaan tanam awal, karena nilainya belum terjadi pada saat keputusan tanam diambil.
- **Interval V25 – V30 (6 interval = 60 hari):** Periode **Pasca Kematangan Fisiologis / Pasca Panen (Post-season)** dari hari ke 180 hingga hari ke 240 setelah tanam. Fitur ini merefleksikan kondisi cuaca saat jagung dibiarkan mengering di lahan sebelum panen manual.

Lima parameter cuaca harian yang dirata-ratakan dalam setiap interval 10-hari:
1. `prcp_V1` s/d `prcp_V30`: Presipitasi rata-rata harian (satuan: mm day⁻¹).
2. `srad_V1` s/d `srad_V30`: Radiasi surya rata-rata harian (satuan: MJ m⁻² day⁻¹).
3. `tmax_V1` s/d `tmax_V30`: Suhu maksimum rata-rata (satuan: °C).
4. `tmin_V1` s/d `tmin_V30`: Suhu minimum rata-rata (satuan: °C).
5. `vp_V1` s/d `vp_V30`: Tekanan uap air rata-rata (satuan: Pa).

---

## 3. Tabel Kamus Data Lengkap (169 Variabel)

| No. | Nama Kolom | Kategori | Deskripsi (Berdasarkan Legend / Paper) | Satuan Asli | Tipe Data | Missing Values | Rentang / Karakteristik Nilai | Status Ketersediaan & Risiko Leakage |
|---:|---|---|---|---|---|---|---|---|
| 1 | `Field_ID` | Identifikasi / Temporal | Unique identifier for each field | - | `int64` | 0 (0.00%) | 1.00 s/d 4585.00 (Mean: 2293.00) | Tersedia sebelum tanam (ID & Tahun) |
| 2 | `YIELD` | Target Utama | Field maize yield | Mg ha-1 | `float64` | 0 (0.00%) | 0.10 s/d 9.80 (Mean: 3.59) | Target Observasi Lapangan (Pasca Panen) |
| 3 | `Year` | Identifikasi / Temporal | Year of cropping event | - | `int64` | 0 (0.00%) | 2012.00 s/d 2018.00 (Mean: 2015.36) | Tersedia sebelum tanam (ID & Tahun) |
| 4 | `Mun_yield` | Konteks Wilayah | Average maize yield in a municipality | Mg ha-1 | `float64` | 0 (0.00%) | 1.13 s/d 4.39 (Mean: 2.61) | Statistik Regional Tahunan (SIAP) |
| 5 | `Lat` | Geografis / Topografi | Latitude coordinates | Degrees | `float64` | 0 (0.00%) | 14.71 s/d 17.76 (Mean: 16.44) | Tersedia sebelum tanam |
| 6 | `Long` | Geografis / Topografi | Longitude coordinates | Degrees | `float64` | 0 (0.00%) | -93.98 s/d -91.56 (Mean: -92.80) | Tersedia sebelum tanam |
| 7 | `Elev` | Geografis / Topografi | Elevation | m above sea level | `int64` | 0 (0.00%) | 7.00 s/d 2849.00 (Mean: 884.70) | Tersedia sebelum tanam |
| 8 | `System` | Pengelolaan Agronomi | Characterization of Hybrid or Landrace based cropping system | Hybrid or Landrace | `str` | 0 (0.00%) | Kategori: 2 unik (Modus: Hybrid) | Tersedia saat penanaman |
| 9 | `Cultivar` | Pengelolaan Agronomi | Genotype information | Name of cultivar if available | `str` | 310 (6.76%) | Kategori: 249 unik (Modus: CRIOLLO) | Tersedia saat penanaman |
| 10 | `Tillage` | Pengelolaan Agronomi | Tillage practices including Conventional, Reduced, and No-Till | Conventional/Reduced/No-Till | `str` | 0 (0.00%) | Kategori: 3 unik (Modus: Conventional) | Tersedia saat penanaman |
| 11 | `Planting` | Pengelolaan Agronomi | Day of the year when maize was planted | Day of Year (DOY) | `int64` | 0 (0.00%) | 91.00 s/d 242.00 (Mean: 165.12) | Tersedia saat penanaman |
| 12 | `Nitrogen` | Pemupukan | Nitrogen added as fertilizer | kg N ha-1 | `float64` | 0 (0.00%) | 0.00 s/d 349.00 (Mean: 109.74) | Rencana/Aplikasi pemupukan |
| 13 | `Phosphorus` | Pemupukan | Phosphorus added as fertilizer | kg P2O5 ha-1 | `float64` | 0 (0.00%) | 0.00 s/d 143.00 (Mean: 23.88) | Rencana/Aplikasi pemupukan |
| 14 | `Potassium` | Pemupukan | Potassium added as fertilizer | kg K2O ha-1 | `float64` | 0 (0.00%) | 0.00 s/d 100.00 (Mean: 9.30) | Rencana/Aplikasi pemupukan |
| 15 | `Slope` | Karakteristik Tanah | Field slope | % | `float64` | 0 (0.00%) | 0.00 s/d 61.19 (Mean: 6.03) | Tersedia sebelum tanam (Peta Tanah INEGI) |
| 16 | `Clay` | Karakteristik Tanah | Soil clay content | % | `int64` | 0 (0.00%) | 5.00 s/d 57.00 (Mean: 30.15) | Tersedia sebelum tanam (Peta Tanah INEGI) |
| 17 | `CEC` | Karakteristik Tanah | Cation Exchange Capacity | cmolc dm-3 | `float64` | 0 (0.00%) | 4.31 s/d 50.80 (Mean: 22.74) | Tersedia sebelum tanam (Peta Tanah INEGI) |
| 18 | `SOM` | Karakteristik Tanah | Soil Organic Matter | % | `float64` | 0 (0.00%) | 0.27 s/d 4.00 (Mean: 1.60) | Tersedia sebelum tanam (Peta Tanah INEGI) |
| 19 | `PH` | Karakteristik Tanah | Soil pH | - | `float64` | 0 (0.00%) | 4.92 s/d 8.25 (Mean: 6.81) | Tersedia sebelum tanam (Peta Tanah INEGI) |
| 20 | `prcp_V1` | Cuaca Gridded (Daymet) | Precipitation per day over 10 days for interval V1 | mm day-1 | `float64` | 0 (0.00%) | 0.00 s/d 17.60 (Mean: 0.79) | Pre-planting (Hari -60 s/d -51) |
| 21 | `prcp_V2` | Cuaca Gridded (Daymet) | Precipitation per day over 10 days for interval V2 | mm day-1 | `float64` | 0 (0.00%) | 0.00 s/d 29.80 (Mean: 1.55) | Pre-planting (Hari -50 s/d -41) |
| 22 | `prcp_V3` | Cuaca Gridded (Daymet) | Precipitation per day over 10 days for interval V3 | mm day-1 | `float64` | 0 (0.00%) | 0.00 s/d 23.70 (Mean: 2.97) | Pre-planting (Hari -40 s/d -31) |
| 23 | `prcp_V4` | Cuaca Gridded (Daymet) | Precipitation per day over 10 days for interval V4 | mm day-1 | `float64` | 0 (0.00%) | 0.00 s/d 28.70 (Mean: 4.67) | Pre-planting (Hari -30 s/d -21) |
| 24 | `prcp_V5` | Cuaca Gridded (Daymet) | Precipitation per day over 10 days for interval V5 | mm day-1 | `float64` | 0 (0.00%) | 0.00 s/d 30.50 (Mean: 5.85) | Pre-planting (Hari -20 s/d -11) |
| 25 | `prcp_V6` | Cuaca Gridded (Daymet) | Precipitation per day over 10 days for interval V6 | mm day-1 | `float64` | 0 (0.00%) | 0.00 s/d 27.90 (Mean: 6.67) | Pre-planting (Hari -10 s/d -1) |
| 26 | `prcp_V7` | Cuaca Gridded (Daymet) | Precipitation per day over 10 days for interval V7 | mm day-1 | `float64` | 0 (0.00%) | 0.00 s/d 29.20 (Mean: 6.51) | POTENSI LEAKAGE: In-season (Hari 0 s/d 9) |
| 27 | `prcp_V8` | Cuaca Gridded (Daymet) | Precipitation per day over 10 days for interval V8 | mm day-1 | `float64` | 0 (0.00%) | 0.00 s/d 27.10 (Mean: 6.13) | POTENSI LEAKAGE: In-season (Hari 10 s/d 19) |
| 28 | `prcp_V9` | Cuaca Gridded (Daymet) | Precipitation per day over 10 days for interval V9 | mm day-1 | `float64` | 0 (0.00%) | 0.00 s/d 23.80 (Mean: 6.16) | POTENSI LEAKAGE: In-season (Hari 20 s/d 29) |
| 29 | `prcp_V10` | Cuaca Gridded (Daymet) | Precipitation per day over 10 days for interval V10 | mm day-1 | `float64` | 0 (0.00%) | 0.00 s/d 22.60 (Mean: 5.83) | POTENSI LEAKAGE: In-season (Hari 30 s/d 39) |
| 30 | `prcp_V11` | Cuaca Gridded (Daymet) | Precipitation per day over 10 days for interval V11 | mm day-1 | `float64` | 0 (0.00%) | 0.00 s/d 54.90 (Mean: 6.05) | POTENSI LEAKAGE: In-season (Hari 40 s/d 49) |
| 31 | `prcp_V12` | Cuaca Gridded (Daymet) | Precipitation per day over 10 days for interval V12 | mm day-1 | `float64` | 0 (0.00%) | 0.00 s/d 46.10 (Mean: 6.39) | POTENSI LEAKAGE: In-season (Hari 50 s/d 59) |
| 32 | `prcp_V13` | Cuaca Gridded (Daymet) | Precipitation per day over 10 days for interval V13 | mm day-1 | `float64` | 0 (0.00%) | 0.00 s/d 49.30 (Mean: 7.06) | POTENSI LEAKAGE: In-season (Hari 60 s/d 69) |
| 33 | `prcp_V14` | Cuaca Gridded (Daymet) | Precipitation per day over 10 days for interval V14 | mm day-1 | `float64` | 0 (0.00%) | 0.00 s/d 52.00 (Mean: 7.77) | POTENSI LEAKAGE: In-season (Hari 70 s/d 79) |
| 34 | `prcp_V15` | Cuaca Gridded (Daymet) | Precipitation per day over 10 days for interval V15 | mm day-1 | `float64` | 0 (0.00%) | 0.00 s/d 51.60 (Mean: 7.94) | POTENSI LEAKAGE: In-season (Hari 80 s/d 89) |
| 35 | `prcp_V16` | Cuaca Gridded (Daymet) | Precipitation per day over 10 days for interval V16 | mm day-1 | `float64` | 0 (0.00%) | 0.00 s/d 46.30 (Mean: 7.74) | POTENSI LEAKAGE: In-season (Hari 90 s/d 99) |
| 36 | `prcp_V17` | Cuaca Gridded (Daymet) | Precipitation per day over 10 days for interval V17 | mm day-1 | `float64` | 0 (0.00%) | 0.00 s/d 38.60 (Mean: 7.17) | POTENSI LEAKAGE: In-season (Hari 100 s/d 109) |
| 37 | `prcp_V18` | Cuaca Gridded (Daymet) | Precipitation per day over 10 days for interval V18 | mm day-1 | `float64` | 0 (0.00%) | 0.00 s/d 32.60 (Mean: 6.07) | POTENSI LEAKAGE: In-season (Hari 110 s/d 119) |
| 38 | `prcp_V19` | Cuaca Gridded (Daymet) | Precipitation per day over 10 days for interval V19 | mm day-1 | `float64` | 0 (0.00%) | 0.00 s/d 36.00 (Mean: 5.04) | POTENSI LEAKAGE: In-season (Hari 120 s/d 129) |
| 39 | `prcp_V20` | Cuaca Gridded (Daymet) | Precipitation per day over 10 days for interval V20 | mm day-1 | `float64` | 0 (0.00%) | 0.00 s/d 34.70 (Mean: 3.92) | POTENSI LEAKAGE: In-season (Hari 130 s/d 139) |
| 40 | `prcp_V21` | Cuaca Gridded (Daymet) | Precipitation per day over 10 days for interval V21 | mm day-1 | `float64` | 0 (0.00%) | 0.00 s/d 28.10 (Mean: 2.71) | POTENSI LEAKAGE: In-season (Hari 140 s/d 149) |
| 41 | `prcp_V22` | Cuaca Gridded (Daymet) | Precipitation per day over 10 days for interval V22 | mm day-1 | `float64` | 0 (0.00%) | 0.00 s/d 24.80 (Mean: 1.90) | POTENSI LEAKAGE: In-season (Hari 150 s/d 159) |
| 42 | `prcp_V23` | Cuaca Gridded (Daymet) | Precipitation per day over 10 days for interval V23 | mm day-1 | `float64` | 0 (0.00%) | 0.00 s/d 24.00 (Mean: 1.38) | POTENSI LEAKAGE: In-season (Hari 160 s/d 169) |
| 43 | `prcp_V24` | Cuaca Gridded (Daymet) | Precipitation per day over 10 days for interval V24 | mm day-1 | `float64` | 0 (0.00%) | 0.00 s/d 17.70 (Mean: 1.05) | POTENSI LEAKAGE: In-season (Hari 170 s/d 179) |
| 44 | `prcp_V25` | Cuaca Gridded (Daymet) | Precipitation per day over 10 days for interval V25 | mm day-1 | `float64` | 0 (0.00%) | 0.00 s/d 15.60 (Mean: 0.90) | POTENSI LEAKAGE: Post-season (Hari 180 s/d 189) |
| 45 | `prcp_V26` | Cuaca Gridded (Daymet) | Precipitation per day over 10 days for interval V26 | mm day-1 | `float64` | 0 (0.00%) | 0.00 s/d 15.50 (Mean: 0.52) | POTENSI LEAKAGE: Post-season (Hari 190 s/d 199) |
| 46 | `prcp_V27` | Cuaca Gridded (Daymet) | Precipitation per day over 10 days for interval V27 | mm day-1 | `float64` | 0 (0.00%) | 0.00 s/d 15.00 (Mean: 0.25) | POTENSI LEAKAGE: Post-season (Hari 200 s/d 209) |
| 47 | `prcp_V28` | Cuaca Gridded (Daymet) | Precipitation per day over 10 days for interval V28 | mm day-1 | `float64` | 0 (0.00%) | 0.00 s/d 15.20 (Mean: 0.16) | POTENSI LEAKAGE: Post-season (Hari 210 s/d 219) |
| 48 | `prcp_V29` | Cuaca Gridded (Daymet) | Precipitation per day over 10 days for interval V29 | mm day-1 | `float64` | 0 (0.00%) | 0.00 s/d 14.20 (Mean: 0.10) | POTENSI LEAKAGE: Post-season (Hari 220 s/d 229) |
| 49 | `prcp_V30` | Cuaca Gridded (Daymet) | Precipitation per day over 10 days for interval V30 | mm day-1 | `float64` | 0 (0.00%) | 0.00 s/d 6.70 (Mean: 0.09) | POTENSI LEAKAGE: Post-season (Hari 230 s/d 239) |
| 50 | `srad_V1` | Cuaca Gridded (Daymet) | Solar radiation per day over 10 days for interval V1 | MJ m-2 day-1 | `float64` | 0 (0.00%) | 12.67 s/d 26.33 (Mean: 22.39) | Pre-planting (Hari -60 s/d -51) |
| 51 | `srad_V2` | Cuaca Gridded (Daymet) | Solar radiation per day over 10 days for interval V2 | MJ m-2 day-1 | `float64` | 0 (0.00%) | 13.83 s/d 26.76 (Mean: 22.09) | Pre-planting (Hari -50 s/d -41) |
| 52 | `srad_V3` | Cuaca Gridded (Daymet) | Solar radiation per day over 10 days for interval V3 | MJ m-2 day-1 | `float64` | 0 (0.00%) | 13.02 s/d 25.92 (Mean: 21.24) | Pre-planting (Hari -40 s/d -31) |
| 53 | `srad_V4` | Cuaca Gridded (Daymet) | Solar radiation per day over 10 days for interval V4 | MJ m-2 day-1 | `float64` | 0 (0.00%) | 13.26 s/d 26.03 (Mean: 20.18) | Pre-planting (Hari -30 s/d -21) |
| 54 | `srad_V5` | Cuaca Gridded (Daymet) | Solar radiation per day over 10 days for interval V5 | MJ m-2 day-1 | `float64` | 0 (0.00%) | 13.29 s/d 26.05 (Mean: 19.48) | Pre-planting (Hari -20 s/d -11) |
| 55 | `srad_V6` | Cuaca Gridded (Daymet) | Solar radiation per day over 10 days for interval V6 | MJ m-2 day-1 | `float64` | 0 (0.00%) | 13.54 s/d 25.56 (Mean: 18.89) | Pre-planting (Hari -10 s/d -1) |
| 56 | `srad_V7` | Cuaca Gridded (Daymet) | Solar radiation per day over 10 days for interval V7 | MJ m-2 day-1 | `float64` | 0 (0.00%) | 13.24 s/d 25.92 (Mean: 18.80) | POTENSI LEAKAGE: In-season (Hari 0 s/d 9) |
| 57 | `srad_V8` | Cuaca Gridded (Daymet) | Solar radiation per day over 10 days for interval V8 | MJ m-2 day-1 | `float64` | 0 (0.00%) | 13.81 s/d 25.25 (Mean: 18.93) | POTENSI LEAKAGE: In-season (Hari 10 s/d 19) |
| 58 | `srad_V9` | Cuaca Gridded (Daymet) | Solar radiation per day over 10 days for interval V9 | MJ m-2 day-1 | `float64` | 0 (0.00%) | 13.94 s/d 24.92 (Mean: 18.89) | POTENSI LEAKAGE: In-season (Hari 20 s/d 29) |
| 59 | `srad_V10` | Cuaca Gridded (Daymet) | Solar radiation per day over 10 days for interval V10 | MJ m-2 day-1 | `float64` | 0 (0.00%) | 13.28 s/d 24.63 (Mean: 18.91) | POTENSI LEAKAGE: In-season (Hari 30 s/d 39) |
| 60 | `srad_V11` | Cuaca Gridded (Daymet) | Solar radiation per day over 10 days for interval V11 | MJ m-2 day-1 | `float64` | 0 (0.00%) | 12.84 s/d 26.12 (Mean: 18.88) | POTENSI LEAKAGE: In-season (Hari 40 s/d 49) |
| 61 | `srad_V12` | Cuaca Gridded (Daymet) | Solar radiation per day over 10 days for interval V12 | MJ m-2 day-1 | `float64` | 0 (0.00%) | 13.14 s/d 25.76 (Mean: 18.54) | POTENSI LEAKAGE: In-season (Hari 50 s/d 59) |
| 62 | `srad_V13` | Cuaca Gridded (Daymet) | Solar radiation per day over 10 days for interval V13 | MJ m-2 day-1 | `float64` | 0 (0.00%) | 12.17 s/d 25.67 (Mean: 18.10) | POTENSI LEAKAGE: In-season (Hari 60 s/d 69) |
| 63 | `srad_V14` | Cuaca Gridded (Daymet) | Solar radiation per day over 10 days for interval V14 | MJ m-2 day-1 | `float64` | 0 (0.00%) | 12.64 s/d 26.07 (Mean: 17.60) | POTENSI LEAKAGE: In-season (Hari 70 s/d 79) |
| 64 | `srad_V15` | Cuaca Gridded (Daymet) | Solar radiation per day over 10 days for interval V15 | MJ m-2 day-1 | `float64` | 0 (0.00%) | 9.29 s/d 25.01 (Mean: 17.18) | POTENSI LEAKAGE: In-season (Hari 80 s/d 89) |
| 65 | `srad_V16` | Cuaca Gridded (Daymet) | Solar radiation per day over 10 days for interval V16 | MJ m-2 day-1 | `float64` | 0 (0.00%) | 10.34 s/d 24.79 (Mean: 16.76) | POTENSI LEAKAGE: In-season (Hari 90 s/d 99) |
| 66 | `srad_V17` | Cuaca Gridded (Daymet) | Solar radiation per day over 10 days for interval V17 | MJ m-2 day-1 | `float64` | 0 (0.00%) | 7.19 s/d 25.09 (Mean: 16.49) | POTENSI LEAKAGE: In-season (Hari 100 s/d 109) |
| 67 | `srad_V18` | Cuaca Gridded (Daymet) | Solar radiation per day over 10 days for interval V18 | MJ m-2 day-1 | `float64` | 0 (0.00%) | 7.75 s/d 22.85 (Mean: 16.31) | POTENSI LEAKAGE: In-season (Hari 110 s/d 119) |
| 68 | `srad_V19` | Cuaca Gridded (Daymet) | Solar radiation per day over 10 days for interval V19 | MJ m-2 day-1 | `float64` | 0 (0.00%) | 7.19 s/d 22.38 (Mean: 16.00) | POTENSI LEAKAGE: In-season (Hari 120 s/d 129) |
| 69 | `srad_V20` | Cuaca Gridded (Daymet) | Solar radiation per day over 10 days for interval V20 | MJ m-2 day-1 | `float64` | 0 (0.00%) | 6.99 s/d 22.94 (Mean: 15.77) | POTENSI LEAKAGE: In-season (Hari 130 s/d 139) |
| 70 | `srad_V21` | Cuaca Gridded (Daymet) | Solar radiation per day over 10 days for interval V21 | MJ m-2 day-1 | `float64` | 0 (0.00%) | 7.27 s/d 21.45 (Mean: 15.63) | POTENSI LEAKAGE: In-season (Hari 140 s/d 149) |
| 71 | `srad_V22` | Cuaca Gridded (Daymet) | Solar radiation per day over 10 days for interval V22 | MJ m-2 day-1 | `float64` | 0 (0.00%) | 6.78 s/d 21.25 (Mean: 15.48) | POTENSI LEAKAGE: In-season (Hari 150 s/d 159) |
| 72 | `srad_V23` | Cuaca Gridded (Daymet) | Solar radiation per day over 10 days for interval V23 | MJ m-2 day-1 | `float64` | 0 (0.00%) | 7.00 s/d 21.39 (Mean: 15.31) | POTENSI LEAKAGE: In-season (Hari 160 s/d 169) |
| 73 | `srad_V24` | Cuaca Gridded (Daymet) | Solar radiation per day over 10 days for interval V24 | MJ m-2 day-1 | `float64` | 0 (0.00%) | 7.77 s/d 23.18 (Mean: 15.22) | POTENSI LEAKAGE: In-season (Hari 170 s/d 179) |
| 74 | `srad_V25` | Cuaca Gridded (Daymet) | Solar radiation per day over 10 days for interval V25 | MJ m-2 day-1 | `float64` | 0 (0.00%) | 7.21 s/d 22.54 (Mean: 15.15) | POTENSI LEAKAGE: Post-season (Hari 180 s/d 189) |
| 75 | `srad_V26` | Cuaca Gridded (Daymet) | Solar radiation per day over 10 days for interval V26 | MJ m-2 day-1 | `float64` | 0 (0.00%) | 7.17 s/d 23.89 (Mean: 15.35) | POTENSI LEAKAGE: Post-season (Hari 190 s/d 199) |
| 76 | `srad_V27` | Cuaca Gridded (Daymet) | Solar radiation per day over 10 days for interval V27 | MJ m-2 day-1 | `float64` | 0 (0.00%) | 7.21 s/d 22.77 (Mean: 15.83) | POTENSI LEAKAGE: Post-season (Hari 200 s/d 209) |
| 77 | `srad_V28` | Cuaca Gridded (Daymet) | Solar radiation per day over 10 days for interval V28 | MJ m-2 day-1 | `float64` | 0 (0.00%) | 8.13 s/d 24.71 (Mean: 16.47) | POTENSI LEAKAGE: Post-season (Hari 210 s/d 219) |
| 78 | `srad_V29` | Cuaca Gridded (Daymet) | Solar radiation per day over 10 days for interval V29 | MJ m-2 day-1 | `float64` | 0 (0.00%) | 7.81 s/d 25.19 (Mean: 17.34) | POTENSI LEAKAGE: Post-season (Hari 220 s/d 229) |
| 79 | `srad_V30` | Cuaca Gridded (Daymet) | Solar radiation per day over 10 days for interval V30 | MJ m-2 day-1 | `float64` | 0 (0.00%) | 11.42 s/d 25.94 (Mean: 18.24) | POTENSI LEAKAGE: Post-season (Hari 230 s/d 239) |
| 80 | `tmax_V1` | Cuaca Gridded (Daymet) | Maximum temperature over 10 days for interval V1 | ⁰C | `float64` | 0 (0.00%) | 18.15 s/d 38.55 (Mean: 31.83) | Pre-planting (Hari -60 s/d -51) |
| 81 | `tmax_V2` | Cuaca Gridded (Daymet) | Maximum temperature over 10 days for interval V2 | ⁰C | `float64` | 0 (0.00%) | 18.45 s/d 39.20 (Mean: 31.84) | Pre-planting (Hari -50 s/d -41) |
| 82 | `tmax_V3` | Cuaca Gridded (Daymet) | Maximum temperature over 10 days for interval V3 | ⁰C | `float64` | 0 (0.00%) | 18.95 s/d 38.65 (Mean: 31.60) | Pre-planting (Hari -40 s/d -31) |
| 83 | `tmax_V4` | Cuaca Gridded (Daymet) | Maximum temperature over 10 days for interval V4 | ⁰C | `float64` | 0 (0.00%) | 19.75 s/d 37.40 (Mean: 31.19) | Pre-planting (Hari -30 s/d -21) |
| 84 | `tmax_V5` | Cuaca Gridded (Daymet) | Maximum temperature over 10 days for interval V5 | ⁰C | `float64` | 0 (0.00%) | 20.00 s/d 38.40 (Mean: 30.92) | Pre-planting (Hari -20 s/d -11) |
| 85 | `tmax_V6` | Cuaca Gridded (Daymet) | Maximum temperature over 10 days for interval V6 | ⁰C | `float64` | 0 (0.00%) | 18.40 s/d 38.15 (Mean: 30.59) | Pre-planting (Hari -10 s/d -1) |
| 86 | `tmax_V7` | Cuaca Gridded (Daymet) | Maximum temperature over 10 days for interval V7 | ⁰C | `float64` | 0 (0.00%) | 21.15 s/d 36.55 (Mean: 30.47) | POTENSI LEAKAGE: In-season (Hari 0 s/d 9) |
| 87 | `tmax_V8` | Cuaca Gridded (Daymet) | Maximum temperature over 10 days for interval V8 | ⁰C | `float64` | 0 (0.00%) | 20.45 s/d 36.55 (Mean: 30.44) | POTENSI LEAKAGE: In-season (Hari 10 s/d 19) |
| 88 | `tmax_V9` | Cuaca Gridded (Daymet) | Maximum temperature over 10 days for interval V9 | ⁰C | `float64` | 0 (0.00%) | 19.70 s/d 36.20 (Mean: 30.46) | POTENSI LEAKAGE: In-season (Hari 20 s/d 29) |
| 89 | `tmax_V10` | Cuaca Gridded (Daymet) | Maximum temperature over 10 days for interval V10 | ⁰C | `float64` | 0 (0.00%) | 20.20 s/d 36.30 (Mean: 30.48) | POTENSI LEAKAGE: In-season (Hari 30 s/d 39) |
| 90 | `tmax_V11` | Cuaca Gridded (Daymet) | Maximum temperature over 10 days for interval V11 | ⁰C | `float64` | 0 (0.00%) | 16.75 s/d 36.35 (Mean: 30.46) | POTENSI LEAKAGE: In-season (Hari 40 s/d 49) |
| 91 | `tmax_V12` | Cuaca Gridded (Daymet) | Maximum temperature over 10 days for interval V12 | ⁰C | `float64` | 0 (0.00%) | 20.40 s/d 36.00 (Mean: 30.35) | POTENSI LEAKAGE: In-season (Hari 50 s/d 59) |
| 92 | `tmax_V13` | Cuaca Gridded (Daymet) | Maximum temperature over 10 days for interval V13 | ⁰C | `float64` | 0 (0.00%) | 20.80 s/d 35.90 (Mean: 30.24) | POTENSI LEAKAGE: In-season (Hari 60 s/d 69) |
| 93 | `tmax_V14` | Cuaca Gridded (Daymet) | Maximum temperature over 10 days for interval V14 | ⁰C | `float64` | 0 (0.00%) | 21.05 s/d 36.15 (Mean: 30.15) | POTENSI LEAKAGE: In-season (Hari 70 s/d 79) |
| 94 | `tmax_V15` | Cuaca Gridded (Daymet) | Maximum temperature over 10 days for interval V15 | ⁰C | `float64` | 0 (0.00%) | 20.45 s/d 35.90 (Mean: 30.05) | POTENSI LEAKAGE: In-season (Hari 80 s/d 89) |
| 95 | `tmax_V16` | Cuaca Gridded (Daymet) | Maximum temperature over 10 days for interval V16 | ⁰C | `float64` | 0 (0.00%) | 20.45 s/d 35.95 (Mean: 29.92) | POTENSI LEAKAGE: In-season (Hari 90 s/d 99) |
| 96 | `tmax_V17` | Cuaca Gridded (Daymet) | Maximum temperature over 10 days for interval V17 | ⁰C | `float64` | 0 (0.00%) | 21.15 s/d 35.65 (Mean: 29.78) | POTENSI LEAKAGE: In-season (Hari 100 s/d 109) |
| 97 | `tmax_V18` | Cuaca Gridded (Daymet) | Maximum temperature over 10 days for interval V18 | ⁰C | `float64` | 0 (0.00%) | 21.40 s/d 35.30 (Mean: 29.63) | POTENSI LEAKAGE: In-season (Hari 110 s/d 119) |
| 98 | `tmax_V19` | Cuaca Gridded (Daymet) | Maximum temperature over 10 days for interval V19 | ⁰C | `float64` | 0 (0.00%) | 20.80 s/d 35.15 (Mean: 29.43) | POTENSI LEAKAGE: In-season (Hari 120 s/d 129) |
| 99 | `tmax_V20` | Cuaca Gridded (Daymet) | Maximum temperature over 10 days for interval V20 | ⁰C | `float64` | 0 (0.00%) | 21.05 s/d 35.60 (Mean: 29.19) | POTENSI LEAKAGE: In-season (Hari 130 s/d 139) |
| 100 | `tmax_V21` | Cuaca Gridded (Daymet) | Maximum temperature over 10 days for interval V21 | ⁰C | `float64` | 0 (0.00%) | 19.70 s/d 35.05 (Mean: 28.96) | POTENSI LEAKAGE: In-season (Hari 140 s/d 149) |
| 101 | `tmax_V22` | Cuaca Gridded (Daymet) | Maximum temperature over 10 days for interval V22 | ⁰C | `float64` | 0 (0.00%) | 19.05 s/d 35.20 (Mean: 28.84) | POTENSI LEAKAGE: In-season (Hari 150 s/d 159) |
| 102 | `tmax_V23` | Cuaca Gridded (Daymet) | Maximum temperature over 10 days for interval V23 | ⁰C | `float64` | 0 (0.00%) | 17.10 s/d 34.95 (Mean: 28.68) | POTENSI LEAKAGE: In-season (Hari 160 s/d 169) |
| 103 | `tmax_V24` | Cuaca Gridded (Daymet) | Maximum temperature over 10 days for interval V24 | ⁰C | `float64` | 0 (0.00%) | 18.65 s/d 35.45 (Mean: 28.48) | POTENSI LEAKAGE: In-season (Hari 170 s/d 179) |
| 104 | `tmax_V25` | Cuaca Gridded (Daymet) | Maximum temperature over 10 days for interval V25 | ⁰C | `float64` | 0 (0.00%) | 16.75 s/d 35.65 (Mean: 28.35) | POTENSI LEAKAGE: Post-season (Hari 180 s/d 189) |
| 105 | `tmax_V26` | Cuaca Gridded (Daymet) | Maximum temperature over 10 days for interval V26 | ⁰C | `float64` | 0 (0.00%) | 16.60 s/d 34.80 (Mean: 28.28) | POTENSI LEAKAGE: Post-season (Hari 190 s/d 199) |
| 106 | `tmax_V27` | Cuaca Gridded (Daymet) | Maximum temperature over 10 days for interval V27 | ⁰C | `float64` | 0 (0.00%) | 18.45 s/d 34.95 (Mean: 28.34) | POTENSI LEAKAGE: Post-season (Hari 200 s/d 209) |
| 107 | `tmax_V28` | Cuaca Gridded (Daymet) | Maximum temperature over 10 days for interval V28 | ⁰C | `float64` | 0 (0.00%) | 17.65 s/d 35.00 (Mean: 28.43) | POTENSI LEAKAGE: Post-season (Hari 210 s/d 219) |
| 108 | `tmax_V29` | Cuaca Gridded (Daymet) | Maximum temperature over 10 days for interval V29 | ⁰C | `float64` | 0 (0.00%) | 18.90 s/d 35.40 (Mean: 28.82) | POTENSI LEAKAGE: Post-season (Hari 220 s/d 229) |
| 109 | `tmax_V30` | Cuaca Gridded (Daymet) | Maximum temperature over 10 days for interval V30 | ⁰C | `float64` | 0 (0.00%) | 18.40 s/d 35.60 (Mean: 29.27) | POTENSI LEAKAGE: Post-season (Hari 230 s/d 239) |
| 110 | `tmin_V1` | Cuaca Gridded (Daymet) | Minimum temperature over 10 days for interval V1 | ⁰C | `float64` | 0 (0.00%) | 2.45 s/d 24.20 (Mean: 17.41) | Pre-planting (Hari -60 s/d -51) |
| 111 | `tmin_V2` | Cuaca Gridded (Daymet) | Minimum temperature over 10 days for interval V2 | ⁰C | `float64` | 0 (0.00%) | 4.00 s/d 24.55 (Mean: 17.80) | Pre-planting (Hari -50 s/d -41) |
| 112 | `tmin_V3` | Cuaca Gridded (Daymet) | Minimum temperature over 10 days for interval V3 | ⁰C | `float64` | 0 (0.00%) | 4.80 s/d 23.95 (Mean: 18.13) | Pre-planting (Hari -40 s/d -31) |
| 113 | `tmin_V4` | Cuaca Gridded (Daymet) | Minimum temperature over 10 days for interval V4 | ⁰C | `float64` | 0 (0.00%) | 5.40 s/d 23.65 (Mean: 18.34) | Pre-planting (Hari -30 s/d -21) |
| 114 | `tmin_V5` | Cuaca Gridded (Daymet) | Minimum temperature over 10 days for interval V5 | ⁰C | `float64` | 0 (0.00%) | 6.80 s/d 24.10 (Mean: 18.49) | Pre-planting (Hari -20 s/d -11) |
| 115 | `tmin_V6` | Cuaca Gridded (Daymet) | Minimum temperature over 10 days for interval V6 | ⁰C | `float64` | 0 (0.00%) | 8.05 s/d 24.65 (Mean: 18.53) | Pre-planting (Hari -10 s/d -1) |
| 116 | `tmin_V7` | Cuaca Gridded (Daymet) | Minimum temperature over 10 days for interval V7 | ⁰C | `float64` | 0 (0.00%) | 9.25 s/d 24.35 (Mean: 18.54) | POTENSI LEAKAGE: In-season (Hari 0 s/d 9) |
| 117 | `tmin_V8` | Cuaca Gridded (Daymet) | Minimum temperature over 10 days for interval V8 | ⁰C | `float64` | 0 (0.00%) | 8.80 s/d 24.00 (Mean: 18.45) | POTENSI LEAKAGE: In-season (Hari 10 s/d 19) |
| 118 | `tmin_V9` | Cuaca Gridded (Daymet) | Minimum temperature over 10 days for interval V9 | ⁰C | `float64` | 0 (0.00%) | 8.60 s/d 24.30 (Mean: 18.41) | POTENSI LEAKAGE: In-season (Hari 20 s/d 29) |
| 119 | `tmin_V10` | Cuaca Gridded (Daymet) | Minimum temperature over 10 days for interval V10 | ⁰C | `float64` | 0 (0.00%) | 8.10 s/d 24.60 (Mean: 18.39) | POTENSI LEAKAGE: In-season (Hari 30 s/d 39) |
| 120 | `tmin_V11` | Cuaca Gridded (Daymet) | Minimum temperature over 10 days for interval V11 | ⁰C | `float64` | 0 (0.00%) | 7.80 s/d 24.20 (Mean: 18.32) | POTENSI LEAKAGE: In-season (Hari 40 s/d 49) |
| 121 | `tmin_V12` | Cuaca Gridded (Daymet) | Minimum temperature over 10 days for interval V12 | ⁰C | `float64` | 0 (0.00%) | 7.30 s/d 24.65 (Mean: 18.31) | POTENSI LEAKAGE: In-season (Hari 50 s/d 59) |
| 122 | `tmin_V13` | Cuaca Gridded (Daymet) | Minimum temperature over 10 days for interval V13 | ⁰C | `float64` | 0 (0.00%) | 7.35 s/d 24.65 (Mean: 18.31) | POTENSI LEAKAGE: In-season (Hari 60 s/d 69) |
| 123 | `tmin_V14` | Cuaca Gridded (Daymet) | Minimum temperature over 10 days for interval V14 | ⁰C | `float64` | 0 (0.00%) | 7.25 s/d 24.60 (Mean: 18.37) | POTENSI LEAKAGE: In-season (Hari 70 s/d 79) |
| 124 | `tmin_V15` | Cuaca Gridded (Daymet) | Minimum temperature over 10 days for interval V15 | ⁰C | `float64` | 0 (0.00%) | 6.00 s/d 29.85 (Mean: 18.42) | POTENSI LEAKAGE: In-season (Hari 80 s/d 89) |
| 125 | `tmin_V16` | Cuaca Gridded (Daymet) | Minimum temperature over 10 days for interval V16 | ⁰C | `float64` | 0 (0.00%) | 6.10 s/d 27.05 (Mean: 18.46) | POTENSI LEAKAGE: In-season (Hari 90 s/d 99) |
| 126 | `tmin_V17` | Cuaca Gridded (Daymet) | Minimum temperature over 10 days for interval V17 | ⁰C | `float64` | 0 (0.00%) | 7.55 s/d 32.00 (Mean: 18.39) | POTENSI LEAKAGE: In-season (Hari 100 s/d 109) |
| 127 | `tmin_V18` | Cuaca Gridded (Daymet) | Minimum temperature over 10 days for interval V18 | ⁰C | `float64` | 0 (0.00%) | 6.10 s/d 30.10 (Mean: 18.21) | POTENSI LEAKAGE: In-season (Hari 110 s/d 119) |
| 128 | `tmin_V19` | Cuaca Gridded (Daymet) | Minimum temperature over 10 days for interval V19 | ⁰C | `float64` | 0 (0.00%) | 6.70 s/d 31.95 (Mean: 18.04) | POTENSI LEAKAGE: In-season (Hari 120 s/d 129) |
| 129 | `tmin_V20` | Cuaca Gridded (Daymet) | Minimum temperature over 10 days for interval V20 | ⁰C | `float64` | 0 (0.00%) | 5.55 s/d 32.05 (Mean: 17.76) | POTENSI LEAKAGE: In-season (Hari 130 s/d 139) |
| 130 | `tmin_V21` | Cuaca Gridded (Daymet) | Minimum temperature over 10 days for interval V21 | ⁰C | `float64` | 0 (0.00%) | 4.00 s/d 31.90 (Mean: 17.28) | POTENSI LEAKAGE: In-season (Hari 140 s/d 149) |
| 131 | `tmin_V22` | Cuaca Gridded (Daymet) | Minimum temperature over 10 days for interval V22 | ⁰C | `float64` | 0 (0.00%) | 2.35 s/d 36.25 (Mean: 16.86) | POTENSI LEAKAGE: In-season (Hari 150 s/d 159) |
| 132 | `tmin_V23` | Cuaca Gridded (Daymet) | Minimum temperature over 10 days for interval V23 | ⁰C | `float64` | 0 (0.00%) | 3.15 s/d 31.60 (Mean: 16.34) | POTENSI LEAKAGE: In-season (Hari 160 s/d 169) |
| 133 | `tmin_V24` | Cuaca Gridded (Daymet) | Minimum temperature over 10 days for interval V24 | ⁰C | `float64` | 0 (0.00%) | 1.20 s/d 30.10 (Mean: 15.89) | POTENSI LEAKAGE: In-season (Hari 170 s/d 179) |
| 134 | `tmin_V25` | Cuaca Gridded (Daymet) | Minimum temperature over 10 days for interval V25 | ⁰C | `float64` | 0 (0.00%) | 0.65 s/d 35.60 (Mean: 15.66) | POTENSI LEAKAGE: Post-season (Hari 180 s/d 189) |
| 135 | `tmin_V26` | Cuaca Gridded (Daymet) | Minimum temperature over 10 days for interval V26 | ⁰C | `float64` | 0 (0.00%) | 0.80 s/d 35.50 (Mean: 15.39) | POTENSI LEAKAGE: Post-season (Hari 190 s/d 199) |
| 136 | `tmin_V27` | Cuaca Gridded (Daymet) | Minimum temperature over 10 days for interval V27 | ⁰C | `float64` | 0 (0.00%) | -0.10 s/d 29.70 (Mean: 15.13) | POTENSI LEAKAGE: Post-season (Hari 200 s/d 209) |
| 137 | `tmin_V28` | Cuaca Gridded (Daymet) | Minimum temperature over 10 days for interval V28 | ⁰C | `float64` | 0 (0.00%) | 1.50 s/d 30.55 (Mean: 15.04) | POTENSI LEAKAGE: Post-season (Hari 210 s/d 219) |
| 138 | `tmin_V29` | Cuaca Gridded (Daymet) | Minimum temperature over 10 days for interval V29 | ⁰C | `float64` | 0 (0.00%) | -2.15 s/d 27.05 (Mean: 15.13) | POTENSI LEAKAGE: Post-season (Hari 220 s/d 229) |
| 139 | `tmin_V30` | Cuaca Gridded (Daymet) | Minimum temperature over 10 days for interval V30 | ⁰C | `float64` | 0 (0.00%) | -1.40 s/d 22.55 (Mean: 15.29) | POTENSI LEAKAGE: Post-season (Hari 230 s/d 239) |
| 140 | `vp_V1` | Cuaca Gridded (Daymet) | Vapor pressure over 10 days for interval V1 | Pa | `int64` | 0 (0.00%) | 252.00 s/d 2772.00 (Mean: 805.31) | Pre-planting (Hari -60 s/d -51) |
| 141 | `vp_V2` | Cuaca Gridded (Daymet) | Vapor pressure over 10 days for interval V2 | Pa | `int64` | 0 (0.00%) | 292.00 s/d 2844.00 (Mean: 879.38) | Pre-planting (Hari -50 s/d -41) |
| 142 | `vp_V3` | Cuaca Gridded (Daymet) | Vapor pressure over 10 days for interval V3 | Pa | `int64` | 0 (0.00%) | 304.00 s/d 2812.00 (Mean: 1035.26) | Pre-planting (Hari -40 s/d -31) |
| 143 | `vp_V4` | Cuaca Gridded (Daymet) | Vapor pressure over 10 days for interval V4 | Pa | `int64` | 0 (0.00%) | 320.00 s/d 2852.00 (Mean: 1275.90) | Pre-planting (Hari -30 s/d -21) |
| 144 | `vp_V5` | Cuaca Gridded (Daymet) | Vapor pressure over 10 days for interval V5 | Pa | `int64` | 0 (0.00%) | 360.00 s/d 2856.00 (Mean: 1554.58) | Pre-planting (Hari -20 s/d -11) |
| 145 | `vp_V6` | Cuaca Gridded (Daymet) | Vapor pressure over 10 days for interval V6 | Pa | `int64` | 0 (0.00%) | 388.00 s/d 2936.00 (Mean: 1774.09) | Pre-planting (Hari -10 s/d -1) |
| 146 | `vp_V7` | Cuaca Gridded (Daymet) | Vapor pressure over 10 days for interval V7 | Pa | `int64` | 0 (0.00%) | 424.00 s/d 2888.00 (Mean: 1909.60) | POTENSI LEAKAGE: In-season (Hari 0 s/d 9) |
| 147 | `vp_V8` | Cuaca Gridded (Daymet) | Vapor pressure over 10 days for interval V8 | Pa | `int64` | 0 (0.00%) | 424.00 s/d 2988.00 (Mean: 1981.38) | POTENSI LEAKAGE: In-season (Hari 10 s/d 19) |
| 148 | `vp_V9` | Cuaca Gridded (Daymet) | Vapor pressure over 10 days for interval V9 | Pa | `int64` | 0 (0.00%) | 472.00 s/d 2940.00 (Mean: 2054.22) | POTENSI LEAKAGE: In-season (Hari 20 s/d 29) |
| 149 | `vp_V10` | Cuaca Gridded (Daymet) | Vapor pressure over 10 days for interval V10 | Pa | `int64` | 0 (0.00%) | 444.00 s/d 3092.00 (Mean: 2098.59) | POTENSI LEAKAGE: In-season (Hari 30 s/d 39) |
| 150 | `vp_V11` | Cuaca Gridded (Daymet) | Vapor pressure over 10 days for interval V11 | Pa | `int64` | 0 (0.00%) | 548.00 s/d 3108.00 (Mean: 2108.31) | POTENSI LEAKAGE: In-season (Hari 40 s/d 49) |
| 151 | `vp_V12` | Cuaca Gridded (Daymet) | Vapor pressure over 10 days for interval V12 | Pa | `int64` | 0 (0.00%) | 568.00 s/d 3112.00 (Mean: 2118.66) | POTENSI LEAKAGE: In-season (Hari 50 s/d 59) |
| 152 | `vp_V13` | Cuaca Gridded (Daymet) | Vapor pressure over 10 days for interval V13 | Pa | `int64` | 0 (0.00%) | 1036.00 s/d 3196.00 (Mean: 2127.13) | POTENSI LEAKAGE: In-season (Hari 60 s/d 69) |
| 153 | `vp_V14` | Cuaca Gridded (Daymet) | Vapor pressure over 10 days for interval V14 | Pa | `int64` | 0 (0.00%) | 1024.00 s/d 3196.00 (Mean: 2138.98) | POTENSI LEAKAGE: In-season (Hari 70 s/d 79) |
| 154 | `vp_V15` | Cuaca Gridded (Daymet) | Vapor pressure over 10 days for interval V15 | Pa | `int64` | 0 (0.00%) | 940.00 s/d 4916.00 (Mean: 2146.55) | POTENSI LEAKAGE: In-season (Hari 80 s/d 89) |
| 155 | `vp_V16` | Cuaca Gridded (Daymet) | Vapor pressure over 10 days for interval V16 | Pa | `int64` | 0 (0.00%) | 948.00 s/d 4224.00 (Mean: 2153.25) | POTENSI LEAKAGE: In-season (Hari 90 s/d 99) |
| 156 | `vp_V17` | Cuaca Gridded (Daymet) | Vapor pressure over 10 days for interval V17 | Pa | `int64` | 0 (0.00%) | 1052.00 s/d 5536.00 (Mean: 2144.31) | POTENSI LEAKAGE: In-season (Hari 100 s/d 109) |
| 157 | `vp_V18` | Cuaca Gridded (Daymet) | Vapor pressure over 10 days for interval V18 | Pa | `int64` | 0 (0.00%) | 956.00 s/d 4948.00 (Mean: 2117.87) | POTENSI LEAKAGE: In-season (Hari 110 s/d 119) |
| 158 | `vp_V19` | Cuaca Gridded (Daymet) | Vapor pressure over 10 days for interval V19 | Pa | `int64` | 0 (0.00%) | 952.00 s/d 5532.00 (Mean: 2104.71) | POTENSI LEAKAGE: In-season (Hari 120 s/d 129) |
| 159 | `vp_V20` | Cuaca Gridded (Daymet) | Vapor pressure over 10 days for interval V20 | Pa | `int64` | 0 (0.00%) | 892.00 s/d 5572.00 (Mean: 2082.94) | POTENSI LEAKAGE: In-season (Hari 130 s/d 139) |
| 160 | `vp_V21` | Cuaca Gridded (Daymet) | Vapor pressure over 10 days for interval V21 | Pa | `int64` | 0 (0.00%) | 516.00 s/d 5524.00 (Mean: 2026.76) | POTENSI LEAKAGE: In-season (Hari 140 s/d 149) |
| 161 | `vp_V22` | Cuaca Gridded (Daymet) | Vapor pressure over 10 days for interval V22 | Pa | `int64` | 0 (0.00%) | 348.00 s/d 6452.00 (Mean: 1991.36) | POTENSI LEAKAGE: In-season (Hari 150 s/d 159) |
| 162 | `vp_V23` | Cuaca Gridded (Daymet) | Vapor pressure over 10 days for interval V23 | Pa | `int64` | 0 (0.00%) | 356.00 s/d 5428.00 (Mean: 1913.87) | POTENSI LEAKAGE: In-season (Hari 160 s/d 169) |
| 163 | `vp_V24` | Cuaca Gridded (Daymet) | Vapor pressure over 10 days for interval V24 | Pa | `int64` | 0 (0.00%) | 388.00 s/d 4844.00 (Mean: 1827.20) | POTENSI LEAKAGE: In-season (Hari 170 s/d 179) |
| 164 | `vp_V25` | Cuaca Gridded (Daymet) | Vapor pressure over 10 days for interval V25 | Pa | `int64` | 0 (0.00%) | 376.00 s/d 6292.00 (Mean: 1761.27) | POTENSI LEAKAGE: Post-season (Hari 180 s/d 189) |
| 165 | `vp_V26` | Cuaca Gridded (Daymet) | Vapor pressure over 10 days for interval V26 | Pa | `int64` | 0 (0.00%) | 412.00 s/d 6284.00 (Mean: 1652.64) | POTENSI LEAKAGE: Post-season (Hari 190 s/d 199) |
| 166 | `vp_V27` | Cuaca Gridded (Daymet) | Vapor pressure over 10 days for interval V27 | Pa | `int64` | 0 (0.00%) | 416.00 s/d 4692.00 (Mean: 1520.10) | POTENSI LEAKAGE: Post-season (Hari 200 s/d 209) |
| 167 | `vp_V28` | Cuaca Gridded (Daymet) | Vapor pressure over 10 days for interval V28 | Pa | `int64` | 0 (0.00%) | 332.00 s/d 4808.00 (Mean: 1348.54) | POTENSI LEAKAGE: Post-season (Hari 210 s/d 219) |
| 168 | `vp_V29` | Cuaca Gridded (Daymet) | Vapor pressure over 10 days for interval V29 | Pa | `int64` | 0 (0.00%) | 300.00 s/d 4540.00 (Mean: 1185.69) | POTENSI LEAKAGE: Post-season (Hari 220 s/d 229) |
| 169 | `vp_V30` | Cuaca Gridded (Daymet) | Vapor pressure over 10 days for interval V30 | Pa | `int64` | 0 (0.00%) | 312.00 s/d 3000.00 (Mean: 1032.25) | POTENSI LEAKAGE: Post-season (Hari 230 s/d 239) |

---

## 4. Panduan Penggunaan Kamus Data untuk Penelitian Skripsi
1. **Pemilihan Variabel Target:**
   - Gunakan `YIELD` (Mg ha⁻¹ = ton ha⁻¹) sebagai target estimasi produktivitas lahan riil.
   - Jangan gunakan `Mun_yield` sebagai target. `Mun_yield` adalah statistik agregat tingkat munisipal dari SIAP yang hanya berfungsi sebagai pembanding makro atau kovariat regional.
2. **Pemisahan Prediktor Berdasarkan Waktu Keputusan (Decision Horizon):**
   - **Model Perencanaan Sebelum Tanam (Pre-Planting Planning):** Gunakan fitur geografi (`Elev`), karakteristik tanah (`Slope`, `Clay`, `CEC`, `SOM`, `PH`), rencana budidaya (`System`, `Tillage`, `Planting`, `Nitrogen`, `Phosphorus`, `Potassium`), dan cuaca historis pra-tanam (`*_V1` s/d `*_V6`). Hindari `*_V7` s/d `*_V30` untuk mencegah data leakage.
   - **Model Evaluasi Hasil / Explanatory Machine Learning (Post-Harvest):** Seluruh variabel cuaca `*_V1` s/d `*_V24` dapat diikutsertakan untuk mengidentifikasi pembatas hasil (*yield gap analysis*).
3. **Kebutuhan Kalibrasi Lokal ASA Indonesia:**
   - Variabel agronomi seperti `System` (Hybrid vs Landrace) dan dosis pupuk N-P-K harus dipetakan terhadap praktik budidaya lokal jagung Madura di Komunitas ASA.
