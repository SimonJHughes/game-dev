import pygame
import math

class Insight():
    def __init__(self, x, y):
        
        #Init
        self.x = x
        self.y = y

        self.frame =0

        self.rectWidth = 25
        self.rectHeight = 25
        
        
        #Load image
        self.sheet = pygame.image.load('src/insight.png')
        self.sheet.set_clip(pygame.Rect(256, 256, 680, 634))
        self.idle_states = { 0: (256, 256, self.rectWidth,  self.rectHeight), 1: (256, 258, self.rectWidth,  self.rectHeight), 2: (256, 260, self.rectWidth,  self.rectHeight), 3:(256, 262, self.rectWidth,  self.rectHeight), 4:(256, 258, self.rectWidth,  self.rectHeight), 5:(256, 254, self.rectWidth,  self.rectHeight) }
        self.rect = pygame.Rect((self.x, self.y, 50, 50))


        

        self.image = pygame.transform.scale(self.sheet.subsurface(self.sheet.get_clip()), (self.rectWidth, self.rectHeight))
        

    def get_frame(self, frame_set):
        #looping the sprite sequences.
        self.frame += 1
        
        #if loop index is higher that the size of the frame return to the first frame 
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        
        return frame_set[self.frame]

    def idle(self):
        self.sheet.set_clip(pygame.Rect(self.get_frame(self.idle_states)))
        self.image = pygame.transform.scale(self.sheet.subsurface(self.sheet.get_clip()), (self.rectWidth, self.rectHeight))
    
    

        
        
        
        
    