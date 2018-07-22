import pygame

# Initialise Pygame
pygame.init()

# Setup Window
surface = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Flappy Bird Clone")

clock = pygame.time.Clock()
FPS = 60
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
quit()