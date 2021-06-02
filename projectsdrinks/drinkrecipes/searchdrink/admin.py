from django.contrib import admin
from . import models
from .models import Drink
from .models import Ingredient
# admin.site.register(Ingredient)
from django.db.models.fields import TextField

class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 3

class DrinkAdmin(admin.ModelAdmin):
    fields = ['nameDrink', 'taste', 'temperature', 'ingredientsProportion', 'descriptionPreparing', 'photo']
    inlines = [IngredientInline]

admin.site.register(Drink, DrinkAdmin)
