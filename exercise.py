import pygame
import sys
import random

# 初始化Pygame
pygame.init()

# 設置窗口大小
# size = width, height = 800, 600
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(SIZE)

# 設置窗口標題
pygame.display.set_caption("動態圖形繪製")

# 初始位置和顏色
x, y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
color = (0, 128, 255)

player = pygame.Rect(x, y, 150, 75)

# 運行標誌
running = True

while running:
    
    # 填充背景色
    screen.fill((0, 0, 0))

    # 繪製矩形
    pygame.draw.rect(screen, color, player)
    
    key = pygame.key.get_pressed()
    
    if player.x >= 0 and player.x <= SCREEN_WIDTH - player.width and player.y >= 0 and player.y <= SCREEN_HEIGHT - player.height:   
        if key[pygame.K_a] == True:
            player.move_ip(-1, 0)
        elif key[pygame.K_d] == True:
            player.move_ip(1, 0)
        elif key[pygame.K_w] == True:
            player.move_ip(0, -1)
        elif key[pygame.K_s] == True:
            player.move_ip(0, 1)
    elif player.x < 0:
        player.x = 0
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    elif player.x > SCREEN_WIDTH - player.width:
        player.x = SCREEN_WIDTH - player.width
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    elif player.y < 0:
        player.y = 0
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    elif player.y > SCREEN_HEIGHT - player.height:
        player.y = SCREEN_HEIGHT - player.height
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # 更新畫面
    pygame.display.update()

pygame.quit()
sys.exit()
