from django.shortcuts import render
import json
import urllib.request
from urllib.parse import urlparse

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        data = {}
        try:
            res = urllib.request.urlopen(f"http://api.openweathermap.org/data/2.5/weather?q={urllib.parse.quote_plus(city)}&appid=b8ef42d84444420011eaf0b910434acd").read()
            json_data = json.loads(res)
            data = {
                "country_code": str(json_data['sys']['country']),
                "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
                "temp": str(json_data['main']['temp']) + 'k',
                "pressure": str(json_data['main']['pressure']),
                "humidity": str(json_data['main']['humidity']),
            }
        except:
            print("Error retrieving weather data.")
    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city, 'data': data})
