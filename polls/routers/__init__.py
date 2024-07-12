from fastapi import FastAPI

from .main_body import router as input_start

__all__ = ("register_routers",)


def register_routers(app: FastAPI):
    app.include_router(input_start)
