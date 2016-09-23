from PIL import Image
from sys import stderr
from sys import exit
from os.path import isfile

import argparse
import shaders

argparser = argparse.ArgumentParser(
	description = 'Applies a comic book filter effect to an image.'
)
argparser.add_argument(
	'-c', '--color',
	dest = 'mono',
	default = True,
	action='store_false',
	help="render the image in color"
)
argparser.add_argument(
	'-s', '--size',
	dest = 'size',
	type = int,
	default = 10,
	help = "diameter of the 'circles' in pixels"
)
argparser.add_argument(
	'infile',
	type = str,
	help = "file to apply the filter effect to"
)
argparser.add_argument(
	'outfile',
	type = str,
	nargs = '?',
	help = "file or path to store the modified image"
)

args = argparser.parse_args()
if not args.outfile:
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
