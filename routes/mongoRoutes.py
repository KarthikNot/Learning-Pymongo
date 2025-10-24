from controllers.db import get_db
from models.schemas import PersonInfo
from fastapi import APIRouter, Depends

dbRouter = APIRouter(prefix='/database')

@dbRouter.get('/get_doc/{name}')
def getDocument(name : str, collection = Depends(get_db)):
    document = collection.find_one({"name": name})
    if document:
        document['_id'] = str(document['_id'])
        return document
    return {"message": "Document not found"}

@dbRouter.post('/post_doc/')
def postDocument(data : PersonInfo, collection = Depends(get_db)):
    result = collection.insert_one(data.model_dump())
    if result.acknowledged: return {'message': 'Data uploaded!', 'id': str(result.inserted_id)}
    return {'message': 'Could not be uploaded!'}