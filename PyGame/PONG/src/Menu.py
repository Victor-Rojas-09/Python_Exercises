import pygame
from PyGame.PONG.src.pong import PongGame


# Initialize pygame once
pygame.init()
pygame.mixer.init()

# Global configuration
SCREEN_SIZE = (800, 450)
SCREEN = pygame.display.set_mode(SCREEN_SIZE)


def show_intro():

    image = pygame.image.load("D:/Projects on Github/PyGame/PONG/assets/Presentation.jpg")
    image = pygame.transform.scale(image, SCREEN_SIZE)

    SCREEN.blit(image, (0, 0))
    pygame.display.flip()

    pygame.time.delay(1200)

    show_menu()


def show_menu():

    image = pygame.image.load("D:/Projects on Github/PyGame/PONG/assets/Menu.jpg")
    image = pygame.transform.scale(image, SCREEN_SIZE)

    running = True

    # Define button area (Play button)
    play_button = pygame.Rect(162, 151, 393, 77)

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

        pygame.display.flip()


def show_help():

    image = pygame.image.load("D:/Projects on Github/PyGame/PONG/assets/Help.jpg")
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

    game = PongGame(800, 500)
    game.game()
    # After game ends, go back to menu
    show_menu()


if __name__ == '__main__':
    show_intro()