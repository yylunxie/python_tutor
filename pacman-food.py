import pygame
import sys

# 初始化pygame
pygame.init()

# 设置窗口大小
size = width, height = 600, 840
screen = pygame.display.set_mode(size)

# 设置窗口标题
pygame.display.set_caption("Pacman地图与食物点")

# 定义颜色
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# 初始位置
pacman_x, pacman_y = 2, 405
# 移動速度
speed = 0.5

# Pacman的大小
pacman_size = 30

# 地图数据，1代表墙壁，0代表通道
map_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 瓦片大小
tile_size = 40

def draw_map(screen, map_data):
    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            if tile == 1:
                pygame.draw.rect(screen, BLUE, (x * tile_size, y * tile_size, tile_size, tile_size))

def draw_food(screen, map_data):
    food_size = 4
    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            if tile == 0:
                food_x = x * tile_size + tile_size // 2 - food_size // 2
                food_y = y * tile_size + tile_size // 2 - food_size // 2
                pygame.draw.rect(screen, YELLOW, (food_x, food_y, food_size, food_size))


# 運行標誌
running = True
# 移動方向
move_direction = None

def check_collision(pacman_x, pacman_y, map_data, direction):
    """
    检查Pacman是否与墙壁发生碰撞。
    :param pacman_x: Pacman的x坐标
    :param pacman_y: Pacman的y坐标
    :param map_data: 地图数据，包含1和0的二维列表，1代表墙壁
    :param tile_size: 每个瓦片的大小
    :return: 如果Pacman与墙壁发生碰撞，返回True，否则返回False
    """
    # 计算Pacman所在的格子位置
    body = 15
    if direction == 'left':
        pos_x = [pacman_x - body, pacman_x - body]
        pos_y = [pacman_y + body, pacman_y - body]
    elif direction == 'right':
        pos_x = [pacman_x + body, pacman_x + body]
        pos_y = [pacman_y + body, pacman_y - body]
    elif direction == 'up':
        pos_x = [pacman_x + body, pacman_x - body]
        pos_y = [pacman_y - body, pacman_y - body]
    elif direction == 'down':
        pos_x = [pacman_x + body, pacman_x - body]
        pos_y = [pacman_y + body, pacman_y + body]
    else:
        return False
    
    for i in range(2):
        grid_x = pos_x[i] // tile_size
        grid_y = pos_y[i] // tile_size
     
        # 检查Pacman所在格子是否为墙壁
        if map_data[int(grid_y)][int(grid_x)] == 1:
            return True
    return False



# 主循环
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
    
    pacman_c_x = next_x + pacman_size // 2
    pacman_c_y = next_y + pacman_size // 2
    # Todo 1: check screen cross boundary
    if not check_collision(pacman_c_x, pacman_c_y, map_data, move_direction):
        pacman_x, pacman_y = next_x, next_y
        
    
    # Todo: detect food collision
         
    
       
    # 填充背景色
    screen.fill(BLACK)
    
    # 绘制地图
    draw_map(screen, map_data)
    
    # 绘制食物点
    draw_food(screen, map_data)
    
    # 繪製Pacman
    pygame.draw.rect(screen, YELLOW, pygame.Rect(pacman_x, pacman_y, pacman_size, pacman_size))
    
    # 更新显示
    pygame.display.flip()

# 退出pygame
pygame.quit()
sys.exit()
