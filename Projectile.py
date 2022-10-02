import pygame
import GameConstants

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
        self.x = x
        self.y = y
        self.facing = facing
        self.vel = 8 * facing
