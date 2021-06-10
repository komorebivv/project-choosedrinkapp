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

    otherdrink_choice = OtherDrink.objects.filter(otherdrink__contains =otherdrinkToChoice)


class FruitForm(forms.Form):
    fruitToChoice = forms.ModelMultipleChoiceField(
        queryset=Fruit.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Teraz pora na owoce:"
    )

    fruit_choice = Fruit.objects.filter(fruit__contains = fruitToChoice)


class OtherAddForm(forms.Form):
    otheraddToChoice = forms.ModelMultipleChoiceField(
        queryset=OtherAdd.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="I jeszcze inne dodatki:"

    )

    otheradd_choice = OtherAdd.objects.filter(otheradd__contains =otheraddToChoice)




