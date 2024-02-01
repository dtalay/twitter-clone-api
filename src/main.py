import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv, find_dotenv

from src.db.models import user, profile
from src.db.db_setup import engine

from src.api.public.register import router as register_router
from src.api.user import router as user_router
from src.api.public.auth import router as auth_router

load_dotenv(dotenv_path=find_dotenv())

user.Base.metadata.create_all(bind=engine)
profile.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(register_router)
app.include_router(user_router)
app.include_router(auth_router)


@app.get("/")
async def root():
    return {"message": "Hello Worlds "}


if __name__ == "__main__":
    print("SERVER STARTING...")
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
