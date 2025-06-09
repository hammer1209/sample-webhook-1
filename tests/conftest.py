""" Conftest file for pytest configuration. """
# tests/conftest.py

import pytest

from fastapi.testclient import TestClient
from src.sample_webhook.main import app

@pytest.fixture
def sample_webhook_client():
    """ Fixture to create a FastAPI test client for the sample webhook application. """
    client = TestClient(app)
    yield client
