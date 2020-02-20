import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

#Set up the pins - 3 & 5 for steering, 11 & 13 for drive
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

#Make sure the motors are all off
GPIO.output(3, False)
GPIO.output(5, False)
GPIO.output(11, False)
GPIO.output(13, False)

movetime = .5  #moves last 1/2 second

def go_fwd():
    GPIO.output(11, True)   #one pin on
    GPIO.output(13, False)  #one pin off
    sleep(movetime)
    GPIO.output(11, False)   
    GPIO.output(13, False)   

def go_back():
    GPIO.output(11, False)  #setting pins the opposite way
    GPIO.output(13, True)   #makes the motor go the other direction
    sleep(movetime)
    GPIO.output(11, False)
    GPIO.output(13, False)
    
def go_left():
    GPIO.output(11, True)    #steering works the same way but with the other motor
    GPIO.output(13, False)
    GPIO.output(3, False)   #moving the car while the wheels are turned
    GPIO.output(5, True)
    sleep(movetime)
    GPIO.output(3, False)
    GPIO.output(5, False)
    GPIO.output(11, False)
    GPIO.output(13, False)

def go_right():
    GPIO.output(11, True)
    GPIO.output(13, False)
    GPIO.output(3, True)
    GPIO.output(5, False)
    sleep(movetime)
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(3, False)
    GPIO.output(5, False)
    
go_fwd()
go_fwd()
go_right()
go_left()
GPIO.cleanup()              # always clean up after yourself

