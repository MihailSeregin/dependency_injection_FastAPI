from fastapi import APIRouter
from dependency_injector.wiring import Provide, inject

router = APIRouter()



from dependency_injector import containers, providers

class Service:
    def __init__(self, param):
        self.param = 5

    def print(self,):
        print(self.param)

class Container(containers.DeclarativeContainer):

    service = providers.Factory(Service, param=5)

@inject
def print_param(service: Service = Provide[Container.service]):
    print(service.param)

@router.get('/')
def home_page():
    return {'message': 'Hello World'}


@router.get("/recommend/")
@inject
def recommend(container, user_id: int): #param
    service = container.service
    service.print()



if __name__=='__main__':
    container = Container()
    container.service().print()
    container.wire(modules=[__name__])
    print_param()
    

