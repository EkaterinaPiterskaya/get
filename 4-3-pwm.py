import RPi.GPIO as GPIO
dac=[8,11,7,1,0,5,12,6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(dac,GPIO.OUT)
p=GPIO.PWM(24,1000)
p.start(0)
try:
    while True:
        DC=int(input())
        p.ChangeDutyCycle(DC)
        print("{:.3f}".format(int(DC)*3.3/100))
finally:
    GPIO.cleanup()