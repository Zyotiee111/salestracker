from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name ='invoice'
urlpatterns = [
    path('create/',views.create,name = "create_invoice"),
    path('viewinvoice/',views.display, name= "view_invoice"),
]