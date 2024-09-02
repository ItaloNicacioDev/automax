from django.db import models

from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.

class Usuario(AbstractUser):
    # Adicione novos campos personalizados, se necessário
     groups = models.ManyToManyField(Group, related_name='usuario_set')
     user_permissions = models.ManyToManyField(Permission, related_name='usuario_permissions_set')

     def __str__(self):
        return self.username