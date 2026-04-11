import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Fill background
screen.fill("white")

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Mouse click events
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            # Left click (1)
            if event.button == 1:
                pygame.draw.circle(screen, "blue", (x, y), 30)

            # Right click (3)
            elif event.button == 3:
                pygame.draw.rect(screen, "black",(x - 50, y - 50, 100, 100), width=5)

    pygame.display.flip()

pygame.quit()
sys.exit()