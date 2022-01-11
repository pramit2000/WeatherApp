from django.shortcuts import render
import requests
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def index(req):
    city_weather = {
        'ishidden': 'hidden'
    }
    weather = {'city_weather': city_weather}
    if req.method == 'GET' or req.POST['city'] == '':
        return render(req,"index.html",weather)

    elif req.method == 'POST':
        cityname = req.POST['city']
        url = 'http://api.openweathermap.org/data/2.5/weather?q=CITY&appid=271d1234d3f497eed5b1d80a07b3fcd1'
        url = url.replace('CITY', cityname)
        data = requests.get(url).json()

        if data['cod'] == '404':
            messages.error(req, 'city not found')
            return render(req,'index.html',weather)

        city_weather = {
            'city':data['name'],
            'country':data['sys']['country'],
            'temp':data['main']['temp'],
            'temp_min':data['main']['temp_min'],
            'temp_max':data['main']['temp_max'],
            'humidity':data['main']['humidity'],
            'visibility':data['visibility'],
            'wind_speed':data['wind']['speed'],
            'desc':data['weather'][0]['description'],
            'icon':data['weather'][0]['icon'],
            'ishidden':''
        }

        weather ={'city_weather':city_weather}
        return render(req, 'index.html', weather)

