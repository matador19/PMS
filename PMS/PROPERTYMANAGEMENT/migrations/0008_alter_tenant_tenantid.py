# Generated by Django 4.0.3 on 2022-04-08 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PROPERTYMANAGEMENT', '0007_rename_housenumber_payments_accountnumber_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='TenantId',
            field=models.BigIntegerField(unique=True),
        ),
    ]