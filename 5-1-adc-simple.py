import RPi.GPIO as GPIO
from time import sleep
dac=[8,11,7,1,0,5,12,6] 
comp=14
troyka=13
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
GPIO.setup(troyka,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(comp,GPIO.IN)
def binin(x):
    return [int(elem) for elem in bin(x)[2:].zfill(8)]
def adc():
    for i in range(256):
        GPIO.output(dac,binin(i))
        compval=GPIO.input(comp)
        sleep(0.005)
        if compval==1:
            return i
try:
    while True:
        i=adc()
        if i!=0:
            if i is not None:
                print(i,'{:.3f} V'.format(i*3.3/256))
            else:
                print(255)
finally:
    GPIO.output(dac,0)
    GPIO.output(troyka,0)
    GPIO.cleanup()