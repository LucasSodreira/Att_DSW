import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Label(models.Model):
    name = models.CharField("Name", max_length=50)

    def _str_(self):
        return self.name


class Disco(models.Model):
    name = models.CharField("Nome", max_length=50)
    description = models.TextField("Descrição", max_length=400)
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


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
