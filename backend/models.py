from django.db import models
from datetime import datetime 
from django.dispatch import receiver
import os
# Create your models here.
class files(models.Model):
    id=models.IntegerField(primary_key=True,unique=True)
    file_id=models.CharField(max_length=1000,default='',unique=True)
    upload_at = models.DateTimeField(default=datetime.now())
    lock=models.CharField(max_length=2,choices=(('0','0'),('1','1')),default='0') 
    delete_file=models.CharField(max_length=10,choices=(('Normal','Normal'),('deleted','deleted')),default='Normal') 
    password=models.CharField(max_length=100,default='none')
    name=models.CharField(max_length=1000)
    file=models.FileField(upload_to='')
    def __str__(self):
        return f"{self.name}|{self.delete_file}"

class like(models.Model):
    like_on = models.DateTimeField(default=datetime.now())
    name=models.CharField(max_length=1000,default='Unknown')
    id=models.AutoField(primary_key=True)
    likeno=models.CharField(default='1',max_length=10000)
    def __str__(self):
        return self.name

@receiver(models.signals.post_delete, sender=files)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    """
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)