# Data Dictionary — Chiapas Field Data 2012–2018

## Ringkasan

- **Jumlah kolom:** 169
- **Jumlah observasi pada file:** 4,585
- **Sumber definisi:** sheet `Legend` pada workbook asli.
- **Tipe data:** tipe hasil pembacaan nilai pada sheet `Data` menggunakan pandas; tipe ini dapat berubah saat file dibaca dengan perangkat lunak lain.
- **Nilai kosong:** dihitung dari sheet `Data` pada workbook yang diberikan.

Kolom `Variable` dan `Description` mengikuti definisi sumber. Tipe data dan jumlah missing value merupakan hasil pemeriksaan file, bukan metadata yang dinyatakan oleh pembuat dataset.

## Definisi variabel

| No. | Variable | Description | Unit (as provided) | Tipe data teramati | Missing |
|---:|---|---|---|---|---:|
| 1 | `Field_ID` | Unique identifier for each field | Not specified | Integer (numeric) | 0 |
| 2 | `YIELD` | Field maize yield | Mg ha-1 | Float (numeric) | 0 |
| 3 | `Year` | Year of cropping event | Not specified | Integer (numeric) | 0 |
| 4 | `Mun_yield` | Average maize yield in a municipality | Mg ha-1 | Float (numeric) | 0 |
| 5 | `Lat` | Latitude coordinates | Degrees | Float (numeric) | 0 |
| 6 | `Long` | Longitude coordinates | Degrees | Float (numeric) | 0 |
| 7 | `Elev` | Elevation | m above sea level | Integer (numeric) | 0 |
| 8 | `System` | Characterization of Hybrid or Landrace based cropping system | Hybrid or Landrace | Text / categorical | 0 |
| 9 | `Cultivar` | Genotype information | Name of cultivar if available | Text / categorical | 310 |
| 10 | `Tillage` | Tillage practices including Conventional, Reduced, and No-Till | Conventional/Reduced/No-Till | Text / categorical | 0 |
| 11 | `Planting` | Day of the year when maize was planted | Day of Year (DOY) | Integer (numeric) | 0 |
| 12 | `Nitrogen` | Nitrogen added as fertilizer | kg N ha-1 | Float (numeric) | 0 |
| 13 | `Phosphorus` | Phosphorus added as fertilizer | kg P2O5 ha-1 | Float (numeric) | 0 |
| 14 | `Potassium` | Potassium added as fertilizer | kg K2O ha-1 | Float (numeric) | 0 |
| 15 | `Slope` | Field slope | % | Float (numeric) | 0 |
| 16 | `Clay` | Soil clay content | % | Integer (numeric) | 0 |
| 17 | `CEC` | Cation Exchange Capacity | cmolc dm-3 | Float (numeric) | 0 |
| 18 | `SOM` | Soil Organic Matter | % | Float (numeric) | 0 |
| 19 | `PH` | Soil pH | Not specified | Float (numeric) | 0 |
| 20 | `prcp_V1` | Precipitation per day over 10 days for interval V1 | mm day-1 | Float (numeric) | 0 |
| 21 | `prcp_V2` | Precipitation per day over 10 days for interval V2 | mm day-1 | Float (numeric) | 0 |
| 22 | `prcp_V3` | Precipitation per day over 10 days for interval V3 | mm day-1 | Float (numeric) | 0 |
| 23 | `prcp_V4` | Precipitation per day over 10 days for interval V4 | mm day-1 | Float (numeric) | 0 |
| 24 | `prcp_V5` | Precipitation per day over 10 days for interval V5 | mm day-1 | Float (numeric) | 0 |
| 25 | `prcp_V6` | Precipitation per day over 10 days for interval V6 | mm day-1 | Float (numeric) | 0 |
| 26 | `prcp_V7` | Precipitation per day over 10 days for interval V7 | mm day-1 | Float (numeric) | 0 |
| 27 | `prcp_V8` | Precipitation per day over 10 days for interval V8 | mm day-1 | Float (numeric) | 0 |
| 28 | `prcp_V9` | Precipitation per day over 10 days for interval V9 | mm day-1 | Float (numeric) | 0 |
| 29 | `prcp_V10` | Precipitation per day over 10 days for interval V10 | mm day-1 | Float (numeric) | 0 |
| 30 | `prcp_V11` | Precipitation per day over 10 days for interval V11 | mm day-1 | Float (numeric) | 0 |
| 31 | `prcp_V12` | Precipitation per day over 10 days for interval V12 | mm day-1 | Float (numeric) | 0 |
| 32 | `prcp_V13` | Precipitation per day over 10 days for interval V13 | mm day-1 | Float (numeric) | 0 |
| 33 | `prcp_V14` | Precipitation per day over 10 days for interval V14 | mm day-1 | Float (numeric) | 0 |
| 34 | `prcp_V15` | Precipitation per day over 10 days for interval V15 | mm day-1 | Float (numeric) | 0 |
| 35 | `prcp_V16` | Precipitation per day over 10 days for interval V16 | mm day-1 | Float (numeric) | 0 |
| 36 | `prcp_V17` | Precipitation per day over 10 days for interval V17 | mm day-1 | Float (numeric) | 0 |
| 37 | `prcp_V18` | Precipitation per day over 10 days for interval V18 | mm day-1 | Float (numeric) | 0 |
| 38 | `prcp_V19` | Precipitation per day over 10 days for interval V19 | mm day-1 | Float (numeric) | 0 |
| 39 | `prcp_V20` | Precipitation per day over 10 days for interval V20 | mm day-1 | Float (numeric) | 0 |
| 40 | `prcp_V21` | Precipitation per day over 10 days for interval V21 | mm day-1 | Float (numeric) | 0 |
| 41 | `prcp_V22` | Precipitation per day over 10 days for interval V22 | mm day-1 | Float (numeric) | 0 |
| 42 | `prcp_V23` | Precipitation per day over 10 days for interval V23 | mm day-1 | Float (numeric) | 0 |
| 43 | `prcp_V24` | Precipitation per day over 10 days for interval V24 | mm day-1 | Float (numeric) | 0 |
| 44 | `prcp_V25` | Precipitation per day over 10 days for interval V25 | mm day-1 | Float (numeric) | 0 |
| 45 | `prcp_V26` | Precipitation per day over 10 days for interval V26 | mm day-1 | Float (numeric) | 0 |
| 46 | `prcp_V27` | Precipitation per day over 10 days for interval V27 | mm day-1 | Float (numeric) | 0 |
| 47 | `prcp_V28` | Precipitation per day over 10 days for interval V28 | mm day-1 | Float (numeric) | 0 |
| 48 | `prcp_V29` | Precipitation per day over 10 days for interval V29 | mm day-1 | Float (numeric) | 0 |
| 49 | `prcp_V30` | Precipitation per day over 10 days for interval V30 | mm day-1 | Float (numeric) | 0 |
| 50 | `srad_V1` | Solar radiation per day over 10 days for interval V1 | MJ m-2 day-1 | Float (numeric) | 0 |
| 51 | `srad_V2` | Solar radiation per day over 10 days for interval V2 | MJ m-2 day-1 | Float (numeric) | 0 |
| 52 | `srad_V3` | Solar radiation per day over 10 days for interval V3 | MJ m-2 day-1 | Float (numeric) | 0 |
| 53 | `srad_V4` | Solar radiation per day over 10 days for interval V4 | MJ m-2 day-1 | Float (numeric) | 0 |
| 54 | `srad_V5` | Solar radiation per day over 10 days for interval V5 | MJ m-2 day-1 | Float (numeric) | 0 |
| 55 | `srad_V6` | Solar radiation per day over 10 days for interval V6 | MJ m-2 day-1 | Float (numeric) | 0 |
| 56 | `srad_V7` | Solar radiation per day over 10 days for interval V7 | MJ m-2 day-1 | Float (numeric) | 0 |
| 57 | `srad_V8` | Solar radiation per day over 10 days for interval V8 | MJ m-2 day-1 | Float (numeric) | 0 |
| 58 | `srad_V9` | Solar radiation per day over 10 days for interval V9 | MJ m-2 day-1 | Float (numeric) | 0 |
| 59 | `srad_V10` | Solar radiation per day over 10 days for interval V10 | MJ m-2 day-1 | Float (numeric) | 0 |
| 60 | `srad_V11` | Solar radiation per day over 10 days for interval V11 | MJ m-2 day-1 | Float (numeric) | 0 |
| 61 | `srad_V12` | Solar radiation per day over 10 days for interval V12 | MJ m-2 day-1 | Float (numeric) | 0 |
| 62 | `srad_V13` | Solar radiation per day over 10 days for interval V13 | MJ m-2 day-1 | Float (numeric) | 0 |
| 63 | `srad_V14` | Solar radiation per day over 10 days for interval V14 | MJ m-2 day-1 | Float (numeric) | 0 |
| 64 | `srad_V15` | Solar radiation per day over 10 days for interval V15 | MJ m-2 day-1 | Float (numeric) | 0 |
| 65 | `srad_V16` | Solar radiation per day over 10 days for interval V16 | MJ m-2 day-1 | Float (numeric) | 0 |
| 66 | `srad_V17` | Solar radiation per day over 10 days for interval V17 | MJ m-2 day-1 | Float (numeric) | 0 |
| 67 | `srad_V18` | Solar radiation per day over 10 days for interval V18 | MJ m-2 day-1 | Float (numeric) | 0 |
| 68 | `srad_V19` | Solar radiation per day over 10 days for interval V19 | MJ m-2 day-1 | Float (numeric) | 0 |
| 69 | `srad_V20` | Solar radiation per day over 10 days for interval V20 | MJ m-2 day-1 | Float (numeric) | 0 |
| 70 | `srad_V21` | Solar radiation per day over 10 days for interval V21 | MJ m-2 day-1 | Float (numeric) | 0 |
| 71 | `srad_V22` | Solar radiation per day over 10 days for interval V22 | MJ m-2 day-1 | Float (numeric) | 0 |
| 72 | `srad_V23` | Solar radiation per day over 10 days for interval V23 | MJ m-2 day-1 | Float (numeric) | 0 |
| 73 | `srad_V24` | Solar radiation per day over 10 days for interval V24 | MJ m-2 day-1 | Float (numeric) | 0 |
| 74 | `srad_V25` | Solar radiation per day over 10 days for interval V25 | MJ m-2 day-1 | Float (numeric) | 0 |
| 75 | `srad_V26` | Solar radiation per day over 10 days for interval V26 | MJ m-2 day-1 | Float (numeric) | 0 |
| 76 | `srad_V27` | Solar radiation per day over 10 days for interval V27 | MJ m-2 day-1 | Float (numeric) | 0 |
| 77 | `srad_V28` | Solar radiation per day over 10 days for interval V28 | MJ m-2 day-1 | Float (numeric) | 0 |
| 78 | `srad_V29` | Solar radiation per day over 10 days for interval V29 | MJ m-2 day-1 | Float (numeric) | 0 |
| 79 | `srad_V30` | Solar radiation per day over 10 days for interval V30 | MJ m-2 day-1 | Float (numeric) | 0 |
| 80 | `tmax_V1` | Maximum temperature over 10 days for interval V1 | ⁰C | Float (numeric) | 0 |
| 81 | `tmax_V2` | Maximum temperature over 10 days for interval V2 | ⁰C | Float (numeric) | 0 |
| 82 | `tmax_V3` | Maximum temperature over 10 days for interval V3 | ⁰C | Float (numeric) | 0 |
| 83 | `tmax_V4` | Maximum temperature over 10 days for interval V4 | ⁰C | Float (numeric) | 0 |
| 84 | `tmax_V5` | Maximum temperature over 10 days for interval V5 | ⁰C | Float (numeric) | 0 |
| 85 | `tmax_V6` | Maximum temperature over 10 days for interval V6 | ⁰C | Float (numeric) | 0 |
| 86 | `tmax_V7` | Maximum temperature over 10 days for interval V7 | ⁰C | Float (numeric) | 0 |
| 87 | `tmax_V8` | Maximum temperature over 10 days for interval V8 | ⁰C | Float (numeric) | 0 |
| 88 | `tmax_V9` | Maximum temperature over 10 days for interval V9 | ⁰C | Float (numeric) | 0 |
| 89 | `tmax_V10` | Maximum temperature over 10 days for interval V10 | ⁰C | Float (numeric) | 0 |
| 90 | `tmax_V11` | Maximum temperature over 10 days for interval V11 | ⁰C | Float (numeric) | 0 |
| 91 | `tmax_V12` | Maximum temperature over 10 days for interval V12 | ⁰C | Float (numeric) | 0 |
| 92 | `tmax_V13` | Maximum temperature over 10 days for interval V13 | ⁰C | Float (numeric) | 0 |
| 93 | `tmax_V14` | Maximum temperature over 10 days for interval V14 | ⁰C | Float (numeric) | 0 |
| 94 | `tmax_V15` | Maximum temperature over 10 days for interval V15 | ⁰C | Float (numeric) | 0 |
| 95 | `tmax_V16` | Maximum temperature over 10 days for interval V16 | ⁰C | Float (numeric) | 0 |
| 96 | `tmax_V17` | Maximum temperature over 10 days for interval V17 | ⁰C | Float (numeric) | 0 |
| 97 | `tmax_V18` | Maximum temperature over 10 days for interval V18 | ⁰C | Float (numeric) | 0 |
| 98 | `tmax_V19` | Maximum temperature over 10 days for interval V19 | ⁰C | Float (numeric) | 0 |
| 99 | `tmax_V20` | Maximum temperature over 10 days for interval V20 | ⁰C | Float (numeric) | 0 |
| 100 | `tmax_V21` | Maximum temperature over 10 days for interval V21 | ⁰C | Float (numeric) | 0 |
| 101 | `tmax_V22` | Maximum temperature over 10 days for interval V22 | ⁰C | Float (numeric) | 0 |
| 102 | `tmax_V23` | Maximum temperature over 10 days for interval V23 | ⁰C | Float (numeric) | 0 |
| 103 | `tmax_V24` | Maximum temperature over 10 days for interval V24 | ⁰C | Float (numeric) | 0 |
| 104 | `tmax_V25` | Maximum temperature over 10 days for interval V25 | ⁰C | Float (numeric) | 0 |
| 105 | `tmax_V26` | Maximum temperature over 10 days for interval V26 | ⁰C | Float (numeric) | 0 |
| 106 | `tmax_V27` | Maximum temperature over 10 days for interval V27 | ⁰C | Float (numeric) | 0 |
| 107 | `tmax_V28` | Maximum temperature over 10 days for interval V28 | ⁰C | Float (numeric) | 0 |
| 108 | `tmax_V29` | Maximum temperature over 10 days for interval V29 | ⁰C | Float (numeric) | 0 |
| 109 | `tmax_V30` | Maximum temperature over 10 days for interval V30 | ⁰C | Float (numeric) | 0 |
| 110 | `tmin_V1` | Minimum temperature over 10 days for interval V1 | ⁰C | Float (numeric) | 0 |
| 111 | `tmin_V2` | Minimum temperature over 10 days for interval V2 | ⁰C | Float (numeric) | 0 |
| 112 | `tmin_V3` | Minimum temperature over 10 days for interval V3 | ⁰C | Float (numeric) | 0 |
| 113 | `tmin_V4` | Minimum temperature over 10 days for interval V4 | ⁰C | Float (numeric) | 0 |
| 114 | `tmin_V5` | Minimum temperature over 10 days for interval V5 | ⁰C | Float (numeric) | 0 |
| 115 | `tmin_V6` | Minimum temperature over 10 days for interval V6 | ⁰C | Float (numeric) | 0 |
| 116 | `tmin_V7` | Minimum temperature over 10 days for interval V7 | ⁰C | Float (numeric) | 0 |
| 117 | `tmin_V8` | Minimum temperature over 10 days for interval V8 | ⁰C | Float (numeric) | 0 |
| 118 | `tmin_V9` | Minimum temperature over 10 days for interval V9 | ⁰C | Float (numeric) | 0 |
| 119 | `tmin_V10` | Minimum temperature over 10 days for interval V10 | ⁰C | Float (numeric) | 0 |
| 120 | `tmin_V11` | Minimum temperature over 10 days for interval V11 | ⁰C | Float (numeric) | 0 |
| 121 | `tmin_V12` | Minimum temperature over 10 days for interval V12 | ⁰C | Float (numeric) | 0 |
| 122 | `tmin_V13` | Minimum temperature over 10 days for interval V13 | ⁰C | Float (numeric) | 0 |
| 123 | `tmin_V14` | Minimum temperature over 10 days for interval V14 | ⁰C | Float (numeric) | 0 |
| 124 | `tmin_V15` | Minimum temperature over 10 days for interval V15 | ⁰C | Float (numeric) | 0 |
| 125 | `tmin_V16` | Minimum temperature over 10 days for interval V16 | ⁰C | Float (numeric) | 0 |
| 126 | `tmin_V17` | Minimum temperature over 10 days for interval V17 | ⁰C | Float (numeric) | 0 |
| 127 | `tmin_V18` | Minimum temperature over 10 days for interval V18 | ⁰C | Float (numeric) | 0 |
| 128 | `tmin_V19` | Minimum temperature over 10 days for interval V19 | ⁰C | Float (numeric) | 0 |
| 129 | `tmin_V20` | Minimum temperature over 10 days for interval V20 | ⁰C | Float (numeric) | 0 |
| 130 | `tmin_V21` | Minimum temperature over 10 days for interval V21 | ⁰C | Float (numeric) | 0 |
| 131 | `tmin_V22` | Minimum temperature over 10 days for interval V22 | ⁰C | Float (numeric) | 0 |
| 132 | `tmin_V23` | Minimum temperature over 10 days for interval V23 | ⁰C | Float (numeric) | 0 |
| 133 | `tmin_V24` | Minimum temperature over 10 days for interval V24 | ⁰C | Float (numeric) | 0 |
| 134 | `tmin_V25` | Minimum temperature over 10 days for interval V25 | ⁰C | Float (numeric) | 0 |
| 135 | `tmin_V26` | Minimum temperature over 10 days for interval V26 | ⁰C | Float (numeric) | 0 |
| 136 | `tmin_V27` | Minimum temperature over 10 days for interval V27 | ⁰C | Float (numeric) | 0 |
| 137 | `tmin_V28` | Minimum temperature over 10 days for interval V28 | ⁰C | Float (numeric) | 0 |
| 138 | `tmin_V29` | Minimum temperature over 10 days for interval V29 | ⁰C | Float (numeric) | 0 |
| 139 | `tmin_V30` | Minimum temperature over 10 days for interval V30 | ⁰C | Float (numeric) | 0 |
| 140 | `vp_V1` | Vapor pressure over 10 days for interval V1 | Pa | Integer (numeric) | 0 |
| 141 | `vp_V2` | Vapor pressure over 10 days for interval V2 | Pa | Integer (numeric) | 0 |
| 142 | `vp_V3` | Vapor pressure over 10 days for interval V3 | Pa | Integer (numeric) | 0 |
| 143 | `vp_V4` | Vapor pressure over 10 days for interval V4 | Pa | Integer (numeric) | 0 |
| 144 | `vp_V5` | Vapor pressure over 10 days for interval V5 | Pa | Integer (numeric) | 0 |
| 145 | `vp_V6` | Vapor pressure over 10 days for interval V6 | Pa | Integer (numeric) | 0 |
| 146 | `vp_V7` | Vapor pressure over 10 days for interval V7 | Pa | Integer (numeric) | 0 |
| 147 | `vp_V8` | Vapor pressure over 10 days for interval V8 | Pa | Integer (numeric) | 0 |
| 148 | `vp_V9` | Vapor pressure over 10 days for interval V9 | Pa | Integer (numeric) | 0 |
| 149 | `vp_V10` | Vapor pressure over 10 days for interval V10 | Pa | Integer (numeric) | 0 |
| 150 | `vp_V11` | Vapor pressure over 10 days for interval V11 | Pa | Integer (numeric) | 0 |
| 151 | `vp_V12` | Vapor pressure over 10 days for interval V12 | Pa | Integer (numeric) | 0 |
| 152 | `vp_V13` | Vapor pressure over 10 days for interval V13 | Pa | Integer (numeric) | 0 |
| 153 | `vp_V14` | Vapor pressure over 10 days for interval V14 | Pa | Integer (numeric) | 0 |
| 154 | `vp_V15` | Vapor pressure over 10 days for interval V15 | Pa | Integer (numeric) | 0 |
| 155 | `vp_V16` | Vapor pressure over 10 days for interval V16 | Pa | Integer (numeric) | 0 |
| 156 | `vp_V17` | Vapor pressure over 10 days for interval V17 | Pa | Integer (numeric) | 0 |
| 157 | `vp_V18` | Vapor pressure over 10 days for interval V18 | Pa | Integer (numeric) | 0 |
| 158 | `vp_V19` | Vapor pressure over 10 days for interval V19 | Pa | Integer (numeric) | 0 |
| 159 | `vp_V20` | Vapor pressure over 10 days for interval V20 | Pa | Integer (numeric) | 0 |
| 160 | `vp_V21` | Vapor pressure over 10 days for interval V21 | Pa | Integer (numeric) | 0 |
| 161 | `vp_V22` | Vapor pressure over 10 days for interval V22 | Pa | Integer (numeric) | 0 |
| 162 | `vp_V23` | Vapor pressure over 10 days for interval V23 | Pa | Integer (numeric) | 0 |
| 163 | `vp_V24` | Vapor pressure over 10 days for interval V24 | Pa | Integer (numeric) | 0 |
| 164 | `vp_V25` | Vapor pressure over 10 days for interval V25 | Pa | Integer (numeric) | 0 |
| 165 | `vp_V26` | Vapor pressure over 10 days for interval V26 | Pa | Integer (numeric) | 0 |
| 166 | `vp_V27` | Vapor pressure over 10 days for interval V27 | Pa | Integer (numeric) | 0 |
| 167 | `vp_V28` | Vapor pressure over 10 days for interval V28 | Pa | Integer (numeric) | 0 |
| 168 | `vp_V29` | Vapor pressure over 10 days for interval V29 | Pa | Integer (numeric) | 0 |
| 169 | `vp_V30` | Vapor pressure over 10 days for interval V30 | Pa | Integer (numeric) | 0 |

