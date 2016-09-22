def irange(image, region = None):
    """
    """
    if region == None:
        X = xrange(image.width)
        Y = xrange(image.height)
    else:
        X = xrange(region[0], region[2])
        Y = xrange(region[1], region[3]);

    pixels = image.load()
    for x in X:
        for y in Y:
            yield pixels[x, y]
