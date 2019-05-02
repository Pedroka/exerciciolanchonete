# coding=utf-8
from django.db import models


class Lanches(models.Model):

    lanche_name = models.CharField('Nome do Lanche',max_length=100)
    lanche_slug = models.SlugField('Identificador Lanche',max_length=100)
    lanche_description = models.TextField('Descricao',blank=True)
    lanche_created = models.DateTimeField('Criado em',auto_now_add=True)
    lanche_modified = models.DateTimeField('Modificado em',auto_now=True)
    ingredientes = models.ManyToManyField('Ingredientes')
    imagem = models.ImageField(blank=True,null=True,upload_to='imagens/',max_length=255)

    class Meta:
        verbose_name = 'Lanche'
        verbose_name_plural = 'Lanches'

    def __str__(self):
        return self.lanche_name

class Ingredientes(models.Model):
    ingrediente_name = models.CharField('Nome Ingrediente',max_length=100)
    ingredient_slug = models.SlugField('Identificador Ingrediente',max_length=100)
    ingredient_price = models.DecimalField('Preço',decimal_places=2,max_digits=6)
    ingredient_created = models.DateTimeField('Criado em',auto_now_add=True)
    ingredient_modifed = models.DateTimeField('Modificado em',auto_now=True)
    imagem = models.ImageField(blank=True,null=True,upload_to='imagens/',max_length=255)

    class Meta:
        verbose_name = 'Ingrediente'
        verbose_name_plural = 'Ingredientes'

    def __str__(self):
        return self.ingrediente_name


