import pygame

class Spell(pygame.sprite.Sprite):
    def __init__(self, x, y, distance, radius, spellType):
        self.x= x
        self.y =y
        self.distance = distance
        self.spellType = spellType
        self.radius = radius
        if (spellType == 'fire'):
            self.color = ((9235, 27, 12))

        elif (spellType == 'light'):
            self.color = ((255, 255, 255))

        elif (spellType == 'dark'):
            self.color = ((0, 0, 0))

        elif (spellType == 'poison'):
            self.color = ((9, 148, 37))

        elif (spellType == 'water'):
            self.color = ((20, 141, 227))

        else:
            self.color= ((148, 3, 10))

    def draw(self,screen):
        pygame.draw.circle(screen, self.color, (self.x,self.y), self.radius)