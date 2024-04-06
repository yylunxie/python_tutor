import pygame
import sys

# 初始化Pygame
pygame.init()

# 设置窗口大小
size = width, height = 960, 540
screen = pygame.display.set_mode(size)

# 设置窗口标题
pygame.display.set_caption("图片处理示例")

# 加载图片，请确保将'path/to/image.png'替换为你的图片文件路径
# 例如: './image.png'
image = pygame.image.load('./img/naruto.jpg').convert_alpha()

# 图片的位置，你可以根据需要修改这些值
x = 100
y = 100


# 指定新的尺寸
new_width = 500
new_height = 300

# 调整图片大小到新的尺寸
# image = pygame.transform.scale(image, (new_width, new_height))


# 运行标志
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 填充背景色，这里使用深蓝色
    screen.fill((255, 255, 255))

    # 将图片绘制到屏幕上指定位置
    screen.blit(image, (x, y))

    # 更新画面
    pygame.display.flip()

# 退出Pygame
pygame.quit()
sys.exit()
