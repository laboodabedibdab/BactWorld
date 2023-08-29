import pygame
import math
from pygame.locals import FULLSCREEN

pygame.init()
inf = pygame.display.Info()
WIDTH = inf.current_w
HEIGHT = inf.current_h
print(WIDTH, HEIGHT)
screen = pygame.display.set_mode((WIDTH, HEIGHT), FULLSCREEN)
clock = pygame.time.Clock()
font = pygame.font.SysFont("Verdana", WIDTH // 50)
big_font = pygame.font.SysFont("Verdana", WIDTH // 25)


class GameObject(pygame.sprite.Sprite):
    def __init__(self, image, pos, mass, radius, specie):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(center=pos)
        self.mass = mass
        self.vel = [0, 0]
        self.radius = radius
        self.specie = specie


class SunPlace(pygame.sprite.Sprite):
    def __init__(self, place, time):
        super().__init__()
        self.x = place[0]
        self.y = place[1]
        self.w = place[2]
        self.h = place[3]
        self.time = pygame.time.get_ticks()//
        self.color = [50 * self.time + 1 for _ in range(3)]
        self.image = pygame.Surface([self.w, self.h])
        self.image.fill(self.color)

    def update(self):
        self.time += 1
        self.time %= 4
        self.color = [50 * self.time + 1 for _ in range(3)]
        self.image.fill(self.color)
    # def cont_pos(self, pos):
    #     if self.x < pos[0] < self.x + self.w and self.y < pos[1] < self.y + self.h:
    #         return 1
    #     else:
    #         return 0


class TriGG(pygame.sprite.Sprite):
    def __init__(self, pos, w):
        super().__init__()
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.w = w
        self.c_pos = pos
        self.num = 0

        self.image = pygame.Surface((w, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (w // 2, 10), 10, 3)
        pygame.draw.circle(self.image, (255, 255, 255), (w // 2, 10), 2)
        pygame.draw.line(self.image, (255, 255, 255), (0, 9), (w, 9), 2)

        self.rect = self.image.get_rect(topleft=pos)

    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            self.c_pos = (pygame.mouse.get_pos()[0], self.c_pos[1])
            self.num = (self.c_pos[0] - self.x + 1) / self.w


class ButtonPg:
    def __init__(self, pos, w, h, color=(0, 0, 0)):
        self.x = pos[0]
        self.y = pos[1]
        self.w = w
        self.h = h
        self.color = color

    def draw(self, color=None):
        if color is None:
            color = self.color
        pygame.draw.rect(screen, color, (self.x, self.y, self.w, self.h))

    def is_mouse(self, pos=None):
        t = False
        if pos is not None:
            if self.x < pos[0] < (self.x + self.w) and self.y < pos[1] < (self.y + self.h):
                t = True
            return t


objects = pygame.sprite.Group()
simulation_paused = False
tr = TriGG((11, 101), 80)
sp = ButtonPg((10, 60), WIDTH / 10 - 20, WIDTH / 40)
clr = ButtonPg((10, 118), WIDTH / 10 - 20, WIDTH / 40, color=(200, 50, 50))
ext = ButtonPg((0, 170), WIDTH / 10, WIDTH / 20, color=(255, 0, 0))
sun_square = SunPlace((WIDTH * 0.2, HEIGHT / 10, WIDTH * 0.6, HEIGHT * 0.8), 1)
G = 10


def update():
    global simulation_paused
    if simulation_paused:
        return
    for obj1 in objects:
        for obj2 in objects:
            if obj1 != obj2:
                dx = obj2.rect.centerx - obj1.rect.centerx
                dy = obj2.rect.centery - obj1.rect.centery
                distance = math.sqrt(dx ** 2 + dy ** 2)
                force_magnitude = (obj1.mass * obj2.mass) / (distance ** 2 + 0.001)
                angle = math.atan2(dy, dx)
                force_x = force_magnitude * math.cos(angle)
                force_y = force_magnitude * math.sin(angle)
                min_distance = obj1.width / 2 + obj2.width / 2

                if distance <= min_distance:
                    overlap = min_distance - distance
                    overlap_x = overlap * math.cos(angle)
                    overlap_y = overlap * math.sin(angle)
                    # obj1.rect.centerx -= overlap_x / 2
                    # obj1.rect.centery -= overlap_y / 2
                    # obj2.rect.centerx += overlap_x / 2
                    # obj2.rect.centery += overlap_y / 2
                    obj1.vel[0] -= overlap_x / obj1.mass
                    obj1.vel[1] -= overlap_y / obj1.mass
                    obj2.vel[0] += overlap_x / obj2.mass
                    obj2.vel[1] += overlap_y / obj2.mass
                obj1.vel[0] += force_x / obj1.mass
                obj1.vel[1] += force_y / obj1.mass
                # obj2.vel[0] += force_x / obj2.mass
                # obj2.vel[1] += force_y / obj2.mass
        if obj1.rect.left <= WIDTH / 10:
            obj1.rect.left = WIDTH / 10
        if obj1.rect.right >= WIDTH:
            obj1.rect.right = WIDTH
        if obj1.rect.top <= 0:
            obj1.rect.top = 0
        if obj1.rect.bottom >= HEIGHT:
            obj1.rect.bottom = HEIGHT
        obj1.rect.centerx += obj1.vel[0] * (1 - tr.num)
        obj1.rect.centery += obj1.vel[1] * (1 - tr.num)
        obj1.vel[0] /= 1.2
        obj1.vel[1] /= 1.2


def draw():
    screen.fill((0, 0, 0))
    sun_square.draw()
    objects.draw(screen)
    pygame.draw.rect(screen, (28, 28, 28), (0, 0, WIDTH // 10, HEIGHT))
    text = font.render(str(round(clock.get_fps())), True, (250, 250, 250))
    screen.blit(text, (int(WIDTH / 100 * 3), 20))
    sp.draw([(0, 200, 0), (200, 0, 0)][simulation_paused])
    text = font.render(str(["start", "pause"][simulation_paused]), True, (250, 250, 250))
    screen.blit(text, [(20, 50), (12, 47)][simulation_paused])
    tr.draw(screen)
    clr.draw()
    text = font.render(str("clear"), True, (250, 250, 250))
    screen.blit(text, (int(WIDTH / 100 * 1.5), 113))
    ext.draw()
    text = big_font.render(str("exit"), True, (250, 250, 250))
    screen.blit(text, (int(WIDTH / 100 * 1.5), 165))
    pygame.display.flip()


bact = ["photosynthetic", "predatory", "electric", "water-filtering", "water-filtering"]
running = True
z = False
while running:
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_q) or (event.type == pygame.QUIT) or (
                event.type == pygame.MOUSEBUTTONDOWN and ext.is_mouse(event.pos)):
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] > 95:
            obj = GameObject(
                "images/" + bact[event.button - 1] + ".png",
                event.pos,
                mass=10,
                width=20,
                height=20,
                specie=bact[event.button - 1]
            )
            objects.add(obj)
        elif (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (
                event.type == pygame.MOUSEBUTTONDOWN and sp.is_mouse(event.pos)):
            simulation_paused = not simulation_paused
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and tr.is_mouse(event.pos):
            z = True

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            z = False
        elif event.type == pygame.MOUSEBUTTONDOWN and clr.is_mouse(event.pos):
            objects = pygame.sprite.Group()
        if z and tr.is_mouse(event.pos):
            tr.correct_c_pos(event.pos)
    update()
    draw()
    clock.tick(40)

pygame.quit()
