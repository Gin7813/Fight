import pygame

class Plane():

    def __init__(self,screen,ai_settings):
        """初始化飞机并设置初始位置"""
        self.screen=screen
        self.ai_settings=ai_settings

        #加载飞机并获得外接矩形
        self.image=pygame.image.load('image/plane.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #将每艘飞机放在屏幕底部中央
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        # 在飞机属性中存储小数的值
        self.centerX = float(self.rect.centerx)
        self.centerY = float(self.rect.centery)

        #设置移动标志
        self.moving_right=False
        self.moving_left=False
        self.moving_down=False
        self.moving_up=False


    def update(self):
        """根据移动标志调整飞机位置"""
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.centerX+=self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>self.screen_rect.left:
            self.centerX-=self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.centerY+=self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top>self.screen_rect.top:
            self.centerY-=self.ai_settings.ship_speed_factor
        #根据center和bot更新rect对象
        self.rect.centerx=self.centerX
        self.rect.centery=self.centerY

    def blitme(self):
        """在指定位置绘制飞机"""
        self.screen.blit(self.image,self.rect)

    def center_plane(self):
        """让飞机初始化"""
        self.centerX=self.screen_rect.centerx
        self.centerY=self.screen_rect.bottom-18