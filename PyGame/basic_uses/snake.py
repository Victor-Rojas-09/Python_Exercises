import pygame
import random

pygame.init()

width, heigth = 800, 600
GRID_SIZE = 20
vel = 10

screen = pygame.display.set_mode((width, heigth))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

snake_body = [(400, 300),(340, 300),(360, 300),(380, 300)]
snake_direction = (1, 0)

food_position = (
    random.randrange(0, width, GRID_SIZE),
    random.randrange(0, heigth, GRID_SIZE),
)

running = True

# Main Loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and snake_direction != (0, 1):
        snake_direction = (0, -1)
    if keys[pygame.K_s] and snake_direction != (0, -1):
        snake_direction = (0, 1)
    if keys[pygame.K_a] and snake_direction != (1, 0):
        snake_direction = (-1, 0)
    if keys[pygame.K_d] and snake_direction != (-1, 0):
        snake_direction = (1, 0)

    # Update
    head_x, head_y = snake_body[0]
    dir_x, dir_y = snake_direction

    new_head = (
        head_x + dir_x * GRID_SIZE,
        head_y + dir_y * GRID_SIZE,
    )

    # Collision with walls
    if (
        new_head[0] < 0 or new_head[0] >= width or
        new_head[1] < 0 or new_head[1] >= heigth
    ):
        running = False

    # Collision with itself
    if new_head in snake_body:
        running = False

    snake_body.insert(0, new_head)

    # Food collision
    if new_head == food_position:
        food_position = (
            random.randrange(0, width, GRID_SIZE),
            random.randrange(0, heigth, GRID_SIZE),
        )
    else:
        snake_body.pop()

    # Draw
    screen.fill((30, 30, 30))

    for segment in snake_body:
        pygame.draw.rect(screen, (0, 200, 0), (*segment, GRID_SIZE, GRID_SIZE))

    pygame.draw.rect(screen, (200, 0, 0), (*food_position, GRID_SIZE, GRID_SIZE))

    pygame.display.flip()
    clock.tick(vel)

pygame.quit()