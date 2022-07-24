import network, time, urequests #internet , interrupciones, request http
import json 
from dht import DHT11
from machine import Pin #Bombillos

def conectaWifi (red, password):
      global miRed
      miRed = network.WLAN(network.STA_IF)     
      if not miRed.isconnected():              #Si no está conectado…
          miRed.active(True)                   #activa la interface
          miRed.connect(red, password)         #Intenta conectar con la red
          print('Conectando a la red', red +"…")
          timeout = time.time ()
          while not miRed.isconnected():           #Mientras no se conecte..
              if (time.ticks_diff (time.time (), timeout) > 10):
                  return False
      return True

sensorDHT = DHT11(Pin(15))

if conectaWifi ("Etbkenliz", "kenliz2314"):

    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
      
    url = "https://api.thingspeak.com/update?api_key=TM1EP8YU9EGKK7DW"  #Write
    
    while True:
        time.sleep(4)
        sensorDHT.measure() #Verifica conexion
        temp=sensorDHT.temperature() #lee temperatura
        hum=sensorDHT.humidity() #lee humedad

        print ("T={:02.} ºC, H={:02d} %".format(temp,hum)) #imprime en pantalla
        #Solicitud get a la ruta y sus parametros
        respuesta = urequests.get(url+"&field1="+str(temp)+"&field2="+str(hum)) 
        #print(respuesta)
        #respuesta = urequests.get(url+"&field1="+str(random.randint(20,35))+"&field2="+str(random.randint(40,80)))
        print(respuesta.text)
        print(respuesta.status_code)
        respuesta.close ()
        time.sleep(1)
        
 
else:
       print ("Imposible conectar")
       miRed.active (False)