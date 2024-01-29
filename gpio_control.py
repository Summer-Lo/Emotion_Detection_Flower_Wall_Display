#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

led_1 = 27
led_2 = 17
led_3 = 22
led_4 = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_1, GPIO.OUT)
GPIO.setup(led_2, GPIO.OUT)
GPIO.setup(led_3, GPIO.OUT)
GPIO.setup(led_4, GPIO.OUT)
GPIO.output(led_1,GPIO.LOW)
GPIO.output(led_2,GPIO.LOW)
GPIO.output(led_3,GPIO.LOW)
GPIO.output(led_4,GPIO.LOW)


if __name__ == '__main__':
    try:
        while True:
            GPIO.output(led_1,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(led_2,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(led_3,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(led_4,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(led_1,GPIO.LOW)
            time.sleep(1)
            GPIO.output(led_2,GPIO.LOW)
            time.sleep(1)
            GPIO.output(led_3,GPIO.LOW)
            time.sleep(1)
            GPIO.output(led_4,GPIO.LOW)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExit Now! and Clearn up all GPIO")
        GPIO.cleanup()
