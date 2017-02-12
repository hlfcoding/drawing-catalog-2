from hlf.core import SubSketch

class Umbrella(object):

    def __init__(self):
        self.radius = 25.0
        self.ribCount = 4
        self.shape = self.createShape()

    @property
    def diameter(self):
        return self.radius * 2

    def setColor(self, h, s, b):
        self.shape.getChild('canopy').setFill(color(h, s, b, 0.9))
        rC = color(h, s, b - 0.1)
        for r in self.shape.getChild('ribs').getChildren():
            r.setFill(rC)

    def createShape(self):
        s = createShape(GROUP)

        canopy = createShape(ELLIPSE, 0, 0, self.diameter, self.diameter)
        s.addChild(canopy)
        s.addName('canopy', canopy)

        ribs = createShape(GROUP)
        for i in range(0, self.ribCount):
            offset = 0.2
            h = self.diameter / 20
            r = createShape(RECT, -self.radius * (1 + offset), -h / 2,
                            self.diameter * (1 + offset), h)
            r.rotate(PI * i / self.ribCount)
            ribs.addChild(r)
        s.addChild(ribs)
        s.addName('ribs', ribs)

        return s

class UmbrellaTest(SubSketch):

    def setup(self):
        self.subject = Umbrella()
        self.subject.setColor(0, 0.4, 1)

    def draw(self):
        shape(self.subject.shape)
