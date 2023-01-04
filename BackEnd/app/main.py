from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.users import login, create_user, validate_user, get_profile

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login.router)
app.include_router(create_user.router)
app.include_router(validate_user.router)
app.include_router(get_profile.router)