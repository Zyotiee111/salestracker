from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name ='customer'
urlpatterns = [
    path('add/',views.add,name = "add_customer"),
    path('show/',views.show, name= "show_customer"),
    path('edit/<int:id>', views.edit, name= "edit_customer"),
    path('delete/<int:id>', views.delete, name = "delete_customer"),
]