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
GPIO.add_event_detect(in1pin, GPIO.RISING, bouncetime=100)
print("init completed")

#Initialize variables
## N blink cycles ti run
#n=int(5)
n=int(input("How many blink cycles do you want to run ? n= "))

#Run the command
while True:
    if GPIO.event_detected(in1pin):
        LED.BlinkLED(n,out1pin)

GPIO.cleanup()
