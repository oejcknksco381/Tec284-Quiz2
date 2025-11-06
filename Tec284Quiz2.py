from gpiozero import Button, RGBLED
from time import sleep


# Setting up the gpio pins 17, 27 and 22
red_button = Button(17)
blue_button = Button(22)
green_button = Button(27)

rgb_led = RGBLED(red=23, green=24, blue=25)

#define function
def check_buttons():

    red = red_button.is_pressed
    green = green_button.is_pressed
    blue = blue_button.is_pressed

#if/else statements for if the buttons are pressed for its combinations
    if red and not green and not blue:

        print("Red")
        rgb_led.color = (1, 0, 0)  

    elif green and not red and not blue:

        print("Green")
        rgb_led.color = (0, 1, 0)  

    elif blue and not red and not green:

        print("Blue")
        rgb_led.color = (0, 0, 1)  

    elif red and green and not blue:

        print("Yellow")
        rgb_led.color = (1, 1, 0)  

    elif red and blue and not green:

        print("Magenta")
        rgb_led.color = (1, 0, 1)  

    elif green and blue and not red:

        print("Cyan")
        rgb_led.color = (0, 1, 1)  

    elif red and green and blue:

        print("White")
        rgb_led.color = (1, 1, 1)  

    else:
        rgb_led.color = (0, 0, 0) #no buttons pressed = no color

#program control and delay for stability
    while True:
        check_buttons()
    sleep(0.1)
