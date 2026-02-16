#splash,xrd,screen
#0x0000ff
from apps import *


def TB(splash, xrd, screen):
    import displayio
    from jpegio import JpegDecoder
    splash.scale=2

    decoder = JpegDecoder()
    width, height = decoder.open("/localapps/TB/TB.jpg")
    bitmap = displayio.Bitmap(width, height, 65535)
    decoder.decode(bitmap)
    
    # FIX: Use a ColorConverter to fix the color "swapping" issu
    # This matches the RGB565_SWAPPED output of the jpegio library
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