import pygame
import sys
from levels import levels  # 导入地图数据


# 初始化pygame
pygame.init()

# 創建一個時鐘對象
clock = pygame.time.Clock()

# 設置窗口大小
size = width, height = 600, 840
screen = pygame.display.set_mode(size)

# 設置窗口標題
pygame.display.set_caption("Pacman地圖與食物點")

# 定義顏色
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# 瓦片大小
tile_size = 40

# Pacman 類定義
class Pacman:
    def __init__(self, x, y, size, speed):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.direction = None

    def move(self):
        if self.direction == 'left':
            self.x -= self.speed
        elif self.direction == 'right':
            self.x += self.speed
        elif self.direction == 'up':
            self.y -= self.speed
        elif self.direction == 'down':
            self.y += self.speed

    def update(self, map_data, tile_size):
        next_x, next_y = self.x, self.y
        self.move()
        if self.check_collision(map_data, tile_size):
            self.x, self.y = next_x, next_y  # 如果發生碰撞，不更新坐標

    # def check_collision(self, map_data, tile_size):
    #     grid_x = int((self.x + self.size // 2) // tile_size)
    #     grid_y = int((self.y + self.size // 2) // tile_size)
    #     return map_data[grid_y][grid_x] == 1
    def check_collision(self, map_data, tile_size):
        if not self.direction:
            return False  # 如果没有方向，则不检查碰撞

        body = self.size / 2
        pacman_x = self.x
        pacman_y = self.y

        # 根据方向计算检测碰撞的两个点
        if self.direction == 'left':
            pos_x = [pacman_x - body, pacman_x - body]
            pos_y = [pacman_y + body, pacman_y - body]
        elif self.direction == 'right':
            pos_x = [pacman_x + body, pacman_x + body]
            pos_y = [pacman_y + body, pacman_y - body]
        elif self.direction == 'up':
            pos_x = [pacman_x + body, pacman_x - body]
            pos_y = [pacman_y - body, pacman_y - body]
        elif self.direction == 'down':
            pos_x = [pacman_x + body, pacman_x - body]
            pos_y = [pacman_y + body, pacman_y + body]

        # 检查每个点是否在墙壁上
        for i in range(2):
            grid_x = int(pos_x[i] // tile_size)
            grid_y = int(pos_y[i] // tile_size)
            if map_data[grid_y][grid_x] == 1:
                return True  # 如果任一检测点在墙壁上，立即返回True

        return False  # 如果没有碰撞，返回False

# 初始化 Pacman 實例
pacman = Pacman(2, 405, 30, 1)

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
    speed = pacman.speed
    # 事件處理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pacman.direction = 'left'
            elif event.key == pygame.K_RIGHT:
                pacman.direction = 'right'
            elif event.key == pygame.K_UP:
                pacman.direction = 'up'
            elif event.key == pygame.K_DOWN:
                pacman.direction = 'down'

    # 更新Pacman的位置
    pacman.update(levels[current_level], tile_size)
    score = check_food(pacman.x, pacman.y, levels[current_level], score)  # 更新得分
         
    if check_level_completion(pacman.x, pacman.y, levels[current_level], tile_size):
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
        pygame.draw.rect(screen, YELLOW, (pacman.x, pacman.y, pacman.size, pacman.size))
        display_score(screen, score, current_level)
        
        # 更新显示
        pygame.display.flip()

    # 控制遊戲最大幀率為60
    clock.tick(60)
    
# 退出pygame
pygame.quit()
sys.exit()
