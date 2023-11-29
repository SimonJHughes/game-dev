import Slime
import pygame
from random import randint
class SmallSlime(Slime.Slime):
    def __init__(self, position, slime):
    
        #load image
        
        if(slime.choice == 1):
            self.sheet = pygame.image.load("src/Slime_Small_Blue.png")
        elif(slime.choice == 2):
            self.sheet = pygame.image.load("src/Slime_Small_Green.png")
        elif(slime.choice == 3):
            self.sheet = pygame.image.load("src/Slime_Small_Red.png")
        else:
            self.sheet = pygame.image.load("src/Slime_Small_White.png")
        startX=0
        startY=0
        #defines area of a single sprite of an image
        self.sheet.set_clip(pygame.Rect(startX, startY, 32, 32))
        
        #loads spritesheet images
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        
        #position image in the screen surface
        self.rect.topleft = position
        
        #variable for looping the frame sequence
        self.frame = 0
        self.direction ='d'
        
        self.rectWidth = 32
        self.rectHeight = 32
       
        
        self.speed = 4
        self.health = 20

       
        

        
        self.down_states ={ 0: (startX, startY, self.rectWidth,  self.rectHeight), 1: (startX+32, startY, self.rectWidth,  self.rectHeight)}
        self.up_states = { 0: (startX, startY+32*2, self.rectWidth,  self.rectHeight), 1: (startX+32, startY+32*2, self.rectWidth,  self.rectHeight)}
        self.left_states = { 0: (startX, startY+32*3, self.rectWidth,  self.rectHeight), 1: (startX+32, startY+32*3, self.rectWidth,  self.rectHeight)}
        self.right_states ={ 0: (startX, startY+32, self.rectWidth,  self.rectHeight), 1: (startX+32, startY+32, self.rectWidth,  self.rectHeight)}

        #self.death_states