import pygame
import player
import spell
import Skeleton
import random


#TODO: Make new skeleton spawn after death, keep corpse of other skeleton on screen
#      Make corpse not deal damage to player
#
#      Put more of spell shooting functionality in player and Spell files. The bones are still there,
#      just get them to work
#
#      Create a draw health bar function to clean up gross pygame.draw.rect calls in gameLoop.
#
#      Put in a background: Tile program? Seems to be what everyone else in the class is using.
#
#      Add particle effects and sprites to spells, not just different colored circles.

pygame.init()

clock = pygame.time.Clock()

FPS = 60


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SPELL_X = 400
SPELL_Y = 300
SPELL_DISTANCE=200
#Change this and you will change the color of the spell :o
SPELL_TYPE = 'light'
SPELL_RADIUS = 5


SPELL_AMT = 5

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("src/background.jpeg")

#set font for lose message
loserFont = pygame.font.Font('src/ENDOR.ttf', 50)








#draw ground image



#load image sequences


#draw background images 


		

player = player.Character((400, 300))
first_skeleton = Skeleton.Skeleton((100, 100))
enemies = [first_skeleton]

#Relics of an ancient time. May be brought back to life? Must try to implement spell firing outside of gameLoop

# testSpell =spell.Spell(player.rect.x, player.rect.y, SPELL_DISTANCE, SPELL_RADIUS, SPELL_SPEED, SPELL_TYPE, SPELL_AMT)

    
# player.equip_spell(testSpell)

particles = []
run = True

timer_interval = 10000
spawn_skeleton = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_skeleton, timer_interval)

while run:
    
    screen.blit(background, (0, 0))
    clock.tick(FPS)
	
    
    
	
    keys = pygame.key.get_pressed()
    
    

   
	
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            run = False
        if(event.type == spawn_skeleton):
            enemies.append(Skeleton.Skeleton((random.randint(100, 700), random.randint(100, 600))))
    
    ################RUDIMENTARY SPELL FUNCTIONALITY UNTIL I CAN GET IT TO WORK OUTSIDE OF GAME LOOP###########################

    for particle in particles:
        if particle.x < 800 and particle.x > 0 and particle.y<600 and particle.y>0:
            particle.x+=particle.xSpeed
            particle.y+=particle.ySpeed
        else:
            particles.pop(0)
        for skeleton in enemies:
            if (pygame.Rect.colliderect(particle.rect, skeleton.rect)):
                #draw skeleton health bar when it takes damage
                particle.rect = (pygame.Rect(-1000, -1000, 0, 0))
                if skeleton.health>0:
                    pygame.draw.rect(screen, (0,255,0),(skeleton.rect.x+3,skeleton.rect.y-7, 30,7))
                    pygame.draw.rect(screen, (255,0,0), ((skeleton.rect.x+33)-(30-skeleton.health),skeleton.rect.y-7, (30-skeleton.health),7))
                else:
                    pygame.draw.rect(screen, (255,0,0), ((skeleton.rect.x+33)-(30),skeleton.rect.y-7, (30),7))
                skeleton.takeDamage(particle)
    
    

    if (keys[pygame.K_SPACE]):
        if len(particles)<5:
            SPELL_XSPEED=0
            SPELL_YSPEED=0
            if player.direction == 'r':
                 SPELL_XSPEED =20
            elif player.direction=='l':
                SPELL_XSPEED=-20
            elif player.direction == 'u':
                SPELL_YSPEED=-20
            elif player.direction =='d':
                SPELL_YSPEED=20

            particles.append(spell.Particle(round(player.rect.x + player.rect.width), round(player.rect.y + player.rect.height), SPELL_DISTANCE, SPELL_RADIUS, SPELL_XSPEED, SPELL_YSPEED, SPELL_TYPE))
            
    ########################################################################################
        

    


    
    
   
    
    for skeleton in enemies:
        screen.blit(pygame.transform.scale(skeleton.image, (50, 60)), skeleton.rect)
    screen.blit(pygame.transform.scale(player.image, (60,60)), player.rect)

    
    

    
            
       

  
    

    
    for skeleton in enemies:
        if (pygame.Rect.colliderect(player.rect, skeleton.rect) and skeleton.health > 0):
            player.takeDamage('skeleton')

    for skeleton in enemies:
        if(skeleton.health<=0):
            skeleton.die()
            #TODO: Spawn a replacement skeleton. Somehow keep original skeleton dead body onscreen.
            #skeleton = Skeleton.Skeleton((400, 100))
        else:
            skeleton.path_to_pos(player.rect.x, player.rect.y)



    if(player.health >0):
        pygame.draw.rect(screen, (0,255,0), (player.rect.x+12,player.rect.y-7, 40,7))
        pygame.draw.rect(screen, (255,0,0), ((player.rect.x+52)-(40-player.health),player.rect.y-7, (40-player.health),7))
        player.handle_event(keys)

        #part of rudimetary spell functionality
        for particle in particles:
            particle.update()
            particle.draw(screen)
        ####################
        
    else:
        # pygame.draw.rect(screen, (255,0,0), ((player.rect.x+52)-(40),player.rect.y-7, (40),7))
        player.die()
        loseMessage = loserFont.render('You Died', True, (148, 3, 10))
        screen.blit(loseMessage, (300,350))
        

   
        
    
        

    
        
    
    
    pygame.display.flip()
    clock.tick(20)
    screen.fill((0,0,0))
    

pygame.quit()