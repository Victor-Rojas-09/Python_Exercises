import pygame

pygame.init()

width, height = 500, 500
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

pos = [250, 250]
speed = 5
w_rect = 100
h_rect = 100

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] & ((pos[1] - speed) > 0):
        pos[1] -= speed
    if keys[pygame.K_DOWN] & ((pos[1] + h_rect + speed) < height):
        pos[1] += speed
    if keys[pygame.K_LEFT] & ((pos[0] - speed) > 0):
        pos[0] -= speed
    if keys[pygame.K_RIGHT] & ((pos[0] + w_rect + speed) < width):
        pos[0] += speed

    screen.fill((0, 0, 0))

    # Rectangle
    pygame.draw.rect(screen, "blue", (pos[0], pos[1], w_rect, h_rect), width=5)
    pygame.display.flip()

    clock.tick(120)

pygame.quit()