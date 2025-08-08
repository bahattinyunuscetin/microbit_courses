# micro\:bit Eğitim Projeleri — README

> Bu repo, micro\:bit ile yapılabilecek eğitim amaçlı projeleri, örnek kodları, bağlantı talimatlarını ve öğretici notları içerir. Hem yeni başlayanlar hem orta seviyedekiler için hazırlanmış, sınıfta veya bireysel öğrenmede kullanılabilir bir kaynak.

---

## İçindekiler

1. Giriş — micro\:bit nedir ve neden kullanmalısın
2. Donanım özellikleri (kısa ama net)
3. micro\:bit v1 vs v2 (kısa farklar)
4. Programlama dilleri ve araçlar
5. Hızlı başlangıç: bilgisayarına bağla, kod yaz, flaşla
6. Repo yapısı ve proje klasörizasyonu
7. Örnek projeler (detaylı liste: amaç, malzeme, zorluk, adımlar)
8. Donanım bağlantı ipuçları (servo, neopixel, sensörler vs.)
9. Sınıf/öğretmen notları ve öğrenme çıktıları
10. Katkıda bulunma rehberi
11. SSS ve sorun giderme
12. Lisans ve kaynaklar

---

## 1) Giriş — micro\:bit nedir ve neden kullanmalısın

BBC micro\:bit, eğitsel amaçlı tasarlanmış küçük, dayanıklı ve programlanabilir bir geliştirme kartıdır. Öğrencilerin kısa sürede somut sonuç görmesini sağlar: LED matrisi ile hızlı geri bildirim, butonlarla etkileşim ve yerleşik sensörlerle gerçek dünya verisi toplama mümkün.

**Neden micro\:bit?**

* Hemen işe başlamak için çok az donanım gerektirir.
* Blok tabanlı (MakeCode) ve metinsel (MicroPython / JavaScript) programlama dillerini destekler — yani kademeli öğretim kolay.
* BLE ve radyo ile mikro-projeler arasında iletişim kurulabilir (sınıf içi eşleştirme & yarışmalar için harika).
* Küçük ve taşınabilir, pil ile çalışır -> saha çalışması, gezi, atölye.

*Kısa: hızlı prototipleme, eğlenceli ve pedagogik.* 🎯

---

## 2) Donanım özellikleri (özet)

* **LED matrix:** 5x5 adet LED — görsel çıktı için.
* **Butonlar:** A ve B — kullanıcı etkileşimi.
* **İvmeölçer (accelerometer):** tilt, shake, hareket algılama.
* **Manyetometre (pusula):** yön tayini.
* **Bluetooth Low Energy (BLE) & radio:** micro\:bit'ler arası veya telefon ile iletişim.
* **USB portu:** güç ve kod yükleme (masaüstünden .hex dosyası sürükle-bırak çalışır).
* **Edge connector (kenar bağlantı):** Pin0, Pin1, Pin2 gibi GPIO pinleri ve ilave güç/ground pinleri — elektronik devreler bağlanır.
* **Sıcaklık & ışık ölçümü:** bazı değerler dahili sensörlerle veya LED/foto direnç ile okunur.

> Not: micro\:bit v2 ile birlikte bazı yeni donanım elemanları (ör. entegre mikrofon ve hoparlör, dokunmatik logo) geldi — projeye göre hangisini kullandığını belirt.

---

## 3) micro\:bit v1 vs v2 — kısaca

* **v1:** Temel özellikler: LED, iki buton, ivmeölçer, pusula, USB.
* **v2:** Dahili mikrofon, hoparlör (ses çalma), dokunmatik logo, daha fazla işlem gücü ve hafıza (gelişmiş yetenekler).

Projede ses/giriş/çıkış kullanacaksan hangi versiyon olduğunu kontrol et — yoksa alternatif bir sürücü/modül gerekebilir.

---

## 4) Programlama dilleri ve araçlar

* **MakeCode (web):** Blok tabanlı + JavaScript. Öğrenciler için en hızlı başlangıç.
* **MicroPython:** Gerçek Python dili; orta/ileri seviye için ideal.
* **Mu editor:** MicroPython ile doğrudan flash atmak için çok kullanışlı, öğretmenlerin favorisi.
* **Diğer:** Scratch eklentileri, bazı C++/ARM tabanlı akımlar (ileri seviye).

**Kod yükleme yolları:**

* MakeCode: web editörde "Download" -> indirilen .hex dosyasını micro\:bit cihazına sürükle.
* MicroPython + Mu: Mu'da kodu yaz, "Flash" ile doğrudan yükle.

---

## 5) Hızlı başlangıç (ilk kod örnekleri)

### A) MicroPython — Zar (dice) örneği

```python
from microbit import *
import random

while True:
    if button_a.was_pressed():
        dice = random.randint(1, 6)
        display.show(str(dice))
    sleep(100)
```

Butona bastıkça 1-6 arası rastgele sayı gösterir. Basit, eğlenceli, öğrenme hızı yüksek.

### B) MakeCode (JavaScript Blocks) — Butona mesaj

```ts
input.onButtonPressed(Button.A, function () {
    basic.showString("Merhaba!")
})
```

---

## 6) Repo yapısı — önerilen düzen

```
/ (root)
├─ README.md
├─ LICENSE
├─ CONTRIBUTING.md
├─ projects/
│  ├─ 01-led-dice/
│  │   ├─ README.md
│  │   ├─ dice.py
│  │   ├─ dice.hex
│  │   └─ assets/
│  ├─ 02-pedometer/
│  │   ├─ README.md
│  │   └─ pedometer.py
│  └─ ...
└─ docs/
   └─ microbit-basics.md
```

