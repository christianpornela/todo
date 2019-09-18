# Generated by Django 2.2.5 on 2019-09-16 13:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoList', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completed',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
