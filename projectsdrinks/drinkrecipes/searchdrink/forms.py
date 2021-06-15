from django import forms
from .models import Alcohol, OtherDrink, Fruit, OtherAdd, Drink


class AlcoholForm(forms.Form):
    alcoholToChoice = forms.ModelMultipleChoiceField(
        queryset=Alcohol.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Wybierz alkohol, który masz:'

    )



class OtherDrinkForm(forms.Form):
    otherdrinkToChoice = forms.ModelMultipleChoiceField(
        queryset=OtherDrink.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Wybierz inne napoje, które posiadasz:'


    )



class FruitForm(forms.Form):
    fruitToChoice = forms.ModelMultipleChoiceField(
        queryset=Fruit.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Teraz pora na owoce:"
    )



class OtherAddForm(forms.Form):
    otheraddToChoice = forms.ModelMultipleChoiceField(
        queryset=OtherAdd.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="I jeszcze inne dodatki:"

    )




class NameDrinkForm(forms.Form):
    name_search = forms.CharField(label='',max_length=100)
