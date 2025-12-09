from requests import post
from fastapi import FastAPI, HTTPException, Depends
from models import User
from config import DATABASE_URL
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()


@app.post("/user/{telegram_id}")
async def get_user(telegram_id: str, data: User):
    user = await User.get_or_none(telegram_id=telegram_id)
    if not user:
        return post(f'http://95.182.118.221:8001/detail/{telegram_id}', data=data).json()

    return {
        "id": user.id,
        "tg_id": user.telegram_id,
        "full_name": user.last_name,
        "username": user.username,
    }


# Tortoise ORM init
register_tortoise(
    app,
    db_url=DATABASE_URL,
    modules={"models": ["models"]},
    generate_schemas=False,    # Agar table yo'q bo'lsa True qilsa ham bo'ladi
    add_exception_handlers=True,
)
