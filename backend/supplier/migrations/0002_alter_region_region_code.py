# Generated by Django 4.0.6 on 2022-08-05 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='region_code',
            field=models.CharField(max_length=10),
        ),
    ]
