import pygame
import time
from random import randint


# Initialise Pygame
pygame.init()


# Game Variables
CLOCK = pygame.time.Clock()
FPS = 60
BACKGROUND_COLOUR = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_X = 800
SCREEN_Y = 400
GAME_FONT = "freesansbold.ttf"

# Setup Window
surface = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
pygame.display.set_caption("Flappy Bird Clone")


def draw_score(count):
    font = pygame.font.Font(GAME_FONT, 20)
    text = font.render("Score: {}".format(count), True, WHITE)
    surface.blit(text, [0, 0])

def draw_blocks(block_x, block_y, block_width, block_height, gap):
    pygame.draw.rect(surface, WHITE, [block_x, block_y, block_width, block_height])
    pygame.draw.rect(surface, WHITE, [block_x, block_y + block_height + gap, block_width, SCREEN_Y])


def draw_flappy_bird(x, y, image):
    surface.blit(image, (x, y))


def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            continue

        return event.key

    return None


def make_text_objects(text, font):
    text_surface = font.render(text, True, WHITE)
    return text_surface, text_surface.get_rect()


def send_message(message):
    small_text = pygame.font.Font(GAME_FONT, 20)
    large_text = pygame.font.Font(GAME_FONT, 150)

    title_text_surface, title_text_rect = make_text_objects(message, large_text)
    title_text_rect.center = SCREEN_X / 2, SCREEN_Y / 2
    surface.blit(title_text_surface, title_text_rect)

    typ_text_surf, typ_text_rect = make_text_objects('Press any key to continue', small_text)
    typ_text_rect.center = SCREEN_X / 2, (SCREEN_Y / 2 + 100)
    surface.blit(typ_text_surf, typ_text_rect)

    pygame.display.update()
    time.sleep(1)

    while replay_or_quit() is None:
        CLOCK.tick()

    main()


def game_over():
    send_message("Kaboom!")


def main():
    # Bird
    bird_x = 150
    bird_y = 200
    bird_y_move = 0
    bird_img = pygame.image.load('assets/flappy_bird.png')
    bird_rect = bird_img.get_rect()

    # Blocks
    block_x = SCREEN_X
    block_y = 0
    block_width = 75
    gap = bird_rect.size[1] * 3
    block_height = randint(0, SCREEN_Y - gap)
    block_move = 3

    # Game
    current_score = 0

    should_quit = False
    while not should_quit:
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                should_quit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    bird_y_move = -5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    bird_y_move = 5

        # Fill Background
        surface.fill(BACKGROUND_COLOUR)

        # Move Bird Along
        bird_y += bird_y_move

        # Draw
        draw_flappy_bird(bird_x, bird_y, bird_img)
        draw_blocks(block_x, block_y, block_width, block_height, gap)
        draw_score(current_score)

        # Boundary Check Ceiling and Floor
        if bird_y > (SCREEN_Y - bird_rect.size[1]) or bird_y < 0:
            game_over()

        # Move Blocks Along
        block_x -= block_move

        # Generate new blocks once they've gone off the screen
        if block_x < (-1 * block_width):
            block_x = SCREEN_X
            block_height = randint(0, SCREEN_Y - gap)

        # Check Upper Block Bounds against Bird
        if bird_x + bird_rect.size[0] > block_x and \
           bird_x < block_x + block_width and \
           bird_y < block_height and \
           bird_x - bird_rect.size[0] < block_width + block_x:
            game_over()

        # Check Lower Block Bounds against Bird
        if bird_x + bird_rect.size[0] > block_x and \
           bird_y + bird_rect.size[1] > block_height + gap and \
           bird_x < block_width + block_x:
            game_over()

        # Update Score
        if block_x > bird_x > block_x - block_move:
            current_score += 1

        # Render the Screen
        pygame.display.update()
        CLOCK.tick(FPS)


main()
pygame.quit()
quit()
