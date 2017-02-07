class Umbrella(object):

    def __init__(self):
        self.radius = 25.0
        self.ribCount = 4
        self.shape = self.createShape()

    @property
    def diameter(self):
        return self.radius * 2

    def createShape(self):
        s = createShape(GROUP)

        canopy = createShape(ELLIPSE, 0, 0, self.diameter, self.diameter)
        s.addChild(canopy)

        for i in range(0, self.ribCount):
            offset = 0.2
            h = self.diameter / 20
            rib = createShape(RECT, -self.radius * (1 + offset), -h / 2,
                              self.diameter * (1 + offset), h)
            rib.rotate(PI * i / self.ribCount)
            s.addChild(rib)

        return s
