from microbit import *
ledX=2
ledY=2

while True:
    joyX=pin0.read_analog()
    joyY=pin0.read_analog()
    joyB=pin2.read_digital()

    if joyX<200:
        if ledX>0:
            display.set_pixel(ledX,ledY,0)
            ledX=ledX-1
    elif joyX>900:
        if ledX<4:
            display.set_pixel(ledX,ledY,0)
            ledX=ledX+1
    elif joyY<200:
        if ledY>0:
            display.set_pixel(ledX,ledY,0)
            ledY=ledY-1
    elif joyY>900:
        if ledY<4:
            display.set_pixel(ledX,ledY,0)
            ledY=ledY+1
    sleep(200)
    display.set_pixel(ledX,ledY,9)