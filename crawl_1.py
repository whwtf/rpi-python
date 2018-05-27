# -*- coding:utf-8 -*-
# 引用re库，用于正则表达式
import re
# 响应HTTP请求
import requests
# MySQL驱动
import mysql.connector

# 定义函数，用参数arcitle_url传递文章地址，返回文章内容
def get_novel_content(arcitle_url):
    # 获取目标网页内容
    response = requests.get(arcitle_url)
    # 定义获取内容的编码
    response.encoding = 'utf-8'
    # 内容赋予变量html
    html = response.text
    # 获取文章内容文本
    arcitle_content = re.findall(r'<div class="tpc_content" id="read_tpc">(.*?)</div>', html, re.S)[0]
    # 内容去空格
    arcitle_content = arcitle_content.strip()
    # 内容去垃圾字符，将不需要的用无内容替换
    arcitle_content = arcitle_content.replace('&nbsp;', '')
    arcitle_content = arcitle_content.replace('<br>', '')
    # 返回结果
    return arcitle_content

# 定义函数，取得列表页文章类别，标题，url
def get_novel_info(list_url):
    response = requests.get(list_url)
    response.encoding = 'utf-8'
    html = response.text
    article_info = re.findall(r'>\[(.*?)\]</a> <h3><a href="htm_(.*?)" id="a_ajax_.*?">\[.*?\] (.*?)</a>', html, re.S)
    return article_info

# 定义函数，将内容写入text文件
def write_to_text(max_page):
    # 以写入方式，utf-8编码建立并打开novel.txt文件
    fb = open('novel.txt', 'w', encoding= 'utf-8')
    page = 1
    while page <= max_page:
        addr_list = 'http://www.????.com/thread.php?id=??&page=%s' % page
        ninfos = get_arcitle_info(addr_list)
        for ninfo in ninfos:
            ncontent = get_article_content('http://www.????.com/pw/htm_%s' % ninfo[1])
            # 写入内容
            fb.write(ninfo[0])
            fb.write('\n')
            fb.write(ninfo[2])
            fb.write('\n')
            fb.write(ncontent)
            fb.write('\n')
            fb.write('\n')
        page = page + 1
    fb.close()
    return

def insert_to_db(max_page):
    page = 1
    # 连接数据库
    conn = mysql.connector.connect(user='python', password='1234', database='python')
    cursor = conn.cursor()
    # 建立article表
    cursor.execute('create table article (id int(20) auto_increment primary key, type varchar(45), title varchar(45), content mediumtex)')
    while page <= max_page:
        addr_list = 'http://www.????.com/thread.php?id=??&page=%s' % page
        ninfos = get_article_info(addr_list)
        # 处理取得内容，以防超出表容量
        for ninfo in ninfos:
            if len(ninfo[0]) > 8:
                ntype = 'ABCD'
            else:
                ntype = ninfo[0]                
            ncontent = get_article_content('http://www.????.com/pw/htm_%s' % ninfo[1])
            # 插入内容
            cursor.execute('insert into article (type, title, content) values (%s, %s, %s)', [ntype, ninfo[2], ncontent])
            # 提交查询
            conn.commit()
        page = page + 1
    # 关闭数据库
    cursor.close()
    return
# 写入文件
write_to_text(10)
# 插入数据库
insert_to_db(10)
