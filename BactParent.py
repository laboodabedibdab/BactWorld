import pygame
import pymunk  #физика игры

#ПРИВЕЕЕЕЕТ
def custom_attraction(obj, obj2): #индивидуальный аттракцион ЭТА ФУНКЦИЯ СЧИТАЕТ ВЕКТОР СИЛЫ
    g = 50000  # Коэффициент притяжения
    distance = obj.body.position.get_distance(obj2.body.position) #объект тело позиция берём дистанцию( объект2 тело димтанция) смотрим дистанцию между двумя телами
    force_magnitude = g / distance ** 2 # величина силы вектор величина силы умноженая на дистанцию в квадрате
    force_vector = force_magnitude * (obj2.body.position - obj.body.position).normalized()# вектор силы (normalized() -  приводит к виду от 0 до 1)
    return force_vector


class BactParent(pygame.sprite.Sprite): # это класс от которого мы будем создавать объекты(спрайты)
    def __init__(self, image: str, pos: tuple, mass: int, radius: int, en: int, speed: int, sig_co: tuple):
                                # картинка позиция масса радиус энергия скорость (sin_go) - коеффициент отвечающий за поведение бактерии
        super().__init__()
        self.image = pygame.image.load(image)
        self.mass = mass
        self.radius = radius
        self.moment = pymunk.moment_for_circle(mass, 0, self.radius) # вычисляет инерцию(масса, чужой радиус, свой радиус)
        self.body = pymunk.Body(self.mass, self.moment) # тело масса и инерция (это тело для работы пиманка)
        self.body.position = pos # позиция
        self.shape = pymunk.Circle(self.body, self.radius) # форма = pymunk.Circle(тело, радиус) - Форма круга, определяемая радиусом
        self.rect = self.image.get_rect() # Команда get_rect() оценивает изображение image и высчитывает прямоугольник, способный окружить его. rect - прямоугольник
        self.rect.centerx = pos[0] # прямоугольник центр по x
        self.rect.centery = pos[1] # прямоугольник центр по y

        self.en = en
        self.speed = speed
        self.sig_co = sig_co

    def update(self, objects): # функция отвечает за обновление
        for obj2 in objects: # из объектов он выбирает первый элемент это и будет obj2
            if self != obj2: # далее он исключает obj2
                attraction_force = custom_attraction(self, obj2) # self передаёт экземпляр
                self.body.apply_force_at_world_point(attraction_force, self.body.position) # apply_force_at_world_point - применить силу к обьекту в спейсе
        self.rect.centerx = self.body.position.x
        self.rect.centery = self.body.position.y

    def draw(self, screen):
        screen.blit(self.image, self.rect.center) # она перед отрисовкой добавляет картинку(в скобках ссылка на картинку и центр шарика)

    def smart_vel_change(self, objects):
        for obj2 in objects:
            distance = self.body.position.get_distance(obj2.body.position)
            print(distance)
