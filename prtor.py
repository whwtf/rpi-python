#!/usr/bin/python3
# encoding: utf-8

# 光敏电阻应用
# 遮挡LED亮，放开LED灭

import RPi.GPIO as GPIO
import time

prtin = 25
ledout = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(prtin, GPIO.IN)
GPIO.setup(ledout, GPIO.OUT)

GPIO.output(ledout, GPIO.LOW)
while True:
    if GPIO.input(prtin) == 1:           # 被遮挡
        GPIO.output(ledout, GPIO.HIGH)   # LED亮
    else:
        GPIO.output(ledout, GPIO.LOW)
    time.sleep(0.01)

