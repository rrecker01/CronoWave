from operator import truediv
import pygame
import Player
import Enemy
import GameConstants
import Entities
import random
import Scroll

pygame.init()

running = True

screen = pygame.display.set_mode((GameConstants.SCREEN_WIDTH, GameConstants.SCREEN_HEIGHT))

screen.fill((255, 255, 255))

platform = pygame.sprite.Group()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

world = pygame.Surface((3*GameConstants.SCREEN_WIDTH, GameConstants.SCREEN_HEIGHT))


player = Player.PC()
weakEnemy = Enemy.weakEnemy(400, GameConstants.SCREEN_HEIGHT/4)
Oven = Enemy.Oven(600,100)


all_sprites.add(player)
all_sprites.add(weakEnemy)

platforms = []

x = 0
y = 0
map = ["                                                                                                                ",
"                                                                                                                ",
"                                                                                                                ",
"                                                                                                                ",
"                                                                                                                ",
"                                                                                                                ",
"                                                                                                                ",
"                                                                                                                ",
"                                                                                                                ",
"                                                                                                                ",
"                                                                                                                ",
"                                                                                                                ",
"                                                                                                                ",
"                                                                                                                ",
"                                                                                                                ",
"gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"]

for row in map:
    for col in row:
        if col == "g":
            g = Entities.Platform(x,y)
            platforms.append(g)
            platform.add(g)
        x += 44
    y += 44
    x = 0

player = Player.PC()


world_length = 3*GameConstants.SCREEN_WIDTH

world = pygame.Surface((world_length, GameConstants.SCREEN_HEIGHT))

camera = Scroll.Camera(player, world_length)



while running:

    timer = pygame.time.Clock()

    for event in pygame.event.get():
        if event.type == GameConstants.KEYDOWN:
            if event.key == GameConstants.K_ESCAPE:
                running = False
        elif event.type == GameConstants.QUIT:
            running = False

    player.collision(platforms)

    pressed_keys = pygame.key.get_pressed()

    movecheck = random.randint(0,100)

    player.update(pressed_keys)
    weakEnemy.update(movecheck)
    Oven.update(movecheck)
    camera.update()
   
    world.fill((255, 255, 255))
   
    i = 0
    while i < len(platforms):
        platforms[i].update
        world.blit(platforms[i].surf, platforms[i].rect)
        i += 1
   
    world.blit(player.surf, player.rect)

    world.blit(weakEnemy.surf, weakEnemy.rect)
    world.blit(Oven.surf, Oven.rect)
   
    camera.draw(world, screen)

    pygame.display.flip()

    timer.tick(70)




pygame.quit()