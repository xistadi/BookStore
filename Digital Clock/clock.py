from os import system
from datetime import datetime
from time import sleep
import random

def get_current_time():
    # get and return current time
    ctime = datetime.now()
    return ctime

def print_digits(ctime):
    #print digital clock
    print(f"\033[{color}m" "\u25A0" * 62)
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
    print(f"    {r1[hour[0]]} {r1[hour[1]]}{r1[':']} {r1[minute[0]]} {r1[minute[1]]} {r1[':']} {r1[second[0]]} {r1[second[1]]}")
    print(f"    {r2[hour[0]]} {r2[hour[1]]}{r2[':']} {r2[minute[0]]} {r2[minute[1]]} {r2[':']} {r2[second[0]]} {r2[second[1]]}")
    print(f"    {r3[hour[0]]} {r3[hour[1]]}{r3[':']} {r3[minute[0]]} {r3[minute[1]]} {r3[':']} {r3[second[0]]} {r3[second[1]]}")
    print(f"    {r4[hour[0]]} {r4[hour[1]]}{r4[':']} {r4[minute[0]]} {r4[minute[1]]} {r4[':']} {r4[second[0]]} {r4[second[1]]}")
    print(f"    {r5[hour[0]]} {r5[hour[1]]}{r5[':']} {r5[minute[0]]} {r5[minute[1]]} {r5[':']} {r5[second[0]]} {r5[second[1]]}\n")
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

r1 = {
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
    ":":
    "      "
}
r2 = {
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
    ":":
    "  \u25A0\u25A0  "
}

r3 = {
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
    ":":
    "      "
}

r4 = {
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
    ":":
    "  \u25A0\u25A0  "
}

r5 = {
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
    ":":
    "      "
}

if __name__ == "__main__":
    color = get_color()
    while True:
        try: #every 3 second change random color 
            clear_screen()
            color = get_color(color)
            print_digits(color)
            sleep(1)
            clear_screen()
            print_digits(color)
            sleep(1)
            clear_screen()
            print_digits(color)
            sleep(1)
        except KeyboardInterrupt: break