#!/usr/bin/python3
# encoding: utf-8

import RPi.GPIO as GPIO
import time
import libbeep

while True:
    t = time.localtime()
    h = t.tm_hour
    m = t.tm_min
    s = t.tm_sec
    w = time.strftime('%w', t)
    #print (h, m, s, w)
    time.sleep(0.3)

    if m == 0 and s == 0:
        if h > 22 or h < 8:  # 为了晚上22点之后，上午8点之前不被打扰，设定了条件 print "continued" continue if h>12:
            h = h-12
        libbeep.beepAction(0.3, 0.5, h)
        time.sleep(1)

    if m == 30 and s == 0:
        if h > 22 or h < 8:
            print("continued")
            continue
        libbeep.beepAction(0.05, 0.05, 2)
        time.sleep(1)
