# Generated by Django 3.2 on 2023-06-07 06:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasedtemplate',
            name='download_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='purchasesummary',
            name='order_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='purchasesummary',
            name='total_amount',
            field=models.FloatField(validators=[django.core.validators.MaxValueValidator(10000000), django.core.validators.MinValueValidator(10)]),
        ),
    ]
