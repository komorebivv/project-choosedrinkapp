from django.db import models
from PIL import Image

class Drink(models.Model):
    nameDrink = models.CharField(max_length=50, verbose_name='Nazwa drinku')
    sweet = 'S'
    bitter ='B'
    sour = 'R'
    TASTE_CHOICES = [
    (sweet, 'słodki'),
    (bitter, 'gorzki'),
    (sour, 'kwaśny')
    ]
    taste = models.CharField(
        max_length=2,
        choices=TASTE_CHOICES,
        default= sweet,
        verbose_name='Smak drinka'
    )
    warm = 'W'
    cold = 'C'
    TEMPERATURE_CHOICE = [
        (warm, 'ciepły'),
        (cold, 'zimny')
    ]

    temperature = models.CharField(
        max_length=2,
        choices=TEMPERATURE_CHOICE,
        default= cold,
        verbose_name='Temperatura'
    )
    ingredientsProportion = models.TextField(verbose_name='Składniki')
    descriptionPreparing = models.TextField(verbose_name='Opis przygotowania')
    photo = models.ImageField(upload_to='uploads/', default='some photo', verbose_name='Zdjęcie drinka')

    def __str__(self):
        return self.nameDrink

class Ingredient(models.Model):
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE, related_name='składniki')
    alcohol = models.CharField(max_length= 20, verbose_name='Alkohol', blank=True)
    otherdrink = models.CharField(max_length= 20, verbose_name='Inne napoje', blank=True)
    fruit = models.CharField(max_length= 20, verbose_name='Owoce', blank=True)
    otheradd = models.CharField(max_length= 30,verbose_name='Inne dodatki', blank=True)

    def __str__(self):
        return self.alcohol




