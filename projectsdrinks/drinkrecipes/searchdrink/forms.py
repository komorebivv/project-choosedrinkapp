from django import forms
from .models import Alcohol, OtherDrink, Fruit, OtherAdd


class AlcoholForm(forms.Form):
    choices = forms.ModelMultipleChoiceField(
        queryset=Alcohol.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

class OtherDrinkForm(forms.Form):
    otherdrink = forms.ModelMultipleChoiceField(
        queryset=OtherDrink.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

class FruitForm(forms.Form):
    fruit = forms.ModelMultipleChoiceField(
        queryset=Fruit.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

class OtherAddForm(forms.Form):
    otheradd = forms.ModelMultipleChoiceField(
        queryset=OtherAdd.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )


