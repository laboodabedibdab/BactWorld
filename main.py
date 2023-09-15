import pygame
import pymunk
from pygame.locals import FULLSCREEN
from photosynthetic import Photosynthetic
from ControlBar import Widgets

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
widgets = Widgets(screen)
places = pygame.sprite.Group()
running = True
FPS = 120

while running:
    events = pygame.event.get()
    for event in events:
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_q) or (event.type == pygame.QUIT):
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] > 140:
            obj: Photosynthetic = Photosynthetic(event.pos)
            objects.add(obj)
            space.add(obj.body, obj.shape)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            comb_group = pygame.sprite.Group()
            comb_group.add(objects)
            comb_group.add(places)
            objects.sprites()[0].smart_vel_change(comb_group)
    screen.fill((0, 0, 0))
    if not widgets.sim_paused:
        space.step(1 / (FPS / widgets.sim_slider.getValue()))
    objects.draw(surface=screen)
    objects.update(objects)
    widgets.update(events, screen, clock)
    if widgets.clearV:
        space = pymunk.Space()
        objects = pygame.sprite.Group()
        widgets.clearV = False
    running = widgets.running
    if not widgets.running:
        print(0)
    pygame.display.flip()
    clock.tick(FPS)
