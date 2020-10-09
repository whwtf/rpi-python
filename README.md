# python-learning

首先
````sh
sudo apt-get update
sudo apt-get install python3-pip
sudo python3 -m pip install --upgrade pip setuptools wheel
````
然后安装所需运行支持：
[Adafruit_Python_DHT](https://github.com/whwtf/Adafruit_Python_DHT)，[Adafruit_Python_GPIO](https://github.com/whwtf/Adafruit_Python_GPIO)，[Adafruit_Python_SSD1306](https://github.com/whwtf/Adafruit_Python_SSD1306)，[rpi-TM1638](https://github.com/whwtf/rpi-TM1638.git)。

文件|说明
----|----
[crawl_1.py](https://github.com/whwtf/python-learning/blob/master/crawl_1.py)|用 **Requests** 实现的极简爬虫，批量爬取文本内容并写入 **Text** 文档或插入到 **MySQL** 数据库。
[MySQL-data-type.md](https://github.com/whwtf/python-learning/blob/master/MySQL-data-type.md)|**MySQL** 字段数据类型说明。
[stats.py](https://github.com/whwtf/python-learning/blob/master/crawl_1.py)|使用 **DHT22** 读取环境温度湿度，并使用 **I2C** 接口 **12864OLED** 显示当前 **日期** 、 **时间** 、**IP** 、 **CPU用量** 、 **内存用量** 、 **磁盘用量** 和 **当前温度湿度** 。
[libbeep.py](https://github.com/whwtf/python-learning/blob/master/libbeep.py)|将 **有源蜂鸣器** 鸣响功能模块化。
[beep.py](https://github.com/whwtf/python-learning/blob/master/beep.py)|**libbeep** 引用示例。
[rgb.py](https://github.com/whwtf/python-learning/blob/master/rgb.py)|**RGB LED** 呈现不同颜色的实现方法。
[prtor.py](https://github.com/whwtf/python-learning/blob/master/prtor.py)|**光敏电阻** 应用示例。
[tm1637.py](https://github.com/whwtf/python-learning/blob/master/tm1637.py)|**TM1637** 4位数码管显示模块。
[tm1637Time_Demo.py](https://github.com/whwtf/python-learning/blob/master/tm1637Time_Demo.py)|**TM1637** 数码管显示当前时间。
[dignum](https://github.com/whwtf/python-learning/blob/master/dignum.py)|**TM1637** 数码管显示示例。