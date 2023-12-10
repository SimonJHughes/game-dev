import pygame
import player
import spell
import Skeleton
import random
import Insight
import Bat
import Slime
import SmallSlime
import BringerOfDeath

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Button:
    def __init__(self, text, x, y, width, height, color, hover_color, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.action = action

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        self.check_hover()
        self.draw_text(surface)

    def check_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.color = self.hover_color
        else:
            self.color = BLACK

    def draw_text(self, surface):
        text_surface = spellUIFont.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
        



#TODO: 
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
SPELL_TYPE_ARR = ['light', 'dark', 'fire', 'poison', 'water']
SPELL_INDEX =0
SPELL_TYPE = SPELL_TYPE_ARR[SPELL_INDEX]
SPELL_RADIUS = 5

button1 = Button("Speed", SCREEN_WIDTH // 2 - 100, 200, 200, 50, BLACK, WHITE, lambda: print("Button 1 clicked"))
button2 = Button("Health", SCREEN_WIDTH // 2 - 100, 300, 200, 50, BLACK, WHITE, lambda: print("Button 2 clicked"))
button3 = Button("Ammo", SCREEN_WIDTH // 2 - 100, 400, 200, 50, BLACK, WHITE, lambda: print("Button 3 clicked"))
button4 = Button("Done", SCREEN_WIDTH // 2 - 100, 500, 200, 50, BLACK, WHITE, lambda: print("Button 3 clicked"))


SPELL_AMT = 5

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("src/background.jpeg")

#set font for lose message
loserFont = pygame.font.Font('src/ENDOR.ttf', 50)
spellUIFont =pygame.font.Font('src/ENDOR.ttf', 25)








#draw ground image



#load image sequences


#draw background images 


		

player = player.Character((400, 300))
first_skeleton = Skeleton.Skeleton((100, 100))
enemies = [first_skeleton]
dead_enemies = []

#Array storing insight entities
total_insight = 0
item_entities = []


#Relics of an ancient time. May be brought back to life? Must try to implement spell firing outside of gameLoop

# testSpell =spell.Spell(player.rect.x, player.rect.y, SPELL_DISTANCE, SPELL_RADIUS, SPELL_SPEED, SPELL_TYPE, SPELL_AMT)

    
# player.equip_spell(testSpell)

particles = []
run = True

skeleton_interval = 10000
spawn_skeleton = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_skeleton, skeleton_interval)

bat_interval = 5000
spawn_bat = pygame.USEREVENT + 2
pygame.time.set_timer(spawn_bat, bat_interval)

slime_interval = 7500
spawn_slime = pygame.USEREVENT + 3
pygame.time.set_timer(spawn_slime, slime_interval)

wavecheck_interval = 2000
wavecheck = pygame.USEREVENT + 4
pygame.time.set_timer(wavecheck, wavecheck_interval)


total_skeletons = 2
skeletons_spawned = 1

total_bats = 1
bats_spawned = 0

total_slimes = 0
slimes_spawned = 0

current_wave = 1
show_menu = False
change_wave = False

speed_cost = 1
health_cost = 1
ammo_cost = 1

max_particles = 5

while run:
    
    screen.blit(background, (-100, 0))
    clock.tick(FPS)
   
    keys = pygame.key.get_pressed()
    
    #If all enemies are dead, change waves
    if(change_wave):
        change_wave = False
        dead_enemies.clear()
        current_wave += 1
        skeletons_spawned = 0
        bats_spawned = 0
        slimes_spawned = 0
        
        total_skeletons *= 1
        total_bats *= 1
        total_slimes *= 1
        if(current_wave == 2):
            total_slimes = 2
        if(current_wave == 3):
            total_bats = 2
        if(current_wave == 4):
            enemies.append(BringerOfDeath.BringerOfDeath((1000, 300)))
            
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            run = False
        if(event.type == spawn_skeleton and not (skeletons_spawned >= total_skeletons)):
            enemies.append(Skeleton.Skeleton((random.randint(100, 700), random.randint(100, 600))))
            skeletons_spawned += 1
            pygame.time.set_timer(spawn_skeleton, int(skeleton_interval * 0.5))
        if(event.type == spawn_bat and not (bats_spawned >= total_bats)):
            enemies.append(Bat.Bat((random.randint(100, 700), random.randint(100, 600))))
            bats_spawned += 1
            pygame.time.set_timer(spawn_bat, int(bat_interval * 0.5))
        if(event.type == spawn_slime and not (slimes_spawned >= total_slimes)):
            enemies.append(Slime.Slime((random.randint(100, 700), random.randint(100, 600))))
            slimes_spawned += 1
            pygame.time.set_timer(spawn_slime, int(slime_interval * 0.5))
        if(event.type == wavecheck and len(dead_enemies) >= total_bats + total_skeletons + total_slimes * 2 + total_slimes):
            show_menu = True
        if (event.type==pygame.KEYDOWN and event.key ==pygame.K_TAB):
                SPELL_INDEX+= 1 
                SPELL_TYPE= SPELL_TYPE_ARR[SPELL_INDEX%len(SPELL_TYPE_ARR)]
        if(event.type == pygame.MOUSEBUTTONDOWN):
            if show_menu:
                if button1.rect.collidepoint(pygame.mouse.get_pos()):
                    if(total_insight >= speed_cost):
                        total_insight -= speed_cost
                        speed_cost *= 2
                        player.speed += 1
                elif button2.rect.collidepoint(pygame.mouse.get_pos()):
                    if(total_insight >= health_cost):
                        total_insight -= health_cost
                        health_cost *= 2
                        player.health += 5
                elif button3.rect.collidepoint(pygame.mouse.get_pos()):
                    if(total_insight >= ammo_cost):
                        total_insight -= ammo_cost
                        ammo_cost *= 2
                        max_particles += 1
                elif button4.rect.collidepoint(pygame.mouse.get_pos()):
                    change_wave = True
                    show_menu = False
        
                
    
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
                    pygame.draw.rect(screen, (0,255,0),(skeleton.rect.x+3,skeleton.rect.y-7, skeleton.maxHealth,7))
                    pygame.draw.rect(screen, (255,0,0), ((skeleton.rect.x+skeleton.maxHealth+3)-(skeleton.maxHealth-skeleton.health),skeleton.rect.y-7, (skeleton.maxHealth-skeleton.health),7))
                else:
                    pygame.draw.rect(screen, (255,0,0), ((skeleton.rect.x+skeleton.maxHealth+3)-(skeleton.health),skeleton.rect.y-7, (skeleton.maxHealth),7))
                skeleton.takeDamage(particle)
                
    for insight in item_entities:
        if(pygame.Rect.colliderect(insight.rect, player.rect)):
            total_insight += 1
            item_entities.remove(insight)
          
    
    

    

    if (keys[pygame.K_SPACE]):
        if(SPELL_TYPE == 'dark'):
            player.health-=1
        if len(particles)< max_particles:
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

            particles.append(spell.Particle(round(player.rect.x + player.rect.width - 10), round(player.rect.y + player.rect.height - 25), SPELL_DISTANCE, SPELL_RADIUS, SPELL_XSPEED, SPELL_YSPEED, SPELL_TYPE))
            
    ########################################################################################
        

    


    
    
    for dead_enemy in dead_enemies:
        screen.blit(pygame.transform.scale(dead_enemy.image, (50, 60)), dead_enemy.rect)
   
    for skeleton in enemies:
        if(isinstance(skeleton, BringerOfDeath.BringerOfDeath)):
            screen.blit(pygame.transform.scale(skeleton.image, (400, 400)), skeleton.rect)
        else:
            screen.blit(pygame.transform.scale(skeleton.image, (50, 60)), skeleton.rect)
     
    for insight in item_entities:
        screen.blit(insight.image, insight.rect)
        
    screen.blit(pygame.transform.scale(player.image, (60,60)), player.rect)

    
    for skeleton in enemies:
        if (pygame.Rect.colliderect(player.rect, skeleton.rect) and skeleton.health > 0):
            if(isinstance(skeleton, Skeleton.Skeleton)): 
                player.takeDamage('skeleton')
            elif(isinstance(skeleton, Slime.Slime)):
                player.takeDamage('slime')
            elif(isinstance(skeleton, Bat.Bat)):
                player.takeDamage('bat')

    for skeleton in enemies:
        if(skeleton.health<=0):
            if(isinstance(skeleton, SmallSlime.SmallSlime)):
                pass
            elif(isinstance(skeleton, Slime.Slime)):
                enemies.append(SmallSlime.SmallSlime((skeleton.rect.x-10, skeleton.rect.y),skeleton))
                enemies.append(SmallSlime.SmallSlime((skeleton.rect.x+10, skeleton.rect.y), skeleton))
            skeleton.die()
            item_entities.append(Insight.Insight(skeleton.rect.x + 20, skeleton.rect.y + 25))
            dead_enemies.append(skeleton)
            enemies.remove(skeleton)
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


   
        
    
        

    
        
    
    #UI
    spellUI = pygame.Surface((200,100))  
    spellUI.set_alpha(128)              
    spellUI.fill((217, 201, 156))  
    currentSpellMessage = spellUIFont.render('Current Spell:', True, (148, 3, 10))
    colorSpell = spell.Particle(0,0,0,0,0,0,SPELL_TYPE)
    currentSpell = spellUIFont.render(SPELL_TYPE, True, colorSpell.color)

    spellUI.blit(currentSpellMessage, (30,20))
    spellUI.blit(currentSpell, (50, 45))
        
    screen.blit(spellUI, (SCREEN_WIDTH-210,20))

    #Insight
    insightUI = pygame.Surface((200,50))  
    insightUI.set_alpha(128)              
    insightUI.fill((217, 201, 156))
    currentInsightMessage = spellUIFont.render(f'Insight: {total_insight}', True, (148, 3, 10))
    
    insightUI.blit(currentInsightMessage, (0, 0))
    screen.blit(insightUI, (10, 10))
    
    #Wave
    waveUI = pygame.Surface((200,50))  
    waveUI.set_alpha(128)              
    waveUI.fill((217, 201, 156))
    currentWaveMessage = spellUIFont.render(f'Wave: {current_wave}', True, (148, 3, 10))
    
    waveUI.blit(currentWaveMessage, (0, 10))
    screen.blit(waveUI, (300, 10))
    
    if(show_menu):
        button1.draw(screen)
        button2.draw(screen)
        button3.draw(screen)
        button4.draw(screen)
    
    pygame.display.flip()
    clock.tick(20)
    screen.fill((0,0,0))
    
    

pygame.quit()