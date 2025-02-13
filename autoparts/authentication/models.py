import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField('Endereço de Email', max_length=127, blank=False, null=False, unique=True)
    username = models.CharField('Nome de Usuário', max_length=127, blank=False, null=False, unique=True)
    password = models.CharField('Senha', max_length=127, blank=True, null=True)
    name = models.CharField('Nome', max_length=127, blank=False, null=False)

    class Meta:
        db_table = 'authentication_user'