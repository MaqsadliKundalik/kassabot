from tortoise import Model, fields

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
    price = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    
    class Meta:
        table = "reports"

class ReportVote(Model):
    id = fields.IntField(pk=True)
    report = fields.ForeignKeyField("models.Report", related_name="votes")
    user = fields.ForeignKeyField("models.User", related_name="votes")
    vote = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    
    class Meta:
        table = "report_votes"
