# Generated by Django 4.2.8 on 2024-01-04 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_todo_amount_todo_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='completed',
            field=models.CharField(default='False', max_length=400),
        ),
    ]
