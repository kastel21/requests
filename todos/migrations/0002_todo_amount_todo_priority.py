# Generated by Django 4.2.8 on 2024-01-04 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='amount',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='priority',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
