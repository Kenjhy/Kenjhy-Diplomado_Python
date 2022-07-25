from machine import Pin
import bluetooth
from BLE import BLEUART

bombillo= Pin(26, Pin.OUT)

name= "EspHugo" 

print (name, "aca")

ble = bluetooth.BLE()
uart = BLEUART(ble, name)


def on_rx():
    
    rx_recibe = uart.read().decode().strip() # leer, decodificar utf8,elimina espacios
    uart.write("EspHugo dice: " + str(rx_recibe) + "\n")
    
       
    
uart.irq(handler = on_rx) # controlador de interrupciones, a quien llamar cuando el pin se active