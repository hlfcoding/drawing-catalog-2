from hlf.core import SubSketch

class Rain(object):

    def __init__(self, count, bounds):
        x, y, w, h = bounds
        r = range(0, count)
        c = float(count)
        self.positions = [(noise(i, 0) * w, noise(0, i) * h) for i in r]
        self.lengths = [1 + noise(i) * 4 for i in r]

class RainTest(SubSketch):

    def setup(self):
        stroke(0)
        self.isCentered = False
        self.subject = Rain(count=100, bounds=(0, 0, 100, 100))

    def draw(self):
        for i, (x, y) in enumerate(self.subject.positions):
            l = self.subject.lengths[i]
            line(x, y, x, y + l)
