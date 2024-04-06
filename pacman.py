import pygame
import sys

# 初始化pygame
pygame.init()

# 設置窗口大小
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

# 設置窗口標題
pygame.display.set_caption("Pacman簡單地圖示例")

# 定義顏色
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# 初始位置
pacman_x, pacman_y = 100, 100
# 移動速度
speed = 5

# Pacman的大小
pacman_size = 50

# 墻壁列表（x位置，y位置，寬度，高度）
walls = [
    (200, 200, 200, 20),
    (400, 100, 20, 300),
    # 添加窗口邊界作為墻壁
    (0, 0, width, 0),  # 上邊界
    (0, height, width, 0),  # 下邊界
    (0, 0, 0, height),  # 左邊界
    (width, 0, 0, height),  # 右邊界
]

# 運行標誌
running = True
# 移動方向
move_direction = None

def will_collide(rect, walls):
    """檢查矩形是否會與牆壁列表中的任一牆壁碰撞"""
    for wall in walls:
        if rect.colliderect(wall):
            return True
    return False

while running:
    # 事件處理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_direction = 'left'
            elif event.key == pygame.K_RIGHT:
                move_direction = 'right'
            elif event.key == pygame.K_UP:
                move_direction = 'up'
            elif event.key == pygame.K_DOWN:
                move_direction = 'down'
        elif event.type == pygame.KEYUP:
            move_direction = None

    # 計算Pacman的下一步位置
    next_x, next_y = pacman_x, pacman_y
    if move_direction == 'left':
        next_x -= speed
    elif move_direction == 'right':
        next_x += speed
    elif move_direction == 'up':
        next_y -= speed
    elif move_direction == 'down':
        next_y += speed

    # 檢查下一步是否會碰撞
    next_rect = pygame.Rect(next_x, next_y, pacman_size, pacman_size)
    if not will_collide(next_rect, [pygame.Rect(*wall) for wall in walls]):
        pacman_x, pacman_y = next_x, next_y

    # 填充背景色
    screen.fill(BLACK)
    
    # 繪製Pacman
    pygame.draw.rect(screen, YELLOW, pygame.Rect(pacman_x, pacman_y, pacman_size, pacman_size))

    # 繪製牆壁
    for wall in walls:
        pygame.draw.rect(screen, BLUE, pygame.Rect(*wall))

    # 更新畫面
    pygame.display.flip()

# 退出
pygame.quit()
sys.exit()
