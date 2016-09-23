from helpers import pixels
from region import Region


class Mask(object):
    # Magic shit may happen because of the next few methods.
    # Leave with the knowledge that they're here, that you may better fight the
    # dragons they spawn.
    def __call__(self, image, region = None, invert = False):
        self.apply(image, region, invert)

    def apply(self, image, region = None, invert = False):
        """
        Applies the mask to the given image.

        @param Image image
        """
        if region == None:
            region = (0, 0, image.size[0], image.size[1])

        data = image.load()
        for color, x, y in pixels(image, region):
            interp_x = float(x - region.left) / region.width
            interp_y = float(y - region.top) / region.width

            opacity = self.test(color, (interp_x, interp_y))
            if invert:
                opacity = 1.0 - opacity

            data[x, y] = (color[0], color[1], color[2], int(color[3] * opacity))

    def test(self, color, xy):
        return 1.0


class CircleMask(Mask):
    def __init__(self, scale = 1.0):
        super(CircleMask, self).__init__()

        self.scale = scale

    @property
    def scale(self):
        return self._scale

    @scale.setter
    def scale(self, value):
        self._scale = value
        self.fade_start = ((value / 2.0) - 0.05) ** 2
        self.fade_end = ((value / 2.0) + 0.05) ** 2

    def test(self, color, xy):
        x = xy[0] - 0.5
        y = xy[1] - 0.5

        distance = x ** 2 + y ** 2

        if distance < self.fade_start:
            return 1.0
        else:
            if distance > self.fade_end:
                return 0.0
            else:
                return (self.fade_end - distance) * 10
