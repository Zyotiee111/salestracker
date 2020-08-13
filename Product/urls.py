from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.track,name = "add_product"),
    path('show/',views.display , name= "show_product"),
    path('edit/<int:id>', views.update, name= "edit_product"),
    path('delete/<int:id>', views.delete, name = "delete_product"),
]