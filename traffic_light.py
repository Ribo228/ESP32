import time
from machine import Pin

led_red = Pin(15, Pin.OUT)  # Sets ESP32 board pin to output mode
led_yellow = Pin(12, Pin.OUT)  # Sets ESP32 board pin to output mode
led_green = Pin(13, Pin.OUT)  # Sets ESP32 board pin to output mode

while True:
    led_red.value(1)  # Turn on red LED
    led_green.value(0)
    led_yellow.value(0)
    time.sleep(3)  # wait 3s
    led_red.value(0)
    led_green.value(0)
    led_yellow.value(1) # Turn on red LED
    time.sleep(1)
    led_red.value(0)
    led_green.value(1)
    led_yellow.value(0)  
    time.sleep(3)
    led_red.value(0)
    led_green.value(0)  
    led_yellow.value(1)
    time.sleep(1)


