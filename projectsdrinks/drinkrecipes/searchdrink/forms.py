from django import forms
from .models import Ingredient, Drink

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields=[]

    alcoholchoice = forms.MultipleChoiceField(
        label = 'Wybierz alkohol',
        required = False,
        widget=forms.CheckboxSelectMultiple,
        # choices = ['alcohol']

    )

