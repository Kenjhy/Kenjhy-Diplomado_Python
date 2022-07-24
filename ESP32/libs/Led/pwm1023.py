from machine import Pin, ADC, PWM
from utime import sleep_ms

led = PWM(Pin(15), freq=10000) #grADUE EL MOVIMIENTO o pulsos DE LA LUZ

#PWM es 123000 = Resolucion, Modulacion por ancho de pulso, por un determinado tiempo y otros apagados, = analoga
#El procesador no trabaja por tiempo
while True:
    #Tiempo encendido
    for i in range(0, 1023):
        led.duty(i) #ciclo de trabajo
        sleep_ms(1) #tIEMPO DE ESPERA PARA HACER LA ITERACION