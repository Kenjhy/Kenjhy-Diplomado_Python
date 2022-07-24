from machine import Pin
#from utime import sleep_ms
from utime import sleep
from dht import DHT11

sensorDHT = DHT11(Pin(4))
file = open("sensores.csv","w")#Abre documeto Modo escritura, 

while True:
    #sleep_ms(1)
    sleep(1)
    sensorDHT.measure() #Inicializar, verificar que a comunicacion entre el sensor este bien
    tem = sensorDHT.temperature() #Guardar una temperatura o lectura de la temperatura ambiente
    hum =sensorDHT.humidity() #Guaradar la humedad
    kel = tem + 273.15 #K = ºC + 273.15.
    far = (tem*9)/5+32 # ºF = ºC x 1.8 + 32. ,,, (°C × 9/5) + 32 =
    file.write(str("T={:02.1f}°c ; H={:02.1f}% ; K={:02.2f}k ; F={:02.3f}f \n ".format(tem, hum, kel, far))) #Escribir sobre el doicumento
    file.flush() #Cerrar el documento
    #file.close() #Cerrar el documento
    #print(tem,hum,kel,far) #50°C,#100% medidas 0 conjelacion 100 ebullicion
    #print("Temperature",tem,"°c","Humedad",hum,"%") #50,#100 medidas
    #print("T={}°c , H={}%, K={}k, F={}f ".format(tem, hum, kel, far)) #Formateando, grados positivos y negativos
    print("T={:02.1f}°c , H={:02.1f}%, K={:02.2f}k, F={:02.3f}f ".format(tem, hum, kel, far)) #Formateando, grados positivos y negativos, :cuantas cifras enteras y cuantas decimales quieor ver
    #Temperatura en °Kelvin: Escala internacional de la temperatura, trabaja desde 0 en adelante mo hay - ni + , conjelacion y ebullicion, 
    
    