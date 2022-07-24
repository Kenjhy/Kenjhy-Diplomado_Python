#------------------------------ [IMPORT]------------------------------------


import network, time, urequests
from machine import Pin, ADC, PWM
from utelegram import Bot
from dht import DHT11
import utime

TOKEN = '5597151200:AAF1bwf12HXiSp9jBXShoOuTlDex2yky1R8'

#--------------------------- [OBJETOS]---------------------------------------

bot = Bot(TOKEN)
bombillo  = Pin(2, Pin.OUT)
sensorDHT = DHT11(Pin(15))


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
    
    print("ok")
    
    @bot.add_message_handler("Hola")
    def help(update):
        update.reply('''¡Estación Metereológica!
                     \n Menu Principal
                     \n Elije una opción:
                     
                     Temperatura  : 1
                     Humedad: 2
                    
                     
                     \n No olvides que estoy para ayudarte''')
    
    @bot.add_message_handler("1")
    def help(update):
        sensorDHT.measure()
        tem = sensorDHT.temperature()
        hum = sensorDHT.humidity()
        update.reply("La temperatura es," + str(tem) + "°c")
                     
        
    @bot.add_message_handler("2")
    def help(update):
        sensorDHT.measure()
        tem = sensorDHT.temperature()
        hum = sensorDHT.humidity()
        update.reply("La Humedad es," + str(hum) + "%")
    
    
    
    bot.start_loop()
    
      

else:
       print ("Imposible conectar")
       miRed.active (False)