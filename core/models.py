from django.db import models

class Label(models.Model):
    name = models.CharField("Name", max_length=50)

    def _str_(self):
        return self.name

class Disco(models.Model):
    name = models.CharField("Nome", max_length=50)
    description = models.TextField("Descrição", max_length=400)
    selo_fonografico = models.ForeignKey(Label, on_delete=models.CASCADE)
    year = models.PositiveIntegerField("Ano", default=2023)
    country = models.CharField("País", max_length=100)
    gender = models.CharField("Genero", max_length=50)
    qtd = models.PositiveIntegerField("Quantidade", default=0)

    def _str_(self):
        return self.name

class Artist(models.Model):
    name = models.CharField("Nome", max_length=50)
    disc = models.ManyToManyField(Disco)

    def _str_(self):
        return self.name