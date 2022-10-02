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
        self.rect.bottom = GameConstants.SCREEN_HEIGHT-220
        self.onGround = True
        self.yVel = 0
        self.xVel = 0
        self.currhealth = 10
        self.invinc = 0


    def update(self, pressed_keys):
        if pressed_keys[GameConstants.K_RIGHT]:
            self.xVel = 5
        if pressed_keys[GameConstants.K_LEFT]:
            self.xVel = -5
        if pressed_keys[GameConstants.K_UP]:
            if self.onGround:
                self.yVel -= 7.9
            self.rect.move_ip(0, self.yVel)
            self.onGround = False
        if self.onGround == False:
            self.yVel +=0.3
        
        
        self.rect.top += self.yVel

        if not pressed_keys[GameConstants.K_LEFT] and not pressed_keys[GameConstants.K_RIGHT]:
            self.xVel = 0
        self.rect.right +=self.xVel

        self.onGround = False


        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom >= GameConstants.SCREEN_HEIGHT:
            self.rect.bottom = GameConstants.SCREEN_HEIGHT
            self.onGround = True
        if self.rect.top <= 0:
            self.rect.top = 0

        #check invincibility
        if self.invinc != 0:
            self.invinc = self.invinc - 1
    def collision(self, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if self.yVel > 0:
                    self.yVel = 0
                    self.onGround = True
                    self.rect.bottom = p.rect.top
                if self.yVel < 0:
                    self.rect.top = p.rect.bottom
                if p.rect.left == self.rect.right:
                    self.rect.right = p.rect.left
                    self.xVel = 0
                if p.rect.right == self.rect.left:
                    self.rect.left = p.rect.right
                    self.xVel = 0
    
    def takeDamage(self,damage):
        if self.invinc == 0:
            self.currhealth = self.currhealth - damage
            self.invinc = 40
        if self.currhealth <= 0:
            return True
        return False

class healthBar(pygame.sprite.Sprite):
    def __init__(self):
        super(healthBar, self).__init__()
        self.length = 300
        self.height = 30
        self.surf = pygame.Surface((self.length,self.height))
        self.surf.fill((0,128,0))
        self.rect = self.surf.get_rect()
        self.rect.bottom = GameConstants.SCREEN_HEIGHT
        self.rect.left = 0

    def update(self, health):
        self.surf = pygame.Surface((health*30,self.height))
        self.surf.fill((0,128,0))
