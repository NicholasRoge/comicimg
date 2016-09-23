# Comic Image Filter

Command to apply a comic filter to a specified image.

## How to Use

```
usage: comicimg [-h] [-c] [-s SIZE] infile [outfile]

Applies a comic book filter effect to an image.

positional arguments:
  infile                file to apply the filter effect to
  outfile               file or path to store the modified image

optional arguments:
  -h, --help            show this help message and exit
  -c, --color           render the image in color
  -s SIZE, --size SIZE  diameter of the 'circles' in pixels
```

Add [bin](bin) to your path and invoke apply the filter by passing at least one argument (the name of the file to apply the filter to) to the [comicimg](bin/comicimg) script.

## License

This project is licensed under the MIT License - see [LICENSE.md](LICENSE.md) file for details.
