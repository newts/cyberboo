import board
import time
import displayio
import digitalio

#led = digitalio.DigitalInOut(board.LED)
#led.direction = digitalio.Direction.OUTPUT


# Grab the display off the board
display = board.DISPLAY

# Setup the file as the bitmap data source
bitmap = displayio.OnDiskBitmap("/boo.bmp")

# Create a TileGrid to hold the bitmap
tile_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)

# Create a Group to hold the TileGrid
group = displayio.Group()
group.append(tile_grid)

# Add the Group to the Display
display.show(group)

def do_blink():
    group.y = 0
    time.sleep(0.2)
    group.y = -64
    time.sleep(0.2)
    group.y = -128
    time.sleep(0.2)
    group.y = -192
    time.sleep(0.2)
    group.y = -256
    time.sleep(0.2)
    
    group.y = -192
    time.sleep(0.2)
    group.y = -128
    time.sleep(0.2)
    group.y = -64
    time.sleep(0.2)
    group.y = 0

def pinner(pp):
    pled = digitalio.DigitalInOut(pp)
    pled.direction = digitalio.Direction.OUTPUT
    while(True):
        pled.value = True
        do_blink()
        pled.value = False
        do_blink()

# Loop forever so you can enjoy your cuppa
while False:
    group.y = 0
    time.sleep(2)
    print("Blinking")
    do_blink()


pinner(board.GPIO7)
