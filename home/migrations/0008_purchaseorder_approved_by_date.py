# Generated by Django 3.2.6 on 2023-04-25 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_purchaseorderquotation'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='approved_by_date',
            field=models.CharField(default='None', max_length=150),
        ),
    ]
