import pygame

pygame.init()
ancho, alto = 500, 500
screen = pygame.display.set_mode((ancho, alto))
clock = pygame.time.Clock()

pos = [250, 250]  # posición inicial
vel = 5           # velocidad de movimiento
radio = 15

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] & ((pos[1] - vel) > 0):  #K_w   K_s  ,K_d   K_a
        pos[1] -= vel
    if keys[pygame.K_DOWN] & ((pos[1] + vel) < alto):
        pos[1] += vel
    if keys[pygame.K_LEFT] & ((pos[0] - vel) > 0):
        pos[0] -= vel
    if keys[pygame.K_RIGHT] & ((pos[0] + vel) < ancho):
        pos[0] += vel

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), pos, radio)
    pygame.display.flip()
    clock.tick(120)

pygame.quit()