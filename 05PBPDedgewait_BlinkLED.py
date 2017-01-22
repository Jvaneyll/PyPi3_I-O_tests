#Create a loop that runs n times to turn on and off the LED

#init libraries
print("initializing library and board")
import LED
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
import time
#init board
GPIO.setmode(GPIO.BOARD)
out1pin=int(16)
in1pin=int(22)

#init I/O
GPIO.setup(out1pin, GPIO.OUT)
GPIO.setup(in1pin, GPIO.IN, GPIO.PUD_DOWN)
print("init completed")

#Initialize variables
n=int(input("How many blink cycles do you want to run ? n= "))

#Run the command
GPIO.wait_for_edge(in1pin, GPIO.RISING)
LED.BlinkLED(n,out1pin)
GPIO.cleanup()
