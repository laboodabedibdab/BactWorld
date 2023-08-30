import pygame
import pymunk


def custom_attraction(obj, obj2):
    g = 50000  # Коэффициент притяжения
    distance = obj.body.position.get_distance(obj2.body.position)
    force_magnitude = g / distance ** 2
    force_vector = force_magnitude * (obj2.body.position - obj.body.position).normalized()
    return force_vector


class BactParent(pygame.sprite.Sprite):
    def __init__(self, image: str, pos: tuple, mass: int, radius: int, en: int, speed: int, sig_co: tuple):

        super().__init__()
        self.image = pygame.image.load(image)
        self.mass = mass
        self.radius = radius
        self.moment = pymunk.moment_for_circle(mass, 0, self.radius)
        self.body = pymunk.Body(self.mass, self.moment)
        self.body.position = pos
        self.rect = self.image.get_rect()
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]

        self.en = en
        self.speed = speed
        self.sig_co = sig_co

    def update(self, objects):
        for obj2 in objects:
            if self != obj2:
                attraction_force = custom_attraction(self, obj2)
                self.body.apply_force_at_world_point(attraction_force, self.body.position)

    def smart_vel_change(self, objects):
        for obj2 in objects:
            distance = self.body.position.get_distance(obj2.body.position)
            print(distance)
