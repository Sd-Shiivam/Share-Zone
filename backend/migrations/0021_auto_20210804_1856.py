# Generated by Django 3.1.7 on 2021-08-04 13:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0020_auto_20210804_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='file_id',
            field=models.CharField(default='', max_length=1000, unique=True),
        ),
        migrations.AlterField(
            model_name='files',
            name='upload_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 4, 18, 56, 0, 511661)),
        ),
        migrations.AlterField(
            model_name='like',
            name='like_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 4, 18, 56, 0, 555511)),
        ),
    ]
