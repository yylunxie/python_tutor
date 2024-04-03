import pygame
import sys
import random

# 初始化Pygame
pygame.init()

# 设置窗口大小
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

# 设置窗口标题
pygame.display.set_caption("图片处理游戏")

# 加载图片
image = pygame.image.load('./img/gray.jpg')
image_rect = image.get_rect()
image_rect.topleft = (200, 150)

# 调整图片大小，确保图片不大于窗口
if image_rect.width > width or image_rect.height > height:
    image = pygame.transform.scale(image, (width, height))
    image_rect = image.get_rect()

# 背景色
background_color = (0, 0, 0)

# 点击次数
click_count = 0

# 运行标志
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if image_rect.collidepoint(event.pos):
                click_count += 1
                # 移动图片
                new_x = random.randint(0, max(0, width - image_rect.width))
                new_y = random.randint(0, max(0, height - image_rect.height))
                image_rect.topleft = (new_x, new_y)
                # 改变背景色
                background_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # 填充背景色
    screen.fill(background_color)

    # 绘制图片
    screen.blit(image, image_rect)

    # 检查点击次数
    if click_count > 10:
        font = pygame.font.SysFont(None, 55)
        text = font.render('恭喜，游戏结束！', True, (255, 255, 255))
        screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))

    # 更新画面
    pygame.display.flip()

pygame.quit()
sys.exit()
