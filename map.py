# map.py
import pygame


class Map:
    def __init__(self, win):
        # 初始化时不加载特定的地图
        self.win = win
        self.background = None

    def load_map(self, image_path):
        # 加载指定的地图图片并调整大小
        self.background = pygame.image.load(image_path)
        self.background = pygame.transform.scale(self.background, self.win.get_size())

    def draw(self):
        # 绘制当前的地图
        if self.background:
            self.win.blit(self.background, (0, 0))
