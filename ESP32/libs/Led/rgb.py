from machine import Pin
from utime import sleep_ms
import _thread

r = Pin(15, Pin.OUT)
g = Pin(2, Pin.OUT)
b = Pin(4, Pin.OUT)

def display(R, G, B):
    r.value(R)
    g.value(G)
    b.value(B)
  
  
  
while True:
    print("Iniciando")
    display(0,0,0) #black
    sleep_ms(500)
    display(0,0,1) #Azul
    sleep_ms(500)
    display(0,1,0) #Verde
    sleep_ms(500)
    display(0,1,1) #Azul aguamarina
    sleep_ms(500)
    display(1,0,0) #Rojo
    sleep_ms(500)
    display(1,0,1) #Morado
    sleep_ms(500)
    display(1,1,0) #Amarillo
    sleep_ms(500)
    display(1,1,1)
    sleep_ms(300) #Blanco 

    
        
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

while True:
    for bombillo in leds[4:8:1]: #De derecha a izquierda
        bombillo.on()
        sleep_ms(50)
        bombillo.off()
        sleep_ms(50)
            


#Cada hilo haga tareas diferentes 

