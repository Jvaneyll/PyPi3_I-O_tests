#Create a loop that runs n times to turn on and off the LED

#init libraries
print("initializing library and board")
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
import time
import signal
#init board
GPIO.setmode(GPIO.BOARD)
in1pin=int(22)
#init I/O
GPIO.setup(in1pin, GPIO.IN, GPIO.PUD_DOWN)
GPIO.add_event_detect(in1pin, GPIO.BOTH, bouncetime=100)
print("init completed")

#Initialize variables
# Create a global var that is a vector of edge timings
tvec=[]
# Prepare a handler that will run a timer for 200 msec ad generate exception to interrupt the monitoring if nothing happens
def timeout_handler():


#Run the loop
#first rising edge is a clock start to monitor edges happening within 3sec - time out runs in that event separately and control the others
#value is appended as first value to tvec monitoring vector
#During the time clock, other rising/falling edges are monitored and appended to tvec
# Whenever time clock is out or that no other event is detected for x msec after falling edges - Process the tvec by conditional for different actions
# Count the number of edges in a time interval - differentiate

while True:
    GPIO.wait_for_edge(in1pin, GPIO.RISING)
    #collect time and append to tvec
    t1=time.time()
    tvec.append(t1)


    GPIO.wait_for_edge(in1pin, GPIO.FALLING,timeout=3000) #,callback= to be added in order to start the timer after button relapse
    t2=time.time()
    tvec.append(t2)
    #launch/re-initialize the timer for 200 msec after falling edge

    if len(tvec)==2 && tvec[2]-tvec[1]>=1500:
        print("hold push")
        LED.BlinkLED(10,out1pin)
        else if len(tvec)==2 && tvec[2]-tvec[1]<=500:
            print("single click")
            LED.BlinkLED(1,out1pin)
        else if len(tvec)>=4 && tvec[2]-tvec[1]<=300 && tvec[3]-tvec[2]<=300 && tvec[4]-tvec[3]<=300:
            print("doube click")
            LED.BlinkLED(5,out1pin)
        tvec=[]

GPIO.cleanup()
