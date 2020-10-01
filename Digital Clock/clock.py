from os import system
from datetime import datetime
from time import sleep
import random
from pyowm import OWM
from pyowm.utils.config import get_default_config

def get_weather():
	config_dict = get_default_config()
	config_dict['language'] = 'ru'  # your language here
	API = ('6d00d1d4e704068d70191bad2673e0cc')
	owm = OWM(API, config_dict)
	mgr = owm.weather_manager()

	place = input("Введите Ваш город: ")
	observation = mgr.weather_at_place('place')
	w = observation.weather
	status = w.detailed_status 

	temp = w.temperature('celsius') ['temp']  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
	return place, temp, status



def get_current_time():
    # get and return current time
    ctime = datetime.now()
    return ctime

def print_digits(color, position):
    #print digital clock
    print(f"\033[{color}m" "\u25A0" * 62)
    print(f"    Температура в городе {place} сейчас: {temp} °C, {status}.\U0001F326")
    print()
    ctime = get_current_time()
    hour = str(ctime.hour)
    minute = str(ctime.minute)
    second = str(ctime.second)
    if(len(hour) < 2):
        hour = f"0{hour}"
    if(len(minute) < 2):
        minute = f"0{minute}"
    if(len(second) < 2):
        second = f"0{second}"
    print(f"    {l1[hour[0]]} {l1[hour[1]]}{l1[f':{position}']} {l1[minute[0]]} {l1[minute[1]]} {l1[f':{position}']} {l1[second[0]]} {l1[second[1]]}")
    print(f"    {l2[hour[0]]} {l2[hour[1]]}{l2[f':{position}']} {l2[minute[0]]} {l2[minute[1]]} {l2[f':{position}']} {l2[second[0]]} {l2[second[1]]}")
    print(f"    {l3[hour[0]]} {l3[hour[1]]}{l3[f':{position}']} {l3[minute[0]]} {l3[minute[1]]} {l3[f':{position}']} {l3[second[0]]} {l3[second[1]]}")
    print(f"    {l4[hour[0]]} {l4[hour[1]]}{l4[f':{position}']} {l4[minute[0]]} {l4[minute[1]]} {l4[f':{position}']} {l4[second[0]]} {l4[second[1]]}")
    print(f"    {l5[hour[0]]} {l5[hour[1]]}{l5[f':{position}']} {l5[minute[0]]} {l5[minute[1]]} {l5[f':{position}']} {l5[second[0]]} {l5[second[1]]}\n")
    print(f"                        {ctime.day} / {ctime.month} / {ctime.year}")
    print(f"\u25A0" * 62)

def get_color(color = 32):
    #return random color from 32 to 38
    while True:
        b = random.randrange(32, 38, 1)
        if b != color: return b

def clear_screen():
    #clear screen terminal using "cls"
    system("cls")

l1 = {
    "1":
    "\u25A0\u25A0\u25A0\u25A0  ",
    "2":
    "\u25A0\u25A0\u25A0\u25A0\u25A0\u25A0",
    "3":
    "\u25A0\u25A0\u25A0\u25A0\u25A0\u25A0",
    "4":
    "\u25A0\u25A0  \u25A0\u25A0",
    "5":
    "\u25A0\u25A0\u25A0\u25A0\u25A0\u25A0",
    "6":
    "\u25A0\u25A0\u25A0\u25A0\u25A0\u25A0",
    "7":
    "\u25A0\u25A0\u25A0\u25A0\u25A0\u25A0",
    "8":
    "\u25A0\u25A0\u25A0\u25A0\u25A0\u25A0",
    "9":
    "\u25A0\u25A0\u25A0\u25A0\u25A0\u25A0",
    "0":
    "\u25A0\u25A0\u25A0\u25A0\u25A0\u25A0",
    ":1":
    "  \u25A0\u25A0  ",
    ":2":
    "      ",
    ":3":
    "      "
}
l2 = {
    "1":
    "  \u25A0\u25A0  ",
    "2":
    "    \u25A0\u25A0",
    "3":
    "    \u25A0\u25A0",
    "4":
    "\u25A0\u25A0  \u25A0\u25A0",
    "5":
    "\u25A0\u25A0    ",
    "6":
    "\u25A0\u25A0    ",
    "7":
    "    \u25A0\u25A0",
    "8":
    "\u25A0\u25A0  \u25A0\u25A0",
    "9":
    "\u25A0\u25A0  \u25A0\u25A0",
    "0":
    "\u25A0\u25A0  \u25A0\u25A0",
    ":1":
    "      ",
    ":2":
    "  \u25A0\u25A0  ",
    ":3":
    "      "
}

