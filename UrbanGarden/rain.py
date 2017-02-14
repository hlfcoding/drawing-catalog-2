from hlf.core import SubSketch

class Rain(object):

    def __init__(self, count, bounds):
        self.bounds = bounds
        self.count = count
        self.positions = []
        self.distribute()
        r = range(0, count)
        self.lengths = [1 + noise(i) * 2 for i in r]
    
    def distribute(self):
        ox, oy, w, h = self.bounds
        gridSize = int(sqrt(self.count))
        cellW = w / gridSize
        cellH = h / gridSize
        r = range(0, gridSize)
        for i in r:
            for j in r:
                x = ox + (i * cellW) + (noise(i, j) * -2 + 1) * cellW
                y = oy + (j * cellH) + (noise(j, i) * -2 + 1) * cellH
                self.positions.append((x, y))

class RainTest(SubSketch):

    def setup(self):
        stroke(0)
        self.isCentered = False
        self.subject = Rain(count=100, bounds=(0.0, 0.0, 100.0, 100.0))

    def draw(self):
        for i, (x, y) in enumerate(self.subject.positions):
            l = self.subject.lengths[i]
            line(x, y, x, y + l)
