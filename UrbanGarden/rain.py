from hlf.core import sketch, SubSketch

class Rain(object):

    def __init__(self, count, bounds, lengthBounds=(1.0, 3.0), intensity=1):
        self.bounds = bounds
        self.count = count
        self.intensity = intensity
        self.lengthBounds = lengthBounds
        self.lengths = []
        self.positions = []
        self.distribute()

    def distribute(self):
        ox, oy, w, h = self.bounds
        self.gridSize = int(sqrt(self.count))
        cellW = w / self.gridSize
        cellH = h / self.gridSize
        self.cellSize = (cellW, cellH)
        minL, maxL = self.lengthBounds
        r = range(0, self.gridSize)
        for i in r:
            for j in r:
                self.lengths.append(minL + noise(i, j) * maxL)
                x = self.distributeX(i, j)
                y = oy + (j * cellH) + (noise(j, i) * -2 + 1) * cellH
                self.positions.append((x, y))

    def distributeX(self, i, j):
        ox, _, w, _ = self.bounds
        cellW, _ = self.cellSize
        return ox + (i * cellW) + (noise(i, j) * -2 + 1) * cellW

    def fall(self):
        _, oy, _, h = self.bounds
        for i, (x, y) in enumerate(self.positions):
            l = self.lengths[i]
            y += pow(l * self.intensity, 0.7)
            if y > oy + h:
                y = oy
                gi = i / self.gridSize
                gj = int(random(0, self.gridSize))
                x = self.distributeX(gi, gj)
            self.positions[i] = (x, y)

class RainTest(SubSketch):

    def setup(self):
        self.bg = 0.0
        self.fg = sketch.invert(self.bg)
        self.isCentered = False
        self.subject = Rain(count=100, bounds=(0.0, 0.0, 100.0, 100.0))

    def draw(self):
        self.subject.fall()
        _, maxL = self.subject.lengthBounds
        for i, (x, y) in enumerate(self.subject.positions):
            l = self.subject.lengths[i]
            stroke(self.fg, sq(l / maxL))
            line(x, y, x, y + l)