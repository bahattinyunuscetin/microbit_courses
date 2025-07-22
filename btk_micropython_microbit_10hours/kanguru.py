from microbit import *
import music

kangaroo = Image("09009:"
                 "99009:"
                 "09990:"
                 "00900:"
                 "99000:")
display.show(kangaroo)
while True:
    if button_a.was_pressed():
        music.set_tempo(bpm=360)
        music.play(music.JUMP_UP)
        for row in range(0,6):
            display.show(kangaroo.shift_up(row))
            sleep(50)
        for row in reversed(range(0,6)):

            display.show(kangaroo.shift_down(-row))
            sleep(50)
            