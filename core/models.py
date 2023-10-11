from django.db import models

class Question(models.Model):
   question = models.CharField(max_length=200)
   pub_date = models.DateField('data publicada')

class Disco(models.Model):
    Nome = models.CharField(max_length=200)
    Descrição = models.CharField(max_length=800)
    Selo_fonográfico = models.CharField(max_length=200)
    Ano = models.IntegerField()
    Pais = models.CharField(max_length=20)
    Genero = models.CharField(max_length=20)
    Quantidade = models.IntegerField()
