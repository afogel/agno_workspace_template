import os
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from phoenix.otel import register

from api.routes.v1_router import v1_router
from api.settings import api_settings


# Initialize Phoenix tracing
tracer_provider = register(
    project_name="test_agno_app",
    batch=True,
    auto_instrument=True,
    endpoint=os.getenv("PHOENIX_COLLECTOR_ENDPOINT", "http://localhost:6006/v1/traces"),
)


def create_app() -> FastAPI:
    """Create a FastAPI App"""

    # Create FastAPI App
    app: FastAPI = FastAPI(
        title=api_settings.title,
        version=api_settings.version,
        docs_url="/docs" if api_settings.docs_enabled else None,
        redoc_url="/redoc" if api_settings.docs_enabled else None,
        openapi_url="/openapi.json" if api_settings.docs_enabled else None,
    )

    # Add v1 router
    app.include_router(v1_router)

    # Add Middlewares
    app.add_middleware(
        CORSMiddleware,
        allow_origins=list(api_settings.cors_origin_list) if api_settings.cors_origin_list else ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


# Create FastAPI app
app = create_app()
