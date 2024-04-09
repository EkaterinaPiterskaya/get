import RPi.GPIO as GPIO
from time import sleep
dac=[8,11,7,1,0,5,12,6] 
comp=14
troyka=13
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
GPIO.setup(comp,GPIO.IN)
GPIO.setup(troyka,GPIO.OUT,initial=GPIO.HIGH)
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
try:
    while True:
        k=adc()
        if k!=0:
            if k is not None:
                print(k,'{:.3f} V'.format(k*3.3/256))
            else:
                print(255)
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()