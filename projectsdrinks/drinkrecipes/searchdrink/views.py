from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AlcoholForm, FruitForm, OtherDrinkForm, OtherAddForm, NameDrinkForm
from .models import Alcohol, OtherDrink, OtherAdd, Fruit, Drink
from itertools import chain
from django.core import serializers
import json



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

    allDrinks = a | b | c | d
    checking = get_list_or_404(allDrinks)
    result_list = list(chain(a, b, c, d))
    results_dict = {i:result_list.count(i) for i in result_list}

    for key, value in results_dict.items():
        generalAmount = key._alcohol.count() + key._otherdrink.count() + key._otheradd.count() + key._fruit.count()
        results_dict[key] = value/generalAmount

    sorted_results = {k: v for k, v in sorted(results_dict.items(), key=lambda item: item[1], reverse=True)}
    sorted_results_iter = iter(sorted_results)
    print(sorted_results)
    bestChoice = next(sorted_results_iter)

    if len(sorted_results) > 1:
        bestChoice_second = next(sorted_results_iter)
        bestChoice_second = Drink.objects.filter(nameDrink__contains=bestChoice_second)
        bestChoice_second_json = serializers.serialize('json', bestChoice_second)
        request.session['bestChoice_second_json'] = bestChoice_second_json
    else:
        if 'bestChoice_second_json' in request.session:
            del request.session['bestChoice_second_json']

    if len(sorted_results) > 2:
        bestChoice_third = next(sorted_results_iter)

    return render(request, 'searchdrink/results.html', {'bestChoice': bestChoice})

def result2(request):
    if request.session.get('bestChoice_second_json', False):
        bestChoice_second_json = request.session['bestChoice_second_json']
        bestChoice_second_list = json.loads(bestChoice_second_json)
        for dicts in bestChoice_second_list:
            for key, values in dicts.items():
                for k, v in dicts['fields'].items():
                    bestChoice_second  = Drink.objects.get(nameDrink__contains=dicts['fields']['nameDrink'])
    else:
        return render(request, 'searchdrink/404.html', {})

    return render(request, 'searchdrink/results2.html', {'bestChoice_second': bestChoice_second})



def bad_request(request, exception):
    return render(request, 'searchdrink/404.html', {})

def searchbyname(request):
    if request.method == 'POST':
        form = NameDrinkForm(request.POST)
        if form.is_valid():
            name_search = form.cleaned_data['name_search']
            searchingcocktail = get_object_or_404(Drink.objects.filter(nameDrink__contains=name_search))
            searchingcocktail_json = serializers.serialize('json', searchingcocktail)
            request.session['searchingcocktail_json'] = searchingcocktail_json
            return HttpResponseRedirect('searchnameresult', searchingcocktail_json, content_type='application/json')
    else:
        form = NameDrinkForm()


    return render(request, 'searchdrink/searchbyname.html', {'form': form})


def searchnameresult(request):
    searchingcocktail_json = request.session['searchingcocktail_json']
    searchingcocktail_list = json.loads(searchingcocktail_json)
    for dicts in searchingcocktail_list:
        for key, values in dicts.items():
            for k, v in dicts['fields'].items():
                finalresult = Drink.objects.get(nameDrink=dicts['fields']['nameDrink'])



    return render(request, 'searchdrink/searchbynameResult.html', {'finalresult': finalresult})



