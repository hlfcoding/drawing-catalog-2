# bitbucket.org/hlfcoding/hlf-processing-drawing-catalog-0

from hlf.core import sketch, SubSketch
from person import *
from rain import *
from umbrella import UmbrellaTest

UmbrellaTest().activate()
# PersonTest().activate()
# RainTest().activate()

def setup():
    colorMode(HSB, sketch.colorScale)
    shapeMode(CENTER)
    SubSketch.active.setupSketch()

def draw():
    SubSketch.active.drawSketch()
