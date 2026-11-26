from app import app


def test_health():
    client = app.test_client()
    reponse = client.get("/health")
    assert reponse.status_code == 200
    assert reponse.get_json()["status"] == "ok"


def test_colis_existant():
    client = app.test_client()
    reponse = client.get("/colis/GT-1001")
    assert reponse.status_code == 200
    assert reponse.get_json()["client"] == "SOTELGAB"


def test_colis_inconnu():
    client = app.test_client()
    reponse = client.get("/colis/GT-9999")
    assert reponse.status_code == 404
