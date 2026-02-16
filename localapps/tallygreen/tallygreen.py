#splash,xrd,screen
#0x888888
from apps import *


def tallygreen(splash,xrd,screen):
    import displayio
    startup(splash)
    splash.scale=2
    bitmap_file = open("localapps/tallygreen/tallygreen.bmp", "rb")
    on_disk_bitmap = displayio.OnDiskBitmap(bitmap_file)
    tile_grid = displayio.TileGrid(on_disk_bitmap, pixel_shader=on_disk_bitmap.pixel_shader)
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