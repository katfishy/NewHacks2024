# main.py
import pygame
from map import Map
from player import Player
from npc import NPC

# 初始化 Pygame
pygame.init()

# 设置窗口大小和标题
win_width, win_height = 1280, 720
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('SUBWAY FLOOD SURVIVAL')

# 创建 Map、Player 和 NPC 实例
map_bg = Map(win)
player = Player(50, 400, 64, 64, win)
dialogues = [
    "Hello, welcome to the subway!",
    "Please be careful during your journey.",
    "If you need help, just ask."
]
npc = NPC(200, 300, 'images/passenger_1.png', dialogues, width=64, height=64)

# 定义场景的地图文件路径
scenes = [
    'images/map_1.png',
    'images/map_2.png',
    'images/map_3.jpg'
]
current_scene = 0
map_bg.load_map(scenes[current_scene])

# 设置字体以显示对话内容
font = pygame.font.Font(None, 36)

# 主循环
running = True
dialogue_text = ""  # 当前显示的对话内容
while running:
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and npc.is_talking:  # 按回车继续对话
                dialogue_text = npc.get_next_dialogue()
                # 对话结束且未到最后场景时切换场景
                if dialogue_text is None and current_scene < len(scenes) - 1:
                    current_scene += 1
                    map_bg.load_map(scenes[current_scene])
                    npc.is_talking = False  # 结束对话
                    dialogue_text = ""  # 清空对话内容
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if npc.rect.collidepoint(event.pos):  # 检查是否点击了 NPC
                npc.start_dialogue()
                dialogue_text = npc.get_next_dialogue()  # 初始化对话内容

    # 获取按键
    keys = pygame.key.get_pressed()
    player.move(keys)

    # 绘制当前场景地图、玩家和 NPC
    map_bg.draw()
    player.draw()
    npc.draw(win)

    # 显示对话内容
    if npc.is_talking and dialogue_text:
        text_surface = font.render(dialogue_text, True, (255, 255, 255))
        win.blit(text_surface, (50, 650))  # 显示在窗口底部

    # 更新显示
    pygame.display.flip()

pygame.quit()