## Panduan membaca kelompok variabel

### Identitas, hasil, lokasi, dan sistem budidaya

- `Field_ID`: pengenal field/lahan.
- `YIELD`: hasil jagung pada field, dalam Mg ha-1 (megagram per hektare; secara numerik setara ton/ha).
- `Mun_yield`: rata-rata hasil jagung tingkat munisipal, bukan hasil field individual.
- `Year`: tahun kejadian budidaya.
- `Lat`, `Long`, `Elev`: koordinat dan elevasi lokasi.
- `System`, `Cultivar`, `Tillage`: sistem berbasis hybrid/landrace, informasi genotipe/varietas, dan praktik olah tanah.
- `Planting`: hari dalam tahun saat penanaman dilakukan (Day of Year / DOY).

### Input agronomi dan karakteristik tanah

- `Nitrogen`, `Phosphorus`, `Potassium`: jumlah unsur/hara pupuk dengan satuan masing-masing sebagaimana ditulis pada sumber (`kg N ha-1`, `kg P2O5 ha-1`, `kg K2O ha-1`).
- `Slope`, `Clay`, `SOM`, `PH`, `CEC`: kemiringan, kandungan liat, bahan organik tanah, pH, dan kapasitas tukar kation.

### Variabel cuaca berurutan (`V1`–`V30`)

