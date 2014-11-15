#!/usr/bin/python
#coding=utf-8
#Filename:hust_lib.py
import urllib
import urllib.request
import re
def get(url):
    data=urllib.request.urlopen(url).read().decode('utf-8')
    about=[]
    about=re.compile(r'<span class="briefcitTitle">\n<a href=.*?">(.*?) / (.*?)</a>\n</span>\n<br />\n<span class="briefcitDetail">\n(.*?)\n<br />\n<span class="briefcitDetail">\n(.*?)<br />\n<br />\n<span class="briefcitDetail">\n(.*?)<br />',re.S).findall(data)
    if about==[]:
        print('未找到')
    return (about)
def show(url):
    for i in range(0,len(get(url))):
        print(get(url)[i])
def next(url):
    ndata=urllib.request.urlopen(url).read().decode('utf-8')
    if re.search('后一页',ndata):
        nurl=re.compile(r'<a href="(.*?)">后一页</a>').findall(ndata)
        url='http://ftp.lib.hust.edu.cn/'+nurl[0]
        z=input('有后一页，按y/Y进入后一页，按n/N退出\n请输入==>')
        if z=='y' or z=='Y':
            show(url)
            next(url)
    else:
        print('当前页为最后一页\n')
key=input("请输入关键词==>")
url="http://ftp.lib.hust.edu.cn/search*chx/X?SEARCH="+urllib.parse.quote(key)
show(url)
next(url)
