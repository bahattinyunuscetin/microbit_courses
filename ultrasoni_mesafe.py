from microbit import *
import machine
import utime
def get_dist():
    pin0.write_digital(0)
    utime.sleep_us(2)
    pin0.write_digital(1)
    utime.sleep_us(10)
    pin0.write_digital(0)
    d=machine.time_pulse_us(pin1,1,11600)
    if d>0:
        return d/58
    else:
        return d
pin1.set_pull(pin1.NO_PULL)
while True:
    if button_a.was_pressed():
        d=get_dist()
        display.scroll(d)
        sleep(150)
    sleep(20)
    