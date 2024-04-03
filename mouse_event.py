import pygame
import sys
import random

# 初始化Pygame
pygame.init()

# 设置窗口大小
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

# 设置窗口标题
pygame.display.set_caption("球颜色切换示例")

# 球的初始颜色
color = (255, 0, 0)

# 球的位置和半径
ball_pos = (width // 2, height // 2)
ball_radius = 40

# 运行标志
running = True

def change_color():
    """随机生成一个新的颜色"""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 处理鼠标事件
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 检查是否为左键点击
            if event.button == 1:
                # 检查点击位置是否在球内
                if (event.pos[0] - ball_pos[0]) ** 2 + (event.pos[1] - ball_pos[1]) ** 2 <= ball_radius ** 2:
                    color = change_color()

    # 填充背景色
    screen.fill((0, 0, 0))

    # 绘制球
    pygame.draw.circle(screen, color, ball_pos, ball_radius)

    # 更新画面
    pygame.display.flip()

# 退出Pygame
pygame.quit()
sys.exit()
