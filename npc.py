# npc.py
import pygame
from dialogue import Dialogue


class NPC:
    def __init__(self, x, y, image_path, dialogues, width=None, height=None):
        self.x = x
        self.y = y
        # 加载 NPC 图像
        self.image = pygame.image.load(image_path)

        # 如果指定了 width 和 height，则缩放图像
        if width and height:
            self.image = pygame.transform.scale(self.image, (width, height))

        # 获取缩放后的矩形区域
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        # 初始化对话
        self.dialogue = Dialogue(dialogues)
        self.is_talking = False

    def draw(self, win):
        # 在窗口上绘制 NPC
        win.blit(self.image, (self.x, self.y))

    def start_dialogue(self):
        # 开始对话
        self.is_talking = True
        self.dialogue = Dialogue(self.dialogue.dialogues)

    def get_next_dialogue(self):
        if self.is_talking:
            current_text = self.dialogue.get_current_dialogue()
            self.dialogue.next_dialogue()
            if self.dialogue.is_finished():
                self.is_talking = False
            return current_text
        return None
