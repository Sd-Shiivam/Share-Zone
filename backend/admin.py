from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header ='File-Share-Zone'
admin.site.register(files)
admin.site.register(like)
admin.site.register(likeuser)