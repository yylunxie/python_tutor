import pygame
import sys
import random

# 初始化Pygame
pygame.init()

# 設置窗口大小
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

# 設置窗口標題
pygame.display.set_caption("動態圖形繪製")

# 初始位置和顏色
x, y = width // 2, height // 2
color = (0, 128, 255)

# 運行標誌
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 10
            elif event.key == pygame.K_RIGHT:
                x += 10
            elif event.key == pygame.K_UP:
                y -= 10
            elif event.key == pygame.K_DOWN:
                y += 10
            # 碰撞邊界時改變顏色
            if x < 0 or x > width or y < 0 or y > height:
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # 填充背景色
    screen.fill((0, 0, 0))

    # 繪製矩形
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 150, 75))

    # 更新畫面
    pygame.display.flip()

pygame.quit()
sys.exit()
