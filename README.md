# Drawing Catalog #2

Python sketches and boilerplate using Processing via jdf/processing.py.

## I. YinYang

![yin-yang-1](https://s-media-cache-ak0.pinimg.com/originals/d4/e6/86/d4e686bfb5b87c14b8949204cd9bd579.jpg)
![yin-yang-2](https://s-media-cache-ak0.pinimg.com/originals/1c/f7/a2/1cf7a2138ebb779f21656de75a4460eb.jpg)

## Notes

PEP8 specifies underscored names for things besides classes. However, the
Processing API uses camelized names, so the code here will / should follow.

Processing doesn't really support modules (classes in other folders) and
classes are just loaded from the sketch folder. To simulate modules and load
files in the `libraries` folder, make a symlink `ln -s <full-library-file-
path> <full-sketch-folder-path>` Then just `import * from <library-file-
name>` in your sketch.
