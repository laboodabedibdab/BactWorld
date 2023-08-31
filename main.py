import pygame
import pymunk
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
space = pymunk.Space()
space.gravity = (0, 0)

objects = pygame.sprite.Group()
places = pygame.sprite.Group()
running = True

while running:
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_q) or (event.type == pygame.QUIT):
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            obj: Photosynthetic = Photosynthetic(event.pos)
            objects.add(obj)
            space.add(obj.body, obj.shape)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            comb_group = pygame.sprite.Group()
            comb_group.add(objects)
            comb_group.add(places)
            objects.sprites()[0].smart_vel_change(comb_group)
    screen.fill((0, 0, 0))
    space.step(1 / 240)
    objects.draw(surface=screen)
    objects.update(objects)
    pygame.display.flip()
    clock.tick(240)
