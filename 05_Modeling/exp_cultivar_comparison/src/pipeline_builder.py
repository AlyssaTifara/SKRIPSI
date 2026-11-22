import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

from cultivar_preprocessor import CultivarPreprocessor

NUMERIC_FEATURES = [
    "Clay", "CEC", "SOM", "PH", "Elev", "Slope",
    "rain_pre60d", "srad_mean_pre60d", "tmax_mean_pre60d", "tmin_mean_pre60d", "vp_mean_pre60d"
]

def get_model(model_name):
    if model_name == "rf":
        return RandomForestRegressor(
            n_estimators=300,
            min_samples_leaf=2,
            max_features=1.0,
            random_state=42,
            n_jobs=-1
        )
    elif model_name == "xgb":
        return XGBRegressor(
            n_estimators=300,
            max_depth=4,
            learning_rate=0.05,
            subsample=0.8,
            colsample_bytree=0.8,
            objective="reg:squarederror",
            random_state=42,
            n_jobs=4,
            verbosity=0
        )
    else:
        raise ValueError(f"Unknown model_name: {model_name}")

def build_pipeline(scenario="A", model_name="rf"):
    """
    Membangun scikit-learn pipeline terintegrasi.
    Skenario A:
      - 11 fitur numerik -> SimpleImputer(median)
      - Fitur System -> OneHotEncoder(handle_unknown='ignore')
      - Model regresi (RF atau XGBoost)
    Skenario B:
      - 11 fitur numerik -> SimpleImputer(median)
      - Fitur System -> OneHotEncoder(handle_unknown='ignore')
      - Fitur Cultivar -> CultivarPreprocessor(min_freq=5) -> OneHotEncoder(handle_unknown='ignore')
      - Model regresi (RF atau XGBoost)
    """
    numeric_transformer = Pipeline([
        ("imputer", SimpleImputer(strategy="median"))
    ])
    
    system_transformer = Pipeline([
        ("system_ohe", OneHotEncoder(handle_unknown="ignore", sparse_output=False))
    ])
    
    if scenario.upper() == "A":
        preprocessor = ColumnTransformer(
            transformers=[
                ("num", numeric_transformer, NUMERIC_FEATURES),
                ("sys", system_transformer, ["System"])
            ],
            remainder="drop"
        )
    elif scenario.upper() == "B":
        cultivar_transformer = Pipeline([
            ("cultivar_clean", CultivarPreprocessor(min_freq=5, unknown_token="UNKNOWN", rare_token="RARE_OR_UNSEEN")),
            ("cultivar_ohe", OneHotEncoder(handle_unknown="ignore", sparse_output=False))
        ])
        preprocessor = ColumnTransformer(
            transformers=[
                ("num", numeric_transformer, NUMERIC_FEATURES),
                ("sys", system_transformer, ["System"]),
                ("cult", cultivar_transformer, ["Cultivar"])
            ],
            remainder="drop"
        )
    else:
        raise ValueError(f"Unknown scenario: {scenario}")
        
    model = get_model(model_name)
    
    pipe = Pipeline([
        ("preprocessor", preprocessor),
        ("regressor", model)
    ])
    return pipe
