import pygame
import sys
from levels import levels  # 导入地图数据


# 初始化pygame
pygame.init()

# 創建一個時鐘對象
clock = pygame.time.Clock()

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
speed = 1

# Pacman的大小
pacman_size = 30



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


def show_score_page(screen, score):
    # 畫面清空
    screen.fill(BLACK)

    # 顯示分數
    font = pygame.font.SysFont('Arial', 48)
    text = font.render(f'Total Score: {score}', True, YELLOW)
    text_rect = text.get_rect(center=(width / 2, height / 2 - 50))
    screen.blit(text, text_rect)

    # 顯示繼續提示
    continue_text = font.render('Press SPACE to continue', True, YELLOW)
    continue_rect = continue_text.get_rect(center=(width / 2, height / 2 + 50))
    screen.blit(continue_text, continue_rect)

    # 更新顯示
    pygame.display.flip()
    
    
def show_end_page(screen):
    # 畫面清空
    screen.fill(BLACK)

    # 顯示結局
    font = pygame.font.SysFont('Arial', 48)
    text = font.render(f'All levels are cleared!', True, YELLOW)
    text_rect = text.get_rect(center=(width / 2, height / 2 - 50))
    screen.blit(text, text_rect)

    # 顯示繼續提示
    continue_text = font.render('Press SPACE to continue', True, YELLOW)
    continue_rect = continue_text.get_rect(center=(width / 2, height / 2 + 50))
    screen.blit(continue_text, continue_rect)

    # 更新顯示
    pygame.display.flip()


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


def check_level_completion(pacman_x, pacman_y, map_data, tile_size):
    grid_x = int(pacman_x // tile_size)
    grid_y = int(pacman_y // tile_size)
    # 檢查Pacman所在的格子是否為終點
    return map_data[grid_y][grid_x] == 9


# 检查Pacman是否与食物点重合并更新得分
def check_food(pacman_x, pacman_y, map_data, score):
    grid_x = int(pacman_x // tile_size)
    grid_y = int(pacman_y // tile_size)

    if map_data[grid_y][grid_x] == 0:  # 检查是否为食物点
        map_data[grid_y][grid_x] = 2  # 标记食物被吃掉
        return score + 10  # 每个食物10分
    return score


def display_score(screen, score, level):
    display_level = level + 1
    font = pygame.font.SysFont('Arial', 24)
    score_text = font.render(f'Score: {score}', True, YELLOW)
    screen.blit(score_text, (10, 10))
    level_text = font.render(f'Level: {display_level}', True, YELLOW)
    screen.blit(level_text, (260, 10))

# 運行標誌
running = True
# 移動方向
move_direction = None
score = 0  # 初始得分

current_level = 0

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
    if not check_collision(pacman_c_x, pacman_c_y, levels[current_level], move_direction):
        pacman_x, pacman_y = next_x, next_y
        score = check_food(pacman_x, pacman_y, levels[current_level], score)
         
    if check_level_completion(pacman_x, pacman_y, levels[current_level], tile_size):
        show_score_page(screen, score)  # 顯示得分頁面
        waiting_for_input = True  # 等待玩家按鍵來繼續
       
        # 如果等待玩家輸入並且按下空格，則加載下一個關卡
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        current_level += 1
                        if current_level < len(levels):
                            map_data = levels[current_level]
                            # 初始位置
                            pacman_x, pacman_y = 2, 405
                            move_direction = None
                            score = 0  # 初始得分
                            # 重新初始化食物、Pacman位置等
                            waiting_for_input = False
                        else:
                            begin = pygame.time.get_ticks()
                            show_end_page(screen)
                            time_pause = True
                            while time_pause:
                                now = pygame.time.get_ticks()
                                if now - begin >= 5000:
                                    running = False
                                    waiting_for_input = False
                                    time_pause = False
    else:
        # 填充背景色
        screen.fill(BLACK)
        
        # 绘制地图
        draw_map(screen, levels[current_level])
        
        # 绘制食物点
        draw_food(screen, levels[current_level])
        
        # 繪製Pacman
        pygame.draw.rect(screen, YELLOW, pygame.Rect(pacman_x, pacman_y, pacman_size, pacman_size))
        display_score(screen, score, current_level)
        
        # 更新显示
        pygame.display.flip()

    # 控制遊戲最大幀率為60
    clock.tick(60)
    
# 退出pygame
pygame.quit()
sys.exit()
