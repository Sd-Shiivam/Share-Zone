from django.db import models
from datetime import datetime 
# Create your models here.
class files(models.Model):
    id=models.AutoField(primary_key=True)
    upload_at = models.DateTimeField(default=datetime.now())
    name=models.CharField(max_length=1000)
    file=models.FileField(upload_to='')
    def __str__(self):
        return self.name

class like(models.Model):
    ids=models.CharField(default='1',max_length=1)
    likeno=models.CharField(default='0',max_length=10000)
    def __str__(self):
        return self.likeno
class likeuser(models.Model):
    like_on = models.DateTimeField(default=datetime.now())
    name=models.CharField(max_length=1000)
    def __str__(self):
        return self.name