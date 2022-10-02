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


player = Player.PC()
weakEnemy = Enemy.weakEnemy(400, GameConstants.SCREEN_HEIGHT-100)
Oven = Enemy.Oven(600, 800)


all_sprites.add(player)
all_sprites.add(weakEnemy)

enemies.add(weakEnemy)
enemies.add(Oven)

ovenMan.add(Oven)

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

    pressed_keys = pygame.key.get_pressed()

    player.gravity()
    movecheck = random.randint(0,100)

    player.update(pressed_keys)
    weakEnemy.update(movecheck)
    Oven.update(movecheck)

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
    
    for waveEnemy in enemyBullet:
        world.blit(waveEnemy.surf, waveEnemy.rect)
    for gre in grenade:
        world.blit(gre.surf, gre.rect)
    camera.draw(world, screen)

    

    

    if pygame.sprite.spritecollideany(player, platform):
        collision = pygame.sprite.spritecollide(player, platform, False)
        if collision:
            if player.rect.bottom -1 == collision[0].rect.top:
                player.rect.bottom = collision[0].rect.top
            if player.rect.top + 1 == collision[0].rect.bottom:
                player.gravity()

    if pygame.sprite.spritecollideany(player, proj):
        player.kill()
        running = False
    pygame.display.flip()

    timer.tick(140)




pygame.quit()