# player.py
import pygame


class Player:
    def __init__(self, x, y, width, height, win):
        # 初始化玩家属性
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10  # 移动速度
        self.is_jump = False
        self.jump_count = 10
        self.win = win

        # 加载并缩放玩家图像
        self.image = pygame.image.load('images/player.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))


    def draw(self):
        # 将玩家图像绘制在窗口上
        self.win.blit(self.image, (self.x, self.y))

    def move(self, keys):
        # 左右移动
        if keys[pygame.K_LEFT] and self.x > self.vel:
            self.x -= self.vel
        elif keys[pygame.K_RIGHT] and self.x < self.win.get_width() - self.width - self.vel:
            self.x += self.vel

        # 跳跃处理
        if not self.is_jump:
            if keys[pygame.K_SPACE]:
                self.is_jump = True
        else:
            if self.jump_count >= -10:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.is_jump = False
                self.jump_count = 10
