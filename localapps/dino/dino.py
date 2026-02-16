#splash,xrd,screen
#0xffff00
from apps import *
def dino(splash,xrd,screen):
    startup(splash)
    import displayio
    from adafruit_display_shapes.circle import Circle
    bitmap_file = open("localapps/dino/dino.bmp", "rb")
    sprite_sheet = displayio.OnDiskBitmap(bitmap_file)

    tile_width = 20
    tile_height = 20
    sprite = displayio.TileGrid(
    sprite_sheet, 
    pixel_shader=sprite_sheet.pixel_shader, 
    width=1, 
    height=1, 
    tile_width=tile_width, 
    tile_height=tile_height
    )
    rex_splash= displayio.Group()
    rex_splash.append(sprite)
    rex_splash.x=150
    rex_splash.y=150
    splash.append(rex_splash)

    sprite[0]=0
    rex=Circle(120, 150, 10, fill=0xffffff)
    state = 0
    splash.append(rex)
    ttimer = 0
    while True:

        print(state)
        if xrd.is_touched() and rex.y == 150:
            state=1
        if state == 1:
            rex.y -= 1
        if rex.y < 100:
            state = 0
        if state == 0 and rex.y < 150:
            rex.y += 1
        if xrd.is_touched():
            ttimer+=1
        elif ttimer > 0:
            ttimer-=1
        if ttimer >400:
            supervisor.reload()
        screen.refresh()