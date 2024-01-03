"""Test v1/health endpoints."""

from fastapi.testclient import TestClient


def test_get_liveness(sync_client: TestClient) -> None:
    """Test liveness endpoint for a successful response."""
    response = sync_client.get("health/liveness")
    assert response.status_code == 200
    assert response.json() == {"message": "I'm alive"}


def test_get_readiness(sync_client: TestClient) -> None:
    """Test readiness endpoint for a successful response."""
    response = sync_client.get("health/readiness")
    assert response.status_code == 200
    assert response.json() == {"message": "I'm ready"}
