from colorsys import hls_to_rgb
from colorsys import rgb_to_hls
from masks import CircleMask
from os.path import isfile
from region import Region

import color


def comicimg(image, mono = True):
    pixels = image.load()
    mask = CircleMask()

    size = 10
    for x in xrange(0, image.size[0], size):
        for y in xrange(0, image.size[1], size):
            mask.region.left = x;
            mask.region.right = min(x + size, image.size[0])
            mask.region.top = y
            mask.region.bottom = min(y + size, image.size[1])

            color = color.mix(irange(image, region))
            hls = rgb_to_hls(color)

            mask.scale = hls[1]
            if mono:
                hls[2] = 0
                color = hls_to_rgb(hls)

            image.paste(color, tuple(mask.region))
			mask(image, region)
