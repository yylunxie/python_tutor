import pygame
import sys
import random

# 初始化Pygame
pygame.init()

# 設置窗口大小
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

# 設置窗口標題
pygame.display.set_caption("圖片處理遊戲")

# 加載圖片
image = pygame.image.load('path/to/image.png')
image_rect = image.get_rect()
image_rect.topleft = (200, 150)

# 背景色
background_color = (0, 0, 0)

# 點擊次數
click_count = 0

# 運行標誌
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if image_rect.collidepoint(event.pos):
                click_count += 1
                # 移動圖片
                image_rect.topleft = (random.randint(0, width - image_rect.width), random.randint(0, height - image_rect.height))
                # 改變背景色
                background_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # 填充背景色
    screen.fill(background_color)

    # 繪製圖片
    screen.blit(image, image_rect)

    # 檢查點擊次數
    if click_count > 10:
        font = pygame.font.SysFont(None, 55)
        text = font.render('恭喜，遊戲結束！', True, (255, 255, 255))
        screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))

    # 更新畫面
    pygame.display.flip()

pygame.quit()
sys.exit()
