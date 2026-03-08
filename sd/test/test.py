#splash,xrd,screen
#0x00ff00
from apps import *
def test(splash,xrd,screen):
    startup(splash)
    from adafruit_display_shapes.circle import Circle
    splash.append(Circle(120, 120, 10, fill=0xffffff))
    ttimer = 0
    while True:
        if xrd.is_touched():
            ttimer+=1
        elif ttimer > 0:
            ttimer-=1
        print(ttimer)
        if ttimer >200:
            supervisor.reload()
        screen.refresh()