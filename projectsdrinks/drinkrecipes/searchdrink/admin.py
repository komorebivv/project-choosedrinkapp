from django.contrib import admin
from . import models
from .models import Drink
from .models import Alcohol, OtherDrink, Fruit, OtherAdd
from django import forms


admin.site.register(Drink)
admin.site.register(Alcohol)
admin.site.register(OtherDrink)
admin.site.register(Fruit)
admin.site.register(OtherAdd)


