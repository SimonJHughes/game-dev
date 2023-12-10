import pygame

class Particle(object):
    def __init__(self, x, y, distance, radius, xSpeed, ySpeed, spellType):
        
        self.x= x
        self.y =y
        self.xSpeed =xSpeed
        self.ySpeed = ySpeed
        self.distance = distance
        self.spellType = spellType
        self.radius = radius
        self.spellType = spellType
        self.rect = pygame.Rect((self.x,self.y, self.radius*2,self.radius*2))
        if (spellType == 'fire'):
            self.color = ((235, 27, 12))
            self.damage = 4

        elif (spellType == 'light'):
            self.color = ((255, 255, 255))
            self.damage = 3

        elif (spellType == 'dark'):
            self.color = ((0, 0, 0))
            self.damage = 9

        elif (spellType == 'poison'):
            self.color = ((9, 148, 37))
            self.damage = 4

        elif (spellType == 'water'):
            self.color = ((20, 141, 227))
            self.damage = 4

        else:
            self.color= ((148, 3, 10))
            self.damage =1

    
          

    def draw(self,screen):
        pygame.draw.circle(screen, self.color, (self.rect.x,self.rect.y), self.radius)

    def update(self):
        self.rect.x +=self.xSpeed
        self.rect.y+= self.ySpeed

class Spell(object):
    def __init__(self, x, y, distance, radius, speed, spellType, amt):
        self.particles =[]
        
        for i in range (amt): 
            self.particle = Particle(x, y, distance, radius, speed, spellType)
            self.particles.append(self.particle) 
    


        
   

