from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    login: str
    id: int
    avatar_url: str
    html_url: str

class PullRequest(BaseModel):
    id: int
    number: int
    state: str
    title: str
    user: User
    merged_at: Optional[str]  # ISO 8601 format
    html_url: str

class GitHubWebhookPayload(BaseModel):
    action: str
    pull_request: PullRequest
    repository: dict
    sender: User

class WebhookEvent(BaseModel):
    event_type: str
    payload: GitHubWebhookPayload