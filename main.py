from fastapi import FastAPI
from container import Container
import endpoints


def create_app() -> FastAPI:
    container = Container()
    container.config.from_yaml("./config.yml")

    app = FastAPI()
    app.container = container
    app.include_router(endpoints.router) 
    return app


app = create_app()
