import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))

clock = pygame.time.Clock()

running = True

# Init Color
COLOR = (0, 0, 0)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                COLOR = (255, 0, 0)   # Red
            elif event.key == pygame.K_b:
                COLOR = (0, 0, 255)   # Blue
            elif event.key == pygame.K_g:
                COLOR = (0, 255, 0)   # Green
            elif event.key == pygame.K_y:
                COLOR = (255, 255, 0) # Yellow

    screen.fill("white")

    # circle
    pygame.draw.circle(screen, COLOR, (250, 250), 80)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()