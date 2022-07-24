#------------------------------ [IMPORT]------------------------------------

import network, time, urequests
from machine import Pin, ADC, PWM, reset
import dht
import utime
import ujson
from umqtt.simple import MQTTClient

#--------------------------- [OBJETOS]---------------------------------------

# MQTT Server Parameters
MQTT_CLIENT_ID = "mqtt_client_id_Esp2" #Inventado
MQTT_BROKER    = "broker.hivemq.com"
MQTT_USER      = ""
MQTT_PASSWORD  = ""
MQTT_TOPIC     = b"area/edifi/piso1/sen1" #b el dato se va como bite, no como string ni entero
#MQTT_TOPIC     = b"area/edia/piso1/sen1" #b el dato se va como bite, no como string ni entero

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

    

#------------------------------------[MQTT]---------------------------------------------------------------------#

if conectaWifi ("Etbkenliz", "kenliz2314"):

    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
    
    
    print("Conectando a  MQTT server... ",MQTT_BROKER,"...", end="")
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)
    client.connect()

    print("Conectado!")

    nuevo_dato = ""
    
#Lectura de sensores
    while True:               
        
        sensor.measure() 
        temperatura = sensor.temperature()
        humedad = sensor.humidity()
                        
        print("Revisando Condiciones ...... ") #Si el dto sigue igual no envia
        
        msg = (b'{0:3.1f},{1:3.1f}'.format(temperatura, humedad))
        
       
      
        if msg != nuevo_dato:
            
            print("Reportando a  MQTT topic {}: {}".format(MQTT_TOPIC, msg))
            client.publish(MQTT_TOPIC, msg)
            nuevo_dato = msg

       
        else:
            print("No hay cambios")
        time.sleep(3)
        
        

else:
       print ("Imposible conectar")
       miRed.active (False)
