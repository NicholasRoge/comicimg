class Circle(object):
	def __init__(self, radius = 1, origin = (0, 0)):
		self.radius = radius
		self.origin = origin

	@property
	def diameter(self):
		return self.radius * 2.0

	@diameter.setter
	def diameter(self, diameter):
		self.radius = diameter / 2.0

	@property
	def origin(self):
		return (self.x + self.radius, self.y + self.radius)

	@origin.setter
	def origin(self, origin):
		self.x = origin[0] - self.radius
		self.y = origin[1] - self.radius

	def contains(self, point):
		x = point[0] - self.origin[0]
		y = point[1] - self.origin[1]

		return x ** 2 + y ** 2 <= self.radius ** 2
