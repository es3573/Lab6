# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

import requests
from .models import City
from forms import CityForm

# Create your views here.
def index(request):
    src = ''
    dst = ''
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=33815ab6524fca76a8bbe9a95df35754'
    
    cities = City.objects.all()        

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    else:
        form = CityForm()
        
    weather_data = []

    for city in cities:
        city_weather = requests.get(weather_url.format(city)).json()
        
        weather = {
                'city' : city,
                'temperature' : city_weather['main']['temp'],
                'description' : city_weather['weather'][0]['description'],
                'icon' : city_weather['weather'][0]['icon']
        }
        weather_data.append(weather)
        city.temp = weather['temperature']
        if city.option == '1':
            src = str(city.name)
        elif city.option == '2':
            dst = str(city.name)
            
        city.save()

    context = {'weather_data' : weather_data, 'form' : form, 'src' : src, 'dst' : dst}
    return render(request, 'weather/index.html', context)
    
    

