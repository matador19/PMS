from tkinter import CASCADE
from django.db import models

# Create your models here.
class Property(models.Model):
    propertyId=models.AutoField(primary_key=True)
    propertyName=models.CharField(max_length=255)
    location=models.CharField(max_length=255) 
    
    def __str__ (self):
        return self.propertyName

class Tenant(models.Model):
    TenantId=models.BigIntegerField()
    TenantName=models.CharField(max_length=255)
    TenantPhone=models.CharField(max_length=255)

    def __str__(self):
        return self.TenantName


class HouseAllocation(models.Model):
    propertyName=models.ForeignKey(Property,null=True,on_delete=models.SET_NULL)
    HouseNumber=models.CharField(max_length=255)
    TenantName=models.ForeignKey(Tenant,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        labelone=str(self.propertyName)
        labeltwo=str(self.HouseNumber)
        labelthree=str(self.TenantName)
        label=labelone+': '+labeltwo+': '+labelthree
        return label