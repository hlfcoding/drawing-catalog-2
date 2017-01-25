# Drawing Catalog #2

Python sketches and boilerplate using Processing via jdf/processing.py.

## Exports

### I. YinYang

![yin-yang-yon](https://cloud.githubusercontent.com/assets/100884/22240247/124216f6-e1cf-11e6-8dd7-c9f3ba237645.gif)

### II. Snowflake

![snowflake](https://cloud.githubusercontent.com/assets/100884/22242809/9cc984c6-e1d9-11e6-9db9-744657a40290.gif)

---

```sh
# gist.github.com/dergachev/4627207
$ ffmpeg -i "$my_file_name.mov" -s 300x300 -pix_fmt rgb24 -r 10 -f gif - | \
> gifsicle --optimize=3 --delay=3 > "$my_file_name.gif"
```

## Setup

To run sketches locally, you'll need to set up the included custom libraries to
be properly imported:

```sh
$ my_p5_py_lib_path=~/Documents/Processing\ 3/modes/PythonMode/mode/Lib
$ my_checkout_path=~/Projects/processing-python-sketches
$ mkdir "$my_p5_py_lib_path"
$ ln -s "$my_checkout_path/libraries" "$my_p5_py_lib_path/hlf"
```

You can check the result via `println(sys.path)` as the first line in a sketch.

## Notes

PEP8 specifies underscored names for things besides classes. However, the
Processing API uses camelized names, so the code here will / should follow.

Processing doesn't really support modules (classes in other folders) and
classes are just loaded from the sketch folder. To simulate modules and load
files in the `libraries` folder, make a symlink `ln -s <full-library-file-
path> <full-sketch-folder-path>` Then just `import * from <library-file-
name>` in your sketch.
