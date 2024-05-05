from collections import namedtuple
from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("deleterecord/<int:id>/",views.delete,name="deleterecord"),
    path("updaterecord/<int:id>/",views.update,name="updaterecord")
]