import pygame
import GameConstants
import random

class wave(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
    

    def draw(self,window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

class waveEnemy(pygame.sprite.Sprite):
    def __init__(self, x, y, facing):
        super(waveEnemy, self).__init__()
        self.surf = pygame.image.load("Sprites/waveprojectike.png")
        self.rect = self.surf.get_rect()
        self.rect.left = x
        self.rect.bottom = y
        self.facing = facing

    def update(self):
        self.rect.move_ip(2*self.facing,0)

        #check borders
        if self.rect.left < 0:
            return False
        if self.rect.right > GameConstants.SCREEN_WIDTH:
            return False

class grenade(pygame.sprite.Sprite):
    def __init__(self,x, y, facing):
        super(grenade, self).__init__()
        #change image
        self.surf = pygame.image.load("Sprites/waveprojectike.png")
        self.rect = self.surf.get_rect()
        self.rect.left = x
        self.rect.bottom = y
        self.facing = facing
        self.gravity = -3
    
    def update(self):
        value = random.randint(0,15)
        if value != 1:
            value = 0
        self.gravity = self.gravity + value
        self.rect.move_ip(2*self.facing, self.gravity)

        #check borders
        if self.rect.left < 0:
            return False
        if self.rect.right > GameConstants.SCREEN_WIDTH:
            return False
        if self.rect.bottom >= GameConstants.SCREEN_HEIGHT:
            return False
