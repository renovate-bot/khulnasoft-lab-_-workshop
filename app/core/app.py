from readyapi import ReadyAPI
from readyapi.middleware.cors import CORSMiddleware
from readyapi.staticfiles import StaticFiles
from app.api import demo_1, demo_2, demo_3, home


def create_app() -> ReadyAPI:
    app = ReadyAPI(title="Readyapi Template")

    app.mount("/static", StaticFiles(directory="static"), name="static")

    app.include_router(home.router)
    app.include_router(demo_1.router)
    app.include_router(demo_2.router)
    app.include_router(demo_3.router)

    origins = [
        "http://localhost:3000",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
