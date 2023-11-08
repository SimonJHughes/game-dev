import pygame
import math

class Insight():
    def __init__(self, x, y):
        
        #Init
        self.x = x
        self.y = y
        
        
        #Load image
        self.sheet = pygame.image.load('src/insight.png')
        self.sheet.set_clip(pygame.Rect(256, 256, 680, 634))
        self.image = pygame.transform.scale(self.sheet.subsurface(self.sheet.get_clip()), (25, 25))
        self.rect = pygame.Rect((self.x, self.y, 25, 25))
    

        
        
        
        
    