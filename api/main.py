import os
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import phoenix as px
from phoenix.otel import register
from openinference.instrumentation.agno import AgnoInstrumentor
from opentelemetry import trace as trace_api
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk import trace as trace_sdk
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, BatchSpanProcessor

from api.routes.v1_router import v1_router
from api.settings import api_settings


# Configure Phoenix tracing
def setup_phoenix_tracing():
    """Setup Phoenix tracing for observability"""
    # Get configuration from environment
    phoenix_api_key = os.getenv("ARIZE_PHOENIX_API_KEY")
    collector_endpoint = os.getenv("PHOENIX_COLLECTOR_ENDPOINT", "http://localhost:6006/v1/traces")
    
    # Create OTLP exporter with batch processing
    otlp_exporter = OTLPSpanExporter(
        endpoint=collector_endpoint,
        headers={"api_key": phoenix_api_key} if phoenix_api_key else None,
    )
    
    # Create tracer provider with batch processor
    tracer_provider = trace_sdk.TracerProvider()
    tracer_provider.add_span_processor(BatchSpanProcessor(otlp_exporter))
    
    # Set as global tracer provider
    trace_api.set_tracer_provider(tracer_provider)
    
    # Instrument Agno
    AgnoInstrumentor().instrument()


# Initialize Phoenix tracing
setup_phoenix_tracing()


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
