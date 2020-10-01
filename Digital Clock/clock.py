from time import sleep
from Packages.print_digits import *
from Packages.clear_screen import *


if __name__ == "__main__":
    tempvalue = 0
    color = get_color()
    while True:
        try: 
            for i in range(1,5):
                clear_screen()
                print_digits(color, i)
                sleep(.3)
                tempvalue += 1
                if tempvalue == 8:
                    tempvalue = 0
                    color = get_color(color)

        except KeyboardInterrupt: break