l3 = {
    "1":
    "  \u25A0\u25A0  ",
    "2":
    "\u25A0\u25A0\u25A0\u25A0\u25A0\u25A0",
    "3":
    "\u25A0\u25A0\u25A0\u25A0\u25A0\u25A0",
    "4":
    "\u25A0\u25A0\u25A0\u25A0\u25A0\u25A0",
    "5":
    "\u25A0\u25A0\u25A0\u25A0\u25A0\u25A0",
    "6":
    "\u25A0\u25A0\u25A0\u25A0\u25A0\u25A0",
    "7":
    "    \u25A0\u25A0",
    "8":
    "\u25A0\u25A0\u25A0\u25A0\u25A0\u25A0",
    "9":
    "\u25A0\u25A0\u25A0\u25A0\u25A0\u25A0",
    "0":
    "\u25A0\u25A0  \u25A0\u25A0",
    ":1":
    "      ",
    ":2":
    "      ",
    ":3":
    "      "
}

l4 = {
    "1":
    "  \u25A0\u25A0  ",
    "2":
    "\u25A0\u25A0    ",
    "3":
    "    \u25A0\u25A0",
    "4":
    "    \u25A0\u25A0",
    "5":
    "    \u25A0\u25A0",
    "6":
    "\u25A0\u25A0  \u25A0\u25A0",
    "7":
    "    \u25A0\u25A0",
    "8":
    "\u25A0\u25A0  \u25A0\u25A0",
    "9":
    "    \u25A0\u25A0",
    "0":
    "\u25A0\u25A0  \u25A0\u25A0",
    ":1":
    "      ",
    ":2":
    "  \u25A0\u25A0  ",
    ":3":
    "      "
}

l5 = {
    "1":
    "\u25A0\u25A0\u25A0\u25A0\u25A0\u25A0",
    "2":
    "\u25A0\u25A0\u25A0\u25A0\u25A0\u25A0",
    "3":
    "\u25A0\u25A0\u25A0\u25A0\u25A0\u25A0",
    "4":
    "    \u25A0\u25A0",
    "5":
    "\u25A0\u25A0\u25A0\u25A0\u25A0\u25A0",
    "6":
    "\u25A0\u25A0\u25A0\u25A0\u25A0\u25A0",
    "7":
    "    \u25A0\u25A0",
    "8":
    "\u25A0\u25A0\u25A0\u25A0\u25A0\u25A0",
    "9":
    "\u25A0\u25A0\u25A0\u25A0\u25A0\u25A0",
    "0":
    "\u25A0\u25A0\u25A0\u25A0\u25A0\u25A0",
    ":1":
    "  \u25A0\u25A0  ",
    ":2":
    "      ",
    ":3":
    "      "
}

if __name__ == "__main__":
    color = get_color()
    place, temp, status = get_weather()
    while True:
        try: #every 3 second change random color 
            clear_screen()
            print_digits(color, 1)
            sleep(.3)
            clear_screen()
            print_digits(color, 2)
            sleep(.3)
            clear_screen()
            print_digits(color, 3)
            sleep(.3)
            clear_screen()
            color = get_color(color)
            print_digits(color, 2)
            sleep(.3)
            clear_screen()
            print_digits(color, 1)
            sleep(.3)
            clear_screen()
            print_digits(color, 2)
            sleep(.3)
            clear_screen()
            print_digits(color, 3)
            sleep(.3)
            clear_screen()
            print_digits(color, 2)
            sleep(.3)
        except KeyboardInterrupt: break