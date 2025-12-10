from pydantic import BaseModel
from requests import post
from fastapi import FastAPI
from models import User
from config import DATABASE_URL
from tortoise.contrib.fastapi import register_tortoise
from typing import Optional

app = FastAPI()

class DataModel(BaseModel):
    id: Optional[int] = None
    last_name: str
    type: Optional[int] = None
    telegram_id: Optional[int] = None
    username: Optional[str] = None
    chat_id: Optional[int] = None
    step: Optional[int] = None
    step_under: Optional[int] = None

@app.post("/user/{telegram_id}")
async def get_user(telegram_id: str, data: DataModel):
    user = await User.get_or_none(telegram_id=telegram_id)
    if not user:
        print(data.json())
        return post(f'http://95.182.118.221:8000/user/detail/{telegram_id}/', data=data.json(), headers={'Content-type': 'application/json'}).json()

    return {
        "id": user.id,
        "chat_id": user.chat_id,
        "full_name": user.last_name,
        "username": user.username,
        "type": user.type,
        "step": user.step,
        "step_under": user.step_under,
    }


# Tortoise ORM init
register_tortoise(
    app,
    db_url=DATABASE_URL,
    modules={"models": ["models"]},
    generate_schemas=False,    # Agar table yo'q bo'lsa True qilsa ham bo'ladi
    add_exception_handlers=True,
)
