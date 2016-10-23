#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'zjbao123'
import json
import urllib2
from PIL import Image,ImageDraw,ImageFont

def weather():
    # 获取每日天气数据
    try:
        url = 'http://api.map.baidu.com/telematics/v3/weather?location=%E6%9D%AD%E5%B7%9E&output=json&ak=KPGX6sBfBZvz8NlDN5mXDNBF&callback='
        s=json.loads(urllib2.urlopen(url).read())
        s1 = s["results"][0]["weather_data"][0]["temperature"]
        s2 = s["results"][0]["weather_data"][0]["weather"]
        # print s["results"][0]["currentCity"]
        # print s["results"][0]["weather_data"][0]["temperature"]
        # print s["results"][0]["weather_data"][0]["weather"]
        return s1,s2
    except :
        print"error"
def draw_pic(l):
    img = Image.open('test.jpg')
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype(u'C:/windows/fonts/逼格锐线体简4.0 (2).TTF', size=50) #字体自己改
    draw.text((img.size[0]/6,img.size[1]/5),unicode(l[0]),font=myfont, fill = (0,177,106))
    draw.text((img.size[0]/3,img.size[1]/5+150),unicode(l[1]),font=myfont, fill = (0,128,131))
    img.save('2.jpg','jpeg')
    print 'ok'

draw_pic(weather())