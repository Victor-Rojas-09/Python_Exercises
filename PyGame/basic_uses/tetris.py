import pygame
import random

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30

COLS = SCREEN_WIDTH // BLOCK_SIZE
ROWS = SCREEN_HEIGHT // BLOCK_SIZE

FPS = 60
FALL_SPEED = 0.5

# Colors
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)


# Simple shape
SHAPES = [
    [[1, 1, 1, 1]]
]

def create_grid(locked_positions):
    """Create the game grid."""

    grid = [[BLACK for _ in range(COLS)] for _ in range(ROWS)]

    for (x, y), color in locked_positions.items():
        if y >= 0:
            grid[y][x] = color

    return grid


def draw_grid(surface, grid):
    """Draw all blocks on screen."""

    for y in range(ROWS):
        for x in range(COLS):
            pygame.draw.rect(
                surface,
                grid[y][x],
                (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            )


def is_valid_position(shape, grid, offset):
    """Check if shape can be placed in a position."""

    off_x, off_y = offset

    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                new_x = x + off_x
                new_y = y + off_y

                # Check boundaries
                if new_x < 0 or new_x >= COLS or new_y >= ROWS:
                    return False

                # Check collision
                if new_y >= 0 and grid[new_y][new_x] != BLACK:
                    return False

    return True


def lock_shape(shape, offset, locked_positions):
    """Add shape blocks to locked positions."""

    off_x, off_y = offset

    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                locked_positions[(off_x + x, off_y + y)] = CYAN


def clear_full_rows(grid, locked_positions):
    """Remove full rows and shift above blocks down."""

    for y in range(ROWS - 1, -1, -1):
        if BLACK not in grid[y]:
            # Remove row
            for x in range(COLS):
                del locked_positions[(x, y)]

            # Move everything above down
            for (x, y2) in sorted(list(locked_positions), key=lambda k: k[1], reverse=True):
                if y2 < y:
                    locked_positions[(x, y2 + 1)] = locked_positions.pop((x, y2))


def draw_shape(surface, shape, offset):
    """Draw current falling shape."""

    off_x, off_y = offset

    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(
                    surface,
                    CYAN,
                    (
                        (off_x + x) * BLOCK_SIZE,
                        (off_y + y) * BLOCK_SIZE,
                        BLOCK_SIZE,
                        BLOCK_SIZE,
                    ),
                )


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris")

    clock = pygame.time.Clock()

    locked_positions = {}
    current_shape = random.choice(SHAPES)
    current_pos = [COLS // 2 - 2, 0]

    fall_timer = 0
    running = True

    while running:
        grid = create_grid(locked_positions)

        # Time control
        delta_time = clock.get_rawtime() / 1000
        fall_timer += delta_time
        clock.tick(FPS)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        # Move left
        if keys[pygame.K_a]:
            new_pos = [current_pos[0] - 1, current_pos[1]]
            if is_valid_position(current_shape, grid, new_pos):
                current_pos = new_pos

        # Move right
        if keys[pygame.K_d]:
            new_pos = [current_pos[0] + 1, current_pos[1]]
            if is_valid_position(current_shape, grid, new_pos):
                current_pos = new_pos

        # Move down
        if keys[pygame.K_s]:
            new_pos = [current_pos[0], current_pos[1] + 1]
            if is_valid_position(current_shape, grid, new_pos):
                current_pos = new_pos

        # Automatic fall
        if fall_timer > FALL_SPEED:
            new_pos = [current_pos[0], current_pos[1] + 1]

            if is_valid_position(current_shape, grid, new_pos):
                current_pos = new_pos
            else:
                # Lock piece
                lock_shape(current_shape, current_pos, locked_positions)

                # New piece
                current_shape = random.choice(SHAPES)
                current_pos = [COLS // 2 - 2, 0]

                # Clear rows
                clear_full_rows(grid, locked_positions)

            fall_timer = 0

        # Draw
        screen.fill(BLACK)

        draw_grid(screen, grid)
        draw_shape(screen, current_shape, current_pos)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()