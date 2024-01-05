# Generated by Django 4.2.8 on 2024-01-04 08:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('todo_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='NotificationTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_time', models.CharField(max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_text', models.CharField(max_length=1000)),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('due_date', models.DateTimeField(null=True, verbose_name='due_date')),
                ('email_notification', models.EmailField(max_length=500, null=True)),
                ('notification_time', models.CharField(max_length=400, null=True)),
                ('sent_reminder', models.CharField(default='False', max_length=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todos.category')),
            ],
        ),
    ]
