#splash,xrd,screen
#0xff00ff
from apps import *

#goob
def pong(splash, xrd, screen):
    import displayio
    from math import cos,sin,atan2
    from math import degrees as deg
    from adafruit_display_shapes.arc import Arc
    from adafruit_display_shapes.circle import Circle
    

    def gle(p1, p2):
        xDiff = p2[0] - p1[0]
        yDiff = p2[1] - p1[1]
        return deg(atan2(-1*yDiff, xDiff))
    def gler(p1, p2):
        xDiff = p2[0] - p1[0]
        yDiff = p2[1] - p1[1]
        return deg(atan2(-1*yDiff, xDiff))
    startup(splash)
    arc1 = Arc(x=120,y=120,radius=120,angle=45,direction=90,segments=20,arc_width=5,fill=0xffffff)
    splash.append(arc1)
    ball = Circle(120, 120, 10, fill=0xffffff)
    splash.append(ball)
    screen.auto_refresh = True 
    a = 0
    nowt = (100,0)
    while True:
        if xrd.is_touched():
            nowt= xrd.touch_read()
            if isinstance(nowt, tuple):
                arc1.direction=gle((120,120),nowt)
        a = gler((120,120),nowt)
        
        
                
    
    
    
    
    
    
    
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