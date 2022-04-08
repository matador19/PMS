from ast import Return
from asyncio.windows_events import NULL
from gettext import NullTranslations
from itertools import chain
import json
from optparse import Values
from time import strftime
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
import requests
import base64
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


def CustomerToBusiness(request):
     #Customer ID
    customer_key = "P5giKpFolWJzLQAqsLWYPJH7GWdS3X2A"
    # Customer secret
    customer_secret = "70otjSiYQptugMc6"
    # Concatenate customer key and customer secret and use base64 to encode the concatenated string
    credentials = customer_key + ":" + customer_secret
    # Encode with base64
    base64_credentials = base64.b64encode(credentials.encode("utf8"))
    credential = base64_credentials.decode("utf8")
    response = requests.request("GET", 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials', headers = { 'Authorization': 'Basic '+credential })
    response=response.json()
    token=response['access_token']
    headers = {
    'Authorization': 'Bearer '+token,
     'Content-Type': 'application/json',
    }
    payload = {
    
    }
    response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl', headers = headers, json=payload)
    response=json.loads(response.text)
    print(response)
    return render(request,'Roysambu.html')