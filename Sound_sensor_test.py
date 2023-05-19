from machine import Pin, SoftI2C
from machine import ADC
from time import sleep
from ssd1306 import SSD1306_I2C
import machine
i2c = SoftI2C(scl=Pin(4), sda=Pin(5))
oled = SSD1306_I2C(128, 64, i2c)
#oled.text("Hello", 10, 10)
adc = ADC(Pin(39))
led = Pin(14, Pin.OUT)

#white frame
oled.fill_rect(5, 5, 30, 50, 1)
#black filling
oled.fill_rect(7, 7, 26, 46, 0)

def charge_level(k, level):
    oled.fill_rect(40, 30, 45, 15, 0)
    oled.fill_rect(9, 9, 22, 42, 0)
    #full charge
    oled.fill_rect(9, 9, 22, 42, 1)
    #charge level
    oled.fill_rect(9, 9, 22, k, 0)
    oled.text("Charge level:",40,15)

    oled.text(f"{str(level)}%",40,30)
    #oled.text("%",67,30)

    oled.show()

while True:
    #oled.fill(0)
    adc.atten(ADC.ATTN_11DB)
    adc_value = adc.read()
    
    level = round(adc_value*100/4095)
    b = 100 - level
    k = int(b*42/100)
    charge_level(k, level)
    
    #voltage = adc_value/4095
    
    
    print(adc_value)
    
    sleep(0.1)