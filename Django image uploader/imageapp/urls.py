from django.urls import path

from . import views

urlpatterns=[
    path("",views.home,name='home'),
    path("details/<int:id>/", views.details, name="details"),
    path("delete/<int:id>/", views.delete_image, name="delete_image"),
      
]