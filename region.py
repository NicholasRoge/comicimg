class Region(object):
	def __init__(self):
		self.x = 0
		self.y = 0
		self.width = 0
		self.height = 0

	@property
	def left(self):
		return self.x

	@left.setter
	def left(self, value):
		self.width -=  value - self.x
		self.x = value

	@property
	def right(self):
		return self.left + self.width

	@right.setter
	def right(self, value):
		self.width = math.max(value - self.left, 0)

	@property
	def top(self):
		return self.y

	@top.setter
	def top(self, value):
		self.height -=  value - self.y
		self.y = value

	@property
	def bottom(self):
		return self.top + self.height

	@bottom.setter
	def bottom(self, value):
		self.height = max(value - self.top, 0)
