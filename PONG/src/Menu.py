import pygame
from PONG.src.pong import PongGame


# Initialize pygame once
pygame.init()
pygame.mixer.init()

# Global configuration
SCREEN_SIZE = (854, 480)
SCREEN = pygame.display.set_mode(SCREEN_SIZE)


def show_intro():

    intro = pygame.mixer.Sound("../assets/sounds/Intro.wav")
    intro.play()

    image = pygame.image.load("../assets/images/FrontPage.png")
    image = pygame.transform.scale(image, SCREEN_SIZE)

    SCREEN.blit(image, (0, 0))
    pygame.display.flip()

    pygame.time.delay(1200)

    show_menu()


def show_menu():

    image = pygame.image.load("../assets/images/Menu.png")
    image = pygame.transform.scale(image, SCREEN_SIZE)
    pygame.mixer.music.load('../assets/sounds/background.mp3')
    pygame.mixer.music.play(-1)

    running = True


    # Define button area
    play_button = pygame.Rect(247, 150, 360, 75)
    help_button = pygame.Rect(246, 236, 360, 73)
    leave_button = pygame.Rect(248, 323, 358, 71)

    while running:
        SCREEN.blit(image, (0, 0))



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    pygame.mixer.music.stop()
                    start_game()
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if help_button.collidepoint(event.pos):
                    show_help()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if leave_button.collidepoint(event.pos):
                    pygame.mixer.music.stop()
                    pygame.quit()
                    return

        pygame.display.flip()


def show_help():

    image = pygame.image.load("../assets/images/Info.png")
    image = pygame.transform.scale(image, SCREEN_SIZE)

    running = True

    return_button = pygame.Rect(298, 403, 258, 48)

    while running:
        SCREEN.blit(image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_button.collidepoint(event.pos):
                    show_menu()

        pygame.display.flip()


def start_game():

    pong = PongGame(854, 480)
    finished = pong.game()

    if finished:
        show_menu()

if __name__ == '__main__':
    show_intro()