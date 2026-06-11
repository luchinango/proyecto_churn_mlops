from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_inicio():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["mensaje"] == "Servicio ML-Ops activo"
    assert data["estado"] == "ok"
    assert "Luis Alberto Martínez Barrientos" in data["autor"]


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["estado"] == "ok"
    assert data["modelo"] == "modelo_churn_v1"


def test_predict_valido():
    payload = {
        "antiguedad": 12,
        "cargo_mensual": 95.5,
        "reclamos": 3,
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["prediccion"] in ("alto_riesgo", "bajo_riesgo")
    assert 0 <= data["probabilidad"] <= 1
    assert data["version_modelo"] == "modelo_churn_v1"
    assert "Luis Alberto Martínez Barrientos" in data["autor"]


def test_predict_campo_faltante():
    payload = {
        "antiguedad": 36,
        "cargo_mensual": 60.5,
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 422


def test_predict_valor_negativo():
    payload = {
        "antiguedad": 12,
        "cargo_mensual": -50,
        "reclamos": 1,
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 422
