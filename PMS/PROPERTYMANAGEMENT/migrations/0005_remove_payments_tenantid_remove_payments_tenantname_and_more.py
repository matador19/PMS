# Generated by Django 4.0.3 on 2022-04-06 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PROPERTYMANAGEMENT', '0004_alter_payments_tenantid_alter_payments_tenantname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payments',
            name='TenantId',
        ),
        migrations.RemoveField(
            model_name='payments',
            name='TenantName',
        ),
        migrations.AlterField(
            model_name='payments',
            name='HouseNumber',
            field=models.CharField(max_length=15, null=True),
        ),
    ]