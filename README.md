# Drawing Catalog 2

## Notes

PEP8 specifies underscored names for things besides classes. However, the
Processing API uses camelized names, so the code here will / should follow.

Processing doesn't really support modules (classes in other folders) and
classes are just loaded from the sketch folder. To simulate modules and load
files in the `libraries` folder, make a symlink `ln -s <full-library-file-
path> <full-sketch-folder-path>` Then just `import * from <library-file-
name>` in your sketch.
