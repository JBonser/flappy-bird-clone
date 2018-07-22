import pygame


# Initialise Pygame
pygame.init()


# PyGame Variables
CLOCK = pygame.time.Clock()
FPS = 60
BACKGROUND_COLOUR = (0, 0, 0)
white = (255, 255, 255)
SCREEN_X = 800
SCREEN_Y = 400


# Setup Window
surface = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
pygame.display.set_caption("Flappy Bird Clone")


# Bird Values
bird_img = pygame.image.load('assets/flappy_bird.png')
bird_x = 150
bird_y = 200
bird_y_move = 0
bird_rect = bird_img.get_rect()


def flappy_bird(x, y, image):
    surface.blit(image, (x, y))


def game_over():
    pygame.quit()
    quit()


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

game_over()
