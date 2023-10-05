import genericpath
from django.db import models


class Question(models.Model):
   question_text = models.CharField(max_length=200)
   pub_date = models.DateTimeField('data publicada')

class Genero(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
   
class Disco(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    selo_fonografico = models.CharField(max_length=255)
    ano = models.IntegerField()
    pais = models.CharField(max_length=255)
    generos = models.ManyToManyField(Genero)
    quantidade = models.IntegerField()

    def __str__(self):
        return f"{self.nome} - {self.selo_fonografico}"
   
Disco.objects.create(
    nome="Abbey Road",
    descricao="O 11º álbum de estúdio da banda britânica de rock The Beatles, lançado em 26 de setembro de 1969.",
    selo_fonografico="Apple Records",
    ano=1969,
    pais="Reino Unido",
    generos=[Genero.ROCK, Genero.POP],
    quantidade=10,
)

# Disco 2
Disco.objects.create(
    nome="Thriller",
    descricao="O 6º álbum de estúdio do cantor e compositor norte-americano Michael Jackson, lançado em 30 de novembro de 1982.",
    selo_fonografico="Epic Records",
    ano=1982,
    pais="Estados Unidos",
    generos=[Genero.POP, Genero.POP],
    quantidade=20,
)

# Disco 3
Disco.objects.create(
    nome="Dark Side of the Moon",
    descricao="O 8º álbum de estúdio da banda britânica de rock progressivo Pink Floyd, lançado em 1 de março de 1973.",
    selo_fonografico="Harvest Records",
    ano=1973,
    pais="Reino Unido",
    generos=[Genero.ROCK, Genero.PROGRESSIVO],
    quantidade=30,
)

# Disco 4
Disco.objects.create(
    nome="Sgt. Pepper's Lonely Hearts Club Band",
    descricao="O 8º álbum de estúdio da banda britânica de rock The Beatles, lançado em 1º de junho de 1967.",
    selo_fonografico="Parlophone Records",
    ano=1967,
    pais="Reino Unido",
    generos=[Genero.ROCK, Genero.POP],
    quantidade=40,
)

# Disco 5
Disco.objects.create(
    nome="Rubber Soul",
    descricao="O 6º álbum de estúdio da banda britânica de rock The Beatles, lançado em 3 de dezembro de 1965.",
    selo_fonografico="Parlophone Records",
    ano=1965,
    pais="Reino Unido",
    generos=[Genero.ROCK, Genero.POP],
    quantidade=50,
)