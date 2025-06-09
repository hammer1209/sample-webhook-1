# tests/conftest.py

import pytest

@pytest.fixture
def sample_webhook_client():
    from fastapi.testclient import TestClient
    from src.sample_webhook.main import app

    client = TestClient(app)
    yield client
