#------------------------------ [IMPORT]------------------------------------


import network, time, urequests
from machine import Pin, ADC, PWM
import dht
import utime
import ujson
import ufirebase as firebase

#--------------------------- [OBJETOS]---------------------------------------
sensor = dht.DHT11(Pin(15))


#----------------------[ CONECTAR WIFI ]---------------------------------------------------------#

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

    

#------------------------------------[BOT]---------------------------------------------------------------------#

if conectaWifi ("Etbkenliz", "kenliz2314"):

    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
    
    firebase.setURL("https://automated-irrigation-sp32-default-rtdb.firebaseio.com/")
    
    #valor=0

    while True:

      #valor = valor + 1

      sensor.measure()
      temperatura = sensor.temperature()
      humedad = sensor.humidity()

      message = ujson.dumps({
        "Humedad": humedad,
        "Temperatura": temperatura,
        }) 

      #Put 
      firebase.put("Estacion/sensor", message, bg=0)
      print("Enviado...", message)
      #firebase.put("Estacion/{}".format(str(valor)), message, bg=0)
      #print("Enviado...", message, " ", valor )

      #Get 
      firebase.get("Estacion/sensor", "dato_recuperado", bg=0)
      print("Recuperado.... "+str(firebase.dato_recuperado))
      #firebase.get("Estacion/{}".format(valor), "dato_recuperado", bg=0)
      #print("Recuperado.... "+str(firebase.dato_recuperado)," ", valor )
      
      
      

else:
       print ("Imposible conectar")
       miRed.active (False)



