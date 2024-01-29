from fastapi import FastAPI

from src.db.models import user, profile
from src.db.db_setup import engine

user.Base.metadata.create_all(bind=engine)
profile.Base.metadata.create_all(bind=engine)


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}