class Region(object):
	def __init__(self):
		self.x = 0
		self.y = 0
		self.width = 0
		self.height = 0

	def __iter__(self):
		yield self.left
		yield self.top
		yield self.right
		yield self.bottom

	def __getitem__(self, key):
		if key == 0:
			return self.left
		elif key == 1:
			return self.top
		elif key == 2:
			return self.right
		elif key == 3:
			return self.bottom
		else:
			return None


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
		self.width = max(value - self.left, 0)

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

	def ltr(self):
		return xrange(self.left, self.right)

	def rtl(self):
		return xrange(self.right, self.left, -1)

	def ttb(self):
		return xrange(self.top, self.bottom)

	def btt(self):
		return xrange(self.bottom, self.top, -1)
