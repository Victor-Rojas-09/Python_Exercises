import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))

clock = pygame.time.Clock()

running = True

while running:

    # endpoint
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color
    screen.fill("white")

    # Line: (surface, color, (x1,y1), (x2,y2), thickness)
    pygame.draw.line(screen, "green", (0, 450), (500, 450), 100)

    # Circle: (surface, color, (x, y), radius, width=0, fill)
    pygame.draw.circle(screen, "blue", (250, 350), 30, width=5)

    # Rectangle: (surface, color, (x,y,width,height), thickness=0 fill)
    pygame.draw.rect(screen, "black", (200, 300, 100, 100), width=5)

    # Polygon: (surface, color, [(x1,y1), (x2,y2), (x3,y3), ...], width=0 fill)
    pygame.draw.polygon(screen, "brown", [(200, 300), (300, 300), (250, 250)], width=6)

    pygame.display.flip()

    # Ellipse: (surface, color, (x,y,width,height), thickness=0 fill)
    pygame.draw.ellipse(screen, "gray", (250, 50, 100, 70), width=4)

    # Arc: (surface, color, (x,y,width,height), start_angle, end_angle, thickness)
    pygame.draw.arc(screen, "gray", (100, 50, 100, 50), 0, (2 * 3.1416), 5)

    # FPS control
    dt = clock.tick(60)

# Close Pygame
pygame.quit()