from turtle import ondrag
import pygame
import GameConstants

class PC(pygame.sprite.Sprite):

    def __init__(self):
        super(PC, self).__init__()
        self.surf = pygame.image.load("Sprites/protagspri.png").convert_alpha()
        self.surf.set_colorkey((255, 255, 255), GameConstants.RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.left = GameConstants.SCREEN_WIDTH/2
        self.rect.bottom = GameConstants.SCREEN_HEIGHT-45
        self.onGround = True
        self.yVel = 0

    def update(self, pressed_keys):
        if pressed_keys[GameConstants.K_RIGHT]:
            self.rect.move_ip(1, 0)
        if pressed_keys[GameConstants.K_LEFT]:
            self.rect.move_ip(-1,0)
        if pressed_keys[GameConstants.K_UP]:
            if self.onGround:
                self.yVel -= 7.9
            self.rect.move_ip(0, self.yVel)
            self.onGround = False
        if self.onGround == False:
            self.yVel +=0.3
        if pressed_keys[GameConstants.K_SPACE]:
            print("hello_world")
        
        self.rect.top += self.yVel


        if self.rect.left < 0:
            self.rect.left = 0
        #if self.rect.right > GameConstants.SCREEN_WIDTH:
         #   self.rect.right = GameConstants.SCREEN_WIDTH
        if self.rect.bottom >= GameConstants.SCREEN_HEIGHT:
            self.rect.bottom = GameConstants.SCREEN_HEIGHT
            self.onGround = True
        if self.rect.top <= 0:
            self.rect.top = 0
    
    def collision(self, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if self.yVel > 0:
                    self.yVel = 0
                    self.onGround = True
                    self.rect.bottom = p.rect.top
                if self.yVel < 0:
                    self.rect.bottom = p.rect.top
