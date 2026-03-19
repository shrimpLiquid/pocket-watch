import supervisor
import bitmaptools
import os
from time import sleep
import sys
from adafruit_display_shapes.filled_polygon import FilledPolygon
sys.path.append("/sd")

global apps
apps = 0
def listapps(num):
    global apps
    print

    direct = [f for f in os.listdir("/sd") if f != "System Volume Information" and not f.startswith(".")]
    apps = len(direct)
    
    f = direct[num]
    

    with open("/sd/"+f+"/"+f+".py", "r") as file:
        lines = file.readlines()
        name = str(f)
        args = str(lines[0]).strip("#\n")
        


        color = str(int(lines[1].strip("#\n"), 16))
        return (name, args, color)
def startup(splash):
    while len(splash) > 0: 
        splash.pop()

def launcher(splash,xrd,screen):
    sleep(2)
    listapps(0)
    from adafruit_display_shapes.circle import Circle
    from math import cos,sin,radians,sqrt
    def dist(p1,p2):
        dist = sqrt( (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 )
        return(dist)
    startup(splash)
    
    #splash.append(Circle(120, 120, 15, fill=0xffffff))
    screen.refresh()
    pois = []
    for i in range(apps):
        aiq = listapps(i)
        angle = radians(((360/apps)*i)-90)
        exec(str(aiq[0]+"circ=Circle("+str(int(cos(angle)*100)+120)+","+str(int(sin(angle)*100)+120)+",15,fill="+aiq[2]+")"))
        exec("splash.append("+aiq[0]+"circ)")
        pois.append((int(cos(angle)*40)+120,int(sin(angle)*40)+120))
        screen.refresh()
    polygon = FilledPolygon(pois,fill=0xffffff,outline=0x0,stroke=4)
    splash.append(polygon)
    while True:
        if xrd.is_touched():
            t = (0,1)
            t = xrd.touch_read()
            if t is not None:
                if dist((120,120),t) < 30:
                    supervisor.reload()
        for i in range(apps):
            angle = radians(((360/apps)*i)-90)
            if xrd.is_touched():
                t = (0,0)
                t = xrd.touch_read()
                if t is not None:
                    if dist((int(cos(angle)*100)+120,int(sin(angle)*100)+120),t) < 20:
                        print(i)
                        print("from ."+listapps(i)[0]+"."+listapps(i)[0]+" import "+listapps(i)[0])
                        name = listapps(i)[0]
                        args = listapps(i)[1]
                        exec("import " + name + "." + name + " as m")
                        exec("m." + name + "(" + args + ")")
            

        screen.refresh()
    
    




        """
from .indev.indev import indev
from .blightfight.blightfight import blightfight
"""