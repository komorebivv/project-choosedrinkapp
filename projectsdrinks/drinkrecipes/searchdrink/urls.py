from django.urls import path
from searchdrink import views

app_name = 'searchdrink'

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('alcohol', views.part1, name='alcohol'),
    path('otherdrink', views.part2, name='otherdrink'),
    path('fruit', views.part3, name='fruit'),
    path('otheradd', views.part4, name='otheradd'),
    path('results', views.results, name='results'),
    path('result2', views.result2, name='result2'),
]

