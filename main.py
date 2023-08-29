import pygame
from pygame.locals import FULLSCREEN
from photosynthetic import Photosynthetic

pygame.init()
inf = pygame.display.Info()
WIDTH = inf.current_w
HEIGHT = inf.current_h
print(WIDTH, HEIGHT)
screen = pygame.display.set_mode((WIDTH, HEIGHT), FULLSCREEN)
clock = pygame.time.Clock()
font = pygame.font.SysFont("Verdana", WIDTH // 50)
big_font = pygame.font.SysFont("Verdana", WIDTH // 25)

objects = pygame.sprite.Group()
running = True

while running:
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_q) or (event.type == pygame.QUIT):
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            obj: Photosynthetic = Photosynthetic(event.pos)
            objects.add(obj)
    screen.fill((0, 0, 0))
    objects.draw(screen)
    objects.update(objects)
    pygame.display.flip()
    clock.tick(40)
