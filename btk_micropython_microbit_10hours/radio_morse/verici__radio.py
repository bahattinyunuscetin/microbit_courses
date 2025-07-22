from microbit import *
import music
import radio
mektup=Image("99999:99099:90909:90009:99999")
radio.on()
radio.config(channel=11)
sinyal=""
sinyalmesajı=""
harf=""
mesajmetni=""
while True:
     if button_a.was_pressed():
        
            sinyal="."
            display.show(Image("00000:00000:00900:00000:00000"))
            music.play("C:1")
            radio.send(sinyal)
            sleep(500)
            display.clear()
     elif button_a.was_pressed():
        
            sinyal="-"
            display.show("-")
            music.play("C:4")
            radio.send(sinyal)
            sleep(500)
            display.clear()
     elif accelerometer.was_gesture("shake"):
         radio.send("ok")
         display.show(Image.YES)
         music.play(music.BA_DING)
         sleep(500)
         display.clear()
     elif accelerometer.was_gesture("down"):
         radio.send("bitti")
         display.show(mektup)
         music.play(music.JUMP_UP)
         sleep(1000)
         for x in range(0,6):
             display.show(mektup.shift_right(x))
             sleep(200)
         sleep(500)
         display.clear()
         display.scroll(mesajmetni)
         mesajmetni=""
         