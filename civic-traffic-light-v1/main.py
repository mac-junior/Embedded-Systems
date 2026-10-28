from machine import Pin
import time

# Pin assignments based on your JSON connections
red_led = Pin(15, Pin.OUT)
yellow_led = Pin(2, Pin.OUT)
green_led = Pin(4, Pin.OUT)

while True:
    # Green Light
    green_led.on()
    time.sleep(5)
    green_led.off()
    
    # Yellow Light
    yellow_led.on()
    time.sleep(2)
    yellow_led.off()
    
    # Red Light
    red_led.on()
    time.sleep(5)
    red_led.off()
