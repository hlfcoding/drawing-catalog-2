# bitbucket.org/hlfcoding/hlf-processing-drawing-catalog-0

from hlf.core import sketch, SubSketch
from person import *
from rain import *
from umbrella import UmbrellaTest

colorMode(HSB, sketch.colorScale)
shapeMode(CENTER)

# UmbrellaTest().activate()
# PersonTest().activate()
RainTest().activate()

SubSketch.active.setup()
SubSketch.active.drawSketch()
