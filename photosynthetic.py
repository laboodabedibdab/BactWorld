from BactParent import BactParent

class Photosynthetic(BactParent):
    def __init__(self, pos):
        super().__init__("images/photosynthetic.png", pos, 10, 10, 100, 0, (0, 0, 0))

    def add_co(self, objects, places):
        super().add_co(objects, places)

