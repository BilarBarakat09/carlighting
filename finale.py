#we import the led and pir sensor and the sleep command
from gpiozero import LED
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
#we inter the GPIO pin for the led and pir
led=LED(2)
pir_gpio = 3
GPIO.setup(pir_gpio,GPIO.IN)
#we make two function one if there is motion and one when there is no motion
def motion():
    print("motion detected")
    led.on()
    sleep(2)
    led.off()
    sleep(1)
def no_motion():
    print("no motion")
    led.off()
    sleep(2)
while True:
    #we check if there is motion then we call the first function
    if GPIO.input(pir_gpio)==1:
        motion()
    #we check if there is motion then we call the second function
    elif GPIO.input(pir_gpio)==0:
        no_motion()