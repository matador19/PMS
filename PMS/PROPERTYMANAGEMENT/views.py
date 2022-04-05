from django.shortcuts import render
from django.http import HttpResponse
from .models import Property, Tenant, HouseAllocation
# Create your views here.
def home(request):
    Githuraiproperty=Property.objects.get(propertyName="Githurai Property")
    Roysambuproperty=Property.objects.get(propertyName="Roysambu Property")
    GithuraiTenants = HouseAllocation.objects.filter(propertyName=1)
    RoysambuTenants = HouseAllocation.objects.filter(propertyName=2)
    print(GithuraiTenants)
    return render(request,'home.html',{'Githuraiproperty':Githuraiproperty,'Roysambuproperty':Roysambuproperty,'GithuraiTenants':GithuraiTenants,'RoysambuTenants':RoysambuTenants})

def Githurai(request):
    Githuraiproperty=Property.objects.get(propertyName="Githurai Property")
    GithuraiTenants=HouseAllocation.objects.filter(propertyName=1)

    PaymentThresholdOne=16500
    PaymentThresholdTwo=25000
    PaymentThresholdThree=30000

    