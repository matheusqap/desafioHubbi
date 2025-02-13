from django.db import models 
from django.core.validators import MinValueValidator
from autoparts.core.models import BaseModel

class Car(BaseModel):
    name = models.CharField(verbose_name='Nome', max_length=127, null=False, blank=False)
    manufacturer = models.CharField(verbose_name='Fabricante', max_length=127, null=False, blank=False)
    year = models.PositiveSmallIntegerField(verbose_name='Ano de Fabricação', null=False, blank=False, validators=[MinValueValidator(1900)])

    class Meta:
        verbose_name_plural = 'Carros'
        verbose_name = 'Carro'