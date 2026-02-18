#splash,xrd,screen
#0xff00ff
from apps import *

#goob
def pong(splash, xrd, screen):
    import displayio
    from time import monotonic as millis
    from math import cos,sin,atan2,sqrt,radians
    from math import degrees as deg
    from random import randint as rand
    from adafruit_display_shapes.arc import Arc
    from adafruit_display_shapes.circle import Circle
    def dist(p1,p2):
        dist = sqrt( (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 )
        return(dist)
    def gle(p1, p2):
        xDiff = p2[0] - p1[0]
        yDiff = p2[1] - p1[1]
        return deg(atan2(-1*yDiff, xDiff))
    def gler(p1, p2):
        xDiff = p2[0] - p1[0]
        yDiff = p2[1] - p1[1]
        return atan2(yDiff, xDiff)
    startup(splash)
    arc1 = Arc(x=120,y=120,radius=120,angle=45,direction=90,segments=2,arc_width=5,fill=0xffffff)
    splash.append(arc1)
    ball = Circle(120, 120, 10, fill=0xffffff)
    splash.append(ball)
    screen.auto_refresh = True 
    a = 0
    ballx,bally=120,130
    pt = 0
    dt = 1
    nowt = (0,0)
    d = 0
    while True:
        if xrd.is_touched():
            nowt= xrd.touch_read()
        if isinstance(nowt, tuple):
                arc1.direction=gle((120,120),nowt)
        if not nowt == (0,0):
            ballx += (cos(a))*dt*0.4
            bally += (sin(a))*dt*0.4
        
        ball.x ,ball.y = int(ballx),int(bally)
        if dist((ballx, bally), (120, 120)) > 110:
            if d == 0:
                norm = atan2(bally - 120, ballx - 120)
                
                a = 2 * norm - a + 3.14159
                
                ballx = 120 + cos(norm) * 108
                bally = 120 + sin(norm) * 108
                
                d = 1
        else:
            d = 0

        dt = (millis()-pt)*1000
        pt = millis()


        
        
                
    
    
    
    
    
    
    
    # ttimer = 0
    # while True:
    #     if xrd.is_touched():
    #         ttimer+=1
    #     elif ttimer > 0:
    #         ttimer-=1
    #     print(ttimer)
    #     if ttimer >200:
    #         supervisor.reload()
    #     screen.refresh()