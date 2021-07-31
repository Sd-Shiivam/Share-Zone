from django.db import models
from datetime import datetime 
# Create your models here.
class files(models.Model):
    id=models.AutoField(primary_key=True)
    upload_at = models.DateTimeField(default=datetime.now())
    name=models.CharField(max_length=1000)
    file=models.FileField(upload_to='file/')
    def __str__(self):
        return self.name
