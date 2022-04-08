from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='PMS-home'),
    path('Githurai/',views.Githurai, name='Githurai'),
    path('Roysambu/',views.Roysambu, name='Roysambu'),
    path('C2B/',views.CustomerToBusiness)
    
]