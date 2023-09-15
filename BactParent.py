import math

import pygame
import pymunk
from abc import abstractmethod


def custom_attraction(obj, obj2):
    g = 50000  # Коэффициент притяжения
    distance = obj.body.position.get_distance(obj2.body.position)
    force_magnitude = g / (distance ** 2 + 1)
    force_vector = force_magnitude * (obj2.body.position - obj.body.position).normalized()
    return force_vector


class BactParent(pygame.sprite.Sprite):
    def __init__(self, image: str, pos: tuple, mass: int, radius: int, en: int, speed: int, sig_co: tuple, space,
                 places, objects):

        super().__init__()
        self.co = (None,0)
        self.objects_co = {}
        self.space = space
        self.places = places
        self.objects = objects
        self.image = pygame.image.load(image)
        self.mass = mass
        self.radius = radius
        self.moment = pymunk.moment_for_circle(mass, 0, self.radius)
        self.body = pymunk.Body(self.mass, self.moment)
        self.body.position = pos
        self.shape = pymunk.Circle(self.body, self.radius)
        self.rect = self.image.get_rect()
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]

        self.en = en
        self.speed = speed
        self.sig_co = sig_co

    def update(self, objects, places):
        self.objects_co = []
        for obj2 in objects:
            if self != obj2:
                attraction_force = custom_attraction(self, obj2)
                self.body.apply_force_at_world_point(attraction_force, self.body.position)
        self.rect.centerx = self.body.position.x
        self.rect.centery = self.body.position.y
        self.add_co(objects, places)
        print(int(self.co[1]))

    def draw(self, screen):
        screen.blit(self.image, self.rect.center)

    def smart_vel_change(self, objects):
        for obj2 in objects:
            distance = self.body.position.get_distance(obj2.body.position)
            print(distance)

    def get_distance(self, x, y, x2=None, y2=None, r=None):
        if r is None:
            return math.sqrt(
                (self.rect.centerx - (x + x2) / 2) ** 2 + (self.rect.centery - (y + y2) / 2) ** 2) - self.radius
        return math.sqrt((self.rect.centerx - x) ** 2 + (self.rect.centery - y) ** 2) - r - self.radius

    @abstractmethod
    def add_co(self, objects, places):
        self.objects = objects
        self.places = places
        for obj in objects:
            if self != obj:
                self.objects_co[obj] = int(
                    self.get_distance(obj.rect.centerx, obj.rect.centery, r=obj.radius) * self.sig_co[3])
        # for plc in places:
        #     self.objects_co.append(self.get_distance(obj.rect.centerx, obj.rect.centery, r=obj.radius))
        # self.places_co
        # max(self.places_co) +
        if len(self.objects_co):
            self.co = min(self.objects_co.items(), key=lambda p: p[1])
