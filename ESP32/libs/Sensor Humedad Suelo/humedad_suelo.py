from machine import Pin, PWM
import utime
from machine import Pin, ADC
from utime import sleep_ms

humedad_tierra = ADC(Pin(39))#Analogo converison digital; trabaja resolucino del procesador
print(humedad_tierra)
humedad_tierra.atten(ADC.ATTN_11DB)
humedad_tierra.width(ADC.WIDTH_10BIT)
# 0 sumergido en agua
#800 -1023 en el aire (o en un suelo muy seco)
#suelo ligeramente húmero  600-700
def main():
    def map(x):
        print("dd",x)
        return float((x - 0) * (1023- 0) / (100 - 0) + 0) # v1.19 -- duty(m) -- 0 y 1023, rango sensor maximo y minimo, valor experado convertido, valor minimo del valor que se espera, valor minimo que se espera
        #return int((x - 0) * (125- 25) / (180 - 0) + 25) # v1.19 -- duty(m) -- 0 y 1023
    while True:
        lectura = float(humedad_tierra.read())
        porcentaje_humedad_suelo = map(lectura)
        print(lectura) #Formatear !!!!!!
        print(porcentaje_humedad_suelo)
             
if __name__=="__main__":
    main()
             
             
    
    


