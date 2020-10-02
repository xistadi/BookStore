from time import sleep
from Packages.print_digits import *
from Packages.clear_screen import *
from Packages.get_color import *
from Packages.get_position import *

if __name__ == "__main__":
    color = get_color() #generator get_color random color from 32 to 38
    position = get_position() #generator get_position for dots range from 1 to 4
    while True:
        try: 
            clear_screen()
            print_digits(next(color), next(position)) #output
            sleep(.3)
        except KeyboardInterrupt: break