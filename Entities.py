import pygame
import GameConstants


class Platform(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        super(Platform, self).__init__()
        self.surf = pygame.image.load("Sprites/insidegroundtile.png")
        self.surf.set_colorkey((255, 255, 255), GameConstants.RLEACCEL)
        self.rect = self.surf.get_rect(midtop=(x,y))
        self.left = x
        self.top = y



    def update(self, pressed_keys):
       if pressed_keys[GameConstants.K_RIGHT]:
            self.rect.move_ip(-1, 0)
       if pressed_keys[GameConstants.K_LEFT]:
            self.rect.move_ip(1,0)