class Settings():

    def __init__(self):

        """初始化游戏设置"""

        #屏幕设置
        self.screen_width=450
        self.screen_height=600
        self.bg_color=(255,255,255)
        self.frame_rate=60
        self.ticks=0
        # 飞机的设置
        self.ship_speed_factor=4.5
        self.plane_limit=1
        #敌人的设置
        self.enemyB_speed_factor=4.5
        self.enemyB_rate=20
        self.enemyB_life=1
        self.enemyG_speed_factor = 3
        self.enemyG_rate = 80
        self.enemyG_life = 3
        self.enemyR_speed_factor = 1.5
        self.enemyR_rate = 160
        self.enemyR_life = 7
        #子弹的设置
        self.bullet_speed_factor=3
        self.bullet_width=2
        self.bullet_height=10
        self.bullet_color=0,0,0
        self.bullet_rate=10
        self.bullet_life=1