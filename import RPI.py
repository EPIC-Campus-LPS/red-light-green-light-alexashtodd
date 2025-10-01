#!/usr/bin/python
import RPi.GPIO as GPIO
import time
from datetime import datetime
moving = 0
pdistance = 0

print("time,cm")
while True: 
    try:
        GPIO.setmode(GPIO.BOARD)

        PIN_TRIGGER = 7
        PIN_ECHO = 11
        pin23 = 16
        pin24= 18

        GPIO.setup(PIN_TRIGGER, GPIO.OUT)
        GPIO.setup(PIN_ECHO, GPIO.IN)
        GPIO.setup(pin23, GPIO.OUT)
        GPIO.setup(pin24, GPIO.OUT)

        GPIO.output(PIN_TRIGGER, GPIO.LOW)

        time.sleep(1)
        current_time = datetime.now()

        GPIO.output(PIN_TRIGGER, GPIO.HIGH)

        time.sleep(0.00001)

        GPIO.output(PIN_TRIGGER, GPIO.LOW)

        while GPIO.input(PIN_ECHO)==0:
                pulse_start_time = time.time()
        while GPIO.input(PIN_ECHO)==1:
                pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time
        distance = round(pulse_duration * 17150, 2)

        # Print time and distance in centimeters
        dt = current_time.strftime("%H:%M:%S")
        print (f"{dt},{distance}")

        moving = abs(distance - pdistance)
        pdistance = distance
        print(moving)
        if (moving >= 1):
              ##green
                print("g")
                GPIO.output(pin23, GPIO.HIGH)
        else:
              GPIO.output(pin23, GPIO.LOW)

        if(moving < 1):
              ##red
              print("r")
              GPIO.output(pin24, GPIO.HIGH)
        else:
              GPIO.output(pin24, GPIO.LOW)

        time.sleep(1)
    finally:
        GPIO.cleanup()

