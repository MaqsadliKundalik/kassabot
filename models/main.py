from tortoise import Model, fields
from datetime import datetime
from config import get_tashkent_time

class User(Model):
    id = fields.IntField(pk=True)
    telegram_id = fields.IntField()
    name = fields.CharField(max_length=255)
    
    class Meta:
        table = "users"

class Report(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="reports")
    caption = fields.TextField()
    price = fields.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        table = "reports"

class ReportVote(Model):
    id = fields.IntField(pk=True)
    report = fields.ForeignKeyField("models.Report", related_name="votes")
    user = fields.ForeignKeyField("models.User", related_name="votes")
    vote = fields.CharField(max_length=255)

    class Meta:
        table = "report_votes"

class InOutFlow(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="inoutflows")
    amount = fields.DecimalField(max_digits=10, decimal_places=2)
    type = fields.CharField(max_length=255)
    description = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    
    class Meta:
        table = "inoutflows"
    
    async def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = get_tashkent_time()
        await super().save(*args, **kwargs)

