import pandas as pd
import numpy as np

csv_path = r'C:\SKRIPSI\02_Raw_Data\Dataset_03_Chiapas\Chiapas_Data.csv'
df = pd.read_csv(csv_path)

print('=== TARGET AUDIT ===')
diff_yield = df['YIELD'] - df['Mun_yield']
print('YIELD vs Mun_yield correlation:', df['YIELD'].corr(df['Mun_yield']))
print('Difference (YIELD - Mun_yield):')
print(diff_yield.describe(percentiles=[0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99]))
gt = (df['YIELD'] > df['Mun_yield']).sum()
lt = (df['YIELD'] < df['Mun_yield']).sum()
print(f'Cases where YIELD > Mun_yield: {gt} ({gt/len(df)*100:.2f}%)')
print(f'Cases where YIELD < Mun_yield: {lt} ({lt/len(df)*100:.2f}%)')

print('\n=== YIELD BY SYSTEM ===')
print(df.groupby('System')['YIELD'].describe())

print('\n=== YIELD BY TILLAGE ===')
print(df.groupby('Tillage')['YIELD'].describe())

print('\n=== OUTLIER AUDIT (IQR METHOD) ===')
for col in ['YIELD', 'Mun_yield', 'Elev', 'Planting', 'Nitrogen', 'Phosphorus', 'Potassium', 'Slope', 'Clay', 'CEC', 'SOM', 'PH']:
    s = df[col]
    q25, q75 = s.quantile(0.25), s.quantile(0.75)
    iqr = q75 - q25
    lower = q25 - 1.5 * iqr
    upper = q75 + 1.5 * iqr
    outliers = s[(s < lower) | (s > upper)]
    print(f'{col}: lower={lower:.2f}, upper={upper:.2f}, outliers={len(outliers)} ({len(outliers)/len(df)*100:.2f}%), min={s.min():.2f}, max={s.max():.2f}')

print('\n=== CONSTANT / ZERO VARIANCE CHECK ===')
numeric_cols = df.select_dtypes(include=[np.number]).columns
stds = df[numeric_cols].std()
zero_std = stds[stds == 0]
print('Columns with zero standard deviation (constant):', list(zero_std.index))

print('\n=== WEATHER RANGE SUMMARY ===')
for w_prefix, name in [('prcp', 'Precipitation (mm/day)'), ('srad', 'Solar Radiation (MJ/m2/day)'), 
                       ('tmax', 'Max Temp (C)'), ('tmin', 'Min Temp (C)'), ('vp', 'Vapor Pressure (Pa)')]:
    w_cols = [f'{w_prefix}_V{i}' for i in range(1, 31)]
    min_all = df[w_cols].min().min()
    max_all = df[w_cols].max().max()
    mean_all = df[w_cols].mean().mean()
    print(f'{name}: min={min_all:.2f}, max={max_all:.2f}, global mean={mean_all:.2f}')

print('\n=== SAMPLE 5 ROWS (HEAD) ===')
sample_cols = ['Field_ID', 'YIELD', 'Year', 'Mun_yield', 'Elev', 'System', 'Cultivar', 'Tillage', 'Planting', 'Nitrogen', 'Slope', 'PH', 'prcp_V1', 'tmax_V1']
print(df[sample_cols].head(5).to_string())
