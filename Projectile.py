from cmath import rect
import re
import pygame
import GameConstants
import random

class wave(pygame.sprite.Sprite):
    def __init__(self, x, y, facing):
        super(wave, self).__init__()
        self.facing = facing
        self.surf = pygame.image.load("Sprites/waveprojectike.png").convert_alpha()
        self.rect = self.surf.get_rect()
        if facing == "left":
            self.rect.right = x
        else:
            self.rect.left = x
        self.rect.bottom = y

    def update(self):
        if self.facing == "left":
            self.rect.move_ip(-4, 0)
        else:
            self.rect.move_ip(4,0)
    

    


class waveEnemy(pygame.sprite.Sprite):
    def __init__(self, x, y, facing):
        super(waveEnemy, self).__init__()
        self.surf = pygame.image.load("Sprites/waveprojectikegreen.png")
        self.rect = self.surf.get_rect()
        self.rect.left = x
        self.rect.bottom = y
        self.facing = facing
        self.damage = 1

    def update(self):
        self.rect.move_ip(2*self.facing,0)

        #check borders
        if self.rect.left < 0:
            return False
        if self.rect.right > GameConstants.SCREEN_WIDTH:
            return False
    
    def returnDamage(self):
        return self.damage
    
class grenade(pygame.sprite.Sprite):
    def __init__(self,x, y, facing):
        super(grenade, self).__init__()
        #change image
        self.surf = pygame.image.load("Sprites/coalattack.png")
        self.rect = self.surf.get_rect()
        self.rect.left = x
        self.rect.bottom = y
        self.facing = facing
        self.damage = 2
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

    def returnDamage(self):
        return self.damage