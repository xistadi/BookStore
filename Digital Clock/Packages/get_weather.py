from pyowm import OWM
from pyowm.utils.config import get_default_config

def get_weather(): 
    #get place, temperature and status from openweathermap.org 
    config_dict = get_default_config()
    config_dict['language'] = 'ru'  # your language here
    API = ('6d00d1d4e704068d70191bad2673e0cc')
    owm = OWM(API, config_dict)
    mgr = owm.weather_manager()

    place = input("Введите Ваш город: ")#get name of city from keyboard
    observation = mgr.weather_at_place('place')
    w = observation.weather
    status = w.detailed_status

    temp = w.temperature('celsius') ['temp']  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    return place, temp, status