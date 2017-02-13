from hlf.core import SubSketch

class Rain(object):

    def __init__(self, count, bounds):
        xmin, ymin, xmax, ymax = bounds
        r = range(0, count)
        self.positions = [(random(xmin, xmax), random(ymin, ymax)) for i in r]
        self.lengths = [random(1, 5) for i in r]

class RainTest(SubSketch):

    def setup(self):
        stroke(0)
        self.isCentered = False
        self.subject = Rain(count=50, bounds=(0, 0, 100, 100))

    def draw(self):
        for i, (x, y) in enumerate(self.subject.positions):
            l = self.subject.lengths[i]
            line(x, y, x, y + l)
