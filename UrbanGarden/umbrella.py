from hlf.animation import Animation
from hlf.core import SubSketch

class Umbrella(object):

    roundEdge = 'round'

    def __init__(self, edgeType=roundEdge, radius=10.0, ribCount=4):
        self.edgeType = edgeType
        self.radius = radius
        self.ribCount = ribCount
        self.shape = self.createShape()
        self.closeAnimation = Animation(id='close', duration=0.3).pause()
        self.openAnimation = Animation(id='open', duration=0.3).pause()
        self.isOpened = True

    @property
    def canopy(self):
        return self.shape.getChild('canopy')

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def ribs(self):
        return self.shape.getChild('ribs').getChildren()

    def ribAngle(self, i):
        return PI * i / self.ribCount

    def setColor(self, h, s, b):
        self.canopy.setFill(color(h, s, b, 0.9))
        rFill = color(h, s, b - 0.1)
        for r in self.ribs:
            r.setFill(rFill)

    def close(self, animated=True):
        if self.closeAnimation.isPlaying:
            return True
        elif self.openAnimation.isPlaying:
            return False
        elif not self.isOpened:
            return False
        self.isOpened = False
        self.closeAnimation.play()
        if not animated:
            self.closeAnimation.skipProgress()
        return True

    def createShape(self):
        s = createShape(GROUP)

        canopy = None
        if self.edgeType is Umbrella.roundEdge:
            canopy = createShape(ELLIPSE, 0, 0, self.diameter, self.diameter)
        s.addChild(canopy)
        s.addName('canopy', canopy)

        ribs = createShape(GROUP)
        for i in range(0, self.ribCount):
            offset = 0.2
            h = self.diameter / 20
            r = createShape(RECT, -self.radius * (1 + offset), -h / 2,
                            self.diameter * (1 + offset), h)
            r.rotate(self.ribAngle(i))
            ribs.addChild(r)
        s.addChild(ribs)
        s.addName('ribs', ribs)

        return s

    def draw(self):
        self.updateAnimations()
        shape(self.shape)

    def open(self, animated=True):
        if self.openAnimation.isPlaying:
            return True
        elif self.closeAnimation.isPlaying:
            return False
        elif self.isOpened:
            return False
        self.isOpened = True
        self.openAnimation.play()
        if not animated:
            self.openAnimation.skipProgress()
        return True

    def updateAnimations(self):
        s = None
        if self.closeAnimation.updateProgress():
            s = 1 - self.closeAnimation.progress
            self.closeAnimation.resetIfNeeded()
        elif self.openAnimation.updateProgress():
            s = self.openAnimation.progress
            self.openAnimation.resetIfNeeded()
        else:
            return False
        canopy = self.canopy
        canopy.resetMatrix()
        canopy.scale(s)
        s = max(0.1, s)
        for i, r in enumerate(self.ribs):
            r.resetMatrix()
            r.rotate(self.ribAngle(i))
            r.scale(s, 1.0)

class UmbrellaTest(SubSketch):

    def setup(self):
        noStroke()
        self.subject = Umbrella(radius=25.0)
        self.subject.setColor(h=0, s=0.4, b=1)

    def draw(self):
        if mousePressed:
            if not self.subject.close():
                self.subject.open()
        self.subject.draw()
