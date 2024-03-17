from machine import Pin
from utime import sleep
from random import randint
#objects
lt1 = Pin(0, Pin.OUT)
lt2 = Pin(1, Pin.OUT)
lt3 = Pin(2, Pin.OUT)
lt4 = Pin(3, Pin.OUT)
lt5 = Pin(4, Pin.OUT)
lt6 = Pin(5, Pin.OUT)
lt7 = Pin(6, Pin.OUT)
lt8 = Pin(7, Pin.OUT)
lt9 = Pin(8, Pin.OUT)
lo1 = Pin(9, Pin.OUT)
lo2 = Pin(10, Pin.OUT)
lo3 = Pin(11, Pin.OUT)
lo4 = Pin(12, Pin.OUT)
lo5 = Pin(13, Pin.OUT)
lo6 = Pin(14, Pin.OUT)
lo7 = Pin(15, Pin.OUT)
lo8 = Pin(16, Pin.OUT)
lo9 = Pin(17, Pin.OUT)
red = Pin(18, Pin.OUT)
blue = Pin(19, Pin.OUT)
submit = Pin(20, Pin.IN)
tens = Pin(21, Pin.IN)
ones  = Pin(22, Pin.IN)
#vars
tcount = 0
ocount = 0
number = randint(0,99)
#for debugging purposes: print(number)
#reset
def reset():
    lt1.value(0)
    lt2.value(0)
    lt3.value(0)
    lt4.value(0)
    lt5.value(0)
    lt6.value(0)
    lt7.value(0)
    lt8.value(0)
    lt9.value(0)
    lo1.value(0)
    lo2.value(0)
    lo3.value(0)
    lo4.value(0)
    lo5.value(0)
    lo6.value(0)
    lo7.value(0)
    lo8.value(0)
    lo9.value(0)
    red.value(0)
    blue.value(0)
#main
reset()
while True:
    sleep(0.5)
    if tens.value() == 1:
        tcount += 1
        if tcount < 10:
            if tcount == 1: lt1.value(1)
            elif tcount == 2: lt2.value(1)
            elif tcount == 3: lt3.value(1)
            elif tcount == 4: lt4.value(1)
            elif tcount == 5: lt5.value(1)
            elif tcount == 6: lt6.value(1)
            elif tcount == 7: lt7.value(1)
            elif tcount == 8: lt8.value(1)
            elif tcount == 9: lt9.value(1)
        else: tcount = 0; lt1.value(0); lt2.value(0); lt3.value(0); lt4.value(0); lt5.value(0); lt6.value(0); lt7.value(0); lt8.value(0); lt9.value(0)
    elif ones.value() == 1:
        ocount += 1
        if ocount < 10:
            if ocount == 1: lo1.value(1)
            elif ocount == 2: lo2.value(1)
            elif ocount == 3: lo3.value(1)
            elif ocount == 4: lo4.value(1)
            elif ocount == 5: lo5.value(1)
            elif ocount == 6: lo6.value(1)
            elif ocount == 7: lo7.value(1)
            elif ocount == 8: lo8.value(1)
            elif ocount == 9: lo9.value(1)
        else: ocount = 0; lo1.value(0); lo2.value(0); lo3.value(0); lo4.value(0); lo5.value(0); lo6.value(0); lo7.value(0); lo8.value(0); lo9.value(0)
    elif submit.value() == 1:
        total_value = 10*tcount + ocount
        if total_value == number: break
        elif total_value > number: red.value(1)
        elif total_value < number: blue.value(1)
        tcount = 0
        ocount = 0
        sleep(1)
        reset()
for x in range(5):
    red.toggle()
    blue.toggle()
    sleep(0.75)
reset()
