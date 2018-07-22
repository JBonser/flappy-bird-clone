import pygame
import time

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


# Bird Values


def flappy_bird(x, y, image):
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
    bird_x = 150
    bird_y = 200
    bird_y_move = 0
    bird_img = pygame.image.load('assets/flappy_bird.png')
    bird_rect = bird_img.get_rect()

    should_quit = False
    while not should_quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                should_quit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    bird_y_move = -5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    bird_y_move = 5

        bird_y += bird_y_move
        surface.fill(BACKGROUND_COLOUR)
        flappy_bird(bird_x, bird_y, bird_img)

        if bird_y > (SCREEN_Y - bird_rect.size[1]) or bird_y < 0:
            game_over()

        pygame.display.update()
        CLOCK.tick(FPS)


main()
pygame.quit()
quit()
