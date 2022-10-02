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
bg = pygame.image.load("Sprites\chernobylfloor1.png")



player = Player.PC()


all_sprites.add(player)

platforms = []
enemies = []

x = 0
y = 0
map = ["                                                                                                                ",
"                                                                                                                ",
"                                                                                                                ",
"                                                                                                                ",
"                                                                                                                ",
"                                                                                                                ",
"                                                                                                                ",
"                          e                             p p p p                                                 ",
"                       lp p pr                  lp pr                                                            ",
"                                                                                                                ",
"                                                                                                                ",
"gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg",
"uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu",
"uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu",
"uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu",
"uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu"]

for row in map:
    for col in row:
        if col == "u" or col == "p" or col == "g" or col == "r" or col == "l":
            g = Entities.Platform(x,y, col)
            platforms.append(g)
            platform.add(g)
        elif col == "o":
            e = Enemy.Oven(x,y)
            all_sprites.add(e)
            enemies.append(e)
        elif col == "e":
            e = Enemy.weakEnemy(x,y)
            all_sprites.add(e)
            enemies.append(e)
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
    camera.update()

    world.fill((0,0,0))
   
    world.blit(bg, (0,0))
    world.blit(bg, (1800 ,0))
    world.blit(bg, (3600 ,0))

   
    i = 0
    while i < len(platforms):
        platforms[i].update
        world.blit(platforms[i].surf, platforms[i].rect)
        i += 1

    i = 0
    while i < len(enemies):
        world.blit(enemies[i].surf, enemies[i].rect)
        enemies[i].collision(platforms)
        enemies[i].update(1)
        i += 1
    
   
    world.blit(player.surf, player.rect)
   
    camera.draw(world, screen)

    pygame.display.flip()

    timer.tick(70)




pygame.quit()