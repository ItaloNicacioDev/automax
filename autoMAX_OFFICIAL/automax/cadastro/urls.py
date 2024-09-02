from django.urls import path

from . import views

urlpatterns = [
    path('', views.cadastro_func, name='cadastro'),
]