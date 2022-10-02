from cmath import rect
import re
import pygame
import GameConstants

class wave(pygame.sprite.Sprite):
    def __init__(self, x, y, facing):
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
    

    