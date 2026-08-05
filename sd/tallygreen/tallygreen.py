#splash,xrd,screen
#0xff00ff
#300
from apps import *

#goob
def tallygreen(splash, xrd, screen):
    import displayio
    from jpegio import JpegDecoder
    startup(splash)
    splash.scale=4
    decoder = JpegDecoder()
    width, height = decoder.open("/sd/tallygreen/tallygreen.jpg")
    bitmap = displayio.Bitmap(width, height, 65535)
    decoder.decode(bitmap)
    
    shader = displayio.ColorConverter(input_colorspace=displayio.Colorspace.RGB565_SWAPPED)
    
    tile_grid = displayio.TileGrid(bitmap, pixel_shader=shader)
    splash.append(tile_grid)
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