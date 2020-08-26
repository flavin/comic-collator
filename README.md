# printcomic
print comics, collate image files and concat images ready to print.

```
 python3 main.py --path /route/to/comic-NN/ --extension png --default_image /route/to/default/000.jpg
```

Options:
* -p, --path
   * image directory
* -e, --extension
   * images file extension
* -w, --wet_run
   * save the output file
* -s, --style [STYLE]
   * how the page are collated, STYLE can be 'western' or 'japanese', default 'western'
* -di, --default_image
   * default image, to fill empty pages.
* -bo, --back_order [ORDER]
   * back print order, ORDER can be ASC or DESC, by default is ASC
   DESC help to print front pages, then take the pages and just put in the printer
   to print background

---
restrictions (aka. stuff to improve):
- files must to have same extension
- don't support joined images.
- prefered same images size.
- assume filename format of number like 00.extension(ex. 01.jpg)
- assume image are portrait.
- collate for letter size papers.
- don't print directly (maybe with a config file to setup the printer values)
- max number of images 99

some possibilities in future:
- config file
- choose image size
   - maybe review images sizes and suggest choose one if are different sizes.
- choose margin
- maybe indicate the format of filenames