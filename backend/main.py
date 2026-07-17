from fastapi import FastAPI
from api.routes import router 

def create_app():
    app = FastAPI(
        title="Agentic Car Auditor",
        description="Multi-Agent Vehicle Evaluation System built with LangGraph",
        version="1.0.0")

    @app.get("/")
    def health_check():
        return {
            "service": "Agentic Car Auditor",
            "status": "running"
        }

    app.include_router(router)
    return app

app = create_app()