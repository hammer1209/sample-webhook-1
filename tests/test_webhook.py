#import pytest
from fastapi.testclient import TestClient
from src.sample_webhook.main import app

client = TestClient(app)

def test_webhook_endpoint():
    # Simulate a GitHub webhook event for a merged pull request
    payload = {
        "action": "closed",
        "pull_request": {
            "merged": True,
            "number": 1,
            "title": "Test PR",
            "user": {
                "login": "testuser"
            }
        }
    }
    
    response = client.post("/webhook", json=payload)
    
    assert response.status_code == 200
    assert response.json() == {"message": "Webhook received and processed."}

def test_webhook_endpoint_not_merged():
    # Simulate a GitHub webhook event for a pull request that is not merged
    payload = {
        "action": "closed",
        "pull_request": {
            "merged": False,
            "number": 2,
            "title": "Test PR Not Merged",
            "user": {
                "login": "testuser"
            }
        }
    }
    
    response = client.post("/webhook", json=payload)
    
    assert response.status_code == 200
    assert response.json() == {"message": "Webhook received but not processed."}