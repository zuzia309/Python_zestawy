"""
gra Snake sterowana myszą
"""

import sys
import random
import pygame


WINDOW_SIZE = 600
CELL_SIZE = 20
GRID_WIDTH = WINDOW_SIZE // CELL_SIZE
GRID_HEIGHT = WINDOW_SIZE // CELL_SIZE

INITIAL_SPEED = 2
GAME_DURATION = 120
FRUIT_LIFETIME_SEC = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOOD_FRUIT_COLOR = (0, 255, 0)
BAD_FRUIT_COLOR = (255, 0, 0)
SNAKE_COLOR = (50, 205, 50)

UP = (0, 1)
DOWN = (0, -1)
LEFT = (-1, 0)
RIGHT = (1, 0)

OPPOSITE = {
    UP: DOWN,
    DOWN: UP,
    LEFT: RIGHT,
    RIGHT: LEFT,
}


def draw_grid(surface: pygame.Surface) -> None:
    for x in range(0, WINDOW_SIZE, CELL_SIZE):
        pygame.draw.line(surface, BLACK, (x, 0), (x, WINDOW_SIZE))
    for y in range(0, WINDOW_SIZE, CELL_SIZE):
        pygame.draw.line(surface, BLACK, (0, y), (WINDOW_SIZE, y))


def spawn_fruit(snake_body, fruit_type, forbidden_positions=None):

    if forbidden_positions is None:
        forbidden_positions = set()
    forbidden = set(snake_body) | set(forbidden_positions)

    while True:
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        pos = (x, y)
        if pos not in forbidden:
            lifetime = FRUIT_LIFETIME_SEC * INITIAL_SPEED
            return {
                "pos": pos,
                "type": fruit_type,
                "lifetime": lifetime,
            }


def choose_direction_from_mouse(snake_body, mouse_pos, current_dir):

    head_x, head_y = snake_body[-1]
    head_px = head_x * CELL_SIZE + CELL_SIZE // 2
    head_py = head_y * CELL_SIZE + CELL_SIZE // 2
    mx, my = mouse_pos

    dx = mx - head_px
    dy = my - head_py

    if abs(dx) > abs(dy):
        new_dir = RIGHT if dx > 0 else LEFT
    else:
        new_dir = UP if dy > 0 else DOWN

    if new_dir == OPPOSITE[current_dir]:
        return current_dir, True

    return new_dir, False


def update_snake(snake_body, direction, good_fruit, bad_fruit):

    head_x, head_y = snake_body[-1]
    new_head = ((head_x + direction[0]) % GRID_WIDTH,
                (head_y + direction[1]) % GRID_HEIGHT)

    # zjadł sam siebie
    if new_head in snake_body:
        return False, "collision"

    snake_body.append(new_head)

    # sprawdzenie kolizji z zatrutym owocem
    if new_head == bad_fruit["pos"]:
        return False, "bad_fruit"

    # sprawdzenie kolizji z dobrym owocem
    if new_head == good_fruit["pos"]:
        # dobre owoce – wąż rośnie (nie usuwamy ogona)
        return True, "good_fruit"

    # zwykły ruch – usuwamy ogon
    snake_body.pop(0)
    return True, None


def draw_scene(surface, snake_body, good_fruit, bad_fruit):
    surface.fill(BLACK)
    draw_grid(surface)

    # rysowanie weza
    for x, y in snake_body:
        rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(surface, SNAKE_COLOR, rect)

    # rysowanie dobrego owocu
    gx, gy = good_fruit["pos"]
    good_rect = pygame.Rect(gx * CELL_SIZE, gy * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(surface, GOOD_FRUIT_COLOR, good_rect)

    # rysowanie zlego owocu
    bx, by = bad_fruit["pos"]
    bad_rect = pygame.Rect(bx * CELL_SIZE, by * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(surface, BAD_FRUIT_COLOR, bad_rect)



def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()

    # stan gry
    snake = [(10, 10)]
    direction = RIGHT

    good_fruit = spawn_fruit(snake, "good")
    bad_fruit = spawn_fruit(snake, "bad", forbidden_positions={good_fruit["pos"]})

    score = 0
    speed = INITIAL_SPEED

    start_ticks = pygame.time.get_ticks()
    next_speedup_time = 30  # pierwsze przyspieszenie po 30 s

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                new_dir, backwards = choose_direction_from_mouse(
                    snake, pygame.mouse.get_pos(), direction
                )
                if backwards:
                    print("Ruch wstecz – koniec gry!")
                    running = False
                    break
                direction = new_dir

        if not running:
            break


        alive, result = update_snake(snake, direction, good_fruit, bad_fruit)
        if not alive:
            if result == "bad_fruit":
                print("Zjadłeś zatruty owoc! Koniec gry!")
            elif result == "collision":
                print("Wąż zderzył się sam ze sobą! Koniec gry!")
            break

        # licznik życia owoców – każdy ma swój lifetime
        good_fruit["lifetime"] -= 1
        bad_fruit["lifetime"] -= 1

        # jeśli dobry owoc "umarł", generujemy nowy w innym miejscu
        if good_fruit["lifetime"] <= 0:
            good_fruit = spawn_fruit(snake, "good", forbidden_positions={bad_fruit["pos"]})

        # jeśli zły owoc "umarł", generujemy nowy
        if bad_fruit["lifetime"] <= 0:
            bad_fruit = spawn_fruit(snake, "bad", forbidden_positions={good_fruit["pos"]})

        # zjedzenie dobrego owocu
        if result == "good_fruit":
            score += 1
            # generujemy nowy dobry owoc, znowu dbając, by nie był na złym
            good_fruit = spawn_fruit(snake, "good", forbidden_positions={bad_fruit["pos"]})

        # czas gry
        elapsed_seconds = (pygame.time.get_ticks() - start_ticks) // 1000
        time_left = GAME_DURATION - elapsed_seconds
        if time_left <= 0:
            print("Koniec czasu!")
            break

        # okresowe przyspieszanie co 30 sekund
        if elapsed_seconds >= next_speedup_time:
            speed += 1
            next_speedup_time += 30


        draw_scene(screen, snake, good_fruit, bad_fruit)
        pygame.display.set_caption(
            f"Snake Game | Wynik: {score} | Pozostały czas: {time_left}s"
        )
        pygame.display.flip()

        clock.tick(speed)

    print(f"Koniec gry! Twój wynik: {score}")
    pygame.quit()
    sys.exit(0)


if __name__ == "__main__":
    main()