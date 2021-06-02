from django.shortcuts import render
from django.http import HttpResponse
from .forms import IngredientForm
from .models import Ingredient

def mainpage(request):
    context={}
    return render(request, 'searchdrink/mainpage.html', context)

# def part1(request):
#         context = {}
#         return render(request, 'searchdrink/part1-choosealcohol.html', context)

def part1(request):
        # if this is a POST request we need to process the form data
    if request.method == 'POST':
            # create a form instance and populate it with data from the request:
        form = IngredientForm(request.POST)
            # check whether it's valid:
        if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
            return HttpResponseRedirect('searchdrink/mainpage.html')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = IngredientForm()

    return render(request, 'searchdrink/part1-choosealcohol.html', {'form': form})
