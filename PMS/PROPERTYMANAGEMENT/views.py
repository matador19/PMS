from asyncio.windows_events import NULL
from gettext import NullTranslations
from itertools import chain
from optparse import Values
from time import strftime
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import Property, Tenant, HouseAllocation,Payments
# Create your views here.
def home(request):
    Githuraiproperty=Property.objects.get(propertyName="Githurai Property")
    Roysambuproperty=Property.objects.get(propertyName="Roysambu Property")
    GithuraiTenants = HouseAllocation.objects.filter(propertyName=1)
    RoysambuTenants = HouseAllocation.objects.filter(propertyName=2)
    return render(request,'home.html',{'Githuraiproperty':Githuraiproperty,'Roysambuproperty':Roysambuproperty,'GithuraiTenants':GithuraiTenants,'RoysambuTenants':RoysambuTenants})

def Githurai(request):
    Githuraiproperty=Property.objects.get(propertyName="Githurai Property")
    GithuraiTenants=HouseAllocation.objects.filter(propertyName=1)
    GithuraiPayment=Payments.objects.filter(AccountNumber__contains='GIT')
    GithuraiTenants=GithuraiTenants.values()
    GithuraiPayment=GithuraiPayment.values()
    all_payments= list()
    Balance=0
    for x in range(GithuraiTenants.count()):
        TenantName=Tenant.objects.get(id=GithuraiTenants[x]['TenantName_id'])
        TenantHouseAllocation= HouseAllocation.objects.filter(TenantName=TenantName)
        HouseNumber=TenantHouseAllocation.values()[0]['HouseNumber']
        TenantPayments= Payments.objects.filter(AccountNumber=HouseNumber).values()
        for TenantPayment in TenantPayments:
            TenantPayment['TenantName']=str(TenantName)
            TenantPayment['Balance']=TenantPayment['AmountPaid']-TenantPayment['AmountToBePaid']
            all_payments.append(TenantPayment)
    today= datetime.now().strftime("%d")
    if today > "05":
        pass

    PaymentThresholdOne=16500
    PaymentThresholdTwo=25000
    PaymentThresholdThree=30000

    return render(request,'Githurai.html',{'Githuraiproperty':Githuraiproperty,'all_payments':all_payments})


def Roysambu(request):
    Roysambuproperty=Property.objects.get(propertyName="Roysambu Property")
    RoysambuTenants=HouseAllocation.objects.filter(propertyName=2)
    RoysambuPayment=Payments.objects.filter(AccountNumber__contains='ROY')
    RoysambuTenants=RoysambuTenants.values()
    RoysambuPayment=RoysambuPayment.values()
    all_payments= list()
    Balance=0
    for x in range(RoysambuTenants.count()):
        TenantName=Tenant.objects.get(id=RoysambuTenants[x]['TenantName_id'])
        TenantHouseAllocation= HouseAllocation.objects.filter(TenantName=TenantName)
        HouseNumber=TenantHouseAllocation.values()[0]['HouseNumber']
        TenantPayments= Payments.objects.filter(AccountNumber=HouseNumber).values()
        for TenantPayment in TenantPayments:
            TenantPayment['TenantName']=str(TenantName)
            TenantPayment['Balance']=TenantPayment['AmountPaid']-TenantPayment['AmountToBePaid']
            all_payments.append(TenantPayment)

    today= datetime.now().strftime("%d")
    if today > "05":
        pass

    PaymentThresholdOne=16500
    PaymentThresholdTwo=25000
    PaymentThresholdThree=30000

    return render(request,'Roysambu.html',{'Roysambuproperty':Roysambuproperty,'all_payments':all_payments})

