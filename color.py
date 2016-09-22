from itertools import product

def average(colors):
	color_avg = (0, 0, 0)
	for color in colors:
		color_avg[0] += color[0]
		color_avg[1] += color[1]
		color_avg[2] += color[2]

	length = len(colors)
	color_avg[0] /= length
	color_avg[1] /= length
	color_avg[2] /= length

	return color_avg
	
class Color(object):
	@staticmethod
	def average(pixels, region = None):
		average_color = [0, 0, 0, 0]
		for point in product(xrange(region.left, region.right), xrange(region.top, region.bottom)):
			for i in xrange(4):
				average_color[i] += pixels[point[0], point[1]][i]

		color_count = region.width * region.height
		for i in xrange(4):
			average_color[i] /= color_count

		return Color(average_color)

	def __init__(self, rgba):
		self.rgba = rgba
