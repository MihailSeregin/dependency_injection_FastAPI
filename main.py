from fastapi import FastAPI
from container import Container
import endpoints


# print(endpoints.router)


def create_app() -> FastAPI:
    container = Container()
    container.config.from_yaml("./config.yml")

    app = FastAPI()
    app.container = container
    app.include_router(endpoints.router) 
    return app


app = create_app()


if __name__=='__main__':
    container = Container()
    container.service().print()
    # container.wire(modules=[])
    print_param()
