import random

from BactParent import BactParent


class Photosynthetic(BactParent):
    def __init__(self, pos, space, objects, places):
        super().__init__("images/photosynthetic.png", pos, 10, 10, 100, 0,
                         (random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10)), space=space,
                         objects=objects,
                         places=places)

    def add_co(self, objects, places):
        super().add_co(objects, places)
