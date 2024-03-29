from django.db import models


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
    _alcohol = models.ManyToManyField('Alcohol', blank=True)
    _otherdrink = models.ManyToManyField('OtherDrink', blank=True)
    _fruit = models.ManyToManyField('Fruit', blank=True)
    _otheradd = models.ManyToManyField('OtherAdd', blank=True)


    ingredientsProportion = models.TextField(verbose_name='Składniki')
    descriptionPreparing = models.TextField(verbose_name='Opis przygotowania')
    photo = models.ImageField(upload_to='uploads/', default='some photo', verbose_name='Zdjęcie drinka')



    def __str__(self):
        return self.nameDrink



class Alcohol(models.Model):
    alcohol = models.CharField(max_length= 20, verbose_name='Alkohol', blank=True)

    def __str__(self):
        return self.alcohol

class OtherDrink(models.Model):
    otherdrink = models.CharField(max_length= 20, verbose_name='Inne napoje', blank=True)

    def __str__(self):
        return self.otherdrink

class Fruit(models.Model):
    fruit = models.CharField(max_length= 20, verbose_name='Owoce', blank=True)


    def __str__(self):
        return self.fruit

class OtherAdd(models.Model):
    otheradd = models.CharField(max_length= 30,verbose_name='Inne dodatki', blank=True)


    def __str__(self):
        return self.otheradd










