from django.urls import path
from . import views



# Sobre/

urlpatterns = [
    path('',views.index)
]