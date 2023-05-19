from machine import Pin,ADC,I2C
import ssd1306
from ssd1306 import SSD1306_I2C
from time import sleep
import machine

adc = ADC(Pin(36))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)

i2c = I2C(scl=Pin(4),sda=Pin(5))
oled=SSD1306_I2C(128,64,i2c)
x0=8
y0=8
x1=34
y1=44

oled.fill(0)
oled.text("5V",50,10)
oled.rect(x0,y0,x1,y1)
oled.text("Voltmeter", 50,28)
oled.text("0V",50,47)
oled.fill_rect(x0+2,y0+2,x1-4,y1-4,1)
oled.show()

while True:
    oled.fill_rect(x0+2,y0+2,x1-4,y1-4,0)
    oled.fill_rect(x0+2,y0+45,x1+5,y1+20,0)
    adc_value=round(adc.read()/819,1)
    oled.text(f"{adc_value}V", 10.55)
    adc_gra = int(adc_value)
    print(adc.read())
    
    oled.fill_rect(x0+2,y1-4-adc_gra*6,x1-4,50-(y1-4-adc_gra*6),1)
    oled.show()
    sleep(0.2)