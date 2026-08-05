#splash,xrd,screen
#0xff8800
#30
from apps import *

def shrek(splash, xrd, screen):
    import displayio
    from jpegio import JpegDecoder
    splash.scale = 2

    decoder = JpegDecoder()
    # Pre-allocate one bitmap and one tilegrid
    width, height = decoder.open("/sd/video/frames/ezgif-frame-001.jpg")
    bitmap = displayio.Bitmap(width, height, 65535)
    shader = displayio.ColorConverter(input_colorspace=displayio.Colorspace.RGB565_SWAPPED)
    tile_grid = displayio.TileGrid(bitmap, pixel_shader=shader)
    splash.append(tile_grid)

    for i in range(2, 287):
        filename = f"/sd/video/frames/ezgif-frame-{i:03d}.jpg"
        try:
            # Decode directly into the existing bitmap
            decoder.open(filename)
            decoder.decode(bitmap)
            screen.refresh()
        except Exception:
            print(Exception)
            break

    ttimer = 0
    while True:
        if xrd.is_touched():
            ttimer += 1
        elif ttimer > 0:
            ttimer -= 1
        if ttimer > 200:
            supervisor.reload()
        screen.refresh()