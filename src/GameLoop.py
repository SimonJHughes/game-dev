import pygame
import player
import spell
import Skeleton


pygame.init()

clock = pygame.time.Clock()

FPS = 60


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SPELL_X = 400
SPELL_Y = 300
SPELL_DISTANCE=200
#Change this and you will change the color of the spell :o
SPELL_TYPE = 'poison'
SPELL_RADIUS = 5


SPELL_AMT = 5

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#set font for lose message
loserFont = pygame.font.Font('src/ENDOR.ttf', 50)








#draw ground image



#load image sequences


#draw background images 


		

player = player.Character((400, 300))
skeleton = Skeleton.Skeleton((100, 100))

#Relics of an ancient time. May be brought back to life? Must try to implement spell firing outside of gameLoop

# testSpell =spell.Spell(player.rect.x, player.rect.y, SPELL_DISTANCE, SPELL_RADIUS, SPELL_SPEED, SPELL_TYPE, SPELL_AMT)

    
# player.equip_spell(testSpell)

particles = []
run = True
while run:
    clock.tick(FPS)
	
    
    
	
    keys = pygame.key.get_pressed()
    
    

   
	
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            run = False
    
    ################RUDIMENTARY SPELL FUNCTIONALITY UNTIL I CAN GET IT TO WORK OUTSIDE OF GAME LOOP###########################

    for particle in particles:
        if particle.x < 800 and particle.x > 0 and particle.y<600 and particle.y>0:
            particle.x+=particle.xSpeed
            particle.y+=particle.ySpeed
        else:
            particles.pop(0)
    
    

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

            particles.append(spell.Particle(round(player.rect.x + player.rect.width //2), round(player.rect.y + player.rect.height//2), SPELL_DISTANCE, SPELL_RADIUS, SPELL_XSPEED, SPELL_YSPEED, SPELL_TYPE))
            
    ########################################################################################
          


    if(player.health>0):
        player.handle_event(keys)

        #part of rudimetary spell functionality
        for particle in particles:
            particle.draw(screen)

    else:
        player.die()
        loseMessage = loserFont.render('You Died', True, (148, 3, 10))
        screen.blit(loseMessage, (300,350))

    



    skeleton.path_to_pos(player.rect.x, player.rect.y)
   
    
    screen.blit(pygame.transform.scale(player.image, (60,60)), player.rect)
    screen.blit(skeleton.image, skeleton.rect)

    
    

    
            
       

    #draw player health bar
    pygame.draw.rect(screen, (0,255,0), (player.rect.x+12,player.rect.y-7, 40,7))
    
    if (pygame.Rect.colliderect(player.rect, skeleton.rect)):
        player.takeDamage('skeleton')


    if(player.health >0):
        pygame.draw.rect(screen, (255,0,0), ((player.rect.x+52)-(40-player.health),player.rect.y-7, (40-player.health),7))
    else:
        pygame.draw.rect(screen, (255,0,0), ((player.rect.x+52)-(40),player.rect.y-7, (40),7))
        

   
        
    
        

    
        
    
    
    pygame.display.flip()
    clock.tick(20)
    screen.fill((0,0,0))
    

pygame.quit()