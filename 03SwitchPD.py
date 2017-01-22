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
print("init completed")

#Initialize variables


#Create a function to run the cycle
def Printswitch():
    while True:
        in1_status=GPIO.input(in1pin)
        if in1_status==GPIO.HIGH:
            print("HIGH")
            time.sleep(0.5)
        else:
            print("LOW")
            time.sleep(0.5)


#Run the command
Printswitch()
GPIO.cleanup()
	

