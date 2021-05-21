import RPi.GPIO as GPIO 
 
buzzerPin = 24    # define buzzerPin 
buttonPin = 12    # define buttonPin 

def setup(): 
  GPIO.setmode(GPIO.BCM)        # use Broadcom SOC GPIO Numbering 
  GPIO.setup(buzzerPin, GPIO.OUT)   # set buzzerPin to OUTPUT mode 
  GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    # set buttonPin to PULL DOWN INPUT mode 

def loop(): 
  while True: 
    if GPIO.input(buttonPin)==GPIO.HIGH: # if button is pressed 
      GPIO.output(buzzerPin,GPIO.HIGH) # turn on buzzer 
#       print ('buzzer turned on >>>') 
    else : # if button is relessed 
      GPIO.output(buzzerPin,GPIO.LOW) # turn off buzzer 
#       print ('buzzer turned off <<<') 

def destroy(): 
  GPIO.cleanup()                     # Release all GPIO 

if __name__ == '__main__':     # Program entrance 
    print ('Program is starting...') 
    setup() 
    try: 
        loop() 
    except KeyboardInterrupt:  # Press ctrl-c to end the program. 
        destroy()
