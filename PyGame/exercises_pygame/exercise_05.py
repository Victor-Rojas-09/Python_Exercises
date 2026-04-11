import pygame

pygame.init()

# Screen
width, height = 500, 500
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

# Rectangle
pos = [250, 250]
speed = 5
w_rect = 100
h_rect = 100

dragging = False
offset_x = 0
offset_y = 0

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        # Mouse button pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            # Check if mouse is inside rectangle
            if (pos[0] <= mouse_x <= pos[0] + w_rect) and (pos[1] <= mouse_y <= pos[1] + h_rect):
                dragging = True

                # Save offset
                offset_x = mouse_x - pos[0]
                offset_y = mouse_y - pos[1]

        # Mouse button released
        if event.type == pygame.MOUSEBUTTONUP:
            dragging = False

        # Mouse movement
        if event.type == pygame.MOUSEMOTION and dragging:
            mouse_x, mouse_y = event.pos
            pos[0] = mouse_x - offset_x
            pos[1] = mouse_y - offset_y

    # Keyboard movement
    keys = pygame.key.get_pressed()

    pos[0] = max(0, min(pos[0], width - w_rect))
    pos[1] = max(0, min(pos[1], height - h_rect))

    screen.fill((0, 0, 0))

    # Rectangle
    pygame.draw.rect(screen, "blue", (pos[0], pos[1], w_rect, h_rect), width=5)

    pygame.display.flip()
    clock.tick(120)

pygame.quit()