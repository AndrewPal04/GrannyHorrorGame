# Horror granny game
#   - you are trying to escape your crazy granny
#   - there is up to 5 different items for you to find to use inside the game
#   - Items: Taser (stuns), Flashlight (see better in dark), Pennies (distract)
#   - you can crouch in the game and hide in cabinents
#   - I want the game to look like a pixel 2d game
#   - there is 3 locks on the door and you have to find the keys to escape.
#   - Granny is only trying to hunt you down if you make a lot of noise or if she sees you outside your room
#   - She will not chase you in your Room or your restroom


#Set up a starting pygame loop and create the screen size, clock, etc.
import pygame
from classes import Background, Player

pygame.init()
screen_width, screen_height=1500,1000
screen=pygame.display.set_mode((screen_width,screen_height))
clock=pygame.time.Clock()

#Create objects
sprite_group=pygame.sprite.Group()

floorOneIMG=pygame.image.load("HorrorFloorOne.png")
floorOne=Background(screen,floorOneIMG,1,750,500)

jackIMG=pygame.image.load("jack.png")
jack=Player(jackIMG,0.09,200,800)

grannyIMG=pygame.image.load("granny.png")
granny=Player(grannyIMG,0.09,200,200)

sprite_group.add(jack)
sprite_group.add(granny)

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
    while True:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        #Workspace
        floorOne.draw()
        sprite_group.draw(screen)
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
        wall8Rect = pygame.Rect(100, 700, 250, 20)
        wall9Rect = pygame.Rect(640, 240, 220, 60)
        wall10Rect = pygame.Rect(700, 330, 100, 50)
        wall11Rect = pygame.Rect(830, 330, 40, 60)
        wall12Rect = pygame.Rect(1130, 700, 300, 20)
        wall13Rect = pygame.Rect(1080, 780, 330, 150)
        wall14Rect = pygame.Rect(1160, 470, 330, 20)
        wall15Rect=pygame.Rect(999,470,80,10)
        walls=[wall1Rect,wall2Rect,wall3Rect,wall4Rect,wall5Rect,wall6Rect,wall7Rect,wall8Rect,wall9Rect,wall10Rect,wall11Rect,wall12Rect,wall13Rect,wall14Rect,wall15Rect]
        #Checking for collision
        for i in range(len(walls)):
            if jack.rect.colliderect(walls[i]):
                obstacle(jack,walls[i])
        #drawing all walls red
        for i in walls:
            pygame.draw.rect(screen,(255,0,0),i)
        
        # pygame.draw.rect(screen,(0,255,0),wall2Rect)  #This will highlight the wall2 as green 
        

        pygame.display.update()
        clock.tick(60)

firstFloor()

#Homework
#Complete all of the walls and collision using the new logic we added in
#Also, try to add in the second floor (new function)
#And make sure to add a rectangle for the stairs, but don't add it into the
#list of walls, since that one will work differently
#Good Luck!