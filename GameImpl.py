from operator import truediv
import pygame
import Player
import Enemy
import Projectile
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
weakEn = pygame.sprite.Group()

world = pygame.Surface((3*GameConstants.SCREEN_WIDTH, GameConstants.SCREEN_HEIGHT))
bg = pygame.image.load("Sprites\chernobylfloor1.png")



player = Player.PC()
weakEnemy = Enemy.weakEnemy(400, 500)
Oven = Enemy.Oven(600, 400)
health = Player.healthBar()

all_sprites.add(player)
all_sprites.add(weakEnemy)

enemies.add(weakEnemy)
enemies.add(Oven)

weakEn.add(weakEnemy) 
ovenMan.add(Oven)



all_sprites.add(player)
playerProjectiles = []
playerShootCooldown = 0
bulletDirection = "right"
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
"                          e                             lp p p pr                                               ",
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
            
            if event.key == GameConstants.K_LEFT:
                bulletDirection = "left"
                #wx = player.rect.left
            elif event.key == GameConstants.K_RIGHT:
                bulletDirection = "right"
                #wx = player.rect.right
            if event.key == GameConstants.K_SPACE:
                if playerShootCooldown == 0:
                    playerShootCooldown = 60
                    if bulletDirection == "left":
                        wx = player.rect.left
                    else:
                        wx = player.rect.right
                    wy = (player.rect.bottom + player.rect.top)/2
                    newWave = Projectile.wave(wx, wy, bulletDirection)
                    playerProjectiles.append(newWave)
        elif event.type == GameConstants.QUIT:
            running = False

    player.collision(platforms)

    pressed_keys = pygame.key.get_pressed()

    movecheck = random.randint(0,100)

    i = 0
    while i < len(playerProjectiles):
        playerProjectiles[i].update()
        i+=1

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

    for enemy in weakEn:
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

    for wave in playerProjectiles:
        world.blit(wave.surf, wave.rect) 
    for waveEnemy in enemyBullet:
        world.blit(waveEnemy.surf, waveEnemy.rect)
    for gre in grenade:
        world.blit(gre.surf, gre.rect)
    camera.draw(world, screen)
    screen.blit(health.surf, health.rect)

  

    if pygame.sprite.spritecollideany(player, proj):
        collision = pygame.sprite.spritecollide(player, proj, False)
        if collision:
            death = player.takeDamage(collision[0].damage)
            health.update(player.currhealth)

            if death:
                player.kill()
                running = False

    pygame.display.flip()
    if playerShootCooldown > 0:
        playerShootCooldown = playerShootCooldown -1
    timer.tick(140)




pygame.quit()