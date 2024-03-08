from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject
from container import Container
from sorters import Pipeline


router = APIRouter()

@router.get('/')
@inject
def home_page():
    return {'message': 'Hello World'}

@router.get("/recommend/")
@inject
def recommend(user_id: int, pipeline: Pipeline = Depends(Provide[Container.pipeline])): 
    return {'recommended_partners' : pipeline.recommend(user_id)}



    

