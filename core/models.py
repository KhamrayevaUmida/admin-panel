from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=20)
    izoh = models.TextField(max_length=500)
    narx = models.IntegerField(default=100)

    def __str__(self):
        return f"{self.name}: {self.izoh}; narxi {self.narx} $"


class Telephone(models.Model):
    name = models.CharField(max_length=20)
    versiya = models.CharField(max_length=20)
    age = models.IntegerField(default=1900)

    def __str_(self):
        return f"{self.name}: versiya={self.versiya}; {self.age}"


class Computer(models.Model):
    company  = models.CharField(max_length=20)
    processor = models.CharField(max_length=20)
    izoh = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.company}; {self.processor}; {self.izoh}"


class Animal(models.Model):
    tur = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    son = models.IntegerField(default=5)

    def __str__(self):
        return f"{self.tur}; {self.color}; {self.son}"


class Fruit(models.Model):
    name = models.CharField(max_length=20)
    tur = models.CharField(max_length=20)
    rang = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}; {self.tur}; {self.rang}"



class Country(models.Model):
    country = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    aholi = models.IntegerField(default=1000)
