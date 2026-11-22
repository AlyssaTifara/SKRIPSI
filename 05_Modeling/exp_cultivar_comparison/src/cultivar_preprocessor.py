import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class CultivarPreprocessor(BaseEstimator, TransformerMixin):
    """
    Preprocessor untuk kolom Cultivar:
    1. Mengisi nilai NaN/kosong dengan token 'UNKNOWN'.
    2. Pada saat fit (hanya data training fold), menghitung frekuensi setiap kategori.
       Kategori dengan frekuensi < min_freq (default 5) dipetakan ke 'RARE_OR_UNSEEN'.
    3. Pada saat transform (data training maupun test fold):
       Kategori yang tidak ada pada frequent categories training fold dipetakan ke 'RARE_OR_UNSEEN'.
    """
    def __init__(self, min_freq=5, unknown_token="UNKNOWN", rare_token="RARE_OR_UNSEEN"):
        self.min_freq = min_freq
        self.unknown_token = unknown_token
        self.rare_token = rare_token
        
    def fit(self, X, y=None):
        if isinstance(X, pd.DataFrame):
            s = X.iloc[:, 0].copy()
        elif isinstance(X, pd.Series):
            s = X.copy()
        else:
            s = pd.Series(np.array(X).ravel())
            
        s = s.fillna(self.unknown_token).astype(str)
        counts = s.value_counts()
        self.frequent_categories_ = set(counts[counts >= self.min_freq].index)
        return self

    def transform(self, X):
        if isinstance(X, pd.DataFrame):
            s = X.iloc[:, 0].copy()
        elif isinstance(X, pd.Series):
            s = X.copy()
        else:
            s = pd.Series(np.array(X).ravel())
            
        s = s.fillna(self.unknown_token).astype(str)
        s_mapped = s.apply(lambda x: x if x in self.frequent_categories_ else self.rare_token)
        return s_mapped.to_numpy().reshape(-1, 1)
