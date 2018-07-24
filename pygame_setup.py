import pygame
from tkinter import *
import tkinter.messagebox

#App class for pygame window
class App():
    #Pass width, height, tickspeed and caption of window to constructor
    def __init__(self,width,height,tickSpeed,caption):
        self.screenx = width
        self.screeny = height
        self.tickSpeed = tickSpeed
        self.caption = caption
        self.screen = None
        self.clock = None
    #Call begin to actually initialise pygame and set the display and clock etc.
    def begin(self):
        pygame.init()
        pygame.mixer.quit()
        pygame.display.set_caption(self.caption)
        self.screen = pygame.display.set_mode((self.screenx, self.screeny))
        self.clock = pygame.time.Clock()

    #Exit pygame and python
    def exit(self):
        pygame.quit()
        quit()
    #Return tickspeed of the clock
    def getTickSpeed(self):
        return self.tickspeed
    #Set a new tickspeed for the clock
    def setTickSpeed(self,newTickSpeed):
        self.tickSpeed = newTickSpeed
    #Return the clock object
    def getClock(self):
        return self.clock
    #Tick the clock at the current tickspeed
    def Tick(self):
        self.clock.tick(self.tickSpeed)
    #Return the surface
    def getScreen(self):
        return self.screen
    #Return the width of the screen
    def getWidth(self):
        return self.screenx
    #Return the height of the screen
    def getHeight(self):
        return self.screeny

#Render text function to blit text to surface
#Pass the text, the font size, the colour, x coordinate, y coordinate, surface to blit to
#Surface is App.getScreen()
def renderText(text,fontSize,colour,x,y,surface):
    font = pygame.font.SysFont("monospace", fontSize)
    text = surface.blit((font.render(text, 1, colour)),(x,y))
    return text

#Save an image of the surface
#Pass the surface (App.getScreen())
def saveImage(surface):
    root = Tk()
    root.withdraw()
    #Tkinter popup box asking if the user wishes to save an image of the screen
    response = tkinter.messagebox.askyesno("Save Image","Would you like to save an image of the screen?")
    root.update()
    if response == True:
        #Save an image of the screen
        pygame.image.save(surface,"screenshot.png")
    else:
        return

#Return string of characters on keyboard from pygame.event
def getKey(key):
    if key == pygame.K_a: return "a"
    elif key == pygame.K_b: return "b"
    elif key == pygame.K_c: return "c"
    elif key == pygame.K_d: return "d"
    elif key == pygame.K_e: return "e"
    elif key == pygame.K_f: return "f"
    elif key == pygame.K_g: return "g"
    elif key == pygame.K_h: return "h"
    elif key == pygame.K_i: return "i"
    elif key == pygame.K_j: return "j"
    elif key == pygame.K_k: return "k"
    elif key == pygame.K_l: return "l"
    elif key == pygame.K_m: return "m"
    elif key == pygame.K_n: return "n"
    elif key == pygame.K_o: return "o"
    elif key == pygame.K_p: return "p"
    elif key == pygame.K_q: return "q"
    elif key == pygame.K_r: return "r"
    elif key == pygame.K_s: return "s"
    elif key == pygame.K_t: return "t"
    elif key == pygame.K_u: return "u"
    elif key == pygame.K_v: return "v"
    elif key == pygame.K_w: return "w"
    elif key == pygame.K_x: return "x"
    elif key == pygame.K_y: return "y"
    elif key == pygame.K_z: return "z"
    elif key == pygame.K_0: return "0"
    elif key == pygame.K_1: return "1"
    elif key == pygame.K_2: return "2"
    elif key == pygame.K_3: return "3"
    elif key == pygame.K_4: return "4"
    elif key == pygame.K_5: return "5"
    elif key == pygame.K_6: return "6"
    elif key == pygame.K_7: return "7"
    elif key == pygame.K_8: return "8"
    elif key == pygame.K_9: return "9"
    elif key == pygame.K_BACKSPACE: return "backspace"
    elif key == pygame.K_SPACE: return "space"
    elif key == pygame.K_RETURN: return "return"
    elif key == pygame.K_ESCAPE: return "escape"
    elif key == pygame.K_UP: return "up"
    elif key == pygame.K_DOWN: return "down"
    elif key == pygame.K_RIGHT: return "right"
    elif key == pygame.K_LEFT: return "left"

