from decimal import Decimal
from django.db import models 
from django.core.validators import MinValueValidator

from autoparts.cars.models import Car
from autoparts.core.models import BaseModel


class Part(BaseModel):
    part_number = models.CharField(verbose_name='Numero da Peça', null=False, blank=False, max_length=65)
    name = models.CharField(verbose_name='Nome da Peça', null=False, blank=False, max_length=127)
    details = models.CharField(verbose_name='Detalhes da Peça', null=False, blank=False, max_length=513)
    price = models.DecimalField(verbose_name='Preço da Peça', decimal_places=2, max_digits=10, null=False, blank=False, validators=[MinValueValidator(Decimal(0))])
    quantity = models.PositiveSmallIntegerField(verbose_name='Quantidade de Peças', null=False, blank=False, validators=[MinValueValidator(0)])

    class Meta:
        verbose_name_plural = 'Peças'
        verbose_name = 'Peça'


class CarParts(BaseModel):
    car = models.ForeignKey(Car, verbose_name='Carro', null=False, blank=False, on_delete=models.PROTECT)
    part = models.ForeignKey(Part, verbose_name='Peça', null=False, blank=False, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Peças dos carros'
        verbose_name = 'Peça do carro'