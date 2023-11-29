import pygame
from random import randint

class Slime(pygame.sprite.Sprite):
    def __init__(self, position):
    
        #load image
        self.choice= randint(1,4)
        if(self.choice == 1):
            self.sheet = pygame.image.load("src/Slime_Medium_Blue.png")
        elif(self.choice == 2):
            self.sheet = pygame.image.load("src/Slime_Medium_Green.png")
        elif(self.choice == 3):
            self.sheet = pygame.image.load("src/Slime_Medium_Red.png")
        else:
            self.sheet = pygame.image.load("src/Slime_Medium_White.png")
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
       
        
        self.speed = 3
        self.health = 20

       
        

        
        self.down_states ={ 0: (startX, startY, self.rectWidth,  self.rectHeight), 1: (startX+32, startY, self.rectWidth,  self.rectHeight), 2: (startX+32*2, startY, self.rectWidth,  self.rectHeight), 3:(startX+32*3, startY, self.rectWidth,  self.rectHeight)}
        self.up_states = { 0: (startX, startY+32*2, self.rectWidth,  self.rectHeight), 1: (startX+32, startY+32*2, self.rectWidth,  self.rectHeight), 2: (startX+32*2, startY+32*2, self.rectWidth,  self.rectHeight), 3:(startX+32*3, startY+32*2, self.rectWidth,  self.rectHeight)}
        self.left_states = { 0: (startX, startY+32*3, self.rectWidth,  self.rectHeight), 1: (startX+32, startY+32*3, self.rectWidth,  self.rectHeight), 2: (startX+32*2, startY+32*3, self.rectWidth,  self.rectHeight), 3:(startX+32*3, startY+32*3, self.rectWidth,  self.rectHeight)}
        self.right_states ={ 0: (startX, startY+32, self.rectWidth,  self.rectHeight), 1: (startX+32, startY+32, self.rectWidth,  self.rectHeight), 2: (startX+32*2, startY+32, self.rectWidth,  self.rectHeight), 3:(startX+32*3, startY+32, self.rectWidth,  self.rectHeight)}

        #self.death_states

       
        
        
    def takeDamage(self, spell):
        
            self.health -=spell.damage
        
    # def die(self):
    #     for i in range (0,6):
    #         self.sheet.set_clip(pygame.Rect(self.death_states[i]))
    #         self.image = self.sheet.subsurface(self.sheet.get_clip())
    #         i+=1

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
        if direction == 'left':
            self.clip(self.left_states)
            #animate rect coordinates
            self.rect.x -= self.speed

            if(self.rect.x<=0):
                self.rect.x=0
            
            
        if direction == 'right':
            self.clip(self.right_states)
            self.rect.x += self.speed
            if(self.rect.x>=800-self.rectWidth):
                self.rect.x=800-self.rectWidth

        if direction == 'up':
            self.clip(self.up_states)
            self.rect.y -= self.speed
            if(self.rect.y<=0):
                self.rect.y=0
        if direction == 'down':
            self.clip(self.down_states)

            self.rect.y += self.speed
            if(self.rect.y>=600-self.rectHeight):
                self.rect.y=600-self.rectHeight

        

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
        

        
        
 
