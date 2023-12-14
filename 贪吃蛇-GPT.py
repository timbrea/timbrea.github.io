import pygame
import random

# 初始化 pygame
pygame.init()

# 设置游戏画面尺寸
SIZE = WIDTH, HEIGHT = 800, 600

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# 创建游戏窗口
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("贪吃蛇")

# 设置时钟对象
clock = pygame.time.Clock()

# 定义蛇的默认方向
UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4

# 定义蛇的默认位置和方向
snake_position = [100, 100]
snake_direction = RIGHT

# 定义蛇的默认长度和身体坐标列表
snake_length = 5
snake_body = [[100, 100], [90, 100], [80, 100], [70, 100], [60, 100]]

# 随机生成一个食物位置
food_position = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]

# 游戏主循环
while True:
    # 处理游戏事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != DOWN:
                snake_direction = UP
            elif event.key == pygame.K_RIGHT and snake_direction != LEFT:
                snake_direction = RIGHT
            elif event.key == pygame.K_DOWN and snake_direction != UP:
                snake_direction = DOWN
            elif event.key == pygame.K_LEFT and snake_direction != RIGHT:
                snake_direction = LEFT

    # 移动蛇的身体
    for i in range(snake_length - 1, 0, -1):
        snake_body[i] = list(snake_body[i - 1])

    # 移动蛇的头部
    if snake_direction == UP:
        snake_body[0][1] -= 10
    elif snake_direction == RIGHT:
        snake_body[0][0] += 10
    elif snake_direction == DOWN:
        snake_body[0][1] += 10
    elif snake_direction == LEFT:
        snake_body[0][0] -= 10

    # 检测蛇是否吃到食物
    if snake_body[0] == food_position:
        food_position = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
        snake_length += 1
        snake_body.append([0, 0])

    # 绘制游戏背景
    screen.fill(BLACK)

    # 绘制蛇和食物
    for part in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(part[0], part[1], 10, 10))
    pygame.draw.rect(screen, WHITE, pygame.Rect(food_position[0], food_position[1], 10, 10))

    # 更新屏幕
    pygame.display.update()

    # 设置帧率
    clock.tick(12)
