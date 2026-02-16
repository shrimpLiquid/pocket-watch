import supervisor
import bitmaptools
import os
from time import sleep
#appslist=[('blightfight','splash,xrd,screen',"0xff0000"),("app","splash,xrd,screen","0x00ff00")]
direct = os.listdir("localapps")
apps=len(direct)
def listapps(num):
    direct = os.listdir("localapps")
    appslist = []
    for f in direct:
            file = open("localapps/"+f+"/"+f+".py")
            lines = file.readlines()  
            appslist.append((str(f).replace(".py","").replace("'","").replace("[","").replace("]",""),str(lines[0]).strip("#\n"),str(lines[1]).strip("#\n")))#sdhkasjzh
    #print(appslist[num])
    return(appslist[num])
def startup(splash):
    while len(splash) > 0: 
        splash.pop()

def launcher(splash,xrd,screen):
    sleep(2)
    from adafruit_display_shapes.circle import Circle
    from math import cos,sin,radians,sqrt
    def dist(p1,p2):
        dist = sqrt( (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 )
        return(dist)
    startup(splash)
    splash.append(Circle(120, 120, 30, fill=0xffffff))
    for i in range(apps):
        angle = radians(((360/apps)*i)-90)
        print(str(listapps(i)[0]+"circ=Circle("+str(int(cos(angle)*100)+120)+","+str(int(sin(angle)*100)+120)+",15,fill="+listapps(i)[2]+")"))
        exec(str(listapps(i)[0]+"circ=Circle("+str(int(cos(angle)*100)+120)+","+str(int(sin(angle)*100)+120)+",15,fill="+listapps(i)[2]+")"))
        exec("splash.append("+listapps(i)[0]+"circ)")
    
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
                        print("from localapps."+listapps(i)[0]+"."+listapps(i)[0]+" import "+listapps(i)[0])
                        exec("from localapps."+listapps(i)[0]+"."+listapps(i)[0]+" import "+listapps(i)[0])
                        exec(listapps(i)[0]+"("+listapps(i)[1]+")")
            

        screen.refresh()
    
    




        """
from localapps.indev.indev import indev
from localapps.blightfight.blightfight import blightfight
"""