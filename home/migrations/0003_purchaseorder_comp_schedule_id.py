# Generated by Django 4.2.8 on 2023-12-17 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_comparativeschedule_dpt_project_requesting_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='comp_schedule_id',
            field=models.CharField(default='None', max_length=300),
        ),
    ]
