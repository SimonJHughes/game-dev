import pygame
import player

pygame.init()

clock = pygame.time.Clock()

FPS = 60

SCREEN_WIDTH = 850
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Neophyte")

def handle_input(key_pressed):
    if(key[pygame.K_LEFT]):
        print("Left key pressed")
        #Handle left
    elif(key[pygame.K_RIGHT]):
        print("Right key pressed")
        #Handle right
    elif(key[pygame.K_UP]):
        print("Up pressed")
        #Handle up
    elif(key[pygame.K_DOWN]):
        print("Down pressed")
        #Handle down
    
    

run = True

while run:
    
    clock.tick(FPS)
    
    key = pygame.key.get_pressed()
    