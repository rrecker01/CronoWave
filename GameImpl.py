from operator import truediv
import pygame
import Player
import Enemy
import GameConstants
import Entities
import random
import Scroll
import Projectile

pygame.init()

running = True

screen = pygame.display.set_mode((GameConstants.SCREEN_WIDTH, GameConstants.SCREEN_HEIGHT))

screen.fill((255, 255, 255))

platform = pygame.sprite.Group()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
ovenMan = pygame.sprite.Group()
proj = pygame.sprite.Group()

world = pygame.Surface((3*GameConstants.SCREEN_WIDTH, GameConstants.SCREEN_HEIGHT))
bg = pygame.image.load("Sprites\chernobylfloor1.png")



player = Player.PC()


all_sprites.add(player)

platforms = []
enemies_map = []

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
            enemies.add(e)
            enemies_map.append(e)
        elif col == "e":
            e = Enemy.weakEnemy(x,y)
            enemies.add(e)
            enemies_map.append(e)
        x += 44
    y += 44
    x = 0

player = Player.PC()


world_length = 3*GameConstants.SCREEN_WIDTH

world = pygame.Surface((world_length, GameConstants.SCREEN_HEIGHT))

camera = Scroll.Camera(player, world_length)

enemyBullet = []
grenade = []

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
    while i < len(enemies_map):
        world.blit(enemies_map[i].surf, enemies_map[i].rect)
        enemies_map[i].collision(platforms)
        enemies_map[i].update(1)
        i += 1

    for enemy in enemies:
        val = enemy.shoot()
        if val != 0:
            shot = Projectile.waveEnemy(round((enemy.rect.left + enemy.rect.right)//2), round((enemy.rect.bottom + enemy.rect.top)//2), enemy.speed)
            proj.add(shot)
            enemyBullet.append(shot)
    
    for oven in ovenMan:
        val2 = oven.shoot2()
        if val2 != 0:
            shot2 = Projectile.grenade(round((oven.rect.left + oven.rect.right)//2), round((oven.rect.bottom + oven.rect.top)//2), enemy.speed)
            grenade.append(shot2)
            proj.add(shot2)
    for waveEnemy in enemyBullet:
       die= waveEnemy.update()
       if die:
        waveEnemy.kill()
    for gre in grenade:
       die= gre.update()
       if die:
        gre.kill()
    
   
    world.blit(player.surf, player.rect)

    
    for waveEnemy in enemyBullet:
        world.blit(waveEnemy.surf, waveEnemy.rect)
    for gre in grenade:
        world.blit(gre.surf, gre.rect)
    camera.draw(world, screen)

  

    if pygame.sprite.spritecollideany(player, proj):
        player.kill()
        running = False

    pygame.display.flip()

    timer.tick(60)




pygame.quit()