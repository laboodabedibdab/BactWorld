import random

from BactParent import BactParent


class Electric(BactParent):
    def __init__(self, pos, space, objects, places):
        super().__init__("images/electric.png", pos, 10, 10, 100, 0, (random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10)), space=space,
                         objects=objects,
                         places=places)

    def get_energy(self):
        pass
