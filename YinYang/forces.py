class SwirlingForce(object):

    def __init__(self,
                 dampener=0.01,
                 offset=0,
                 radius=100):
        self.dampener = dampener
        self.offset = offset
        self.radius = radius

    def theta(self, element):
        return element.tick * self.dampener + self.offset

    def apply(self, element):
        # Convert polar to cartesian coordinates.
        t = self.theta(element)
        x = self.radius * cos(t)
        y = self.radius * sin(t)
        element.position.set(x, y)

