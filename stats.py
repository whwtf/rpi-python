#!/usr/bin/python3
# encoding: utf-8

# 用DHT22读取当前环境温度和湿度
# 用12864OLED显示当前日期，时间，IP，CPU，内存，磁盘用量
# DHT22 out 接树莓派 BCM18
# OLED 接 BCM2，BCM3

import time
import Adafruit_DHT
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import subprocess

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

sensor = Adafruit_DHT.DHT22     #定义使用DHT22
pin = 18                        #DHT22 out脚接树莓派BCM18

RST = None                      #I2C接口OLED不使用此引脚
# 使用 128x64 分辨率OLED，接口使用I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()                    #初始化库
disp.clear()                    #清除屏显
disp.display()

# 使用单色模式建立满屏空白图案
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)

draw.rectangle((0, 0, width, height), outline=0, fill=0)

padding = -2
top = padding
bottom = height-padding

x = 0

font = ImageFont.load_default()

# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('Minecraftia.ttf', 8)

while True:

    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    # Shell scripts for system monitoring from here : https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load
    cmd = "hostname -I | cut -d\' \' -f1"
    IPr = subprocess.check_output(cmd, shell=True)
    IP = str(IPr.decode('utf8').strip()).strip('b')     #格式化显示内容，去掉垃圾字符
    cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
    CPUr = subprocess.check_output(cmd, shell=True)
    CPU = str(CPUr.decode('utf8').strip()).strip('b')
    cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.1f%%\", $3,$2,$3*100/$2 }'"
    MemUsager = subprocess.check_output(cmd, shell=True)
    MemUsage = str(MemUsager.decode('utf8').strip()).strip('b')
    cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %.1f/%dGB %s\", $3,$2,$5}'"
    Diskr = subprocess.check_output(cmd, shell=True)
    Disk = str(Diskr.decode('utf8').strip()).strip('b')

    #读取环境温度与湿度
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    #读取当前日期时间并格式化
    timenow = time.strftime('%Y-%m-%d %H:%M',time.localtime(time.time()))

    draw.text((x, top), timenow,  font=font, fill=255)
    draw.text((x, top + 10), "IP: " + IP,  font=font, fill=255)
    draw.text((x, top + 20), CPU, font=font, fill=255)
    draw.text((x, top + 30), MemUsage,  font=font, fill=255)
    draw.text((x, top + 40), Disk,  font=font, fill=255)
    
    if humidity is not None and temperature is not None:
        draw.text((x, top + 50), 'T={0:0.1f}*C  H={1:0.1f}%'.format(temperature, humidity), font=font, fill=255)
    else:
        print('Failed to get reading. Try again!')

    # Display image.
    disp.image(image)
    disp.display()
    time.sleep(10)
