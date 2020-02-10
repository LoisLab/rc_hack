import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

#Set up the pins
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

#Make sure the motors are all off
GPIO.output(3, True)
GPIO.output(5, True)
GPIO.output(11, True)
GPIO.output(13, True)

movetime = .5

def go_fwd():
    GPIO.output(3, True)
    GPIO.output(5, False)
    sleep(movetime)
    GPIO.output(3, True)
    GPIO.output(5, True)

def go_back():
    GPIO.output(3, False)
    GPIO.output(5, True)
    sleep(movetime)
    GPIO.output(3, True)
    GPIO.output(5, True)
    
def go_right():
    GPIO.output(3, True)
    GPIO.output(5, False)
    GPIO.output(11,False)
    sleep(movetime)
    GPIO.output(3, True)
    GPIO.output(5, True)
    GPIO.output(11, True)

def go_left():
    GPIO.output(3, True)
    GPIO.output(5, False)
    GPIO.output(13,False)
    sleep(movetime)
    GPIO.output(3, True)
    GPIO.output(5, True)
    GPIO.output(13, True)
    
go_fwd()
go_fwd()
go_right()
go_left()
GPIO.cleanup()

