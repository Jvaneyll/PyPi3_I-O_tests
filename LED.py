#Create a function to run the blink cycles

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
import time

def BlinkLED(n,outpin):
    i=1
    while i<=n:
        if i%2==0:
            GPIO.output(outpin,True)
            time.sleep(0.5)
            GPIO.output(outpin,False)
            time.sleep(0.5)
        else:
            GPIO.output(outpin,True)
            time.sleep(0.2)
            GPIO.output(outpin,False)
            time.sleep(0.8)

        print(str(n-i) + " cycles left on " + str(n) + " requested")
        i=i+1
    print("blink cycles completed")
