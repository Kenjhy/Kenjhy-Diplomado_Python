from machine import Pin
from hcsr04 import HCSR04
import time
import utime
from utime import sleep

def encender(duracion, cant, npin):
	""" Esta función se desarrolla para encender cualquier led"""
	
	led =Pin(npin, Pin.OUT)
	
	for x in range (cant):
		led.value(1)
		time.sleep_ms(duracion)
		led.value(0)
		time.sleep_ms(duracion)
	return("DONE")
 
def lista():
	""" Esta función se desarrolla para encender los led del auto fantastico"""
	
	d1= Pin(19, Pin.OUT)
	d2= Pin(18, Pin.OUT)
	d3= Pin(5, Pin.OUT)
	d4= Pin(21, Pin.OUT)
	d5= Pin(16, Pin.OUT)
	d6= Pin(4, Pin.OUT)
	d7= Pin(2, Pin.OUT)
	d8= Pin(15, Pin.OUT)
	
	leds=[d1, d2, d3, d4, d5, d6, d7, d8]
	
	while True:
		for bombillo in leds[::1]:
			bombillo.value(1)
			utime.sleep_ms(50)
			bombillo.value(0)
			utime.sleep_ms(50)
		for bombillo in leds[::-1]:
			bombillo.value(1)
			utime.sleep_ms(50)
			bombillo.value(0)
			utime.sleep_ms(50)
			
	def sensorHCSR04():
		"""Sensor de distancia"""
		medidor = HCSR04 (trigger_pin = 4, echo_pin = 5)
		
		while (True):
			try:
				distancia = medidor.distance_cm ()
				print ("Distancia = ", distancia)
				sleep (1)
			except:
				print ("Error.!")
		
	
