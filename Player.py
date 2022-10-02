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

    def update(self, pressed_keys):
        if pressed_keys[GameConstants.K_RIGHT]:
            self.rect.move_ip(1, 0)
        if pressed_keys[GameConstants.K_LEFT]:
            self.rect.move_ip(-1,0)
        if pressed_keys[GameConstants.K_UP]:
            self.rect.move_ip(0, -2)
        if pressed_keys[GameConstants.K_SPACE]:
            print("hello_world")


        if self.rect.left < 0:
            self.rect.left = 0
        #if self.rect.right > GameConstants.SCREEN_WIDTH:
         #   self.rect.right = GameConstants.SCREEN_WIDTH
        if self.rect.bottom >= GameConstants.SCREEN_HEIGHT:
            self.rect.bottom = GameConstants.SCREEN_HEIGHT
        if self.rect.top <= 0:
            self.rect.top = 0

    def gravity(self):
        self.rect.move_ip(0, 1)    

    

