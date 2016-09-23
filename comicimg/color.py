def mix(colors):
	"""
	Mixes a list of rgb triplets.

	@param iterable(r, g, b) colors List of colors to be mixed.

	@return tuple(r, g, b) The result of a numeric average of each channel's
	values.
	"""
	color_avg = [0, 0, 0]
	color_count = 0
	for color in colors:
		color_avg[0] += color[0]
		color_avg[1] += color[1]
		color_avg[2] += color[2]
		color_count += 1

	color_avg[0] /= color_count
	color_avg[1] /= color_count
	color_avg[2] /= color_count

	return tuple(color_avg)
