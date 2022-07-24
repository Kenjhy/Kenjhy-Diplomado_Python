from machine import Pin
from time import sleep

#Creamos un objeto que es el pin d2
red=Pin(15, Pin.OUT)
yellow=Pin(2, Pin.OUT)
gren=Pin(4, Pin.OUT)

while True:
    red.on()
    yellow.value(0) #apagado
    gren.off()
    sleep(1) #Mantener el estado anterior en ese etado
    red.off()
    yellow.value(1) #prendido
    gren.off()
    sleep(0.3)
    red.off()
    yellow.off()
    gren.on()
    sleep(0.3)
    
