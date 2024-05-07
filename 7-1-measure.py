import RPi.GPIO as GPIO
import time
from matplotlib import pyplot

GPIO.setmode(GPIO.BCM)

leds=[9,10,22,27,17,4,3,2]
GPIO.setup(leds,GPIO.OUT)

dac=[6,12,5,0,1,7,11,8]
GPIO.setup(dac,GPIO.OUT,initial=GPIO.HIGH)

comp=14
GPIO.setup(comp,GPIO.IN)
troyka=13
GPIO.setup(troyka,GPIO.OUT,initial=GPIO.HIGH)

#перевод в двоичную систему 
def binary(a):
    return [int(elem) for elem in bin(a)[2:].zfill(8)]

#значение напряжения на выходе тройка-модуля
def adc():
    left,right=0,256
    while left+1!=right:
        m=(left+right)//2
        GPIO.output(dac,binary(m))
        time.sleep(0.02)
        if GPIO.input(comp)==1:
            right=m
        else:
            left=m
    return left 


try:
    pok_troyka=0
    new_measures=[]
    start_time=time.time()
    #измерения во время зарядки конденсатора
    print('начало зарядки конденсатора')
    
    while pok_troyka<256:
        pok_troyka=adc()
        print(pok_troyka)
        new_measures.append(pok_troyka)
        time.sleep(0)
        GPIO.output(leds,binary(pok_troyka))
    GPIO.setup(troyka,GPIO.OUT,initial=GPIO.LOW)

    #измерения во время разрядки конденсатора 
    print('начало разрядки конденсатора')
    while pok_troyka>170:
        pok_troyka=adc()
        print(pok_troyka)
        new_measures.append(pok_troyka)
        time.sleep(0)
        GPIO.output(leds,binary(pok_troyka))
    finish_time=time.time()
    experiment_time=finish_time-start_time

    #построение графика
    count = len(new_measures)
    print('Строим графики')
    x=[i*experiment_time/count for i in range(len(new_measures))]
    y=[i/256*3.3 for i in new_measures]
    pyplot.plot(x,y)
    pyplot.xlabel('Время')
    pyplot.ylabel('Показания АЦП')
    pyplot.show()

    #Занесение данных в файлы
    print('Заносим данные в файлы')
    with open('data.txt','w') as f:
        for i in new_measures:
            f.write(str(i)+'\n')
        
        with open('settings.txt','w') as f:
            f.write(str(1/experiment_time/count)+'\n')
            f.write('0.01289')
    print('общая продолжительность эксперимента {},период одного измерения{},средняя частота дискретизации проведённых измерений{},шаг квантования АЦП{}'.format(experiment_time,experiment_time/count,1/experiment_time/count,0.013))


finally:
    GPIO.output(leds,0)
    GPIO.output(dac,0)
    GPIO.cleanup()