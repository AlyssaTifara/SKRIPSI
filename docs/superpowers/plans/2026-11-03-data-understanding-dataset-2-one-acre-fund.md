# Implementation Plan: Data Understanding Dataset 2 (One Acre Fund MEL Maize Survey 2016-2022)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Conduct an academic, fully reproducible Data Understanding and Exploratory Data Analysis on Dataset 2 (`One_Acre_Fund_MEL_maize_survey_data_2016-2022.csv`) to assess its structure, quality, target characteristics, feature relevance, data leakage risks, and fitness for predicting maize yield to support layer hen feed planning at Komunitas ASA Indonesia, Sumenep.

**Architecture:** 
1. Compute all dataset metrics, summary tables, and high-resolution exploratory charts via a dedicated generation script into `03_Exploration/Dataset_02_One_Acre_Fund/output/`.
2. Construct Notebook 1 (`01_Data_Understanding_One_Acre_Fund.ipynb`) focusing on dataset overview, full categorized data dictionary (confirmed vs provisional), and observation unit semantics.
3. Construct Notebook 2 (`02_Data_Quality_EDA_One_Acre_Fund.ipynb`) focusing on quality audit, target variable analysis, bivariate/multivariate EDA, leakage risk analysis, thesis contextual relevance (Sumenep vs Sub-Saharan Africa), and research implications.
4. Synthesize the findings into an executive markdown report (`output/LAPORAN_DATA_UNDERSTANDING_DATASET_02_ONE_ACRE_FUND.md`).

**Tech Stack:** Python 3, Pandas, NumPy, Matplotlib, Seaborn, Scipy, Jupyter Notebook format (JSON `nbformat` v4).

**Spec:** User Master Prompt for Dataset 2 Data Understanding; Thesis Context (`01_Context/THESIS_CONTEXT_ANTIGRAVITY.md`).

## Global Constraints
- Target directory: `03_Exploration/Dataset_02_One_Acre_Fund/`.
- Strict isolation: Do NOT read, modify, combine, or cross-analyze with Dataset 1 (`Smart_Farming_Crop_Yield_2024 (2).csv`) or its three notebooks.
- Keep raw dataset strictly unmodified.
- Distinguish verified facts from provisional interpretations.
- No predictive model training in this phase.
- All notebooks must be self-contained and run sequentially without errors.

## Review Focus
1. **Target variable integrity:** `yield_kg_ha` contains 263 genuine zero values (1.78%) reflecting crop failures; ensure they are properly documented rather than naively discarded.
2. **Data leakage identification:** Features like `harvest_date` or potential post-harvest survey recordings must be classified as potential leakage if used for pre-planting planning.
3. **Severe missingness in agronomic inputs:** Variables such as `manure` (94.0%), `hyb_type` (82.5%), `striga` (82.9%), and `comp_kg_ha` (52.3%) have heavy missingness and must be evaluated cautiously.
4. **Contextual transferability to Sumenep, Madura:** Acknowledge agro-climatic differences (East Africa highland/sub-humid vs Madura lowland dry/tropical monsoon, hybrid seeds vs Madura local/Guluk-guluk varieties).
5. **No Dataset 1 cross-contamination:** Every notebook header, metadata, markdown cell, and output explicitly attributes Dataset 2.

---

### Task 1: Generate Visualizations and Structured Summary Tables
**Files:**
- Create: `03_Exploration/Dataset_02_One_Acre_Fund/output/figures/` (PNG charts)
- Create: `03_Exploration/Dataset_02_One_Acre_Fund/output/tables/` (CSV / summary files)
- Script: `C:\Users\tissa\.gemini\antigravity\brain\3360babb-d57f-4153-b267-87ebb0fd8a29\scratch\generate_eda_assets.py`

- [x] Write script to generate:
  - Figure 1: `yield_distribution.png` (Histogram, KDE, Boxplot, QQ-plot)
  - Figure 2: `yield_by_country.png` (Boxplot & Violin plot of yield across 7 countries)
  - Figure 3: `yield_by_year.png` (Yield distribution trends across 2016-2022)
  - Figure 4: `correlation_heatmap.png` (Top numerical features correlated with yield)
  - Figure 5: `soil_climate_yield_scatter.png` (Bivariate scatter/regression of N, P, elevation, temperature vs yield)
  - Figure 6: `missing_values_bar.png` (Bar chart of missing value percentages across 53 columns)
  - Table: `data_quality_summary.csv`
  - Table: `target_summary_by_country_year.csv`
- [x] Run the script and verify that all figures and tables are generated properly.

### Task 2: Create Notebook 1 - Data Understanding & Data Dictionary
**Files:**
- Create: `03_Exploration/Dataset_02_One_Acre_Fund/01_Data_Understanding_One_Acre_Fund.ipynb`

