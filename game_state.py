class GameState():
    """跟踪游戏信息"""

    def __init__(self,ai_settings):
        """初始化统计信息"""
        self.ai_settings=ai_settings
        self.reset_state()
        #游戏开始时处于活动状态
        self.game_active=True

    def reset_state(self):
        """初始化游戏运行过程中可变化的信息"""
        self.plane_left=self.ai_settings.plane_limit