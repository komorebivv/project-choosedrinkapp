from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AlcoholForm, FruitForm, OtherDrinkForm, OtherAddForm
from .models import Alcohol, OtherDrink, OtherAdd, Fruit, Drink
from itertools import chain



def mainpage(request):
    context={}
    return render(request, 'searchdrink/mainpage.html', context)

def part1(request):

    if request.method == 'POST':
        form = AlcoholForm(request.POST)
        if form.is_valid():
            alcohols = request.POST.getlist('alcoholToChoice')
            request.session['alcohols'] = alcohols
            return HttpResponseRedirect('otherdrink')
    else:
        form = AlcoholForm()
        return render(request, 'searchdrink/part1-choosealcohol.html', {'form': form})

def part2(request):
    if request.method == 'POST':
        form = OtherDrinkForm(request.POST)
        if form.is_valid():
            otherdrinks = request.POST.getlist('otherdrinkToChoice')
            request.session['otherdrinks']=otherdrinks
            return HttpResponseRedirect('fruit')
    else:
        form = OtherDrinkForm()

    return render(request, 'searchdrink/part2-chooseotherdrinks.html', {'form': form})

def part3(request):
    if request.method == 'POST':
        form = FruitForm(request.POST)
        if form.is_valid():
            fruits = request.POST.getlist('fruitToChoice')
            request.session['fruits'] = fruits
            return HttpResponseRedirect('otheradd')
    else:
        form = FruitForm()

    return render(request, 'searchdrink/part3-choosefruits.html', {'form': form})

def part4(request):
    if request.method == 'POST':
        form = OtherAddForm(request.POST)
        if form.is_valid():
            otheradds = request.POST.getlist('otheraddToChoice')
            request.session['otheradds'] = otheradds
            return HttpResponseRedirect('results')
    else:
        form = OtherAddForm()

    return render(request, 'searchdrink/part4-chooseotheradd.html', {'form': form})

def results(request):
    alcohols = request.session['alcohols']
    otherdrinks = request.session['otherdrinks']
    fruits = request.session['fruits']
    otheradds = request.session ['otheradds']

    selected_alcohols = Alcohol.objects.filter(id__in=alcohols)
    selected_otherdrinks = OtherDrink.objects.filter(id__in=otherdrinks)
    selected_fruits = Fruit.objects.filter(id__in=fruits)
    selected_otheradds = OtherAdd.objects.filter(id__in=otheradds)



    a = Drink.objects.filter(_alcohol__in=selected_alcohols)
    b = Drink.objects.filter(_otherdrink__in=selected_otherdrinks)
    c = Drink.objects.filter(_fruit__in=fruits)
    d = Drink.objects.filter(_otheradd__in=selected_otheradds)

    result_list = list(chain(a, b, c, d))
    results_dict = {i:result_list.count(i) for i in result_list}
    sorted_results = {k: v for k, v in sorted(results_dict.items(), key=lambda item: item[1], reverse=True)}
    namebestChoice = next(iter(sorted_results))
    bestChoice = Drink.objects.get(nameDrink__contains=namebestChoice)

    return render(request, 'searchdrink/results.html', {'bestChoice': bestChoice})