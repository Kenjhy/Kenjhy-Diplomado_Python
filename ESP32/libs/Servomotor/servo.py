print("Hello, ESP32!")
from machine import Pin, PWM
from utime import sleep_ms

servo = PWM(Pin(5), freq=50)

while True:
    for angulo in range(25, 125):  #35-138, 25-125, 20-130
        servo.duty(angulo)
        sleep_ms(50)
    
    print("nuevo")
    
#Vesiion 1.19
#     for angulo in range(1800, 8000):  #35-138, 25-125
#         servo.duty_u16(angulo)
#         sleep_ms(1)
#         
#     print("ok")
