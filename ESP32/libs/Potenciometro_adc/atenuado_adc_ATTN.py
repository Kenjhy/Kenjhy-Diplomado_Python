from machine import Pin, ADC
from utime import sleep_ms

pot = ADC(Pin(36))#Analogo converison digital; trabaja resolucino del procesador
pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_10BIT)

ldr = ADC(Pin(39))#Analogo converison digital; trabaja resolucino del procesador
ldr.atten(ADC.ATTN_11DB) #light dependent resistor, foto resistencia
ldr.width(ADC.WIDTH_10BIT)


while True:
    lec_pot = pot.read()
    lec_ldr = ldr.read()
    print(lec_pot," ", lec_ldr)
    sleep_ms(100)

