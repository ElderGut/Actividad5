
import pandas as pd
from sklearn.datasets import load_breast_cancer

def cargar_datos():
    data = load_breast_cancer()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df["target"] = data.target
    return df

def limpiar_datos(df):
    df_clean = df.copy()
    df_clean = df_clean.drop_duplicates()
    df_clean = df_clean.dropna()
    return df_clean
