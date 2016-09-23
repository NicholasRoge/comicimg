def pixels(image, region = None):
    """
    Iterates over all or, optionally, only a single region of an image, yielding
    triplet containing each pixel's color, x position, and y position.

    @param Image image Image to iterate over.
    @param iterable region Region to constrain iteration to.

    @return generator(tuple(color, x, y))
    """
    if region == None:
        X = xrange(image.width)
        Y = xrange(image.height)
    else:
        X = xrange(region[0], region[2])
        Y = xrange(region[1], region[3]);

    data = image.load()
    for x in X:
        for y in Y:
            yield (data[x, y], x, y)

def colors(image, region = None):
    """
    """
    for pixel in pixels(image, region):
        yield pixel[0]
