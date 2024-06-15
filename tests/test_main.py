import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_get_token():
    response = client.post(
        "/token",
        data={"username": "user1", "password": "password"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"


def test_get_bonus():
    # Получаем токен
    response = client.post(
        "/token",
        data={"username": "user1", "password": "password"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    token = response.json()["access_token"]

    # Запрашиваем информацию о бонусах
    response = client.get(
        "/bonus",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    json_response = response.json()
    assert "current_level" in json_response
    assert "next_level" in json_response
    assert "cashback" in json_response
    assert "next_level_threshold" in json_response
    assert json_response["current_level"] == "silver"
    assert json_response["next_level"] == "gold"
    assert json_response["cashback"] == "5%"
    assert json_response["next_level_threshold"] == 5000


def test_invalid_token():
    response = client.get(
        "/bonus",
        headers={"Authorization": "Bearer invalid_token"}
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Could not validate credentials"}
