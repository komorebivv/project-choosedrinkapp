from django.urls import path
from searchdrink import views

app_name = 'searchdrink'

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('alcohol', views.part1, name='alcohol'),
]