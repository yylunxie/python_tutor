import pygame
import sys

# 初始化Pygame
pygame.init()

# 设置窗口大小
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

# 设置窗口标题
pygame.display.set_caption("绘制图形示例")

# 颜色定义
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# 运行标志
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 填充背景色
    screen.fill(black)

    # 绘制线条
    pygame.draw.line(screen, white, (10, 10), (630, 10), 5)

    # 绘制矩形
    pygame.draw.rect(screen, red, pygame.Rect(50, 50, 100, 50))

    # 绘制多边形
    pygame.draw.polygon(screen, green, [(100, 100), (150, 150), (200, 120), (120, 90)])

    # 更新画面
    pygame.display.flip()

# 退出Pygame
pygame.quit()
sys.exit()
