import pygame

class Skeleton(pygame.sprite.Sprite):
    def __init__(self, position):
    
        #load image
        self.sheet = pygame.image.load("src/skeleton.png")
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
        self.direction ='d'
        
        self.rectWidth = 34
        self.rectHeight = 48
       
        
        self.speed = 10

       
        self.down_idle_states= { 0: (startX, startY+127, self.rectWidth,  self.rectHeight)}
        self.right_idle_states= { 0: (startX, startY+190, self.rectWidth,  self.rectHeight)}
        self.left_idle_states = { 0: (startX, startY+61, self.rectWidth, self.rectHeight)}
        self.up_idle_states= { 0: (startX, startY, self.rectWidth,  self.rectHeight) }    

        
        self.down_states ={ 0: (startX, startY+127, self.rectWidth,  self.rectHeight), 1: (startX+64, startY+127, self.rectWidth,  self.rectHeight), 2: (startX+64*2, startY+127, self.rectWidth,  self.rectHeight), 3:(startX+64*3, startY+127, self.rectWidth,  self.rectHeight), 4:(startX+64*4, startY+127, self.rectWidth,  self.rectHeight), 5:(startX+64*5, startY+127, self.rectWidth,  self.rectHeight), 6:(startX+64*6, startY+127, self.rectWidth,  self.rectHeight), 7:(startX+64*7, startY+127, self.rectWidth,  self.rectHeight), 8:(startX+64*8, startY+127, self.rectWidth,  self.rectHeight) }
        self.up_states = { 0: (startX, startY, self.rectWidth, self.rectHeight), 1: (startX+64, startY, self.rectWidth, self.rectHeight), 2: (startX+64*2, startY, self.rectWidth, self.rectHeight), 3: (startX+64*3, startY, self.rectWidth, self.rectHeight), 4: (startX+64*4, startY, self.rectWidth, self.rectHeight), 5: (startX+64*5, startY, self.rectWidth, self.rectHeight), 6: (startX+64*6, startY, self.rectWidth, self.rectHeight), 7: (startX+64*7, startY, self.rectWidth, self.rectHeight), 8: (startX+64*8, startY, self.rectWidth, self.rectHeight)}
        self.left_states = { 0: (startX, startY+61, self.rectWidth, self.rectHeight), 1: (startX+64, startY+61, self.rectWidth, self.rectHeight), 2: (startX+64*2, startY+61, self.rectWidth, self.rectHeight), 3: (startX+64*3, startY+61, self.rectWidth, self.rectHeight), 4: (startX+64*4, startY+61, self.rectWidth, self.rectHeight), 5: (startX+64*5, startY+61, self.rectWidth, self.rectHeight), 6: (startX+64*6, startY+61, self.rectWidth, self.rectHeight), 7: (startX+64*7, startY+61, self.rectWidth, self.rectHeight), 8: (startX+64*7, startY+61, self.rectWidth, self.rectHeight) }
        self.right_states = { 0: (startX, startY+190, self.rectWidth, self.rectHeight), 1: (startX+64, startY+190, self.rectWidth, self.rectHeight), 2: (startX+64*2, startY+190, self.rectWidth, self.rectHeight), 3: (startX+64*3, startY+190, self.rectWidth, self.rectHeight), 4: (startX+64*4, startY+190, self.rectWidth, self.rectHeight), 5: (startX+64*5, startY+190, self.rectWidth, self.rectHeight), 6: (startX+64*6, startY+190, self.rectWidth, self.rectHeight), 7: (startX+64*7, startY+190, self.rectWidth, self.rectHeight), 8: (startX+64*7, startY+190, self.rectWidth, self.rectHeight) }

        self.rectWidth= 75
        self.rectHeight=75
        
        
        

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

        if direction == 'stand_left':
            self.clip(self.left_idle_states)
        if direction == 'stand_right':
            self.clip(self.right_idle_states)
        if direction == 'stand_up':
            self.clip(self.up_idle_states)
        if direction == 'stand_down':
            self.clip(self.down_idle_states)

        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, event, keys):
        
        

        if (keys[pygame.K_w] or keys[pygame.K_UP]):
            self.update('up')
            self.direction = 'u'
            

        if (keys[pygame.K_s] or keys[pygame.K_DOWN]):
            self.update('down')
            self.direction = 'd'
        
        
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]):
            self.update('left')
            self.direction ='l'

        if ((keys[pygame.K_d] or keys[pygame.K_RIGHT])):
            self.update('right')
            self.direction = 'r'
            
       
        
            
        #it is what it is
        if ((not keys[pygame.K_d] and not keys[pygame.K_RIGHT] 
             and not keys[pygame.K_a] and not keys[pygame.K_LEFT] 
             and not keys[pygame.K_s] and not keys[pygame.K_DOWN] 
             and not keys[pygame.K_w] and not keys[pygame.K_UP]) 
             or ((keys[pygame.K_w] or keys[pygame.K_UP]) 
                 and (keys[pygame.K_s] or keys[pygame.K_DOWN]))
             or ((keys[pygame.K_d] or keys[pygame.K_RIGHT]) 
                 and (keys[pygame.K_a] or keys[pygame.K_LEFT]))
            ):
            
            self.idle()
        

        
        
       
    def idle(self):
        if (self.direction == 'd'):
            self.update('stand_down')
        if (self.direction == 'u'):
            self.update('stand_up')
        if (self.direction == 'r'):
            self.update('stand_right')
        if (self.direction == 'l'):
            self.update('stand_left')
