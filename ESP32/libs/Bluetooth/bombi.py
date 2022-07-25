from machine import Pin
import bluetooth
import utime
from dht import DHT11

led =Pin(23,Pin.OUT)
sensorDHT = DHT11(Pin(15))
sensorDHT.measure()

while True:
    
    tem = sensorDHT.temperature()
    hum = sensorDHT.humidity()
    print(hum)
    if(hum >=50 and hum <=60):
        led.value(1)
        print("led on")
    else:
        led.value(0)
        print("led off")
    utime.sleep(0.5)
