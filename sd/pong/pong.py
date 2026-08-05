#splash,xrd,screen
#0xffff00
#60
from apps import *

def pong(splash, xrd, screen):
    import displayio
    from time import monotonic as millis
    from time import sleep
    from math import cos,sin,atan2,sqrt,radians
    from math import degrees as deg
    from random import randint as rand
    from adafruit_display_shapes.arc import Arc
    from adafruit_display_shapes.circle import Circle
    
    def dist(p1,p2):
        return sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
    
    def gle(p1, p2):
        return deg(atan2(p1[1] - p2[1], p2[0] - p1[0]))

    startup(splash)
    arc1 = Arc(x=120,y=120,radius=120,angle=45,direction=0,segments=3,arc_width=2,fill=0xffffff)
    splash.append(arc1)
    ball = Circle(120, 120, r=8, fill=0xffffff)
    splash.append(ball)
    screen.auto_refresh = True
    a = 0
    ballx, bally = 120.0, 120.0
    pt = millis()
    nowt = (0,0)
    d = 0
    
    while True:
        if xrd.is_touched():
            nowt = xrd.touch_read()
            if isinstance(nowt, tuple):
                touch_angle = gle((120, 120), nowt)-180+22
                arc1.direction = touch_angle - (arc1.angle / 2)

        if nowt != (0,0):
            
            dt = (millis() - pt)
            ballx += (cos(a)) * dt * 150
            bally += (sin(a)) * dt * 150
            pt = millis()
        else:
            pt = millis()

        ball.x, ball.y = int(ballx)-8, int(bally)-8
        
        
        ball_angle = gle((120, 120), (ballx, bally))
        touch_angle = arc1.direction + (arc1.angle / 2)
        diff = (ball_angle - touch_angle + 180) % 360 - 180

        if dist((ballx, bally), (120, 120)) > 110:
            if abs(diff) < 25: 
                if d == 0:
                    norm = atan2(bally - 120, ballx - 120)
                    a = 2 * norm - a + 3.14159
                    a += radians(rand(-10, 10))
                    ballx = 120 + cos(norm) * 104
                    bally = 120 + sin(norm) * 104
                    d = 1
            else: 
                ball.fill = 0xff8800
                sleep(0.5)
                ballx, bally = 120, 120
                nowt = (0,0)
                a = 0
                d = 0
                ball.fill = 0xffffff
        else:
            d = 0