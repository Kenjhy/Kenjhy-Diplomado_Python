from machine import Pin, ADC
from utime import sleep_ms

sensor_adc = ADC(Pin(36))#Analogo converison digital; trabaja resolucino del procesador

while True:
    factor_conversion = 3.3/65535
    factor_dos = 400/65535
    lectura = sensor_adc.read_u16()
    voltaje = lectura*factor_conversion
    distancia = lectura*factor_dos
    #lectura = sensor_adc.read_u16()#Trae , lee 16 bits
    print(lectura,voltaje, distancia)
    sleep_ms(100)
