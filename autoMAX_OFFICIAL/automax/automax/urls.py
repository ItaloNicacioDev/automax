
from django.contrib import admin
from django.urls import path , include
from  cadastro import views
from  login import views

urlpatterns = [
    #rota, view resposavel, nome de ref
    path('admin/', admin.site.urls),
     # Para redirecionar para o login por padrão
    path('', include('login.urls')),
    #Pag de cadastro de funcionario
    path('cadastro/', include('cadastro.urls')),
]
