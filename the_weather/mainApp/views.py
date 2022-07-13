from django.shortcuts import render
import requests
from .models import City # регистрация в admin отображает города из бызы данных
from .forms import CityForm # Ообразить города и  данные из бабы данных



def index(request):
    cities = City.objects.all()# возращает все обьекты из базы данных


    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&lang=ru&appid=6dfe2a578d5b3b6b189af7a2f5d41d63&units=metric'


    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    weather_data = []

    for city in cities:
        city_weather = requests.get(url.format(city.name)).json()# запрос данных из api

        weather = {
            'city' : city.name,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon'],
            'humidity': city_weather['main']['humidity'],
            'pressure': city_weather['main']['pressure'],
            'country': city_weather['sys']['country'],
            #'sunrise': city_weather['sys']['sunrise'],
            #'sunset': city_weather['sys']['sunset'],
            'windspeed': city_weather['wind']['speed'],
            'visibility':city_weather['visibility'],

        }

    weather_data.append(weather)
    print(weather_data)

    context = {'weather_data': weather_data, 'form': form}

    return render(request, 'index.html', context)