- [x] Structure the notebook cells:
  1. Title and Research Context (Thesis title, Supervisor, SIB Polinema context, Dataset 2 identity).
  2. Setup and Library Imports (`pandas`, `numpy`, `matplotlib`).
  3. Raw Data Loading (`02_Raw_Data/Dataset_02_One_Acre_Fund/One_Acre_Fund_MEL_maize_survey_data_2016-2022.csv`).
  4. Dataset Overview (Shape: 14,773 rows, 53 columns; sample head & tail; data types breakdown; units verification).
  5. Observation Unit & Scope Analysis (Smallholder maize survey plots across 7 East/West African countries, 2016-2022, cluster coordinates).
  6. Comprehensive Data Dictionary (Grouped by Category: Identity & Geography, Temporal & Season, Soil & Topography, Climate & Biometeorology, Seed & Hybrid Attributes, Agronomic Practices & Fertilization, Crop Stress & Biotic Factors, Harvest Target).
  7. Verification Summary: Confirmed vs Provisional Column Meanings.
- [x] Execute / validate notebook JSON and content integrity.

### Task 3: Create Notebook 2 - Data Quality, Target Assessment, & EDA
**Files:**
- Create: `03_Exploration/Dataset_02_One_Acre_Fund/02_Data_Quality_EDA_One_Acre_Fund.ipynb`

- [x] Structure the notebook cells:
  1. Title, Academic Objectives, and Dataset 2 Attribution.
  2. Library Imports and Data Loading.
  3. Data Quality Audit:
     - Missing value analysis (tables, percentages, threshold grouping: <5%, 5-30%, >30%).
     - Duplication checks (exact row duplicates = 0, cluster coordinate overlap = 1,996).
     - Anomaly, zero-value, and negative value checks.
     - Outlier inspection using IQR and Z-score methods.
     - Low variance and sparse feature assessment.
  4. Target Variable Assessment (`yield_kg_ha`):
     - Descriptive statistics (mean: 2,969.06 kg/ha, median: 2,713.87 kg/ha, std: 1,686.07 kg/ha).
     - Distribution shape (skewness: 0.8246, kurtosis: 0.7831).
     - Breakdown by country (Kenya, Tanzania, Rwanda, Zambia, Burundi, Nigeria, Uganda).
     - Breakdown by year (2016-2022) and season (first vs second season).
     - Zero yield assessment (263 cases, 1.78% total crop failure).
     - Outlier boundaries (IQR upper bound 7,247.07 kg/ha; 296 records / 2.00%).
     - Feasibility evaluation for regression modeling.
  5. Exploratory Data Analysis (EDA):
     - Univariate target visualizations.
     - Spatial & Temporal comparisons.
     - Agronomic factors vs yield (N, P, K fertilizers, planting density, hybrid adoption).
     - Environmental factors vs yield (elevation, precipitation, temperature, soil pH, organic carbon).
     - Biotic stress impact (pests, diseases, striga, excess water).
  6. Feature Relevance & Data Leakage Assessment:
     - Candidate pre-planting features (soil, elevation, baseline climate).
     - Candidate in-season features (seasonal precipitation, fertilizer, pest control).
     - Post-harvest features / Data leakage risks (harvest date, post-harvest surveys).
     - High-missingness / unviable features.
  7. Alignment with ASA Indonesia & Sumenep Thesis Context:
     - Geographic & climatic divergence (East Africa vs Sumenep, Madura).
     - Agronomic differences (hybrids vs local varieties like Guluk-guluk, irrigation vs rainfed).
     - Bridge to Layer Hen Feed Planning (converting yield kg/ha to feed supply, daily intake 110-120g/hen/day with 50% maize ratio).
     - Information gaps requiring ASA Indonesia stakeholder input.
  8. Research Implications and Methodological Recommendations.
- [x] Execute / validate notebook JSON and content integrity.

### Task 4: Synthesize Comprehensive Markdown Summary Report
**Files:**
- Create: `03_Exploration/Dataset_02_One_Acre_Fund/output/LAPORAN_DATA_UNDERSTANDING_DATASET_02_ONE_ACRE_FUND.md`

- [x] Write a structured report covering all 8 points requested in the Master Prompt:
  1. Identitas dataset dan jumlah observasi.
  2. Karakteristik variabel dan target.
  3. Temuan kualitas data.
  4. Temuan utama EDA.
  5. Potensi fitur dan risiko data leakage.
  6. Relevansi dataset terhadap penelitian.
  7. Keterbatasan dan kebutuhan data tambahan.
  8. Kesimpulan kelayakan Dataset 2.
  9. Daftar file yang berhasil dibuat dan lokasi penyimpanannya.

### Task 5: Final Review and Deliverable Verification
- [x] Confirm no files in Dataset 1 were modified or touched.
- [x] Verify that all outputs, tables, charts, and notebooks are intact in `03_Exploration/Dataset_02_One_Acre_Fund/`.
