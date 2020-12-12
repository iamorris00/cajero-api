from typing import Dict
from pydantic import BaseModel


class UserInDB(BaseModel):  # Create the artificial table of the database
    username: str  # Artificial columns
    password: str
    balance: int


database_users = Dict[str, UserInDB]  # Creates the artificial database

database_users = {
    "koopa15": UserInDB(**{
        "username": "koopa15",
        "password": "koopa95",
        "balance": 971031
    }),
    "michi31": UserInDB(**{
        "username": "michi31",
        "password": "michi97",
        "balance": 950415
    })
}


def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None


def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db
