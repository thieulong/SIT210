import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

led = 4

GPIO.setup(led, GPIO.OUT)
GPIO.output(led, GPIO.LOW)

def LED_off():
    GPIO.output(led, GPIO.LOW)

def dit_flash():
    GPIO.output(led, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(led, GPIO.LOW)

def dah_flash():
    GPIO.output(led, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(led, GPIO.LOW)

def intra_delay():
    time.sleep(0.1)

def inter_delay():
    time.sleep(0.3)

def space_delay():
    time.sleep(0.7)

def morse_flash(morse_code):
    for symbol in morse_code:
        if symbol == "/":
            space_delay()
        if symbol == " ":
            inter_delay()
        if symbol == ".":
            dit_flash()
            intra_delay()
        if symbol == "/":
            dah_flash()
            intra_delay()


