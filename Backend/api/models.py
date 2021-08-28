from django.db import models

# Create your models here.

class Tags_info(models.Model):
    task_id = models.CharField(max_length=255)
    info = models.JSONField()


