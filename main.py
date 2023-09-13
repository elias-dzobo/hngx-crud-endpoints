from fastapi import FastAPI, APIRouter, status
import uvicorn 
from pydantic import BaseModel
import user
from models import models 
from fastapi.middleware.cors import CORSMiddleware 
from db.database import engine 

models.Base.metadata.create_all(bind=engine) 


app = FastAPI()

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


app.include_router(user.router, tags=['User'], prefix='/api') 

@app.get('/healthcheck')
def root():
    return {'message': 'API Running Successfully'} 