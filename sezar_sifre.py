from microbit import *

alfabe = "abcdefghijklmnoprstuvwxyz"
harfSirasi = 0
mesajHarfleri = ""
sifreliMesajHarfleri = ""
kaydirmaDegeri = 0

while True:
    accX = accelerometer.get_x()
    display.show(alfabe[harfSirasi])

    if accX < -800:
        harfSirasi -= 1
        if harfSirasi < 0:
            harfSirasi = len(alfabe) - 1
        display.show(alfabe[harfSirasi])
        sleep(300)

    elif accX > 800:
        harfSirasi += 1
        if harfSirasi >= len(alfabe):
            harfSirasi = 0
        display.show(alfabe[harfSirasi])
        sleep(300)

    if button_a.was_pressed():
        kaydirmaDegeri = harfSirasi
        display.scroll(str(kaydirmaDegeri))

    elif button_b.was_pressed():
        mesajHarfleri += alfabe[harfSirasi]
        sifreIndexi = (harfSirasi + kaydirmaDegeri) % len(alfabe)
        sifreliMesajHarfleri += alfabe[sifreIndexi]
        display.show(Image.YES)
        sleep(300)
        display.clear()

    elif accelerometer.was_gesture("shake"):
        display.scroll(mesajHarfleri)
        sleep(500)
        display.show(Image.ARROW_E)
        sleep(1000)
        display.scroll(sifreliMesajHarfleri)
        sleep(1000)
        # Sıfırlama
        harfSirasi = 0
        kaydirmaDegeri = 0
        sifreliMesajHarfleri = ""
        mesajHarfleri = ""

        
            
        
        
      