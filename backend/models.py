from django.db import models
from datetime import datetime 
# Create your models here.
class files(models.Model):
    id=models.AutoField(primary_key=True)
    upload_at = models.DateTimeField(default=datetime.now())
    lock=models.CharField(max_length=2,choices=(('0','0'),('1','1')),default='0') 
    password=models.CharField(max_length=100,default='none')
    name=models.CharField(max_length=1000)
    file=models.FileField(upload_to='')
    def __str__(self):
        return self.name

class like(models.Model):
    like_on = models.DateTimeField(default=datetime.now())
    name=models.CharField(max_length=1000,default='Unknown')
    id=models.AutoField(primary_key=True)
    likeno=models.CharField(default='1',max_length=10000)
    def __str__(self):
        return self.name