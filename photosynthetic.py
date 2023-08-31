from BactParent import BactParent


class Photosynthetic(BactParent):
    def __init__(self, pos):
        """

        :rtype: object
        """
        super().__init__("images/photosynthetic.png", pos, 10, 10, 100, 0, (0, 0, 0))