Her proje klasöründe: kısa amaç, gerekli malzemeler, adım adım uygulama, çalışma kodu (.py) ve MakeCode/hex dosyası bulunmalı.

---

## 7) Örnek projeler (öğrenme hedefi + malzeme + zorluk + kısa adımlar)

> Aşağıdaki projeler sınıf için mükemmel. Her biri için `projects/{num}-{name}/README.md` oluşturuldu.

### 01 - LED Zar (Dice)

* **Zorluk:** Başlangıç
* **Malzeme:** micro\:bit
* **Amaç:** Rastgele sayı, buton girişi, LED çıktısı
* **Adımlar:** Butonla tetikleme, random sayı, display.show

### 02 - Reaksiyon Zamanı Oyunu

* **Zorluk:** Başlangıç
* **Malzeme:** micro\:bit
* **Amaç:** Rast süre ölçümü, kullanıcı etkileşimi, puanlama

### 03 - Adım Sayar (Pedometer)

* **Zorluk:** Orta
* **Malzeme:** micro\:bit, kayış veya cep
* **Amaç:** İvmeölçer verisini işleme, filtreleme, basit algoritma

### 04 - Dijital Pusula

* **Zorluk:** Orta
* **Malzeme:** micro\:bit
* **Amaç:** Manyetometre kullanımı, yön gösterimi

### 05 - NeoPixel Renkli Şerit

* **Zorluk:** Orta
* **Malzeme:** micro\:bit (Pin0), NeoPixel şerit (WS2812), harici güç kaynağı
* **Amaç:** Adreslenebilir LED kontrolü, renkler ve döngüler

### 06 - Uzaktan Kumandalı Araç (Radio/BLE)

* **Zorluk:** Orta-İleri
* **Malzeme:** micro\:bit ×2, motor sürücü (L298N gibi), DC motorlar, şasi, pil
* **Amaç:** radio veya BLE ile kumanda, motor sürme, protokoller

### 07 - Bitki Nem Monitörü

* **Zorluk:** Orta
* **Malzeme:** Soil moisture sensörü, micro\:bit, direnç, breadboard
* **Amaç:** Analog veri okuma (ADC), eşik belirleme, uyarı

### 08 - Sıcaklık Veri Kaydedici (Data Logger)

* **Zorluk:** Orta
* **Malzeme:** micro\:bit, ikinci micro\:bit veya bilgisayar (seri kayıt)
* **Amaç:** Zaman serisi, veri gönderimi (radio/serial)

### 09 - Ses Kontrollü Proje (v2 için ideal)

* **Zorluk:** Orta
* **Malzeme:** micro\:bit v2
* **Amaç:** Mikrofon girişi, eşikli tetikleme, sesle komut

### 10 - Morse Kodu Işık/İletiştirme

* **Zorluk:** Başlangıç-Orta
* **Malzeme:** micro\:bit
* **Amaç:** Karakter kodlama, zamanlama, iletişim

### 11 - Dijital Evcil Hayvan (Digital Pet)

* **Zorluk:** Orta
* **Malzeme:** micro\:bit, buton veya sensörler
* **Amaç:** State machine, depolama fikirleri, kullanıcı etkileşimi

### 12 - Robotik Kol / İleri Elektronik Uygulama

* **Zorluk:** İleri
* **Malzeme:** Servo motorlar, sürücü kartlar, harici power
* **Amaç:** PWM, hassas kontrol, multi-axis koordinasyon

---

## 8) Donanım bağlantı ipuçları — güvenlik ve pratik bilgiler

* **Her zaman GND ortak olsun:** harici güç kaynağı kullandığında micro\:bit ground'u ile ortaklayın.
* **Servoları doğrudan micro\:bit 3V çıkışına bağlamayın** (yüksek akım çekebilir) — harici power kullan.
* **NeoPixel gibi LED şeritler yüksek akım çeker:** uygun güç kaynağı ve kondansatör kullan.
* **Analog pinler:** Pin0/Pin1/Pin2 genelde analog/dijital I/O olarak kullanılır — sensörleri bu pinlere bağlayın.
* **Koruma dirençleri:** LED veya belirli sensörlerde gerekebilir; her bağlantıda veri sayfasını kontrol et.

---

## 9) Sınıf / Öğretmen notları — öğrenme çıktılarına göre değerlendirme

Her proje için şu maddeleri değerlendir: teknik gerçekleştirme, yorum ve sunum, kod temizliği, genişletilebilirlik. Projeyi 3 seviyede rubric ile puanlayın (başlangıç/orta/ileri hedeflerine göre).

---

## 10) Katkıda bulunma

1. Bu repo'yu fork'la.
2. `projects/` altında yeni proje klasörü oluştur: `NN-proje-adi/`.
3. `README.md`, kod dosyaları, varsa hex/mpy dosyalarını ekle.
4. Pull request atarken proje tanımını, öğrenme hedeflerini ve kullanılan malzemeleri açıkça yaz.

Lütfen açık ve öğretici olun — sınıf içinde öğretmenlerin rahatlıkla kullanabileceği formatta yazın.

---

## 11) SSS / Sorun giderme

**S: micro\:bit bilgisayara görünmüyor.**

* A: USB kablosunun data desteklediğinden emin ol. Kablonun sadece şarj için olan versiyonları görünmeyebilir.

**S: Kod yükleniyor gibi ama çalışmıyor.**

* A: Doğru versiyonu (v1/v2) kontrol et; ayrıca gerekli harici güç var mı? Seri port logunu kontrol et.

**S: NeoPixel çok parlak / yanıyor.**

* A: Harici güç ile birlikte direnç ve ortak toprak kullan.

---




