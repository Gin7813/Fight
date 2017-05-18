import sys

import pygame

from settings import Settings
from plane import Plane
from pygame.sprite import Group
from game_state import GameState
import game_function as gf

def run_game():
    # 初始化游戏
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Fight")

    #创建一个存储游戏信息的实例
    state=GameState(ai_settings)

    #创建飞机
    plane=Plane(screen,ai_settings)

    bullets=Group()
    enemiesB=Group()
    enemiesG=Group()
    enemiesR=Group()


    # 开始游戏的主循环
    while True:

        # 监视键鼠
        gf.check_events(plane)

        if state.game_active:
            # 每次循环都重绘屏幕
            gf.update_screen(ai_settings, screen, plane, enemiesB, enemiesG, enemiesR, bullets)
            plane.update()
            gf.update_bullets(bullets,enemiesB,enemiesG,enemiesR)
            gf.update_enemy(ai_settings,plane,enemiesB,enemiesG,enemiesR,bullets,state,screen)
            #print(len(enemiesB))
            #print(len(enemiesG))
            #print(len(enemiesR))
            #print(len(bullets))

run_game()
