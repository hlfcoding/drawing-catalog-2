from hlf.animation import Animation
from hlf.core import SubSketch

class Umbrella(object):

    def __init__(self):
        self.radius = 25.0
        self.ribCount = 4
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

    def rotateRib(self, rib, i):
        rib.rotate(PI * i / self.ribCount)

    def setColor(self, h, s, b):
        self.canopy.setFill(color(h, s, b, 0.9))
        rC = color(h, s, b - 0.1)
        for r in self.ribs:
            r.setFill(rC)

    def close(self):
        if self.closeAnimation.isPlaying:
            return True
        elif self.openAnimation.isPlaying:
            return False
        elif not self.isOpened:
            return False
        self.isOpened = False
        self.closeAnimation.play()
        return True

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
            self.rotateRib(r, i)
            ribs.addChild(r)
        s.addChild(ribs)
        s.addName('ribs', ribs)

        return s

    def open(self):
        if self.openAnimation.isPlaying:
            return True
        elif self.closeAnimation.isPlaying:
            return False
        elif self.isOpened:
            return False
        self.isOpened = True
        self.openAnimation.play()
        return True

    def updateAnimations(self):
        s = None
        if self.closeAnimation.updateProgress():
            p = self.closeAnimation.progress
            s = 1 - p
            if p == 1.0:
                self.closeAnimation.reset()
        elif self.openAnimation.updateProgress():
            p = self.openAnimation.progress
            s = p
            if p == 1.0:
                self.openAnimation.reset()
        if s is None:
            return False
        canopy = self.canopy
        canopy.resetMatrix()
        canopy.scale(s)
        s = max(0.1, s)
        for i, r in enumerate(self.ribs):
            r.resetMatrix()
            self.rotateRib(r, i)
            r.scale(s, 1.0)

class UmbrellaTest(SubSketch):

    def setup(self):
        noStroke()
        self.subject = Umbrella()
        self.subject.setColor(0, 0.4, 1)

    def draw(self):
        background(0.87)
        if mousePressed:
            if not self.subject.close():
                self.subject.open()
        self.subject.updateAnimations()
        shape(self.subject.shape)
