from microbit import *
import music

while True:
    for x in range(0,5):
        display.set_pixel(x,2,9)
        sleep(30)
        display.set_pixel(x,2,0)
        sleep(30)

        if button_a.is_pressed():
            if(x==3):
                display.clear()
                display.show(Image.HEART)
                audio.play(Sound.GIGGLE)
                sleep(1000)
                display.clear()
            else:
                 display.clear()
                 display.show(Image.NO)
                 audio.play(Sound.SAD)
                 sleep(1000)
                 display.clear()
    for x in reversed(range(0,5)):
        display.set_pixel(x,2,9)
        sleep(30)
        display.set_pixel(x,2,0)
        sleep(30)

        if button_a.is_pressed():
            if(x==3):
                display.clear()
                display.show(Image.HEART)
                audio.play(Sound.GIGGLE)
                sleep(1000)
                display.clear()
            else:
                 display.clear()
                 display.show(Image.NO)
                 audio.play(Sound.SAD)
                 sleep(1000)
                 display.clear()         