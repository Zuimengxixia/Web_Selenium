import sys
import pygame
from Chapter_12_test_project.settings import Settings
from Chapter_12_test_project.ship import Ship

def run_game():
    '''初始化pygame、设置和屏幕对象'''
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #穿件一艘飞船
    ship =Ship(screen)

    #开始游戏的主循环
    while True:

        '''监视键盘和鼠标'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #每次循环时都重绘屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        # 让最近绘制的屏幕可见
        pygame.display.flip()

run_game()

