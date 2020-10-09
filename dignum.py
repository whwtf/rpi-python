#!/usr/bin/env python
# tm1637 test
# show cur timer

import tm1637
import RPi.GPIO as GPIO
import time

CLK = 21
DATA  = 20
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

d = tm1637.TM1637(CLK, DATA)
d.showDoublePoint(1)    # 显示中间两个点
d.showData([5,6,7,9])   # 显示内容


GPIO.cleanup()
