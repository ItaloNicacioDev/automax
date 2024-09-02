from django.urls import path
from .views import register, login, logout_view
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'), # Define a URL raiz para a página inicial
]