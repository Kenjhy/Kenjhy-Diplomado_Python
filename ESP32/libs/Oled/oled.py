from machine import Pin, I2C
from libs.ssd1306 import SSD1306_I2C
from dht import DHT11
from utime import sleep

ancho = 128
alto = 64
fila = 5

sensorDHT = DHT11(Pin(15))
i2c = I2C(0, scl=Pin(22), sda=Pin(21)) #Puerto por defecto,
oled = SSD1306_I2C(ancho, alto, i2c) #comunicacion

print(i2c.scan())#Verifica que exista comunicacion cerial con la tarjeta

while True:
    
    sensorDHT.measure()
    tem = sensorDHT.temperature() #Guardar una temperatura o lectura de la temperatura ambiente
    hum =sensorDHT.humidity() #Guaradar la humedad
    oled.fill(0) #Borrar la pantalla
    #oled.text("hola",0,0) #Enviar str, columna , fila
    #oled.text("area andina", 0, 10)
    #oled.text("-------------", 0, 20)
    oled.text("Temperatura", 0, 0)
    oled.text(str(tem), 0, 10)
    oled.text("Humedad", 0, 20)
    oled.text(str(hum),0,30)
    oled.show()
    sleep(1)

