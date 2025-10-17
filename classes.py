import pygame
import math


class Text():
    def __init__(self,surface, text, size, color, x, y):
        font_name = pygame.font.match_font('arial')
        self.surface = surface
        self.text = text 
        self.size = size
        self.font = pygame.font.Font(font_name, self.size)
        self.color=color
        self.x=x
        self.y=y
    def draw(self):
        text_surface=self.font.render(self.text, True,self.color)
        text_rect =text_surface.get_rect()
        text_rect.midtop = (self.x, self.y)
        self.surface.blit(text_surface ,text_rect)

class Background(pygame.sprite.Sprite):
    def __init__(self, surface, image, scale, x, y):
        pygame.sprite.Sprite.__init__(self)
        #width/height
        self.surface=surface
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, ((int(width * scale)),int(height * scale)))
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
    def draw(self):
        self.surface.blit(self.image,(self.rect.x,self.rect.y))


class Player(pygame.sprite.Sprite):
    def __init__(self, image, scale, x, y):
        pygame.sprite.Sprite.__init__(self)
        #width/height
        self.speed=3
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, ((int(width * scale)),int(height * scale)))
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
    def update(self):
        keystate=pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.rect.y-=self.speed
        if keystate[pygame.K_s]:
            self.rect.y+=self.speed
        if keystate[pygame.K_d]:
            self.rect.x+=self.speed
        if keystate[pygame.K_a]:
            self.rect.x-=self.speed
    def chase(self,target):
        distance=math.hypot(target.rect.x-self.rect.x, target.rect.y-self.rect.y)
        if distance < 200:
            if target.rect.x>self.rect.x:
                self.rect.x+=1.5
            if target.rect.x<self.rect.x:
                self.rect.x-=1.5
            if target.rect.y>self.rect.y:
                self.rect.y+=1.5
            if target.rect.y<self.rect.y:
                self.rect.y-=1.5
        #IF she isn't close to us, will she be still or move randomly?
