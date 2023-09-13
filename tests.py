from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    response = client.get('/healthcheck')
    assert response.status_code == 200
    assert response.json() == {'message': 'API Running Successfully'}


def test_create_user():
    sample_payload = {
        "name": "Nice",
        "track": "backend"
    }
    response = client.post("/api/", json=sample_payload)
    assert response.status_code == 201
    

def test_get_user(userId = "4a307aa9-9c66-4cee-b893-5d0b093a4c47"):
    response = client.get(f"/api/{userId}")
    assert response.status_code == 200
    assert response.json() == {
    "status": "success",
    "user": {
        "name": "Rod",
        "track": "frontend",
        "id": "4a307aa9-9c66-4cee-b893-5d0b093a4c47"
    }
    }

def test_update_user(userId = "26f52bae-ac1b-4241-b8e6-fa5757676ce2"):
    sample_payload = {
        "name": "Unique",
        "track": "Mobile",
    }
    response = client.patch(f"/api/{userId}", json=sample_payload)
    assert response.status_code == 200
    assert response.json() == {
        "Status": "success",
        "user": {
            "name": "Unique",
            "track": "Mobile",
            "id": "26f52bae-ac1b-4241-b8e6-fa5757676ce2"
        }
    }


def test_delete_user(userId = "ed6bc55d-df95-4e33-bfd0-e5040dd403de"):
    response = client.delete(f"/api/{userId}")
    assert response.status_code == 204
    


def test_get_user_not_found():
    response = client.get(
        f"/api/16303002-876a-4f39-ad16-e715f151bab3"
    )  # GUID not in DB
    assert response.status_code == 404
    assert response.json() == {
  "detail": "No user with this id: 16303002-876a-4f39-ad16-e715f151bab3 found"
}
