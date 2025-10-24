import uvicorn
from fastapi import FastAPI
from routes.mainRoutes import mainRouter
from routes.mongoRoutes import dbRouter 

app = FastAPI()

app.include_router(mainRouter)
app.include_router(dbRouter)

if __name__ == '__main__':
    uvicorn.run()