# Generated by Django 4.0.6 on 2022-08-13 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0005_company_alter_supplier_supplier_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier',
            old_name='supplier_name',
            new_name='company',
        ),
    ]
