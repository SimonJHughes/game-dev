import pygame
from random import randint
class Mud(pygame.sprite.Sprite):
    def __init__(self, position):
    
        #load image
        
        self.sheet = pygame.image.load("src/mud.png")
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect= self.image.get_rect()
        
        self.width = randint(60, 100)
        self.height = self.width + randint(-50, 50)

        self.rect.width = self.width
        self.rect.height = self.height
        self.rect.topleft = position
