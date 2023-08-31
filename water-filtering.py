from BactParent import BactParent


class WaterFiltering(BactParent):
    def __init__(self, pos):
        super().__init__("images/water-filtering.png", pos, 10, 10, 100, 0, (0, 0, 0))

    def get_energy(self):
        pass
