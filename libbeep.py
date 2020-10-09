#!/usr/bin/python3
# encoding: utf-8

# 将有源蜂鸣器鸣响功能模块化，引用方法：
# import libbeep
# libbeep.beep(名叫时长)
# libbeep.beepAction(时长, 间隔时长, 重复次数)

import RPi.GPIO as GPIO
import time

PIN_NO = 23  # GPIO编号，可自定义

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_NO, GPIO.OUT)

#哔1次，时长作为参数传递
def beep(seconds):
    GPIO.output(PIN_NO, GPIO.HIGH)
    time.sleep(seconds)
    GPIO.output(PIN_NO, GPIO.LOW)

#哔N次，时长、间隔时长、重复次数作为参数传递
def beepAction(secs, sleepsecs, times):
    for i in range(times):
        beep(secs)
        time.sleep(sleepsecs)


#beepAction(0.02, 0.02, 30)
