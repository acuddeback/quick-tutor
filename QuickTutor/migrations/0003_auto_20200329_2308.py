# Generated by Django 3.0.2 on 2020-03-30 04:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('QuickTutor', '0002_auto_20200322_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='course_topic',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='session',
            name='end_date_and_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 30, 5, 8, 39, 47913, tzinfo=utc)),
        ),
    ]
