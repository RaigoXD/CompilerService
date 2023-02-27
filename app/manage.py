from fastapi import FastAPI

#cors 
from fastapi.middleware.cors import CORSMiddleware

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

    application.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )   

    application.include_router(sintaxis_verify, prefix="/api")

    return application


app = get_application()
