from color import Color
from itertools import product
from region import Region
from shapes import Circle

import math

class ComicShader():
    def __init__(self, scale = 1, color = True):
		self.color = color
		self.scale = scale

    def __call__(self, image):
		diameter = int(10 * self.scale)
		pixels = image.load()
		region = Region()

		if diameter <= 0:
			return

		for x in xrange(0, image.size[0], diameter):
			for y in xrange(0, image.size[1], diameter):
				region.x = x;
				region.y = y;
				region.width = min(diameter, image.size[0] - region.x)
				region.height = min(diameter, image.size[1] - region.y)

				self.dot(pixels, region, diameter)

    def dot(self, pixels, region, diameter, invert = False):
		circle = Circle()
		circle.diameter = diameter
		circle.x = region.left
		circle.y = region.top

		dot_color = Color.average(pixels, region)

		old_origin = circle.origin
		lightness = 0.2126 * dot_color.rgba[0] + 0.7152 * dot_color.rgba[1] + 0.0722 * dot_color.rgba[2]
		circle.diameter *= 0.25 + (1 - (lightness / 255)) * 0.75
		circle.origin = old_origin

		if not self.color:
			for i in xrange(3):
				dot_color.rgba[i] = int(lightness)

		for point in product(xrange(region.left, region.right), xrange(region.top, region.bottom)):
			opacity = 0
			for corner in product((point[0], point[0] + 1), (point[1], point[1] + 1)):
				if circle.contains(corner):
					opacity += 0.25

			color = dot_color.rgba[0:3]
			color.append(int(dot_color.rgba[3] * (opacity * 255)))
			pixels[point[0], point[1]] = tuple(color)
