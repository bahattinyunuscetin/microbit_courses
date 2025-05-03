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
morseCode = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
    "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
    "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
    ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
    "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
    "--..": "Z",
    
    "-----": "0", ".----": "1", "..---": "2", "...--": "3",
    "....-": "4", ".....": "5", "-....": "6", "--...": "7",
    "---..": "8", "----.": "9"
}

while True:
    gelenMesaj=radio.receive()
    if gelenMesaj is not None:
        if gelenMesaj=="ok":
            display.show(Image.YES)
            music.play(music.BA_DING)
            sleep(500)
            display.clear()

            harf=morseCode.get(sinyalmesajı,Image.SAD)

            if harf!=Image.SAD:
                display.show(harf)
                sleep(1000)
                mesajmetni=mesajmetni+harf
            else:
                display.show(harf)
                sleep(1000)
            display.clear()
            sinyalsirasi=0
            sinyalmesajı=""
            sinyal=""
        elif gelenMesaj==".":
            display.show(Image("00000:00000:00900:00000:00000"))
            music.play("C:1")
            sleep(300)
            display.clear()
            sinyal="."
            sinyalmesajı=sinyalmesajı+sinyal
        elif gelenMesaj=="-":
            display.show(Image("-"))
            music.play("C:4")
            sleep(300)
            display.clear()
            sinyal="-"
            sinyalmesajı=sinyalmesajı+sinyal
        elif gelenMesaj=="bitti":
            display.show(mektup)
            music.play(music.JUMP_UP)
            sleep(1000)
            for x in range(0,6):
                display.show(mektup.shift_right(-x))
                sleep(200)
            sleep(300)
            display.scroll(mesajmetni)
            mesajmetni=""
            sinyalmesajı=""
            harf=""
            sinyal=""
        
            
                
                
        
     