from django.contrib import admin
from . import models
from .models import Drink
from .models import Alcohol, OtherDrink, Fruit, OtherAdd
from django import forms

class AlcoholInline(admin.TabularInline):
    model = Alcohol
    extra = 3

class OtherDrinkInline(admin.TabularInline):
    model = OtherDrink
    extra = 3

class FruitInline(admin.TabularInline):
    model = Fruit
    extra = 3

class OtherAddInline(admin.TabularInline):
    model = OtherAdd
    extra = 3

class DrinkAdmin(admin.ModelAdmin):
    fields = ['nameDrink', 'taste', 'temperature', 'ingredientsProportion', 'descriptionPreparing', 'photo']
    inlines = [AlcoholInline, OtherDrinkInline, FruitInline, OtherAddInline]



admin.site.register(Drink, DrinkAdmin)
