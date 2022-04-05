# Generated by Django 4.0.3 on 2022-04-05 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PROPERTYMANAGEMENT', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TenantId', models.BigIntegerField()),
                ('TenantName', models.CharField(max_length=255)),
                ('TenantPhone', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HouseAllocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HouseNumber', models.CharField(max_length=255)),
                ('TenantName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PROPERTYMANAGEMENT.tenant')),
                ('propertyName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PROPERTYMANAGEMENT.property')),
            ],
        ),
    ]