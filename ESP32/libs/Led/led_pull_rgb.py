from machine import Pin
from utime import sleep_ms

#Configuracion polo a tierra GND 3V3 pull_up
##Si no presiono el boton esta 1 prendido
##Si presiono el boton esta 0 apagado

#Configuracion polo + 3V3 voltios pull_up
##Si no presiono el boton esta 0 prendido
##Si presiono el boton esta 1 apagado

sensor = Pin(22, Pin.IN, Pin.PULL_DOWN) #cONECTADO AL NEGATIVO Y A LA ENTRADA, BAJAR DERRIBAR

r = Pin(15, Pin.OUT)
g = Pin(2, Pin.OUT)
b = Pin(4, Pin.OUT)

def display(R, G, B):
    r.value(R)
    g.value(G)
    b.value(B)


while True:
    estado=sensor.value()#Si no coloco nada el devuelve el estado en que se encuentar el pin, revisa el estado
    #print(estado) #Imprime el estado
    sleep_ms(50) #Cada 200 milisegundos revisa el estado
    if estado == 1:
        display(0,0,1)
        #print(contador)
    else:
        display(1,0,0)

