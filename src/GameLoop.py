import pygame
import player


pygame.init()

clock = pygame.time.Clock()

FPS = 24


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))








#draw ground image



#load image sequences


#draw background images 


		

player = player.Character((400, 300))

run = True
while run:
    clock.tick(FPS)
	
    
    
	
    keys = pygame.key.get_pressed()

    
        

    
	
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            run = False
	
    player.handle_event(event, keys)
    
    screen.blit(pygame.transform.scale(player.image, (60,60)), player.rect)
    
    pygame.display.flip()
    clock.tick(20)
    screen.fill((0,0,0))
    

pygame.quit()