from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject
from container import Container



router = APIRouter()

@router.get('/')
@inject
def home_page():
    return {'message': 'Hello World'}


@router.get("/recommend/")
@inject
def recommend(pipeline: Depends(Provide[Container.pipeline]), user_id: int): 
    pipeline.recommend(user_id)



    

