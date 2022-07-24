#------------------------------ [IMPORT]------------------------------------


import network, time, urequests
from machine import Pin, ADC, PWM
import utime
import ujson
import ufirebase as firebase

#--------------------------- [OBJETOS]---------------------------------------



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
    
    #firebase.setURL("https://estacion-esp32-metereologica-default-rtdb.firebaseio.com/")
    firebase.setURL("https://estacion-esp32-meteorologica-default-rtdb.firebaseio.com/")
        
    while True:

        

      #Put Tag2, cOLOCAR INFROAMCION EN FIREBASE
      firebase.put("hugo/sensor", {"valor_a": ["andinas",5,3.6], "valor_b": "xxx"}, bg=0)
      print("dato enviado")


      #Get Tag2
      firebase.get("hugo/sensor", "dato", bg=0)
      print("Buscar: "+str(firebase.dato))
      
      
      

else:
       print ("Imposible conectar")
       miRed.active (False)


