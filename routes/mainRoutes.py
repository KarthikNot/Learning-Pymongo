from fastapi import APIRouter, Request
from models.schemas import PersonInfo

mainRouter = APIRouter()

@mainRouter.get('/')
def homeRoute():
    return {'message' : 'hello'}

@mainRouter.get(f'/parameter-path/DynamicRouting')
def parameterPath_DR():
    return {'message' : 'Dynamic Routing Path'}

@mainRouter.get(f'/parameter-path/{id}')
def parameterPath(id : int):
    return {'message' : 'Parameter Path', 'Id' : id}

@mainRouter.get(f'/query-parameters')
def queryParameters(this : bool):
    if this: return True
    return False

@mainRouter.get(f'/send-request')
def sendRequest(data : PersonInfo):
    return {'message' : data}
