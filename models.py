from tortoise import fields
from tortoise.models import Model

class User(Model):
    id = fields.IntField(pk=True)
    telegram_id = fields.CharField(max_length=100, unique=True, index=True)
    chat_id = fields.CharField(max_length=100, unique=True, index=True)
    last_name = fields.CharField(max_length=255, null=True)
    username = fields.CharField(max_length=255, null=True)
    type = fields.IntField()
    step = fields.IntField()
    step_under = fields.IntField()

    class Meta:
        table = "user_user"
