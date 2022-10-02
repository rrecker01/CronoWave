import pygame
import GameConstants
import random



class weakEnemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(weakEnemy, self).__init__()
        self.surf = pygame.image.load("Sprites/weakenemy.png").convert_alpha()
        self.surf.set_colorkey((255,255,255), GameConstants.RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.left = x
        self.rect.bottom = y
        self.speed = random.randint(0,1)
        if self.speed == 0:
            self.speed = -1
        self.timer = random.randint(22, 28)
    def update(self, move):
        if move <= self.timer:
            self.rect.move_ip(0, 0)
        
        if self.rect.left < 0:
            self.rect.left = 0
            self.speed = -self.speed
        if self.rect.right > GameConstants.SCREEN_WIDTH:
            self.rect.right = GameConstants.SCREEN_WIDTH
            self.speed = -self.speed
        if self.rect.bottom >= GameConstants.SCREEN_HEIGHT:
            self.rect.bottom = GameConstants.SCREEN_HEIGHT
        if self.rect.top <= 0:
            self.rect.top = 0

class Oven(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Oven, self).__init__()
        self.surf = pygame.image.load("Sprites/ovenman.png").convert_alpha()
        self.surf.set_colorkey((255,255,255), GameConstants.RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.left = x
        self.rect.bottom = y
        self.speed = random.randint(0,1)
        if self.speed == 0:
            self.speed = -1
        self.timer = random.randint(4,7)
    def update(self, move):
        if move <= self.timer:
            self.rect.move_ip(self.speed,0)
        if self.rect.left < 0:
            self.rect.left = 0
            self.speed = -self.speed
        if self.rect.right > GameConstants.SCREEN_WIDTH:
            self.rect.right = GameConstants.SCREEN_WIDTH
            self.speed = -self.speed
        if self.rect.bottom >= GameConstants.SCREEN_HEIGHT:
            self.rect.bottom = GameConstants.SCREEN_HEIGHT
        if self.rect.top <= 0:
            self.rect.top = 0

class Idol(pygame.sprite.Sprite):
    def __init__(self):
        super(Idol, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

class WorldOven(pygame.sprite.Sprite):
    def __init__(self):
        super(WorldOven, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
