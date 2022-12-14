# Generated by Django 4.0.6 on 2022-08-13 09:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0003_country_function_service_supplier_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='avg_cost',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='avg_delivery_time',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='escalations',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='rating',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(60)]),
        ),
        migrations.AddField(
            model_name='supplier',
            name='resources',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
