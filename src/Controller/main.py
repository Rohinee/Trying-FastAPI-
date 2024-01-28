from fastapi import FastAPI
from Models import model

from DBConnect.dbconnect import engine
from Routers import auth, admin, todo, user
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
model.Base.metadata.create_all(bind=engine)


app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(todo.router)
app.include_router(user.router)
