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
def yak(renk):
    for pixel in range(0,len(neopix)):
        neopix[pixel]=renk
    neopix.show()
    return
while True:
    yak(red)
    sleep(1000)
    
    yak(green)
    sleep(1000)
    
    yak(blue)
    sleep(1000)
    
    yak(yellow)
    sleep(1000)
    
    yak(cyan)
    sleep(1000)
    
    yak(magenta)
    sleep(1000)
    
    yak(orange)
    sleep(1000)
    
    yak(purple)
    sleep(1000)
    
    yak(pink)
    sleep(1000)
    
    yak(gray)
    sleep(1000)
