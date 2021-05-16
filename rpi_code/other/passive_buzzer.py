#!/usr/bin/env python3
########################################################################
# Filename    : Alertor.py
# Description : Make Alertor with buzzer and button
# Author      : www.freenove.com
# modification: 2019/12/27
########################################################################
import RPi.GPIO as GPIO
import time
import math

buzzerPin = 24    # define the buzzerPin
buttonPin = 12    # define the buttonPin
startPin = 16
def setup():
    global p
    GPIO.setmode(GPIO.BCM)         # Use PHYSICAL GPIO Numbering
    GPIO.setup(buzzerPin, GPIO.OUT)   # set RGBLED pins to OUTPUT mode
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    # Set buttonPin to INPUT mode, and pull up to LOW level, 3.3V
    GPIO.setup(startPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    # Set buttonPin to INPUT mode, and pull up to LOW level, 3.3V
    p = GPIO.PWM(buzzerPin, 1) 
    p.start(0);
    
def loop():
    freq = 2000
    duty_cycle=50
    while True:
        if GPIO.input(buttonPin)==GPIO.HIGH:
            alertor(duty_cycle)
#             print ('alertor turned on >>> ')
        else :
            stopAlertor()
#             print ('alertor turned off <<<')
        if GPIO.input(startPin) == GPIO.HIGH:
            duty_cycle = int(input('change duty cycle to:'))
            print(f"freq changed to {freq}")
            
def alertor(freq):
    p.start(50)
    p.ChangeFrequency(freq)
#     for x in range(0,361):      # Make frequency of the alertor consistent with the sine wave 
#         sinVal = math.sin(x * (math.pi / 180.0))        # calculate the sine value
#         toneVal = 2000 + 200   # Add to the resonant frequency with a Weighted
#         p.ChangeFrequency(toneVal)      # Change Frequency of PWM to toneVal
#         time.sleep(0.5)
        
def stopAlertor():
    p.stop()
            
def destroy():
    GPIO.output(buzzerPin, GPIO.LOW)     # Turn off buzzer
    GPIO.cleanup()                       # Release GPIO resource

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()

