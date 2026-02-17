import board
import displayio
from time import sleep
import time
import busio
from apps import *
import vectorio
from adafruit_pcf8563.pcf8563 import PCF8563
from math import radians as rad
from math import cos,sin,sqrt
from CircuitPython_XiaoRoundDisplay import XiaoRoundDisplay # type: ignore
from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.roundrect import RoundRect
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.filled_polygon import FilledPolygon
from adafruit_display_shapes.line import Line
import terminalio
import microcontroller # Import microcontroller modul
from adafruit_display_text import label

def dist(p1,p2):
        dist = sqrt( (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 )
        return(dist)
try:
    microcontroller.cpu.frequency = 200*1000000
    print(":)")
except ValueError:
    print(":(")
    pass

displayio.release_displays()
prespuf = 0
touch = 0
prepos = 0
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
try:
	i2c = busio.I2C(board.SCL, board.SDA)
except:
	import supervisor
	supervisor.reload()
rtc = PCF8563(i2c)
xrd = XiaoRoundDisplay(i2c, spi, 90)
screen = xrd.display()  # Screen object
screen.auto_refresh = False
global splash
splash = displayio.Group()
screen.root_group = splash
hourc = Circle(110, 110, 10, fill=0xaa00ff)
splash.append(hourc)
if True:
	xiic = Circle(120,11, 10, outline=0xffffff)
	splash.append(xiic)
	xiit = label.Label(terminalio.FONT, text="12", color=0xffffff,x=115,y=10)
	splash.append(xiit)

	vic = Circle(120,229, 10, outline=0xffffff)
	splash.append(vic)
	vit = label.Label(terminalio.FONT, text="6", color=0xffffff,x=118,y=230)
	splash.append(vit)

	iiic = Circle(229,120, 10, outline=0xffffff)
	splash.append(iiic)
	iiit = label.Label(terminalio.FONT, text="3", color=0xffffff,x=228,y=120)
	splash.append(iiit)

	ixc = Circle(11,119, 10, outline=0xffffff)
	splash.append(ixc)
	ixt = label.Label(terminalio.FONT, text="9", color=0xffffff,x=9,y=119)
	splash.append(ixt)

	ic = Circle(174,24, 10, outline=0xffffff)
	splash.append(ic)
	it = label.Label(terminalio.FONT, text="1", color=0xffffff,x=172,y=24)
	splash.append(it)

	iic = Circle(214,64, 10, outline=0xffffff)
	splash.append(iic)
	iit = label.Label(terminalio.FONT, text="2", color=0xffffff,x=212,y=64)
	splash.append(iit)

	ivc = Circle(214,173, 10, outline=0xffffff)
	splash.append(ivc)
	ivt = label.Label(terminalio.FONT, text="4", color=0xffffff,x=212,y=173)
	splash.append(ivt)

	vc = Circle(174,213, 10, outline=0xffffff)
	splash.append(vc)
	vt = label.Label(terminalio.FONT, text="5", color=0xffffff,x=172,y=213)
	splash.append(vt)

	viic = Circle(65,213, 10, outline=0xffffff)
	splash.append(viic)
	viit = label.Label(terminalio.FONT, text="7", color=0xffffff,x=63,y=213)
	splash.append(viit)

	viiic = Circle(25,173, 10, outline=0xffffff)
	splash.append(viiic)
	viiit = label.Label(terminalio.FONT, text="8", color=0xffffff,x=23,y=173)
	splash.append(viiit)

	xc = Circle(25,64, 10, outline=0xffffff)
	splash.append(xc)
	xt = label.Label(terminalio.FONT, text="10", color=0xffffff,x=20,y=64)
	splash.append(xt)

	xic = Circle(65,24, 10, outline=0xffffff)
	splash.append(xic)
	xit = label.Label(terminalio.FONT, text="11", color=0xffffff,x=60,y=24)
	splash.append(xit)

secc = Circle(110, 110, 10, fill=0xffa0ff)
splash.append(secc)

minc = Circle(110, 110, 10, fill=0x00ffff)
splash.append(minc)

circle2 = Circle(120, 120, 10, fill=0xffffff)
splash.append(circle2)

if 1==0:
	t = time.struct_time((2026, 2, 14, 16, 41, 30, 1, -1, -1))
	rtc.datetime = t
	
seca=0
mina=1
houra =0
hour = 0
splash.scale=1

while True:
	try:
		t = rtc.datetime
		circle2.fill = 0xffffff
	except:
		circle2.fill = 0xff0000
		t = time.struct_time((0, 0, 0, 0, 0, 0, 0, 0, 0))
	seca = (t.tm_sec/60*360)-90
	seca +=1
	secc.x = int(110+cos(rad(seca))*60)
	secc.y = int(110+sin(rad(seca))*60)
	mina = (((t.tm_min/60)*360))-90
	minc.x = int(110+cos(rad(mina))*85)
	minc.y = int(110+sin(rad(mina))*85)
	hour = t.tm_hour
	if hour >12:
		hour -= 12
	houra = (((t.tm_hour/12)*360))-90
	hourc.x = int(110+cos(rad(houra))*109)
	hourc.y = int(110+sin(rad(houra))*109)
	screen.refresh()
	prespuf=0
	cpos=0
	if xrd.is_touched():
		nowt= xrd.touch_read()
		if isinstance(nowt, tuple):
			if dist(nowt,(120,120)) < 40: 
				launcher(splash,xrd,screen)
	touch = int(xrd.is_touched())