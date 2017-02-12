# bitbucket.org/hlfcoding/hlf-processing-drawing-catalog-0

from person import *

colorMode(HSB, 1)
shapeMode(CENTER)
translate(width / 2, height / 2)
noStroke()

p = Person()
p.umbrella.setColor(0, 0.4, 1)
p.draw()
