import pygame

class PongGame:

    def __init__(self, width: int, height: int):
        pygame.init()
        pygame.mixer.init()

        self.width = width
        self.height = height

        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

        # Font
        self.font = pygame.font.SysFont("Arial", 40)
        self.game_over_font = pygame.font.SysFont("Arial", 60)

        self.collision_sound = pygame.mixer.Sound("../assets/sounds/pong.wav")
        self.point_sound = pygame.mixer.Sound("../assets/sounds/points.wav")
        self.game_over = pygame.mixer.Sound("../assets/sounds/game_over.wav")

        # Ball
        self.ball_pos = [width // 2, height // 2]
        self.ball_vel_x = 3
        self.ball_vel_y = 3
        self.ball_radius = 15

        # Left paddle
        self.left_x = 20
        self.left_y = height // 2 - 40
        self.paddle_width = 10
        self.paddle_height = 80
        self.paddle_speed = 5

        # Right paddle
        self.right_x = width - 30
        self.right_y = height // 2 - 40

        # Score
        self.player1_score = 0
        self.player2_score = 0

        self.winner_text = ""
        self.running = True


    def game(self):

        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return False

            keys = pygame.key.get_pressed()

            # Move ball
            self.ball_pos[0] += self.ball_vel_x
            self.ball_pos[1] += self.ball_vel_y

            # Bounce top/bottom
            if (self.ball_pos[1] - self.ball_radius <= 0) or (self.ball_pos[1] + self.ball_radius >= self.height):
                self.ball_vel_y *= -1

            # Move left paddle
            if keys[pygame.K_w]:
                self.left_y -= self.paddle_speed
            if keys[pygame.K_s]:
                self.left_y += self.paddle_speed

            # Move right paddle
            if keys[pygame.K_UP]:
                self.right_y -= self.paddle_speed
            if keys[pygame.K_DOWN]:
                self.right_y += self.paddle_speed

            # Clamp paddles
            self.left_y = max(0, min(self.height - self.paddle_height, self.left_y))
            self.right_y = max(0, min(self.height - self.paddle_height, self.right_y))

            # Collision left paddle
            if (
                (self.ball_pos[0] - self.ball_radius) < (self.left_x + self.paddle_width) and
                (self.ball_pos[0] + self.ball_radius) > self.left_x and
                (self.ball_pos[1] - self.ball_radius) <= (self.left_y + self.paddle_height) and
                (self.ball_pos[1] + self.ball_radius) >= self.left_y
            ):
                self.collision_sound.play()

                self.ball_pos[0] = self.left_x + self.paddle_width + self.ball_radius
                self.ball_vel_x *= -1

            # Collision right paddle
            if (


                (self.ball_pos[0] - self.ball_radius) < (self.right_x + self.paddle_width) and
                (self.ball_pos[0] + self.ball_radius) > self.right_x and
                (self.ball_pos[1] - self.ball_radius) <= (self.right_y + self.paddle_height) and
                (self.ball_pos[1] + self.ball_radius) >= self.right_y
            ):
                self.collision_sound.play()

                self.ball_pos[0] = self.right_x - self.ball_radius
                self.ball_vel_x *= -1

            # Score conditions
            if self.ball_pos[0] < 0:
                self.point_sound.play()
                self.player2_score += 1

                self.ball_pos = [self.width // 2, self.height // 2]
                self.ball_vel_x *= -1

            if self.ball_pos[0] > self.width:
                self.point_sound.play()
                self.player1_score += 1

                self.ball_pos = [self.width // 2, self.height // 2]
                self.ball_vel_x *= -1

            # Game Over condition
            if self.player1_score > 4:
                self.winner_text = "Player 1 Win"
                return self.end_game()

            elif self.player2_score > 4:
                self.winner_text = "Player 2 Win"
                return self.end_game()

            self.screen.fill((0, 0, 0))

            # Draw ball & paddles
            pygame.draw.circle(self.screen, (255, 0, 0), self.ball_pos, self.ball_radius)
            pygame.draw.rect(self.screen, (255, 255, 255), (self.left_x, self.left_y, self.paddle_width, self.paddle_height))
            pygame.draw.rect(self.screen, (255, 255, 255), (self.right_x, self.right_y, self.paddle_width, self.paddle_height))

            # Draw score
            score_text = self.font.render(f"{self.player1_score}  -  {self.player2_score}", True, (255, 255, 255))
            self.screen.blit(score_text, (self.width // 2 - score_text.get_width() // 2, 20))

            pygame.display.flip()
            self.clock.tick(120)

        pygame.quit()
        return False

    def end_game(self):
        self.screen.fill((0, 0, 0))

        game_over_text = self.game_over_font.render("GAME OVER", True, (255, 0, 0))
        winner_render = self.font.render(self.winner_text, True, (255, 255, 255))

        self.game_over.play()

        self.screen.blit(game_over_text, (
            self.width // 2 - game_over_text.get_width() // 2,
            self.height // 2 - 50
        ))

        self.screen.blit(winner_render, (
            self.width // 2 - winner_render.get_width() // 2,
            self.height // 2 + 20
        ))

        pygame.display.flip()

        pygame.time.delay(3000)

        return True