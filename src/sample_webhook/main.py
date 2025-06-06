from fastapi import FastAPI
from sample_webhook.api.routes import router as api_router

app = FastAPI(title="Sample Webhook")

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)