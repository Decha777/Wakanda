# Generated by Django 2.2.7 on 2019-11-30 22:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tutorials', '0002_tutorial_tutorial_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Date published'),
        ),
    ]
