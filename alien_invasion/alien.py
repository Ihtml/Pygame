# -*- coding: utf-8 -*-
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        # 初始化飞船并设置初始位置
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像并获取其外接矩形
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 将每艘新飞船放在屏幕左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 储存精准位置
        self.x = float(self.rect.x)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

            
    def blitme(self):
        # 指定位置绘制
        self.screen.blit(self.image, self.rect)
