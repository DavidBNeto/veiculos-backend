import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from app.api.routers.veiculo_router import get_veiculo_router
from app.config import settings


# Function to initialize the FastAPI app.
def init_app() -> FastAPI:
    app = FastAPI(title=settings.API_TITLE)
    # Include the car router.
    app.include_router(get_veiculo_router())
    # Include the CORS middleware.
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["OPTIONS", "GET", "POST", "PUT", "DELETE"],
        # Headers should be pdf or json, but more testing is required
        # "Content-Type", "???", "application/json"
        allow_headers=["*"]
    )
    return app


# Create the FastAPI app.
app = init_app()

# Create a handler for AWS Lambda.
handler = Mangum(app)

# Start the server.
if __name__ == "__main__":
    uvicorn.run(app,
                host=settings.API_HOST,
                reload=True,
                port=settings.API_PORT)
