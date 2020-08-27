# Comic Collator
Comic collator, collate image files and concat images leaving ready to print.


```
python comic-collator/__main__.py --path /route/to/comic-NN/ --extension png --default_image /route/to/default/000.jpg
```

**Options**:
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
   DESC help to print front pages and then put again in same order front was printed.
   To print

   For example will produce:

     ```
     front 1
     front 2
     front 3
     back for front 3
     back for front 2
     back for front 1
     ```

---

restrictions (aka. stuff to improve):
* files must to have same extension
* don't support joined images.
* prefered same images size.
* assume filename format is a number like these examples: 1.jpg or 01.jpg or 001.jpg
   * the priority try to find 1.jpg then 01.jpg and at the end 001.jpg if is not found
   return default images if is specified.
* assume image are portrait.
* collate for letter size papers.
* don't print directly (maybe with a config file to setup the printer values)
* max number of images 999

some possibilities in future:
* config file
* choose image size
   * maybe review images sizes and suggest choose one if are different sizes.
* choose extension
   * for example if are only one extension use that one, if has more ask for validation, or priority.
* choose margin
* maybe indicate the format of filenames
* don't require the default image and draw an white page.
* don't require path and use current directory.
