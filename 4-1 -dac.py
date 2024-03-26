import RPi.GPIO as GPIO
import sys 
dac=[8,11,7,1,0,5,12,6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
def decimal2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
try:
    while True:
        x=input("Введите число от 0 до 255  ")
        if x=='q':
            break
        elif x.isdigit() and int(x)%1==0 and 0<=int(x)<=255:
            GPIO.output(dac,decimal2bin(int(x)))
            print("{:.4f}".format(int(x)/256*3.3))
        elif not x.isdigit:
            print("Введен неверный тип данных")
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()