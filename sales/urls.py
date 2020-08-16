from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name ='sale'
urlpatterns = [
    path('add/',views.add,name = "add_sale"),
    path('show/',views.show, name= "show_sale"),
    path('edit/<int:id>', views.edit, name= "edit_sale"),
    path('delete/<int:id>', views.delete, name = "delete_sale"),
    path('createinvoice/',views.create,name = "create_invoice"),
    path('showinvoice/',views.display, name = "show_invoice"),
  
   
]