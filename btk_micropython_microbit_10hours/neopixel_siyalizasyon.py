from microbit import *
import neopixel
neopix=neopixel.NeoPixel(pin0,24)
red         = (255, 0, 0)
green       = (0, 255, 0)
blue        = (0, 0, 255)
yellow      = (255, 255, 0)
cyan        = (0, 255, 255)
magenta     = (255, 0, 255)
orange      = (255, 165, 0)
purple      = (128, 0, 128)
pink        = (255, 192, 203)
brown       = (139, 69, 19)
gray        = (128, 128, 128)
black       =(0)
def sinyal(bas,git,renk):
    for pixel in range(bas,git):
        neopix[pixel]=renk
    neopix.show()
    return
while True:
    if accelerometer.get_x()>500:
        sinyal(0,13,yellow)
        sleep(500)
        sinyal(0,13,black)
        sleep(500)
    elif accelerometer.get_x()<-500:
        sinyal(13,24,yellow)
        sleep(500)
        sinyal(13,24,black)
        sleep(500)
    else:
        sinyal(0,24,black)
        
        