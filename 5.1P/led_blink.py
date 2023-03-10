import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

led_pin = 4

GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(0.25)
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(0.25)
except KeyboardInterrupt:
    GPIO.cleanup()