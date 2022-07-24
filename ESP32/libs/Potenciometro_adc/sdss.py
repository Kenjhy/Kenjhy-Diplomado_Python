from machine import Pin, ADC, PWM
from utime import sleep_ms

led = PWM(Pin(15), freq=10000) #grADUE EL MOVIMIENTO o pulsos DE LA LUZ

pot = ADC(Pin(36))#Analogo converison digital; trabaja resolucino del procesador
pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_10BIT)

#PWM es 123000 = Resolucion, Modulacion por ancho de pulso, por un determinado tiempo y otros apagados, = analoga
#El procesador no trabaja por tiempo
while True:
    #Tiempo encendido
        lec_pot = pot.read()
        led.duty(lec_pot) #ciclo de trabajo
        sleep_ms(50) #tIEMPO DE ESPERA PARA HACER LA ITERACION
