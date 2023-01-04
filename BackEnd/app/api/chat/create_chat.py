from fastapi import Request
from pydantic import BaseModel
from app.api.models import *
from pony.orm import db_session
from fastapi import APIRouter
from app.get_user import *

router = APIRouter()


# body que me deberian pasar en el request
class BodyChat(BaseModel):
    name: str
    password: str

@router.post("/create_chat")
async def user_createchat(body: BodyChat, request: Request):
    with db_session:
        curent_user = get_user(request.headers)
        if curent_user == None:     # no existe el usuario en la bd o no hay header
            return {'error': 'Invalid X-Token header'}
        chat = Chat(name=body.name, password=body.password, user=curent_user)                      
        commit()
        return {'chat_id': chat.id}