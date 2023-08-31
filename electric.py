from BactParent import BactParent


class Electric(BactParent):
    def __init__(self, pos):
        super().__init__("images/electric.png", pos, 10, 10, 100, 0, (0, 0, 0))

    def get_energy(self):
        pass
