#!/usr/bin/env python

from PIL import Image
from sys import stderr
from sys import exit
from os.path import isfile

import argparse
import shaders

argparser = argparse.ArgumentParser(description = 'Adds a comic book filter effect to an image.')
argparser.add_argument('infile', type = str, help = "File to apply the filter effect to.")
argparser.add_argument('outfile', type = str, default = "", nargs = '?', help = "Defaults to the value of infile.")
argparser.add_argument('-c', '--color', default = True, dest = 'mono', action='store_false', help="Flag indicating image should be rendered in color.")
argparser.add_argument('-s', '--size', type = int, default = 10, dest = 'size')

args = argparser.parse_args()
if args.outfile == "":
	args.outfile = args.infile


try:
	image = Image.open(args.infile)
except IOError as e:
	if not isfile(args.infile):
		stderr.write("No such file:  %s\n" % args.infile)

		exit(2)
	else:
		stderr.write("%s\n" % e.strerror)

		exit(2)

target = Image.new("RGBA", image.size, None)
target.paste(image)
shaders.comicimg(target, mono = args.mono, size = args.size)
target.save(args.outfile)
