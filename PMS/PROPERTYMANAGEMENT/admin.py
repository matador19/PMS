from django.contrib import admin
from .models import Property, Tenant, HouseAllocation,Payments
# Register your models here.
admin.site.register(Property)
admin.site.register(Tenant)
admin.site.register(HouseAllocation)
admin.site.register(Payments)