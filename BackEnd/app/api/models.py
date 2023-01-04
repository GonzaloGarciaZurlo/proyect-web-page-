from pony.orm import *

db = Database()

class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    username = Required(str)
    email = Required(str)
    password = Required(str)
    avatar = Optional(str)
    is_validated = Required(bool)
    verify_token = Optional(str)
    chats = Set("Chat")

class Chat(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    password = Optional(str)
    user = Required(User)

db.bind(provider='sqlite', filename='database.sqlite', create_db=True)

db.generate_mapping(create_tables=True)