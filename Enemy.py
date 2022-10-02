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
        self.onGround = False
        self.yVel = 0
        self.speed = -1
        self.timer = random.randint(22, 28)
    def update(self, move):
        if move <= self.timer:
            self.rect.move_ip(self.speed, 0)
        
        if not self.onGround:
            self.yVel += 0.3

        self.rect.top += self.yVel
        self.onGround = False

    def collision(self, platforms):
        for p in platforms:
            if p.rect.topleft == self.rect.bottomleft or p.rect.topright == self.rect.bottomright:
                self.speed = -self.speed
            if pygame.sprite.collide_rect(self, p):
                if self.yVel > 0:
                    self.yVel = 0
                    self.onGround = True
                    self.rect.bottom = p.rect.top

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
    
    def collision(self, platforms):
        for p in platforms:
            if not pygame.sprite.collide_rect(self, p):
                self.speed = -self.speed


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
