"""Tests for the Flask API."""


def test_health_endpoint():
    from server.app import create_app

    client = create_app().test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
