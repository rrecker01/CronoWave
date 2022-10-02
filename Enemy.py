import pygame
import GameConstants
import random
import Projectile


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
        self.cool = 90

    def update(self):
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
        
    def shoot(self):
        #check to shoot
        if self.cool == 0:
            self.cool = 300
            return self.speed
        else:
            self.cool = self.cool - 1
            return 0


class Oven(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Oven, self).__init__()
        self.surf = pygame.image.load("Sprites/ovenman.png").convert_alpha()
        self.surf.set_colorkey((255,255,255), GameConstants.RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.left = x
        self.rect.bottom = y
        self.onGround = False
        self.yVel = 0
        self.speed = -1
        self.cool = 90
        self.cool2 = 100

    def update(self):
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

    def shoot(self):
        #check to shoot
        if self.cool == 0:
            self.cool = 60
            return self.speed
        else:
            self.cool = self.cool - 1
            return 0
    def shoot2(self):
        #check to shoot
        if self.cool2 == 0:
            self.cool2 = 90
            return self.speed
        else:
            self.cool2 = self.cool2 - 1
            return 0


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
