import pygame

pygame.init()
width, height = 800, 500
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont("Arial", 40)
game_over_font = pygame.font.SysFont("Arial", 60)

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

game_over = False
winner_text = ""

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if not game_over:
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

        # Clamp paddles
        left_y = max(0, min(height - paddle_height, left_y))
        right_y = max(0, min(height - paddle_height, right_y))

        # Collision left paddle
        if (
            (ball_pos[0] - ball_radius) < (left_x + paddle_width) and
            (ball_pos[0] + ball_radius) > left_x and
            (ball_pos[1] - ball_radius) <= (left_y + paddle_height) and
            (ball_pos[1] + ball_radius) >= left_y
        ):
            ball_vel_x *= -1

        # Collision right paddle
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

        # Game Over condition
        if player1_score > 3:
            game_over = True
            winner_text = "Player 1 Win"
        elif player2_score > 3:
            game_over = True
            winner_text = "Player 2 Win"

    screen.fill((0, 0, 0))

    # Draw ball & paddles
    pygame.draw.circle(screen, (255, 0, 0), ball_pos, ball_radius)
    pygame.draw.rect(screen, (255, 255, 255), (left_x, left_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, (255, 255, 255), (right_x, right_y, paddle_width, paddle_height))

    # Draw score
    score_text = font.render(f"{player1_score}  -  {player2_score}", True, (255, 255, 255))
    screen.blit(score_text, (width // 2 - score_text.get_width() // 2, 20))

    # Draw Game Over
    if game_over:
        game_over_text = game_over_font.render("GAME OVER", True, (255, 0, 0))
        winner_render = font.render(winner_text, True, (255, 255, 255))

        screen.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2, height // 2 - 50))
        screen.blit(winner_render, (width // 2 - winner_render.get_width() // 2, height // 2 + 20))

    pygame.display.flip()
    clock.tick(120)

pygame.quit()