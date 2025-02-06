import pygame
import random
import sys


pygame.init()


WIDTH, HEIGHT = 600, 400  
GRID_SIZE = 20          
SNAKE_SPEED = 10      
SNAKE_COLOR = (64, 224, 208) 
FOOD_COLOR = (255, 36, 0) 
BACKGROUND_COLOR = (0, 0, 0)  


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()


snake = [(WIDTH // 2, HEIGHT // 2)]
snake_direction = (1, 0) 
food = (random.randrange(0, WIDTH // GRID_SIZE) * GRID_SIZE,
        random.randrange(0, HEIGHT // GRID_SIZE) * GRID_SIZE)


def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, SNAKE_COLOR,
                        (segment[0], segment[1], GRID_SIZE, GRID_SIZE))


def draw_food():
    pygame.draw.rect(screen, FOOD_COLOR,
                     (food[0], food[1], GRID_SIZE, GRID_SIZE))


def check_collisions():
    head = snake[0]

    
    if (head[0] < 0 or head[0] >= WIDTH or
        head[1] < 0 or head[1] >= HEIGHT):
        return True

    
    if head in snake[1:]:
        return True
    
    return False


def generate_food():
     while True:
        new_food = (random.randrange(0, WIDTH // GRID_SIZE) * GRID_SIZE,
                    random.randrange(0, HEIGHT // GRID_SIZE) * GRID_SIZE)
        if new_food not in snake:
            return new_food


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


    head = (snake[0][0] + snake_direction[0] * GRID_SIZE,
            snake[0][1] + snake_direction[1] * GRID_SIZE)
    snake.insert(0, head)

 
    if head == food:
        food = generate_food() 
    else:
        snake.pop() 

    
    if check_collisions():
        running = False 
        
    
    screen.fill(BACKGROUND_COLOR)
    draw_snake()
    draw_food()
    pygame.display.flip()

   
    clock.tick(SNAKE_SPEED)


pygame.quit()
sys.exit()
