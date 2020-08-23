# printcomic
print comics

```
 python3 main.py -path /route/to/comic-NN/ -extension png --default_image ../000.jpg
```

will return the list of images ordered to print

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