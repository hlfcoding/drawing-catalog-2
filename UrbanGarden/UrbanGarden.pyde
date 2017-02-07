# bitbucket.org/hlfcoding/hlf-processing-drawing-catalog-0

from umbrella import *

colorMode(HSB, 1)
shapeMode(CENTER)
translate(width / 2, height / 2)
noStroke()

u = Umbrella()
u.setColor(0, 0.4, 1)
shape(u.shape)
