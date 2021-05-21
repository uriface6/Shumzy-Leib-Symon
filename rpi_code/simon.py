import RPi.GPIO as GPIO
from time import sleep
from random import randint
import threading
TIME_TO_SHINE = 0.2
INTERMEDIATE_DELAY = 0.01

buzzerPin = 24

sixteenth = 0.1
triole = 0.4 / 3

led_red = 17
led_grn = 13
led_ylw = 19
led_blu = 26

btn_red = 12
btn_grn = 16
btn_ylw = 20
btn_blu = 21

led_pins = [led_red, led_grn, led_ylw, led_blu]
btn_pins = [btn_red, btn_grn, btn_ylw, btn_blu]
labels = ["red", "green", "yellow", "blue"]
freqs = [261.63, 293.66, 329.63, 392.00, 440.00]

lose_music_1 = [523.25, 392.00, 329.63]
lose_music_2 = [440.00, 493.88, 440.00, 415.30, 466.16, 415.30]
lose_music_3 = [392.00, 329.63, 293.66, 329.63]

start_music = [329.628, 329.628, 329.628, 261.626, 329.628, 391.995, 195.998]

seq = []


def setup():
    GPIO.setmode(GPIO.BCM) # use Broadcom GPIO Numbering
    
    global p
    GPIO.setup(buzzerPin, GPIO.OUT)   # set RGBLED pins to OUTPUT mode
    p = GPIO.PWM(buzzerPin, 1)
    p.start(0)
    p.stop()
    for ledPin in led_pins:        
        GPIO.setup(ledPin, GPIO.OUT) # set the ledPin to OUTPUT mode
        GPIO.output(ledPin, GPIO.LOW) # make ledPin output LOW level
        print ('using pin%d for led'%ledPin)
    for btn_pin in btn_pins:
        GPIO.setup(btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        print ('using pin%d for button'%btn_pin)

def turn_on_led(index):
    GPIO.output(led_pins[index], GPIO.HIGH)
    
    
def turn_off_led(index):
    GPIO.output(led_pins[index], GPIO.LOW)

def flash(index):
    """
    lights up led no. <index> for <TIME_TO_SHINE> seconds.
    
    :param index: index of light in led_pins to shine.
    :returns: None.
    """
    turn_on_led(index)
    start_buzz(index)
    sleep(TIME_TO_SHINE)
    turn_off_led(index)
    stop_buzz()
    sleep(INTERMEDIATE_DELAY)

def add_rnd_light_to_seq():
    print('watch!')
    new_elem = randint(0,3)
    print(f'adding {labels[new_elem]} to list.')
    seq.append(new_elem)
    for elem in seq:
        flash(elem)

def start_buzz(index):
    p.start(1)
    p.ChangeFrequency(freqs[index])


def stop_buzz():
    p.stop()


def start_tune():
    p.stop()
    p.ChangeFrequency(start_music[0])
    p.start(1)
    sleep(2 * sixteenth - 0.05)
    p.stop()
    sleep(0.05)
    p.ChangeFrequency(start_music[1])
    p.start(1)
    sleep(2 * sixteenth)
    p.stop()
    sleep(2 * sixteenth)
    p.start(1)
    p.ChangeFrequency(start_music[2])
    sleep(2 * sixteenth)
    p.stop()
    sleep(2 * sixteenth)
    p.start(1)
    p.ChangeFrequency(start_music[3])
    sleep(2 * sixteenth - 0.05)
    p.stop()
    sleep(0.05)
    p.start(1)
    p.ChangeFrequency(start_music[4])
    sleep(3 * sixteenth)
    p.stop()
    sleep(sixteenth)
    p.start(1)
    p.ChangeFrequency(start_music[5])
    sleep(3 * sixteenth)
    p.stop()
    sleep(5 * sixteenth)
    p.start(1)
    p.ChangeFrequency(start_music[6])
    sleep(4 * sixteenth)
    p.stop()

def play_lose_tune():
    print('in play lose')
    p.stop()
    p.start(1)
    p.ChangeFrequency(lose_music_1[0])
    sleep(sixteenth)
    p.stop()
    sleep(2 * sixteenth)
    p.start(1)
    p.ChangeFrequency(lose_music_1[1])
    sleep(sixteenth)
    p.stop()
    sleep(2 * sixteenth)
    p.start(1)
    p.ChangeFrequency(lose_music_1[2])
    sleep(sixteenth)
    p.stop()
    sleep(sixteenth)
    p.start(1)
    for note in lose_music_2:
        p.ChangeFrequency(note)
        sleep(triole)
    for note in lose_music_3:
        p.ChangeFrequency(note)
        sleep(sixteenth)
    sleep(2 * sixteenth)
    p.stop()

def oscillate(speed: int = 1):
    """
    oscillate between leds, pretty...
    """
    for ledPin in led_pins:
        GPIO.output(ledPin, GPIO.HIGH)
#         print ('led turned on <<<')
        sleep(0.1 / speed)
        GPIO.output(ledPin, GPIO.LOW)
#         print ('led turned off <<<')
        sleep(0.1 / speed)

def oscillate_faster_and_faster():
    speed = 1
    while not threading.current_thread().stopped():
        oscillate(speed)
        speed += 1


def barber_shop_sound():
    x = 0
    p.start(1)
    while not threading.current_thread().stopped():
        toneVal = 300 + x
        p.ChangeFrequency(toneVal) 
        sleep(0.01)
        x += 1
    p.stop()


def input_loop():
    for i, buttonPin in enumerate(btn_pins):
        if GPIO.input(buttonPin)==GPIO.HIGH:
            print("button pressed")
            GPIO.output(led_pins[i], GPIO.HIGH)
            print (f"{labels[i]} led turned on <<<")
            sleep(0.2)
            GPIO.output(led_pins[i], GPIO.LOW)
            print (f'{labels[i]} led turned off <<<')
            sleep(0.2)
        

def check_input():
    for idx, btn_pin in enumerate(btn_pins):
        if GPIO.input(btn_pin) == GPIO.HIGH:
            return idx
    return None

def test_user():
    """
    waits for user to input the sequence
    and checks to see he entered it correctly.
    """
    print('now you!')
    won = True
    for item in seq:
        while(True):
            pressed_index = check_input()
            if pressed_index == item:
                flash(pressed_index)
                break
            elif pressed_index != None:
                flash(pressed_index)
                sleep(0.5)
                t1 = StoppableThread(target=play_lose_tune)
                t2 = StoppableThread(target=flash_all_lights)
                t1.start()
                t2.start()
                t1.join()
                t2.stop()
                t2.join()
                return not won
    return won


class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self,  *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()


def flash_all_lights():
    """
    flashing lights to show user he lost.
    """
    while not threading.current_thread().stopped():
        for idx in range(4):
            turn_on_led(idx)
        sleep(0.1)
        for idx in range(4):
            turn_off_led(idx)
        sleep(0.1)

def update_speed():
    input_index = check_input()
    
    TIME_TO_SHINE /= input_index
    if input_index > 1:
        INTERMEDIATE_DELAY /= 2

def destroy():
    print(">>> cleaning up stuff...")
    GPIO.output(buzzerPin, GPIO.LOW)     # Turn off buzzer
    GPIO.cleanup() # Release all GPIO
    
    
def should_try_again():
    print('try again? \nGrn==yes\nRed==no')
    while(True):
        pressed_index = check_input()
        if pressed_index == 1:
            return True
        elif pressed_index == 0:
            return False
    
if __name__ == "__main__":
    setup()
    start_tune()
#     print("""what speed would you like?
# red = slow
# green = normal
# yellow = fast
# blue = crazy""")
#     #update_speed()
    round = 1
    
    try:
        while(True):
            print(f'round {round}...')
            sleep(1)
            add_rnd_light_to_seq()
            won = test_user()
            if not won:
                print('better luck next time...')
                try_again = should_try_again()
                if try_again:
                    print('resetting...')
                    t1 = StoppableThread(target=start_tune)
                    t1.start()
                    t2 = StoppableThread(target=oscillate_faster_and_faster)
                    t2.start()
                    t1.join()
                    print('t1 joined.')
                    t2.stop()
                    t2.join()
                    round = 1
                    seq = []
                else:
                    break
            print(f'you won round {round}!')
            round += 1
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
    print('bye!')
    destroy()
