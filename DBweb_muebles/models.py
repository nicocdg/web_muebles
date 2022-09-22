from django.db import models

class Sillones(models.Model):
    modelo = models.CharField(max_length=40)
    material = models.CharField(max_length=40)
    cuerpos = models.IntegerField()

class Mesas(models.Model):
    modelo = models.CharField(max_length=40)
    material = models.CharField(max_length=40)
    capacidadPersonas = models.IntegerField()

class Armarios(models.Model):
    modelo = models.CharField(max_length=40)
    material = models.CharField(max_length=40)
    puertas = models.IntegerField()
