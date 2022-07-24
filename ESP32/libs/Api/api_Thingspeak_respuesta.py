import network, time, urequests
from machine import Pin
import json

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


if conectaWifi ("Etbkenliz", "kenliz2314"):

    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
      
    #url = "https://api.thingspeak.com/channels/1794531/feeds.json?results=2"
    url = "https://api.thingspeak.com/channels/1802256/feeds.json?results=2" #Read
    
    while True:
        
        
        consulta=urequests.get(url)
        print(consulta)
        datos=consulta.json() #Guarda en json
        print (datos)
        tem=datos["feeds"][1]["field1"] #Obtenemos los datos
        hum=datos["feeds"][1]["field2"] #Obtenemos los datos
        print("Tem={}°C, Hum={}%".format(tem,hum)) #Imprimo en consola
        time.sleep(1)
 
else:
       print ("Imposible conectar")
       miRed.active (False)