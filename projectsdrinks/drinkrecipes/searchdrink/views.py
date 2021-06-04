from django.shortcuts import render
from django.http import HttpResponse
from .forms import AlcoholForm, FruitForm, OtherDrinkForm, OtherAddForm

def mainpage(request):
    context={}
    return render(request, 'searchdrink/mainpage.html', context)



def part1(request):
    if request.method == 'POST':
        form = AlcoholForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('searchdrink/otherdrink.html')
    else:
        form = AlcoholForm()

    return render(request, 'searchdrink/part1-choosealcohol.html', {'form': form})

def part2(request):
    if request.method == 'POST':
        form = OtherDrinkForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('searchdrink/fruit.html')
    else:
        form = OtherDrinkForm()

    return render(request, 'searchdrink/part2-chooseotherdrinks.html', {'form': form})

def part3(request):
    if request.method == 'POST':
        form = FruitForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('searchdrink/otheradd.html')
    else:
        form = FruitForm()

    return render(request, 'searchdrink/part3-choosefruits.html', {'form': form})

def part4(request):
    if request.method == 'POST':
        form = OtherAddForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('searchdrink/mainpage.html')
    else:
        form = OtherAddForm()

    return render(request, 'searchdrink/part4-chooseotheradd.html', {'form': form})



