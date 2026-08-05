import board
import displayio
from time import sleep
import time
import busio
import vectorio
from adafruit_pcf8563.pcf8563 import PCF8563
from math import radians as rad
from math import cos,sin,sqrt,floor
from CircuitPython_XiaoRoundDisplay import XiaoRoundDisplay 
from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.arc import Arc
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.roundrect import RoundRect
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.filled_polygon import FilledPolygon
from adafruit_display_shapes.line import Line
import terminalio
import microcontroller 
from adafruit_display_text import label
import os
import storage
import adafruit_sdcard
import digitalio

import supervisor
supervisor.runtime.autoreload = False
def dist(p1,p2):
        dist = sqrt( (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 )
        return(dist)



displayio.release_displays()
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
i2c = busio.I2C(board.SCL, board.SDA)





rtc = PCF8563(i2c)
xrd = XiaoRoundDisplay(i2c, spi, 90)
screen = xrd.display() 
screen.auto_refresh = False



splash = displayio.Group()
screen.root_group = splash


hourc = Circle(110, 110, 10, fill=0xaa00ff)
splash.append(hourc)
screen.refresh()

runapp = ""

if runapp != "":
    exec("from localapps."+runapp+"."+runapp+" import "+runapp+"")
    exec(runapp+"(splash,xrd,screen)")

cs = digitalio.DigitalInOut(board.D2)
try:
    
    sdcard = adafruit_sdcard.SDCard(spi, cs, baudrate=400000)
    vfs = storage.VfsFat(sdcard)
    storage.mount(vfs, '/sd')
    print("SD Card mounted:", os.listdir('/sd'))
except Exception as e:
    print("SD Error:", e)

if True:
    xiic = Circle(120,11, 10, outline = 0xffffff)
    splash.append(xiic)
    screen.refresh()
    
    xiit = label.Label(terminalio.FONT, text="12", color=0xffffff,x=115,y=10)
    splash.append(xiit)
    screen.refresh()

    vic = Circle(120,229, 10, outline = 0xffffff)
    splash.append(vic)
    screen.refresh()
    vit = label.Label(terminalio.FONT, text="6", color=0xffffff,x=118,y=230)
    splash.append(vit)
    screen.refresh()

    iiic = Circle(229,120, 10, outline = 0xffffff)
    splash.append(iiic)
    screen.refresh()
    iiit = label.Label(terminalio.FONT, text="3", color=0xffffff,x=228,y=120)
    splash.append(iiit)
    screen.refresh()

    ixc = Circle(11,119, 10, outline = 0xffffff)
    splash.append(ixc)
    screen.refresh()
    ixt = label.Label(terminalio.FONT, text="9", color=0xffffff,x=9,y=119)
    splash.append(ixt)
    screen.refresh()

    ic = Circle(174,24, 10, outline = 0xffffff)
    splash.append(ic)
    screen.refresh()
    it = label.Label(terminalio.FONT, text="1", color=0xffffff,x=172,y=24)
    splash.append(it)
    screen.refresh()

    iic = Circle(214,64, 10, outline = 0xffffff)
    splash.append(iic)
    screen.refresh()
    iit = label.Label(terminalio.FONT, text="2", color=0xffffff,x=212,y=64)
    splash.append(iit)
    screen.refresh()

    ivc = Circle(214,173, 10, outline = 0xffffff)
    splash.append(ivc)
    screen.refresh()
    ivt = label.Label(terminalio.FONT, text="4", color=0xffffff,x=212,y=173)
    splash.append(ivt)
    screen.refresh()

    vc = Circle(174,213, 10, outline = 0xffffff)
    splash.append(vc)
    screen.refresh()
    vt = label.Label(terminalio.FONT, text="5", color=0xffffff,x=172,y=213)
    splash.append(vt)
    screen.refresh()

    viic = Circle(65,213, 10, outline = 0xffffff)
    splash.append(viic)
    screen.refresh()
    viit = label.Label(terminalio.FONT, text="7", color=0xffffff,x=63,y=213)
    splash.append(viit)
    screen.refresh()

    viiic = Circle(25,173, 10, outline = 0xffffff)
    splash.append(viiic)
    screen.refresh()
    viiit = label.Label(terminalio.FONT, text="8", color=0xffffff,x=23,y=173)
    splash.append(viiit)
    screen.refresh()

    xc = Circle(25,64, 10, outline = 0xffffff)
    splash.append(xc)
    screen.refresh()
    xt = label.Label(terminalio.FONT, text="10", color=0xffffff,x=20,y=64)
    splash.append(xt)
    screen.refresh()

    xic = Circle(65,24, 10, outline = 0xffffff)
    splash.append(xic)
    screen.refresh()
    xit = label.Label(terminalio.FONT, text="11", color=0xffffff,x=60,y=24)
    splash.append(xit)
    screen.refresh()

secc = Circle(110, 110, 10, fill=0xffa0ff)
splash.append(secc)

minc = Circle(110, 110, 10, fill=0x00ffff)
splash.append(minc)

circle2 = Circle(120, 120, 10, fill=0xffffff)
splash.append(circle2)
###


if 0==1:
    t = time.struct_time((2026, 4, 11, 9, 19, 30, 1, -1, -1))
    rtc.datetime = t
    
seca=0
mina=1
houra =0
hour = 0
splash.scale=1
mint = label.Label(terminalio.FONT, text="goob", color=0x0000ff,x=115,y=10)
mintxp = label.Label(terminalio.FONT, text="goob", color=0x0000ff,x=115,y=10)
splash.append(mint)
splash.append(mintxp)
while True:
    
    try:
        t = rtc.datetime
        circle2.fill = 0xffffff
    except:
        circle2.fill = 0xff0000
        from random import randint as ran
        t = time.struct_time((0, 0, 0, ran(0,23), ran(0,59), ran(0,59), 0, 0,0))
    seca = (t.tm_sec/60*360)-90
    seca +=1
    secc.x = int(110+cos(rad(seca))*60)
    secc.y = int(110+sin(rad(seca))*60)
    secc.fill = (0xffb0ff,0xff90ff)[int(t.tm_sec)%2]
    mina = (((t.tm_min/60)*360))-90
    minc.x = int(110+cos(rad(mina))*85)
    minc.y = int(110+sin(rad(mina))*85)
    smin = str(t.tm_min-(floor((t.tm_min)/5)*5))
    mint.x ,mint.y = minc.x+5+[0,3][len(smin)-2],minc.y+10
    mint.text = smin
    mintxp.x ,mintxp.y = minc.x+6+[0,3][len(smin)-2],minc.y+10
    mintxp.text = smin
    hour = t.tm_hour
    if hour >12:
        hour -= 12
    houra = (((t.tm_hour/12)*360))-90
    #houra += 5

    hourc.x = int(110+cos(rad(houra))*109)
    hourc.y = int(110+sin(rad(houra))*109)
    screen.refresh()
    prespuf=0
    cpos=0
    if xrd.is_touched():
        nowt= xrd.touch_read()
        if isinstance(nowt, tuple):
            if dist(nowt,(120,120)) < 40: 
                from apps import *
                launcher(splash,xrd,screen)
    touch = int(xrd.is_touched())