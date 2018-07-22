import pygame


# Initialise Pygame
pygame.init()

# Setup Window
surface = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Flappy Bird Clone")

# Game Variables
clock = pygame.time.Clock()
FPS = 60
black = (0, 0, 0)
white = (255, 255, 255)

# Bird Values
bird_img = pygame.image.load('assets/flappy_bird.png')
bird_x = 150
bird_y = 200


def flappy_bird(x, y, image):
    surface.blit(image, (x, y))


game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    surface.fill(black)
    flappy_bird(bird_x, bird_y, bird_img)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()
