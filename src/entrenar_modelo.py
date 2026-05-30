from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "models"
TRAIN_DATA = DATA_DIR / "train.csv"
MODEL_FILE = MODELS_DIR / "modelo_churn.pkl"
ALGORITMO = "RandomForestClassifier"
HIPERPARAMETROS = {"n_estimators": 100, "random_state": 42}


def entrenar_modelo():
    """
    Entrena un modelo simple de clasificación para predecir churn.
    """
    if not TRAIN_DATA.exists():
        raise FileNotFoundError(
            "No se encontró data/train.csv. Primero ejecuta src/preparar_datos.py"
        )

    MODELS_DIR.mkdir(exist_ok=True)

    df = pd.read_csv(TRAIN_DATA)
    X = df.drop(columns=["churn"])
    y = df["churn"]

    modelo = Pipeline(
        steps=[
            ("escalado", StandardScaler()),
            (
                "clasificador",
                RandomForestClassifier(
                    n_estimators=HIPERPARAMETROS["n_estimators"],
                    random_state=HIPERPARAMETROS["random_state"],
                ),
            ),
        ]
    )

    modelo.fit(X, y)
    print(f"Algoritmo: {ALGORITMO}")
    print(f"Hiperparámetros: {HIPERPARAMETROS}")
    joblib.dump(modelo, MODEL_FILE)

    print("Modelo entrenado correctamente.")
    print(f"Modelo guardado en: {MODEL_FILE}")


if __name__ == "__main__":
    entrenar_modelo()
