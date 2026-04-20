import pygame
from PONG.src.pong import PongGame


# Initialize pygame once
pygame.init()
pygame.mixer.init()

# Global configuration
SCREEN_SIZE = (854, 480)
SCREEN = pygame.display.set_mode(SCREEN_SIZE)


def show_intro():

    image = pygame.image.load("../assets/images/presentation.png")
    image = pygame.transform.scale(image, SCREEN_SIZE)

    SCREEN.blit(image, (0, 0))
    pygame.display.flip()

    pygame.time.delay(1200)

    show_menu()


def show_menu():

    image = pygame.image.load("../assets/images/menu.png")
    image = pygame.transform.scale(image, SCREEN_SIZE)

    running = True


    # Define button area (Play button)
    play_button = pygame.Rect(210, 177, 418, 78)
    help_button = pygame.Rect(210, 269, 417, 80)

    while running:
        SCREEN.blit(image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    print("Starting game...")
                    start_game()
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if help_button.collidepoint(event.pos):
                    print("help image...")
                    show_help()

        pygame.display.flip()


def show_help():

    image = pygame.image.load("../assets/images/help.png")
    image = pygame.transform.scale(image, SCREEN_SIZE)

    running = True

    while running:
        SCREEN.blit(image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        pygame.display.flip()


def start_game():

    game = PongGame(854, 480)
    game.game()
    # After game ends, go back to menu
    show_menu()


if __name__ == '__main__':
    show_intro()