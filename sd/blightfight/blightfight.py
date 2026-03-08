#splash,xrd,screen
#0xff0000
from apps import*
import displayio
import microcontroller # Import microcontroller module
import time # Import time module
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.rect import Rect
from random import randint, seed # Import seed to potentially ensure consistency if needed



def blightfight(splash,xrd,screen):
    startup(splash)
    
    # Disable auto_refresh to only update when screen.refresh() is called
    screen.auto_refresh = False 
    
    bmp = displayio.Bitmap(60, 60, 10)
    palette = displayio.Palette(10)
    palette[0] =0x000000
    palette[1] =0xff4444
    palette[2] =0xff7f44
    palette[3] =0xffff44
    palette[4] =0x44ff44
    palette[5] =0x44ffff
    palette[6] =0x4444ff
    palette[7] =0x7f44ff
    palette[8] =0xff44ff
    palette[9] =0xffffff
    splash.scale=4
    
    # Create a TileGrid using the Bitmap and Palette
    tile_grid = displayio.TileGrid(bmp, pixel_shader=palette)
    splash.append(tile_grid)
    
    ttimer = 0
    def clamp(n, minn, maxn):
        # Use built-in min/max for clamping
        return max(min(maxn, n), minn)
    
    blig = [[10,10,1],[30,6,2],[50,10,3],[6,30,8],[30,30,9],[54,30,4],[10,50,7],[30,54,6],[50,50,5]]
    
    while True:
        # Clear the bitmap using the faster C-implemented fill method
        bmp.fill(0) 
        for i in range(10):
        # Optimize the inner loops
            for p in blig:
                # Move bounds checking outside the inner loop
                x = clamp(p[0], 0, 59)
                y = clamp(p[1], 0, 59)
                color_index = p[2]
                if bmp[x, y] in [0, color_index]:
                    bmp[x, y] = color_index
                
                # Simplified collision check
                p[0],p[1]=clamp(p[0],0,59),clamp(p[1],0,59)
                if not bmp[p[0],p[1]] in [0,p[2]]:
                    blig.remove(p)
                bmp[x, y] = color_index
                # else: the point is effectively removed from blig for the next frame
                
                # Reproduction (no change needed here, as it's already using randint)
                if 1 == randint(0, 100):
                    blig.append(p)


                # Movement logic (no change needed)
                D = randint(0, 3)
                if D == 0: p[0] += 1
                elif D == 1: p[0] -= 1
                elif D == 2: p[1] += 1
                elif D == 3: p[1] -= 1
            
        
        # Manually refresh the display after all changes are made
        screen.refresh()

        # Handle user input with a short sleep to yield to background tasks
        if xrd.is_touched():
            blig = [[10,10,1],[30,6,2],[50,10,3],[6,30,8],[30,30,9],[54,30,4],[10,50,7],[30,54,6],[50,50,5]]
            screen.refresh()
            print(0)
        
        # Original ttimer logic can stay, but maybe add a small sleep in the loop if needed for stability
        # time.sleep(0.01) # Optional: add a tiny sleep if the board struggles or for consistent timing
        
        if xrd.is_touched():
            ttimer+=1
        elif ttimer > 0:
                ttimer-=1
        if ttimer >2:
            supervisor.reload()

