""" Sample Webhook API for handling GitHub pull request events. """

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..services.webhook_handler import handle_webhook_event

router = APIRouter()

class PullRequestPayload(BaseModel):
    """ Represents the payload structure for GitHub pull request events. """
    action: str
    pull_request: dict


# TODO: Unit Test

# TODO: Deploy
# TODO: 1. Create AppService in my Azure (Or, would an Azure Function be better?)
# TODO: 2. Copy files to the resource in Azure
# TODO: 3. Update hammer1209/sample-webhook repo to call webhook in Azure
# TODO: 4. Update configuration to get settings (environment, mongoDB connection)
# TODO:    from the correct TIW location

@router.post("/webhook")
async def handle_webhook(payload: PullRequestPayload):
    """ Handle incoming GitHub webhook events for pull requests. """

    response = "Pull request ignored."

    if payload.action == "closed" and payload.pull_request.get("merged"):

        # Logic to handle the merged pull request
        # return {"message": "Pull request merged successfully."}

        response = handle_webhook_event(payload.model_dump().__dict__)
        if response is None:
            raise HTTPException(400, "Pull request not processed.")

    raise HTTPException(status_code=200, detail=response)
