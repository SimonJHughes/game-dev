import pygame
import time

class BringerOfDeath(pygame.sprite.Sprite):
    def __init__(self, position):
    
        #load image
        self.sheet = pygame.image.load("src/Bringer-of-Death-SpritSheet.png")
        startX=60
        startY=119
        #defines area of a single sprite of an image
        self.sheet.set_clip(pygame.Rect(startX, startY, 88, 85))
        
        #loads spritesheet images
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        
        self.image = pygame.transform.scale(self.image, (600, 600))
        
        #position image in the screen surface
        self.rect.topleft = position
        
        
        #variable for looping the frame sequence
        self.frame = 0
        self.direction ='d'
        
        self.rectWidth = 88
        self.rectHeight = 85
       
        
        self.speed = 3
        self.health = 4
        self.maxHealth=100
        self.isDead = False
        self.isSuperDead = False
        
        self.hitbox = pygame.Rect(self.rect.left + 90, self.rect.top + 100, self.rect.width + 100, self.rect.width + 200)
        self.strikezone = pygame.Rect(self.rect.left, self.rect.top + 50, self.rect.width + 200, self.rect.height + 200)
        self.attacking = False

       
        
        self.walk_states = { 0: (startX, 107, self.rectWidth, self.rectHeight), 1: (startX+140, 107, self.rectWidth, self.rectHeight), 2: (startX+140*2, 107, self.rectWidth, self.rectHeight), 3: (startX+140*3, 107, self.rectWidth, self.rectHeight), 4: (startX+140*4, 107, self.rectWidth, self.rectHeight), 5: (startX+140*5, 107, self.rectWidth, self.rectHeight), 6: (startX+140*6, 107, self.rectWidth, self.rectHeight), 7: (startX+140*7, 107, self.rectWidth, self.rectHeight)}
        
        
        
        self.attackWidth =139
        self.attackHeight =92
        startX=66
        startY=204
        self.attack_states = { 0: (startX, startY, self.rectWidth, self.rectHeight), 1: (201, startY, self.rectWidth, self.rectHeight), 2: (343, startY, self.rectWidth, self.rectHeight), 3: (474, startY, self.rectWidth, self.rectHeight), 4: (561, 193, self.attackWidth, self.attackHeight), 5: (699, 193, self.attackWidth+2, self.attackHeight), 6: (841, 193, self.attackWidth, self.attackHeight), 7: (975, 193, self.attackWidth, self.attackHeight), 8: (3, 291, self.attackWidth, self.attackHeight), 9: (202, 291, self.rectWidth, self.rectHeight)}
        
        

        self.death_states ={0: (341, 291, self.rectWidth, self.rectHeight), 1: (481, 291, self.rectWidth, self.rectHeight), 2: (622, 291, self.rectWidth, self.rectHeight), 3: (759, 291, self.rectWidth, self.rectHeight), 4: (901, 291, self.rectWidth, self.rectHeight), 5: (1032, 291, self.rectWidth, self.rectHeight), 6:(67,380,self.rectWidth,self.rectHeight), 7: (204, 380, self.rectWidth, self.rectHeight), 8: (340,380, self.rectWidth, self.rectHeight), 9: (480,380,self.rectWidth,self.rectHeight), 10: (619,380,self.rectWidth,self.rectHeight), 11: (762,380,self.rectWidth,self.rectHeight), 12: (900,380,self.rectWidth,self.rectHeight)}
        
        
        
        
    def takeDamage(self, spell):
        
            self.health -=spell.damage
        
    def die(self):
        self.frame = -1
        self.clip(self.death_states)
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.isDead = True
        
        

    def get_frame(self, frame_set):
        #looping the sprite sequences.
        self.frame += 1
            
        
        #if loop index is higher that the size of the frame return to the first frame 
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
            if(frame_set == self.attack_states):
                self.attacking = False
            elif(frame_set == self.death_states):
                self.frame = len(frame_set) - 1
                
        
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:     
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def update(self, direction):
        if(not self.isDead):
            if direction == 'left':
                self.clip(self.walk_states)
                #animate rect coordinates
                self.rect.x -= self.speed
                self.hitbox.x -= self.speed
                self.strikezone.x -= self.speed

                if(self.rect.x<=0):
                    self.rect.x=0
                
                
            if direction == 'right':
                self.clip(self.walk_states)
                self.rect.x += self.speed
                self.hitbox.x += self.speed
                self.strikezone.x += self.speed
                if(self.rect.x>=800-self.rectWidth):
                    self.rect.x=800-self.rectWidth

            if direction == 'up':
                self.clip(self.walk_states)
                self.rect.y -= self.speed
                self.hitbox.y -= self.speed
                self.strikezone.y -= self.speed
                
                if(self.rect.y<=0):
                    self.rect.y=0
            if direction == 'down':
                self.clip(self.walk_states)

                self.rect.y += self.speed
                self.hitbox.y += self.speed
                self.strikezone.y += self.speed
                if(self.rect.y>=600-self.rectHeight):
                    self.rect.y=600-self.rectHeight

            

            if direction == 'right':
                self.image = self.sheet.subsurface(self.sheet.get_clip())
                self.image= pygame.transform.flip(self.image, 1, 0)


            else:
                self.image = self.sheet.subsurface(self.sheet.get_clip())
                
        else:
            self.clip(self.death_states)
            self.image = self.sheet.subsurface(self.sheet.get_clip())
        
    def path_to_pos(self, x, y):
        if(not self.attacking):
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
        else:
            self.clip(self.attack_states)
            if(self.direction == 'r'):
                self.image = self.sheet.subsurface(self.sheet.get_clip())
                self.image = pygame.transform.flip(self.image, 1, 0)
            else:
                self.image = self.sheet.subsurface(self.sheet.get_clip())
            
        

    def attack(self):
        self.attacking = True
        self.frame = 0
        self.clip(self.attack_states)
        self.image = self.sheet.subsurface(self.sheet.get_clip())
       
  
