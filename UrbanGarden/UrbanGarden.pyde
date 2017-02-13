# bitbucket.org/hlfcoding/hlf-processing-drawing-catalog-0

from hlf.core import SubSketch
from person import *
from rain import *
from umbrella import UmbrellaTest

colorMode(HSB, 1)
shapeMode(CENTER)
noStroke()

# UmbrellaTest().activate()
# PersonTest().activate()
RainTest().activate()

SubSketch.active.setup()
SubSketch.active.drawSketch()
