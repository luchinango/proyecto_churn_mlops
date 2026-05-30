from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_inicio():
    response = client.get("/")
    assert response.status_code == 200
    assert "mensaje" in response.json()


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert "estado" in response.json()
    assert "modelo_disponible" in response.json()

def test_predict():
    payload = {
        "edad": 28,
        "antiguedad_meses": 8,
        "saldo_promedio": 1200,
        "reclamos": 3,
        "usa_app": 0,
    }
    response = client.post("/predict", json=payload)

    if response.status_code == 200:
        data = response.json()
        assert "churn_predicho" in data
        assert data["churn_predicho"] in (0, 1)
        assert "probabilidad_churn" in data
    else:
        assert response.status_code == 503
        assert "detail" in response.json()