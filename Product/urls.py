from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.add,name = "add_product"),
    path('show/',views.show , name= "show_product"),
    path('edit/<int:id>', views.edit, name= "edit_product"),
    path('delete/<int:id>', views.delete, name = "delete_product"),
]