from microbit import *
import neopixel
neopix=neopixel.NeoPixel(pin0,24)

while True:
    for pixel in range (0,24):
        neopix[pixel]=(255,0,0)
        neopix.show()

        sleep(50)
        
    for pixel in reversed (range(0,24)):
        neopix[pixel]=(0,0,0)
        neopix.show()
        sleep(50)
    neopix.clear()
    sleep(500)