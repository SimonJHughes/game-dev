import pygame
import time

class Bat(pygame.sprite.Sprite):
    #FIX ALL CLIPS FOR SPRITE
    def __init__(self, position):
    
        #load image
        self.sheet = pygame.image.load("src/fly.png")
        startX=14
        startY=526
        #defines area of a single sprite of an image
        self.sheet.set_clip(pygame.Rect(startX, startY+397, 34, 48))
        
        #loads spritesheet images
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        
        #position image in the screen surface
        self.rect.topleft = position
        
        #variable for looping the frame sequence
        self.frame = 0
        
        
        self.rectWidth = 34
        self.rectHeight = 48
       
        
        self.speed = 2
        self.health = 30

       
        
        self.fly_states = { 0: (startX, startY+190, self.rectWidth, self.rectHeight), 1: (startX+64, startY+190, self.rectWidth, self.rectHeight), 2: (startX+64*2, startY+190, self.rectWidth, self.rectHeight), 3: (startX+64*3, startY+190, self.rectWidth, self.rectHeight), 4: (startX+64*4, startY+190, self.rectWidth, self.rectHeight), 5: (startX+64*5, startY+190, self.rectWidth, self.rectHeight), 6: (startX+64*6, startY+190, self.rectWidth, self.rectHeight), 7: (startX+64*7, startY+190, self.rectWidth, self.rectHeight), 8: (startX+64*7, startY+190, self.rectWidth, self.rectHeight) }

        self.death_states ={0: (startX, startY+768, self.rectWidth, self.rectHeight), 1: (startX+64, startY+768, self.rectWidth, self.rectHeight), 2: (startX+64*2, startY+768, self.rectWidth, self.rectHeight), 3: (startX+64*3, startY+768, self.rectWidth, self.rectHeight), 4: (startX+64*4, startY+768, self.rectWidth, self.rectHeight), 5: (startX+64*5, startY+768, self.rectWidth, self.rectHeight)}

        self.rectWidth= 75
        self.rectHeight=75
        
        
    def takeDamage(self, spell):
        
            self.health -=spell.damage
        
    def die(self):
        self.sheet = pygame.image.load("src/batDeath.png")
        startX=14
        startY=526
        #defines area of a single sprite of an image
        self.sheet.set_clip(pygame.Rect(startX, startY+397, 34, 48))
        
        #loads spritesheet images
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()

        for i in range (0,6):
            self.sheet.set_clip(pygame.Rect(self.death_states[i]))
            self.image = self.sheet.subsurface(self.sheet.get_clip())
            i+=1

    def get_frame(self, frame_set):
        #looping the sprite sequences.
        self.frame += 1
        
        #if loop index is higher that the size of the frame return to the first frame 
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def update(self, direction):
        
        self.clip(self.fly_states)
        self.rect.x += self.speed
        if(self.rect.x>=800-self.rectWidth):
            self.rect.x=800-self.rectWidth


        self.image = self.sheet.subsurface(self.sheet.get_clip())
        
    def path_to_pos(self, x, y):
        x_distance = self.rect.x - x
        y_distance = self.rect.y - y
        
        if(abs(x_distance) > abs(y_distance)):
            if(x_distance > 0):
                self.update('left')
                self.direction = 'l'
            elif(x_distance <= 0):
                self.update('right')
                self.direction = 'r'
        else:
            if(y_distance > 0):
                self.update('up')
                self.direction = 'u'
            elif(y_distance <= 0):
                self.update('down')
                self.direction = 'd'
        

        
        
       
   