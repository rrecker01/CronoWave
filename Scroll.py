import pygame
import GameConstants

class Camera():
    def __init__(self, target, worldLength):
        super().__init__()
        self.target = target
        self.cam = target.rect
        self.worldLength = worldLength
        self.area = pygame.Rect(self.cam.left, self.cam.top, GameConstants.SCREEN_WIDTH, GameConstants.SCREEN_HEIGHT)

    def update(self):
        if self.target:
            self.cam.center = self.target.rect.center
            if self.cam.left <= 0:
                self.cam.left = 0
            if self.cam.right >= self.worldLength:
                self.cam.right = self.worldLength
            if self.cam.bottom >= GameConstants.SCREEN_HEIGHT:
                self.cam.bottom = GameConstants.SCREEN_HEIGHT
            

    def draw(self, surface, screen):
        screen.blit(surface, (-self.cam.left+GameConstants.SCREEN_WIDTH/2, 0))
        



            


