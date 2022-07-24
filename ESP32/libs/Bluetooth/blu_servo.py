from machine import Pin, PWM
import bluetooth
from BLE import BLEUART
import utime


name= "EspHugo"

print (name, "aca ok")

ble = bluetooth.BLE()
uart = BLEUART(ble, name)

servo = PWM(Pin(15), freq=50)

def map(x):
        return int((x - 0) * (125-25) / (180 - 0) + 25)
    

def on_rx():
    
    rx_recibe = uart.read().decode().strip()
    uart.write("EspHugo dice: " + str(rx_recibe) + "\n")
    print(rx_recibe)
    
    if rx_recibe == "0":
        
        m = map(0)
        servo.duty(m)
        
    if rx_recibe == "!B813":
        
        m = map(0)
        servo.duty(m)
        
    if rx_recibe == "90":
        
        m = map(90)
        servo.duty(m)
        
    if rx_recibe == "!B516":
        
        m = map(90)
        servo.duty(m)
        
    if rx_recibe == "180":
        
        m = map(180)
        servo.duty(m)
        
    if rx_recibe == "!B714":
        
        m = map(180)
        servo.duty(m)
        
        
        
    
    
uart.irq(handler = on_rx)

