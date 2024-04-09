import RPi.GPIO as GPIO
from time import sleep
dac=[8,11,7,1,0,5,12,6] 
leds=[9,10,22,27,17,4,3,2]
comp=14
troyka=13
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
GPIO.setup(leds,GPIO.OUT)
GPIO.setup(troyka,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(comp,GPIO.IN)
def binin(x):
    return [int(elem) for elem in bin(x)[2:].zfill(8)]
def adc():
    k=0
    for i in range(7,-1,-1):
        k+=2**i
        GPIO.output(dac,binin(k))
        sleep(0.005)
        if GPIO.input(comp)==GPIO.HIGH:
            k-=2**i
    return k
def volume(n):
    n=int(n/256*10)
    mas=[0]*8
    for i in range(n-1):
        mas[i]=1
    return mas
try:
    while True:
        k=adc()
        if k!=0:
            if k is not None:
                GPIO.output(leds,volume(k))
finally:
    GPIO.output(dac,0)
    GPIO.output(troyka,0)
    GPIO.cleanup()