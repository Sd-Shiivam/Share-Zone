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
    def delete(self,using=None, keep_parents=False):
        self.file.delete(self.file.name)
        super().delete()