from machine import Pin
from utime import sleep_ms
import _thread

a = Pin(15, Pin.OUT)
b = Pin(2, Pin.OUT)
c = Pin(4, Pin.OUT)
d = Pin(5, Pin.OUT)
e = Pin(18, Pin.OUT)
f = Pin(19, Pin.OUT)
g = Pin(21, Pin.OUT)
h = Pin(22, Pin.OUT)

leds = [a,b,c,d,e,f,g,h]
    

#while True:
    #for bombillo in leds:
     #   bombillo.on()
      #  sleep_ms(20)
#        bombillo.off()
 #       sleep_ms(20)
        
    #for bombillo in leds[0:4]: #Solo 4
    #for bombillo in leds[0:8:2]: #Intervalo de 2
     #   bombillo.on()
      #  sleep_ms(100)
       # bombillo.off()
        #sleep_ms(100)
       
    #for bombillo in leds[::1]: #De izqioerda a derecha
     #   bombillo.on()
      #  sleep_ms(100)
       # bombillo.off()
        #sleep_ms(100)
    #for bombillo in leds[::-1]: #De derecha a izquierda
     #   bombillo.on()
      #  sleep_ms(100)
       # bombillo.off()
        #sleep_ms(100)

def nuevo():
    while True:
        for bombillo in leds[0:4:1]: #De derecha a izquierda
            bombillo.on()
            sleep_ms(500)
            bombillo.off()
            sleep_ms(500)
            
_thread.start_new_thread(nuevo,())


while True:
    for bombillo in leds[4:8:1]: #De derecha a izquierda
        bombillo.on()
        sleep_ms(50)
        bombillo.off()
        sleep_ms(50)
            


#Cada hilo haga tareas diferentes 
