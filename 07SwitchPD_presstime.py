#Create a loop that runs n times to turn on and off the LED

#init libraries
print("initializing library and board")
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
import time
#init board
GPIO.setmode(GPIO.BOARD)
in1pin=int(22)
#init I/O
GPIO.setup(in1pin, GPIO.IN, GPIO.PUD_DOWN)
GPIO.add_event_detect(in1pin, GPIO.BOTH, bouncetime=100)
print("init completed")

#Initialize variables

#Run the loop

# Count the number of edges in a time interval - differentiate 

while True:
    GPIO.wait_for_edge(in1pin, GPIO.RISING)
    t1=time.time()
    #print(t1)

    GPIO.wait_for_edge(in1pin, GPIO.FALLING,timeout=3000)
    t2=time.time()
    #print(t2)

    print(t2-t1)
    #if t2-t1<1:
        #LED.BlinkLED(n,out1pin)
    #else:
        #LED.BlinkLED(n,out1pin)

GPIO.cleanup()
