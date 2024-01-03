import pytest
from fastapi.testclient import TestClient

from company_analyzer_svc.main import app


@pytest.fixture(scope="session")
def sync_client() -> TestClient:
    """Provides a synchronous HTTP client for testing the FastAPI app.

    Returns:
        A TestClient instance for making synchronous HTTP requests.
    """
    client = TestClient(app, raise_server_exceptions=False)
    return client
