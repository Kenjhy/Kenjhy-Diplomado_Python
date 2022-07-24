print("Hello, ESP32!")
from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
#from dht import DHT11
from utime import sleep

ancho = 128
alto = 64

#sensorDHT = DHT11(Pin(15))
i2c = I2C(0, scl=Pin(22), sda=Pin(21)) #Puerto por defecto,
oled = SSD1306_I2C(ancho, alto, i2c) #comunicacion

sensor= ADC(Pin(36))

print(i2c.scan())#Verifica que exista comunicacion cerial con la tarjeta

while True:
  valor = int((sensor.read_u16())/500)
  oled.fill_rect(1,15,valor,15,1) #comienzo x y y, y hasta que poscicion de x y y voy, bits prendidos
  oled.show()
  oled.fill_rect(1,15,valor,15,0)
  sleep(0.3)
  # oled.fill(1) #Prende todos los pixeles del modulo, ON
  # oled.show()
  # sleep(2)
  # oled.fill(0) #Prende todos los pixeles del modulo, OFF
  # oled.show()
  # sleep(2)
  # #Dibujar una linea recta
  # oled.fill_rect(0,0,60,20,1) #valores de inicioa y de finalizacion 128*64, bit
  # oled.show()