from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get(
        "/", headers={"content-type": "text/html; charset=utf-8"})
    assert response.status_code == 200
    assert b"Containerisation template work<" in response.content
    response = client.get("/assets/css/bs/style3.css")
    assert response.status_code == 200


def test_about():
    response = client.get("/about",
                          headers={"content-type": "text/html; charset=utf-8"})
    assert response.status_code == 200
    assert b"About" in response.content


def test_docker():
    response = client.get("/docker",
                          headers={"content-type": "text/html; charset=utf-8"})
    assert response.status_code == 200
    assert b"Dockerfile" in response.content


def test_kubernetes():
    response = client.get("/kubernetes",
                          headers={"content-type": "text/html; charset=utf-8"})
    assert response.status_code == 200
    assert b"kubeservice.yaml" in response.content

