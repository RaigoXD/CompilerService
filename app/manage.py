from fastapi import FastAPI

# controllers
from app.routes.index import sintaxis_verify


def get_application() -> FastAPI:
    metadata = [
        {
            "name": "LexerBackend",
            "description": "Backend to verify the sintaxis of miniC",
        }
    ]

    application = FastAPI(
        title="Lexer backend",
        description="This backend is used to verify the sintaxis of miniC",
        version="1.0.0",
        openapi_tags=metadata,
    )

    application.include_router(sintaxis_verify, prefix="/api")

    return application


app = get_application()
