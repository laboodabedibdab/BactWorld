import math
import pygame


class BactParent(pygame.sprite.Sprite):
    def __init__(self, image: str, pos: tuple, mass: int, radius: int):

        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(center=pos)
        self.mass = mass
        self.vel = [0, 0]
        self.radius = radius

    def update(self, objects):
        for bact in objects:
            if bact != self:
                dx = bact.rect.centerx - self.rect.centerx
                dy = bact.rect.centery - self.rect.centery
                distance = math.sqrt(dx ** 2 + dy ** 2)
                force_magnitude = (self.mass * bact.mass) / (distance ** 2 + 0.001) * 20
                angle = math.atan2(dy, dx)
                force_x = force_magnitude * math.cos(angle)
                force_y = force_magnitude * math.sin(angle)
                min_distance = self.radius + bact.radius

                if distance <= min_distance:
                    overlap = min_distance - distance
                    overlap_x = overlap * math.cos(angle)
                    overlap_y = overlap * math.sin(angle)
                    self.vel[0] -= overlap_x / self.mass
                    self.vel[1] -= overlap_y / self.mass
                    bact.vel[0] += overlap_x / bact.mass
                    bact.vel[1] += overlap_y / bact.mass
                elif distance > min_distance+5:
                    self.vel[0] += force_x / self.mass
                    self.vel[1] += force_y / self.mass
        self.rect.move_ip(self.vel)
        self.vel = [self.vel[0]/1.01, self.vel[1]/1.01]
    # def smart_vel_change(self, en, pos, signals):
    #