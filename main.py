
import pygame, random
from classes import Background, Player, Text

pygame.init()
screen_width, screen_height=1500,1000
screen=pygame.display.set_mode((screen_width,screen_height))
clock=pygame.time.Clock()

#Create objects
sprite_group=pygame.sprite.Group()
jackIMG=pygame.image.load("jack.png")
jack=Player(jackIMG,0.09,200,800)

#dark
darkIMG=pygame.image.load("dark1.png")
dark=Background(screen,darkIMG,0.5,jack.rect.x-1400,jack.rect.y-900)
fdark=Background(screen,darkIMG,0.7,jack.rect.x-1400,jack.rect.y-900)

#granny
grannyIMG=pygame.image.load("granny.png")
granny=Player(grannyIMG,0.09,200,200)

#flashlight
flashlightIMG=pygame.image.load("flashlight.png")
flashlight=Background(screen,flashlightIMG,0.04,1420,555)
haveFlashlight=False

#Losing Text
loseText=Text(screen,"You Lose!",100,(255,0,0),screen_width//2,screen_height//2)

#Key
keyIMG=pygame.image.load("key.png")
key=Background(screen,keyIMG,0.04,50,314)
haveKey=False

sprite_group.add(jack)

def obstacle(user, obstacle):
    a = user.rect
    b = obstacle
    overlap_left = a.right - b.left
    overlap_right = b.right - a.left
    overlap_top = a.bottom - b.top
    overlap_bottom = b.bottom - a.top
    min_x = overlap_left if overlap_left < overlap_right else overlap_right
    min_y = overlap_top if overlap_top < overlap_bottom else overlap_bottom
    if min_x < min_y:
        if overlap_left < overlap_right:
            a.right = b.left
        else:
            a.left = b.right
    else:
        if overlap_top < overlap_bottom:
            a.bottom = b.top
        else:
            a.top = b.bottom

def firstFloor():
    global haveFlashlight, dark, haveKey, key
    floorOneIMG=pygame.image.load("HorrorFloorOne.png")
    floorOne=Background(screen,floorOneIMG,1,750,500)
    sprite_group.add(granny)
    if haveKey:
        if key in sprite_group:
            sprite_group.remove(key)
    else:
        sprite_group.add(key)
    if not haveFlashlight:
        sprite_group.add(flashlight)
    else:
        if flashlight in sprite_group:
            sprite_group.remove(flashlight)
        
    if haveFlashlight:
        sprite_group.add(fdark)
    else:
        sprite_group.add(dark)
    
    granny.rect.x=200
    granny.rect.y=200
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        #Workspace
        keystate=pygame.key.get_pressed()
        floorOne.draw()
        sprite_group.draw(screen)
        if haveFlashlight:
            fdark.rect.x=jack.rect.x-2000
            fdark.rect.y=jack.rect.y-1200
        else:
            dark.rect.x=jack.rect.x-1400
            dark.rect.y=jack.rect.y-900
        jack.update()
        granny.chase(jack)
        #get rid of them later

        print("x",jack.rect.x,"y",jack.rect.y)
        # House Boundaries in first floor
        if jack.rect.x>1435:
            jack.rect.x=1435
        if jack.rect.x<14:
            jack.rect.x=14
        if jack.rect.y>880:
            jack.rect.y=880
        if jack.rect.y<25:
            jack.rect.y=25

        #                     x   y   w   h
        wall1Rect=pygame.Rect(460,340,25,230)
        wall2Rect=pygame.Rect(0,580,790,10)
        wall3Rect=pygame.Rect(460,100,25,100)
        wall4Rect=pygame.Rect(970,200,10,500)
        wall5Rect=pygame.Rect(950,100,10,100)
        wall6Rect=pygame.Rect(10,760,150,500)
        wall7Rect=pygame.Rect(999,280,180,10)
        wall8Rect = pygame.Rect(340, 620, 10, 90)
        wall9Rect = pygame.Rect(690, 300, 130, 70)
        wall10Rect = pygame.Rect(700, 330, 100, 50)
        wall11Rect = pygame.Rect(880, 350, 40, 60)
        wall12Rect = pygame.Rect(1130, 700, 300, 20)
        wall13Rect = pygame.Rect(1100, 720, 330, 150)
        wall14Rect = pygame.Rect(1160, 470, 330, 20)
        wall15Rect=pygame.Rect(999,470,80,10)
        wall16Rect = pygame.Rect(720, 620, 10, 100)
        wall17Rect = pygame.Rect(340, 840, 10, 90)
        wall18Rect = pygame.Rect(720, 840, 10, 90)
        wall19Rect = pygame.Rect(970, 840, 10, 90)
        stairsRect= pygame.Rect(1360, 40, 110, 160)
        walls=[wall8Rect,wall9Rect,wall10Rect,wall11Rect,wall12Rect,wall13Rect,wall14Rect,wall15Rect,wall1Rect,wall2Rect,wall3Rect,wall4Rect,wall5Rect,wall6Rect,wall7Rect,wall8Rect,wall9Rect,wall10Rect,wall11Rect,wall12Rect,wall13Rect,wall14Rect,wall15Rect,wall16Rect,wall17Rect,wall18Rect,wall19Rect]
        #Checking for collision
        for i in range(len(walls)):
            if jack.rect.colliderect(walls[i]):
                obstacle(jack,walls[i])
        for i in range(len(walls)):
            if granny.rect.colliderect(walls[i]):
                obstacle(granny,walls[i])
        if jack.rect.colliderect(stairsRect):
            secondFloor()
        if jack.rect.colliderect(flashlight.rect):
            if keystate[pygame.K_e]:
                if not haveFlashlight:
                    haveFlashlight=True
                    sprite_group.remove(flashlight)
                    sprite_group.add(fdark)
                    sprite_group.remove(dark)
        if jack.rect.colliderect(granny.rect):
            loseText.draw()
            pygame.display.update()
            pygame.time.delay(2000)
            pygame.quit()
            quit()
        if jack.rect.colliderect(key.rect):
            if keystate[pygame.K_e]:
                if not haveKey:
                    haveKey=True
                    sprite_group.remove(key)
                
        #drawing all walls red
        # for i in walls:
        #     pygame.draw.rect(screen,(255,0,0),i)
        
        # pygame.draw.rect(screen,(0,255,0),wall2Rect)  #This will highlight the wall2 as green 
        pygame.display.update()
        clock.tick(60)
    
def secondFloor():
    floorTwoIMG = pygame.image.load("attic.png")
    floorTwo = Background(screen, floorTwoIMG, 1, 750, 500)
    sprite_group.remove(granny)
    if flashlight in sprite_group:
        sprite_group.remove(flashlight)
    if key in sprite_group:
        sprite_group.remove(key)
    granny.rect.x=2000
    granny.rect.y=2000
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        floorTwo.draw()
        sprite_group.draw(screen)
        jack.update()

        # Same screen size and movement boundaries
        if jack.rect.x > 1435:
            jack.rect.x = 1435
        if jack.rect.x < 14:
            jack.rect.x = 14
        if jack.rect.y > 880:
            jack.rect.y = 880
        if jack.rect.y < 25:
            jack.rect.y = 25

        couchRect = pygame.Rect(780, 250, 420, 160)             # Couch
        wardrobeRect = pygame.Rect(120, 180, 200, 300)          # Wardrobe
        boxesRect = pygame.Rect(120, 580, 260, 200)             # Boxes stack
        lampRect = pygame.Rect(1100, 630, 60, 140)               # Floor lamp  
        crackedWindowRect = pygame.Rect(220, 90, 120, 120)      # Window above wardrobe

        walls = [
            couchRect, wardrobeRect, boxesRect, tvRect,
            lampRect,  crackedWindowRect
        ]
        for w in walls:
            if jack.rect.colliderect(w):
                obstacle(jack, w)
            # pygame.draw.rect(screen, (255, 0, 0), w)


        pygame.display.update()
        clock.tick(60)


firstFloor()
secondFloor()

