class Size:
    height = 10.0
    width = 10.0

    @property
    def radius(self):
        if self.width != self.height:
            raise Exception('Width and height not the same.')
        return self.width / 2

    @radius.setter
    def radius(self, value):
        self.width = self.height = value

class Skin:
    fill = None
    stroke = None
    strokeWeight = 1

    def apply(self):
        if self.fill is None:
            noFill()
        else:
            fill(self.fill)
        if self.stroke is None:
            noStroke()
        else:
            stroke(self.stroke)
            strokeWeight(self.strokeWeight)

class Element(object):

    def __init__(self, id, position=None, size=None, skin=None):
        self.id = id
        self.position = PVector() if position is None else position
        self.size = Size() if size is None else size
        self.skin = Skin() if skin is None else skin
        self.children = []
        self.forces = []
        self.velocity = PVector()

    def __del__(self):
        self.forces = []

    def draw(self):
        self.skin.apply()
        self._handleDraw()
        for el in self.children:
            el.draw()

    def updatePosition(self):
        self.position.add(self.velocity)
        for el in self.children:
            el.updatePosition()

    def updateVelocity(self):
        for f in self.forces:
            self._applyForce(f)
        for el in self.children:
            el.updateVelocity()

    def _applyForce(self, force):
        if callable(force):
            force = force()
        self.velocity.add(force)

    def _handleDraw(self):
        ellipse(
            self.position.x,
            self.position.y,
            self.size.width,
            self.size.height
        )

    def log(self, value, label=None):
        println('element \'{0}\': {1} {2}'
            .format(self.id, value, '' if label is None else '({})'.format(label)))
