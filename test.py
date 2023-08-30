import random

import pygame
import pymunk

# Инициализация Pygame
pygame.init()

# Окно
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pymunk Custom Attraction")

# Цвета
white = (255, 255, 255)
red = (255, 0, 0)

# Pymunk Space
space = pymunk.Space()
space.gravity = (0, 0)  # Отключение гравитации

speed = int(input())


# Функция для притяжения между спрайтами
def custom_attraction(body, other_body):
    G = 50000  # Коэффициент притяжения
    distance = body.position.get_distance(other_body.position)
    force_magnitude = G / distance ** 2
    force_vector = force_magnitude * (other_body.position - body.position).normalized()
    return force_vector


# Создание круглых спрайтов
circles = []

for _ in range(40):
    radius = 5
    mass = 1
    moment = pymunk.moment_for_circle(mass, 0, radius)
    body = pymunk.Body(mass, moment)
    x = random.randint(radius, screen_width - radius)
    y = random.randint(radius, screen_height - radius)
    body.position = x, y
    shape = pymunk.Circle(body, radius)
    space.add(body, shape)
    circles.append(body)

# Главный цикл
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Применение пользовательской силы притяжения между спрайтами
    for i, body in enumerate(circles):
        for other_body in circles[:i] + circles[i + 1:]:
            attraction_force = custom_attraction(body, other_body)
            body.apply_force_at_world_point(attraction_force, body.position)
        pos_x, pos_y = body.position
        radius = 10
        if pos_x - radius < 0:
            body.velocity = pymunk.Vec2d(20, body.velocity.y)
        elif pos_x + radius > screen_width:
            body.velocity = pymunk.Vec2d(-20, body.velocity.y)
        if pos_y - radius < 0:
            body.velocity = pymunk.Vec2d(body.velocity.x, 20)
        elif pos_y + radius > screen_height:
            body.velocity = pymunk.Vec2d(body.velocity.x, -20)
    # Обновление Pymunk
    space.step(1 / speed)

    # Отрисовка
    screen.fill(white)

    for body in circles:
        pos_x, pos_y = body.position
        radius = 5
        pygame.draw.circle(screen, red, (int(pos_x), int(pos_y)), int(radius))

    pygame.display.flip()
    clock.tick(240)

pygame.quit()
