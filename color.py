def mix(colors):
	"""
	Mixes a list of rgb triplets.

	@param iterable(rgb) colors List of colors to be mixed.

	@return rgb The result of a numeric average of each channel's values.
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

def rgb(r, g, b):
	"""
	Makes an rgb triplet.

	@param numeric r Red channel value
	@param numeric g Green channel value
	@param numeric b Blue channel value

	@return tuple(numeric, numeric, numeric) Returns a tuple containing, in
	order, the red, green, and blue channel values.
	"""
	return (r, g, b)
