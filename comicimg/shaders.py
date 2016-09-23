from colorsys import hls_to_rgb
from colorsys import rgb_to_hls
from helpers import colors
from masks import CircleMask
from math import log
from os.path import isfile
from region import Region

import color


def comicimg(image, mono = True, size = 10):
    pixels = image.load()
    mask = CircleMask()

    region = Region()
    for x in xrange(0, image.size[0], size):
        for y in xrange(0, image.size[1], size):
            region.left = x
            region.right = min(region.left + size, image.size[0])
            region.top = y
            region.bottom = min(region.top + size, image.size[1])

            cell_color = color.mix(colors(image, region))

            hls = rgb_to_hls(cell_color[0] / 255.0, cell_color[1] / 255.0, cell_color[2] / 255.0)
            hls = [value for value in hls] #seriously, python...

            # A short explanation for the following:
            #
            mask.scale = 1.0 - hls[1]

            something = 0.25
            something_else = 1.0 + 2.0 * something
            mask.scale = (mask.scale * something_else) + something
            if mask.scale < something:
                continue

            if mono:
                hls[2] = 0
                cell_color = hls_to_rgb(*hls)
                cell_color = tuple(int(value * 255) for value in cell_color)

            image.paste(cell_color, tuple(region))

            mask(image, region)
