from fastapi.testclient import TestClient
from app.main import app
import jwt
from pony.orm import db_session
from app.api.models import *

client = TestClient(app)

SECRET_KEY = "my_secret_key"
ALGORITHM = "HS256"
dummy_user = {
    "email": "famaf01@gmail.com",
    "password": "nuevofamaf"
}
dummy_user2 = {
    "email": "famaf02@gmail.com",
    "password": "nuevofamaf"
}
encoded_jwt = jwt.encode(dummy_user, SECRET_KEY, algorithm=ALGORITHM)
encoded = encoded_jwt.decode("utf-8")

encoded_jwt2 = jwt.encode(dummy_user2, SECRET_KEY, algorithm=ALGORITHM)
encoded2 = encoded_jwt2.decode("utf-8")


# test create Chat
def test_create_chat():
    with db_session:
        User(username = "pedro", email = "famaf01@gmail.com", password = "nuevofamaf", is_validated = True)
    response = client.post(
        "/create_chat",
        headers={"authorization": "Bearer " + encoded},
        json={"name": "example", "password": "asd"}
    )
    assert response.status_code == 200
    with db_session:
        m = Chat.get(user = User.get(email = "famaf01@gmail.com"))
    assert response.json() == {'chat_id': m.id}
    with db_session:
        delete(m for m in Chat if m.name == "example" and m.user == User.get(email = "famaf01@gmail.com"))
        delete (u for u in User if u.email == "famaf01@gmail.com")


def test_invalid_token():
    response = client.post(
        "/create_chat",
        headers={"authorization": "Bearer " + encoded2},
        json={"name": "example", "password": "asd"}
    )
    assert response.status_code == 200
    assert response.json() == {"error": "Invalid X-Token header"}


def test_invalid_header():
    response = client.post(
        "/create_chat",
        headers={"authorization": encoded},
        json={"name": "example", "password": "asd"}
    )
    assert response.status_code == 200
    assert response.json() == {'error': 'Invalid X-Token header'}