Kelompok variabel cuaca memiliki 30 interval (`V1` sampai `V30`), masing-masing mewakili interval 10 hari. Sheet `Legend` menyebut rentang keseluruhan dari 60 hari sebelum tanam sampai 240 hari setelah tanam.

| Prefix | Arti | Unit |
|---|---|---|
| `prcp_Vn` | Presipitasi per hari pada interval 10-harian ke-n | mm day-1 |
| `srad_Vn` | Radiasi surya per hari pada interval 10-harian ke-n | MJ m-2 day-1 |
| `tmax_Vn` | Suhu maksimum pada interval 10-harian ke-n | °C |
| `tmin_Vn` | Suhu minimum pada interval 10-harian ke-n | °C |
| `vp_Vn` | Tekanan uap pada interval 10-harian ke-n | Pa |

`n` adalah nomor interval 1–30, bukan nomor bulan. Definisi ini tidak menetapkan tanggal kalender spesifik untuk setiap `Vn`; gunakan dokumentasi sumber/metadata temporal DAYMET jika pemetaan tanggal yang presisi diperlukan.

## Catatan kualitas dan penggunaan

1. `Cultivar` memiliki 310 nilai kosong dari 4.585 observasi. Missing value tidak boleh otomatis dianggap sebagai satu varietas atau sebagai bukti bahwa varietas tidak ditanam.
2. Pada file yang diperiksa, `Field_ID` tidak kosong dan tidak berulang; tidak ditemukan baris identik duplikat. Pemeriksaan ini tidak menjamin tidak adanya duplikasi konseptual atau pengukuran yang keliru.
3. `YIELD` dan `Mun_yield` memiliki unit yang sama, tetapi tingkat agregasinya berbeda (field vs munisipal). Jangan menukar keduanya tanpa alasan analitis.
4. Fitur cuaca pada interval setelah tanam hanya tersedia setelah periode tersebut terjadi. Untuk skenario prediksi sebelum tanam, fitur pascatanam berisiko menyebabkan *data leakage*.
5. Satuan dan deskripsi dicantumkan sesuai sheet `Legend`. Jangan mengubah atau mengonversi satuan tanpa mencatat transformasinya.

## Singkatan

- `CEC`: Cation Exchange Capacity (kapasitas tukar kation).
- `SOM`: Soil Organic Matter (bahan organik tanah).
- `PH`: pH tanah (tidak ada unit yang dicantumkan pada legend).
- `DOY`: Day of Year, nomor hari dalam satu tahun.
- `Mg ha-1`: megagram per hektare, setara secara numerik dengan ton per hektare.
- `V1`–`V30`: indeks interval waktu 10-harian.

---

**Catatan:** Data dictionary ini tidak menambahkan interpretasi yang tidak tersedia pada sheet `Legend`. Bila unit tidak dicantumkan oleh sumber, ditulis `Not specified`.