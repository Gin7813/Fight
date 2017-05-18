import pygame

import random

from pygame.sprite import Sprite

class Enemy(Sprite):
    """表示单个敌人的类"""

    def __init__(self,ai_settings,screen):
        """初始化敌人起始位置"""
        super(Enemy,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings

        # 敌人运动速度
        self.speed_factor = 0

        # 敌人生命
        self.life_point = 0

class EnemyB(Enemy):
    """蓝色敌人"""

    def __init__(self,ai_settings,screen):
        super().__init__(ai_settings,screen)

        #加载敌人图像，并设置其rect属性
        self.image=pygame.image.load('image/enemyB.bmp')
        self.rect=self.image.get_rect()

        #每个敌人初始位置在
        self.rect.x=random.randint(screen.get_rect().left,screen.get_rect().right-self.rect.width)
        self.rect.y=-self.rect.height

        #存储敌人准确位置
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)

        # 敌人运动速度
        self.speed_factor = ai_settings.enemyB_speed_factor

        # 敌人生命
        self.life_point = ai_settings.enemyB_life

    def blitme(self):
         """在指定位置绘制外星人"""
         self.screen.blit(self.image, self.rect)

    def update(self):
        """向下移动敌人"""
        # 更新表示敌人位置的小数值
        self.y += self.speed_factor
        # 更新表示子弹的rect位置
        self.rect.y = self.y

class EnemyG(Enemy):
    """绿色敌人"""

    def __init__(self,ai_settings,screen):
        super().__init__(ai_settings,screen)

        #加载敌人图像，并设置其rect属性
        self.image=pygame.image.load('image/enemyG.bmp')
        self.rect=self.image.get_rect()

        #每个敌人初始位置在
        self.rect.x=random.randint(screen.get_rect().left,screen.get_rect().right-self.rect.width)
        self.rect.y=-self.rect.height

        #存储敌人准确位置
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)

        # 敌人运动速度
        self.speed_factor = ai_settings.enemyG_speed_factor

        # 敌人生命
        self.life_point = ai_settings.enemyG_life

    def blitme(self):
         """在指定位置绘制外星人"""
         self.screen.blit(self.image, self.rect)

    def update(self):
        """向下移动敌人"""
        # 更新表示敌人位置的小数值
        self.y += self.speed_factor
        # 更新表示子弹的rect位置
        self.rect.y = self.y
class EnemyR(Enemy):
    """红色敌人"""

    def __init__(self,ai_settings,screen):
        super().__init__(ai_settings,screen)

        #加载敌人图像，并设置其rect属性
        self.image=pygame.image.load('image/enemyR.bmp')
        self.rect=self.image.get_rect()

        #每个敌人初始位置在
        self.rect.x=random.randint(screen.get_rect().left,screen.get_rect().right-self.rect.width)
        self.rect.y=-self.rect.height

        #存储敌人准确位置
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)

        # 敌人运动速度
        self.speed_factor = ai_settings.enemyR_speed_factor

        # 敌人生命
        self.life_point = ai_settings.enemyR_life

    def blitme(self):
         """在指定位置绘制外星人"""
         self.screen.blit(self.image, self.rect)

    def update(self):
        """向下移动敌人"""
        # 更新表示敌人位置的小数值
        self.y += self.speed_factor
        # 更新表示子弹的rect位置
        self.rect.y = self.y