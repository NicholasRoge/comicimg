from region import Region

class Mask(object):
    # Magic shit may happen because of the next few methods.
    # Leave with the knowledge that they're here, that you may better fight the
    # dragons they spawn.
    def __call__(self, image, region = None, invert = False):
        self.apply(image, image, region, invert)

    def apply(self, image, region = None, invert = False):
        """
        Applies the mask to the given image.

        @param Image image
        """
        if region == None:
            region = (0, 0, image.size[0], image.size[1])

        for pixel, x, y in irange(image, region):
            pixel = pixels[x, y]

            interp_x = float(x) / image.size[0]
            interp_y = float(y) / image.size[1]

            opacity = self.test(pixel, interp_x, interp_y)
            if self.invert:
                opacity = 1.0 - opacity

            pixel[3] *= opacity

            pixels[x, y] = pixel

    def test(color, interp_x, interp_y):
        return 1.0


class CircleMask(Mask):
    def __init__(self, scale = 1.0, region = None):
        super(self).__init__(region)

        self.scale = scale

    def test(self, color, xy):
        x = xy[0] - 0.5
        y = xy[1] - 0.5

        fade_start = self.scale - 0.05
        fade_end = self.scale + 0.05

        distance = sqrt(x ** 2 + y ** 2)
        if distance < fade_start:
            return 1.0
        else:
            if distance > fade_end:
                return 0.0
            else:
                return (fade_end - distance) * 10
