class Umbrella(object):

    def __init__(self):
        self.radius = 25.0
        self.shape = self.createShape()

    @property
    def diameter(self):
        return self.radius * 2

    def createShape(self):
        g = createShape(GROUP)

        e = createShape(ELLIPSE, 0, 0, self.diameter, self.diameter)
        withOffset = 1.2
        h = self.diameter / 20
        r = createShape(RECT, -self.radius * withOffset, -h / 2,
                        self.diameter * withOffset, h)
        r2 = createShape(RECT, -self.radius * withOffset, -h / 2,
                         self.diameter * withOffset, h)
        r2.rotate(PI / 2)

        g.addChild(e)
        g.addChild(r)
        g.addChild(r2)
        return g
