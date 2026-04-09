import pygame

pygame.init()
width, height = 800, 500
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Ball
ball_pos = [250, 250]
ball_vel_x = 3
ball_vel_y = 3
ball_radius = 15

# Left paddle
left_x = 20
left_y = height // 2 - 40
paddle_width = 10
paddle_height = 80
paddle_speed = 5

# Right paddle
right_x = width - 30
right_y = height // 2 - 40

# Score
player1_score = 0
player2_score = 0

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if player1_score > 3 or player2_score > 3:
        running = False

    keys = pygame.key.get_pressed()

    # Move ball
    ball_pos[0] += ball_vel_x
    ball_pos[1] += ball_vel_y

    # Bounce top/bottom
    if (ball_pos[1] - ball_radius <= 0) or (ball_pos[1] + ball_radius >= height):
        ball_vel_y *= -1

    # Move left paddle
    if keys[pygame.K_w]:
        left_y -= paddle_speed
    if keys[pygame.K_s]:
        left_y += paddle_speed

    # Move right paddle
    if keys[pygame.K_UP]:
        right_y -= paddle_speed
    if keys[pygame.K_DOWN]:
        right_y += paddle_speed

    # Clamp paddles inside screen
    left_y = max(0, min(height - paddle_height, left_y))
    right_y = max(0, min(height - paddle_height, right_y))

    # Collision with left paddle
    if (
        (ball_pos[0] - ball_radius) < (left_x + paddle_width) and
        (ball_pos[0] + ball_radius) > left_x and
        (ball_pos[1] - ball_radius) <= (left_y + paddle_height) and
        (ball_pos[1] + ball_radius) >= left_y
    ):
        ball_vel_x *= -1

    # Collision with right paddle
    if (
        (ball_pos[0] - ball_radius) < (right_x + paddle_width) and
        (ball_pos[0] + ball_radius) > right_x and
        (ball_pos[1] - ball_radius) <= (right_y + paddle_height) and
        (ball_pos[1] + ball_radius) >= right_y
    ):
        ball_vel_x *= -1

    # Score conditions
    if ball_pos[0] < 0:
        player2_score += 1
        ball_pos = [250, 250]
        ball_vel_x *= -1

    if ball_pos[0] > width:
        player1_score += 1
        ball_pos = [250, 250]
        ball_vel_x *= -1

    screen.fill((0, 0, 0))

    # Draw ball
    pygame.draw.circle(screen, (255, 0, 0), ball_pos, ball_radius)

    # Draw paddles
    pygame.draw.rect(screen, (255, 255, 255), (left_x, left_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, (255, 255, 255), (right_x, right_y, paddle_width, paddle_height))

    pygame.display.flip()
    clock.tick(120)

pygame.quit()