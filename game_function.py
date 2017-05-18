import sys

import pygame

from bullet import Bullet
from enemy import EnemyB
from enemy import EnemyG
from enemy import EnemyR
from time import sleep

def check_keydown_events(event,plane):
    """响应按下"""
    if event.key == pygame.K_RIGHT:
        plane.moving_right = True
    if event.key == pygame.K_LEFT:
        plane.moving_left = True
    if event.key == pygame.K_DOWN:
        plane.moving_down = True
    if event.key == pygame.K_UP:
        plane.moving_up = True

def check_keyup_events(event,plane):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        plane.moving_right = False
    if event.key == pygame.K_LEFT:
        plane.moving_left = False
    if event.key == pygame.K_DOWN:
        plane.moving_down = False
    if event.key == pygame.K_UP:
        plane.moving_up = False

def check_events(plane):
    """响应键鼠"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,plane)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,plane)


def update_screen(ai_settings,screen,plane,enemiesB,enemiesG,enemiesR,bullets):
    # 时钟
    clock = pygame.time.Clock()
    #控制帧率
    clock.tick(ai_settings.frame_rate)
    ai_settings.ticks+=1
    screen.fill(ai_settings.bg_color)
    #产生飞机
    plane.blitme()
    #固定产生蓝色敌人
    if ai_settings.ticks%ai_settings.enemyB_rate==0:
        new_enemyB=EnemyB(ai_settings,screen)
        enemiesB.add(new_enemyB)
    for enemyB in enemiesB.sprites():
        enemyB.blitme()
    # 固定产生绿色敌人
    if ai_settings.ticks % ai_settings.enemyG_rate == 0:
        new_enemyG = EnemyG(ai_settings, screen)
        enemiesG.add(new_enemyG)
    for enemyG in enemiesG.sprites():
        enemyG.blitme()
    # 固定产生红色敌人
    if ai_settings.ticks % ai_settings.enemyR_rate == 0:
        new_enemyR = EnemyR(ai_settings, screen)
        enemiesR.add(new_enemyR)
    for enemyR in enemiesR.sprites():
        enemyR.blitme()
    #固定产生子弹
    if ai_settings.ticks%ai_settings.bullet_rate==0:
        new_bullet=Bullet(ai_settings,screen,plane)
        bullets.add(new_bullet)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

def update_bullets(bullets,enemiesB,enemiesG,enemiesR):
    """更新子弹位置，并删除已消失的子弹"""
    bullets.update()
    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #检查是否有子弹击中敌人，如果有就删除相应子弹和敌人
    check_bullet_enemy_collisions(bullets,enemiesB,enemiesG,enemiesR)

def check_bullet_enemy_collisions(bullets,enemiesB,enemiesG,enemiesR):
    #collisions = pygame.sprite.groupcollide(bullets, enemiesB, True, True)
    for bullet in bullets.copy():
        for enemyB in enemiesB.copy():
            if pygame.sprite.collide_rect(bullet,enemyB):
                if enemyB.life_point-bullet.life<=0:
                    enemiesB.remove(enemyB)
                    bullets.remove(bullet)
                else:
                    bullets.remove(bullet)
                    enemyB.life_point-=bullet.life
        for enemyG in enemiesG.copy():
            if pygame.sprite.collide_rect(bullet,enemyG):
                if enemyG.life_point-bullet.life<=0:
                    enemiesG.remove(enemyG)
                    bullets.remove(bullet)
                else:
                    bullets.remove(bullet)
                    enemyG.life_point-=bullet.life
        for enemyR in enemiesR.copy():
            if pygame.sprite.collide_rect(bullet,enemyR):
                if enemyR.life_point-bullet.life<=0:
                    enemiesR.remove(enemyR)
                    bullets.remove(bullet)
                else:
                    bullets.remove(bullet)
                    enemyR.life_point-=bullet.life

def plane_hit(ai_settings,state,screen,plane,enemiesB,enemiesG,enemiesR,bullets):
    """响应被敌人撞到的飞机"""

    # 清空敌人和子弹列表
    enemiesB.empty()
    enemiesG.empty()
    enemiesR.empty()
    bullets.empty()

    # 飞机初始化
    plane.center_plane()

    if state.plane_left>0:
        #ship_left减1
        state.plane_left-=1
        # 暂停
        sleep(1)
    else:
        state.game_active=False

def update_enemy(ai_settings,plane,enemiesB,enemiesG,enemiesR,bullets,state,screen):
    enemiesB.update()
    #删除消失的敌人
    for enemyB in enemiesB.copy():
        if enemyB.rect.top >= screen.get_rect().bottom:
            enemiesB.remove(enemyB)

    #检测敌人和飞机碰撞
    if pygame.sprite.spritecollideany(plane,enemiesB):
        print("Shit!")
        plane_hit(ai_settings,state,screen,plane,enemiesB,enemiesG,enemiesR,bullets)

    enemiesG.update()
    # 删除消失的敌人
    for enemyG in enemiesG.copy():
        if enemyG.rect.top >= screen.get_rect().bottom:
            enemiesG.remove(enemyG)

    # 检测敌人和飞机碰撞
    if pygame.sprite.spritecollideany(plane, enemiesG):
        print("Shit!")
        plane_hit(ai_settings, state, screen, plane, enemiesB, enemiesG, enemiesR, bullets)

    enemiesR.update()
    # 删除消失的敌人
    for enemyR in enemiesR.copy():
        if enemyR.rect.top >= screen.get_rect().bottom:
            enemiesR.remove(enemyR)

    # 检测敌人和飞机碰撞
    if pygame.sprite.spritecollideany(plane, enemiesR):
        print("Shit!")
        plane_hit(ai_settings, state, screen, plane, enemiesB, enemiesG, enemiesR,bullets)

    # 让最近绘制的屏幕可见
    pygame.display.flip()