import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 600, 400  # Размеры окна
GRID_SIZE = 20          # Размер клетки
SNAKE_SPEED = 10       # Скорость змейки (кадры в секунду)
SNAKE_COLOR = (64, 224, 208) #
FOOD_COLOR = (255, 36, 0) # Красный
BACKGROUND_COLOR = (0, 0, 0) # 

# Инициализация окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()

# Начальная позиция змейки и еды
snake = [(WIDTH // 2, HEIGHT // 2)]
snake_direction = (1, 0) # Змейка двигается вправо
food = (random.randrange(0, WIDTH // GRID_SIZE) * GRID_SIZE,
        random.randrange(0, HEIGHT // GRID_SIZE) * GRID_SIZE)

# Функция для рисования змейки
def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, SNAKE_COLOR,
                        (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

# Функция для рисования еды
def draw_food():
    pygame.draw.rect(screen, FOOD_COLOR,
                     (food[0], food[1], GRID_SIZE, GRID_SIZE))

# Функция для проверки столкновений
def check_collisions():
    head = snake[0]

    # Столкновение со стеной
    if (head[0] < 0 or head[0] >= WIDTH or
        head[1] < 0 or head[1] >= HEIGHT):
        return True

    # Столкновение с собой
    if head in snake[1:]:
        return True
    
    return False

# Функция для генерации новой еды
def generate_food():
     while True:
        new_food = (random.randrange(0, WIDTH // GRID_SIZE) * GRID_SIZE,
                    random.randrange(0, HEIGHT // GRID_SIZE) * GRID_SIZE)
        if new_food not in snake:
            return new_food

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            if event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            if event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            if event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)

    # Движение змейки
    head = (snake[0][0] + snake_direction[0] * GRID_SIZE,
            snake[0][1] + snake_direction[1] * GRID_SIZE)
    snake.insert(0, head)

    # Проверка, съедена ли еда
    if head == food:
        food = generate_food() # Генерируем новую еду
    else:
        snake.pop() # Если не съедена, то удаляем хвост

    # Проверка столкновений
    if check_collisions():
        running = False # Если столкновение, то конец игры
        
    # Отрисовка
    screen.fill(BACKGROUND_COLOR)
    draw_snake()
    draw_food()
    pygame.display.flip()

    # Задержка
    clock.tick(SNAKE_SPEED)

# Выход из Pygame
pygame.quit()
sys.exit()