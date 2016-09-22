from colorsys import hls_to_rgb
from colorsys import rgb_to_hls
from masks import CircleMask
from region import Region

import color

class ComicShader():
    def __init__(self, scale = 1, mono = True):
		self.mono = mono
		self.scale = scale

    def __call__(self, image):
		self.apply(image)

    def apply(self, image):
		pixels = image.load()
        mask = CircleMask()

        size = 10
		for x in xrange(0, image.size[0], size):
			for y in xrange(0, image.size[1], size):
				mask.region.x = x;
				mask.region.y = y;
				mask.region.width = min(size, image.size[0] - region.x)
				mask.region.height = min(size, image.size[1] - region.y)

                color = color.average(image, region)
                hls = rgb_to_hls(color)

                mask.scale = hls[1]
                if self.mono:
                    hls[2] = 0
                    color = hls_to_rgb(hls)

                image.paste(color, tuple(mask.region))
                mask.apply(image)
