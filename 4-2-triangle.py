import RPi.GPIO as GPIO
from time import sleep
dac=[8,11,7,1,0,5,12,6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
try:
    T=input()
    while True:
    
        t=float(T)/256/2
        for i in range(256):
            GPIO.output(dac,dec2bin(i))
            sleep(t)
        for i in range(255,-1,-1):
            GPIO.output(dac,dec2bin(i))
            sleep(t)
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()