import pyscreenshot as ImageGrab

from PIL import ImageChops, Image, ImageOps, ImageFilter
import time
from pynput.mouse import Button, Controller


mouse = Controller()
time.sleep(5)
while True:
            # part of the screen
    im=ImageGrab.grab(bbox=(1869,600,1870,1080))
        # im.show()

    
    px = im.load()
    x = 0
    while x <= 478:
        if px[0, x] == (84, 252, 252):
            print("\a")
            mouse.press(Button.right)
            mouse.release(Button.right)
            time.sleep(0.45)
            mouse.press(Button.right)
            mouse.release(Button.right)
            time.sleep(2.5)
            x = x + 100000
            
        x = x + 1
