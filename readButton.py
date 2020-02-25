from gpiozero import Button
from signal import pause
from os import system

button = Button(27)

def pressButton():
    system("python3 actTakePicture.py")

button.when_pressed = pressButton

pause()
