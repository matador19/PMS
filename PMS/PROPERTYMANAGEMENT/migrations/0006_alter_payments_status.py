# Generated by Django 4.0.3 on 2022-04-06 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PROPERTYMANAGEMENT', '0005_remove_payments_tenantid_remove_payments_tenantname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='Status',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
