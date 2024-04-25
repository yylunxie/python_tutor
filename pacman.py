import pygame
import sys

# 初始化pygame
pygame.init()

# 設置窗口大小
size = width, height = 480, 640
screen = pygame.display.set_mode(size)

# 設置窗口標題
pygame.display.set_caption("Pacman")

# 定義顏色
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# 初始位置
pacman_x, pacman_y = 2, 49*6+2
# 移動速度
speed = 0.5

# Pacman的大小
pacman_size = 30

# 墻壁列表（x位置，y位置，寬度，高度）
walls = [
    # Horinzontal walls
    (48, 49, 48*3, 4),
    (48*6, 49, 48*3, 4),
    (48, 49*3, 48, 4),
    (48*4, 49*3, 48*3, 4),
    (48*3, 49*4, 48, 4),
    (48*4, 49*6, 48, 4),
    (48*6, 49*6, 48, 4),
    (48*4, 49*7, 48*3+4, 4),
    (48*4, 49*8, 48*3, 4),
    (48*1, 49*10, 48, 4),
    (48*3, 49*10, 48, 4),
    (48*7, 49*10, 48*2, 4),
    (0, 49*11, 48, 4),
    (48*5, 49*11, 48*2, 4),
    (48, 49*12, 48*3, 4),
    (48*9, 49*12, 48, 4),
    # Vertical walls
    (48*2, 49*1, 4, 49),
    (48, 49*2, 4, 49),
    (48*5, 0, 4, 49*2),
    (48*8, 49, 4, 49),
    (48*3, 49*2, 4, 49*3),
    (48*6, 49*2, 4, 49),
    (48*4, 49*6, 4, 49),
    (48*7, 49*6, 4, 49),
    (48*3, 49*7, 4, 49*2),
    (48*6, 49*8, 4, 49*2),
    (48*5, 49*9, 4, 49*2),
    (48*2, 49*10, 4, 49),
    (48*8, 49*10, 4, 49*2),
    (48*3, 49*11, 4, 49),
    (48*6, 49*12, 4, 49),
    # Big square
    (48*5, 49*3, 48, 49*2),
    (0, 49*4, 48*2, 49*2),
    (0, 49*7, 48*2, 49*2),
    (48*8, 49*4, 48*2, 49*2),
    (48*8, 49*7, 48*2, 49*2),
    # 添加窗口邊界作為墻壁
    (0, 0, width, 1),  # 上邊界
    (0, height-1, width, 1),  # 下邊界
    (0, 0, 1, height),  # 左邊界
    (width-1, 0, 1, height),  # 右邊界
]

        
# 食物位置列表和已被吃掉的食物集合     
food_positions = [(x, y) for y in range(height // 10) for x in range(width // 10) if not any(pygame.Rect(x*10, y*10, 10, 10).colliderect(pygame.Rect(*wall)) for wall in walls)]
food_eaten = set()
score = 0  # 初始得分

# 運行標誌
running = True
# 移動方向
move_direction = None

def will_collide(rect, walls):
    """檢查是否會與牆壁列表中的任一牆壁碰撞"""
    for wall in walls:
        if rect.colliderect(wall):
            return True
    return False


# 更新显示得分
def display_score():
    font = pygame.font.SysFont(None, 36)
    score_surface = font.render('Score: {}'.format(score), True, YELLOW)
    screen.blit(score_surface, (10, 10))
    
    

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
        # elif event.type == pygame.KEYUP:
        #     move_direction = None

    # 計算Pacman的下一步位置
    next_x, next_y = pacman_x, pacman_y
    if move_direction == 'left':
        next_x -= speed
        # next_x = next_x - speed
    elif move_direction == 'right':
        next_x += speed
    elif move_direction == 'up':
        next_y -= speed
    elif move_direction == 'down':
        next_y += speed

    # 檢查下一步是否會碰撞
    next_pacman = pygame.Rect(next_x, next_y, pacman_size, pacman_size)
    if not will_collide(next_pacman, [pygame.Rect(*wall) for wall in walls]):
        pacman_x, pacman_y = next_x, next_y
        if (int(pacman_x // 10), int(pacman_y // 10)) in food_positions and (int(pacman_x // 10), int(pacman_y // 10)) not in food_eaten:
            food_eaten.add((int(pacman_x // 10), int(pacman_y // 10)))
            score += 10  # 增加得分

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
