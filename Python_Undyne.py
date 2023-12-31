from mss import mss
from PIL import Image
import pynput
import keyboard

#WARNING, If any attacks are white, then you have to hit them yourself AND if any attacks are blue you have to dodge them youself. It literally takes too long to check for white and blue 
  
keys = set()

def on_press(key):
     keys.add(key)


def on_release(key):
     keys.remove(key)
     
keyboardController = pynput.keyboard.Controller()

def PressKey(key):
     keyboardController.press(key)
     keyboardController.release(key)

def IfSpear(colour):
    isBlack=colour[0] <= black and colour[1] <= black #If the colour is the background (black). B is not included as sometimes black is (0,0,70)
    isWhite= colour[0]==colour[1] and colour[1] == colour[2] #All 3 colours being the same is only true for the border of the box and for the characters
    isShield = colour[0] >= shieldR1 and colour[0] <= shieldR2 and colour[1] >= shieldG1 and colour[1] <= shieldG2 #If the colour is the blue shield
    return not (isBlack or isWhite or isShield)
    #IE return  if not (If the colour is the background (black), if  and ''''''
#def IfBlue(colour):
#    return colour[0] >= blueR1 and colour[0] <= blueR2 and colour[1] >= blueG1 and colour[1] <= blueG2 and colour[2] >= blueB

midpointX = 960
midpointY = 540
#The spears are 47 pixels wide so check every 45 pixels
#Start looking 75 pixels out from midpoint
black = 20 #If a colour is less than or equal to this
shieldR1 = 35
shieldR2 = 65
shieldG1 = 50
shieldG2 = 70
#blueR1 = 20
#blueR2 = 40
#blueG1 = 190
#blueG2 = 205
#blueB = 240 #It goes up to 255 so I don't need 2 blues

while True:
    while keyboard.is_pressed("q") == False:
        with mss() as sct:
            sct.shot()


        im = Image.open('monitor-1.png') # Can be many different formats.
        pix = im.load()
                    
        
        for i in range(80,121, 40): #So 80 and 120 (It can't be any further because of yellow spears)
            if IfSpear(pix[midpointX - i, midpointY]):
                #if IfBlue(pix[midpointX - i, midpointY]):
                #    PressKey(pynput.keyboard.Key.up)
                #else:
                    PressKey(pynput.keyboard.Key.left)
                    break
            elif IfSpear(pix[midpointX + i, midpointY]):
                #if IfBlue(pix[midpointX + i, midpointY]):
                #    PressKey(pynput.keyboard.Key.up)
                #else:
                    PressKey(pynput.keyboard.Key.right)
                    break
            elif IfSpear(pix[midpointX, midpointY - i]):
                #if IfBlue(pix[midpointX, midpointY - 1]):
                #    PressKey(pynput.keyboard.Key.left)
                #else:
                    PressKey(pynput.keyboard.Key.up)
                    break
            elif IfSpear(pix[midpointX, midpointY + i]):
                #if IfBlue(pix[midpointX, midpointY + i]):
                #    PressKey(pynput.keyboard.Key.left)
                #else:
                    PressKey(pynput.keyboard.Key.down)
                    break
                    