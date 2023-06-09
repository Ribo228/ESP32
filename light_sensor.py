from machine import Pin, I2C
from machine import ADC
import time
import machine
import ssd1306

# using default address 0x3C
i2c = machine.I2C(1, scl = machine.Pin(4), sda = machine.Pin(5), freq = 400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
adc = ADC(Pin(39))
adc.atten(ADC.ATTN_11DB)

while True:
    i = adc.read()
    print(i)
    n = round(i/4095*100)
    print(n)
    time.sleep(0.5)
    oled.fill(0)
    oled.text('Brightness: '+ str(n) + '%', 2, 2, 1)
    oled.fill_rect(10, 20, 104, 40, 1)
    oled.fill_rect(12+n, 22, (100-n), 36, 0)
    oled.show()
    