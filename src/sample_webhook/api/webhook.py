from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class PullRequestPayload(BaseModel):
    action: str
    pull_request: dict

@router.post("/webhook")
async def handle_webhook(payload: PullRequestPayload):
    if payload.action == "closed" and payload.pull_request.get("merged"):
        # Logic to handle the merged pull request
        return {"message": "Pull request merged successfully."}
    raise HTTPException(status_code=400, detail="Invalid event")