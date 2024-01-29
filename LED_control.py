#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

# LED Pin Assignment
led_1 = 17      # Pin no 11
led_2 = 27      # Pin no 13
led_3 = 22      # Pin no 15
led_4 = 23      # Pin no 16
led_5 = 24      # Pin no 18 
led_6 = 25      # Pin no 22
led_7 = 5       # Pin no 29
led_8 = 6       # Pin no 31

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_1, GPIO.OUT)
GPIO.setup(led_2, GPIO.OUT)
GPIO.setup(led_3, GPIO.OUT)
GPIO.setup(led_4, GPIO.OUT)
GPIO.setup(led_5, GPIO.OUT)
GPIO.setup(led_6, GPIO.OUT)
GPIO.setup(led_7, GPIO.OUT)
GPIO.setup(led_8, GPIO.OUT)

# GPIO default status
GPIO.output(led_1,GPIO.LOW)
GPIO.output(led_2,GPIO.LOW)
GPIO.output(led_3,GPIO.LOW)
GPIO.output(led_4,GPIO.LOW)
GPIO.output(led_5,GPIO.LOW)
GPIO.output(led_6,GPIO.LOW)
GPIO.output(led_7,GPIO.LOW)
GPIO.output(led_8,GPIO.LOW)

# Variables
emotions = ["anger","contempt","disgust","fear","happy","neutral","sad","surprise"]
led_emo = [led_1,led_2,led_3,led_4,led_5,led_6,led_7,led_8]
on_status = 0

def on_led(emotion, second):
    global on_status
    done = False
    if on_status == 1:
        print("LED busy now!")
        done = False
        return done
    else:
        if emotion in emotions:
            on_status = 1
            index = emotions.index(str(emotion))
            GPIO.output(led_emo[index],GPIO.HIGH)
            time.sleep(second)
            GPIO.output(led_emo[index],GPIO.LOW)
            on_status = 0
            print("LED is free now!")
            done = True
            return done


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
            GPIO.output(led_5,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(led_6,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(led_7,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(led_8,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(led_1,GPIO.LOW)
            time.sleep(1)
            GPIO.output(led_2,GPIO.LOW)
            time.sleep(1)
            GPIO.output(led_3,GPIO.LOW)
            time.sleep(1)
            GPIO.output(led_4,GPIO.LOW)
            time.sleep(1)
            GPIO.output(led_5,GPIO.LOW)
            time.sleep(1)
            GPIO.output(led_6,GPIO.LOW)
            time.sleep(1)
            GPIO.output(led_7,GPIO.LOW)
            time.sleep(1)
            GPIO.output(led_8,GPIO.LOW)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExit Now! and Clearn up all GPIO")
        GPIO.cleanup()

