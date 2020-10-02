from Packages.get_weather import *
from Packages.get_current_time import *

place, temp, status = get_weather()
def print_digits(color, position):
    #print digital clock
    print(f"\033[{color}m" "\u25A0" * 62)
    print(f"    Температура в городе {place} сейчас: {temp} °C, {status}.\n")#place, temp, status from get_weather()
    ctime, hour, minute, second = get_current_time()
    print(f"    {l1[hour[0]]} {l1[hour[1]]}{l1[f':{position}']} {l1[minute[0]]} {l1[minute[1]]} {l1[f':{position}']} {l1[second[0]]} {l1[second[1]]}")
    print(f"    {l2[hour[0]]} {l2[hour[1]]}{l2[f':{position}']} {l2[minute[0]]} {l2[minute[1]]} {l2[f':{position}']} {l2[second[0]]} {l2[second[1]]}")
    print(f"    {l3[hour[0]]} {l3[hour[1]]}{l3[f':{position}']} {l3[minute[0]]} {l3[minute[1]]} {l3[f':{position}']} {l3[second[0]]} {l3[second[1]]}")
    print(f"    {l4[hour[0]]} {l4[hour[1]]}{l4[f':{position}']} {l4[minute[0]]} {l4[minute[1]]} {l4[f':{position}']} {l4[second[0]]} {l4[second[1]]}")
    print(f"    {l5[hour[0]]} {l5[hour[1]]}{l5[f':{position}']} {l5[minute[0]]} {l5[minute[1]]} {l5[f':{position}']} {l5[second[0]]} {l5[second[1]]}\n")
    print(f"                        {ctime.day} / {ctime.month} / {ctime.year}")
    print(f"\u25A0" * 62)


#numbers and dots
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
    "      ",
    ":4":
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
    "      ",
    ":4":
    "  \u25A0\u25A0  "
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
    "      ",
    ":4":
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
    "      ",
    ":4":
    "  \u25A0\u25A0  "
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
    "      ",
    ":4":
    "      "
}