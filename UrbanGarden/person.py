from hlf.core import SubSketch
from umbrella import *

class Person(object):

    blackHair = (0.05, 0.1, 0.3)

    def __init__(self):
        self.umbrella = Umbrella()
        self.shape = self.createShape()

    @property
    def head(self):
        return self.shape.getChild('head')

    def setColors(self, head=blackHair):
        self.head.setFill(color(*head))

    def createShape(self):
        s = createShape(GROUP)

        head = createShape(ELLIPSE, 0, 0, 7, 9)
        s.addChild(head)
        s.addName('head', head)

        return s

    def draw(self):
        shape(self.shape)
        self.umbrella.draw()

class PersonTest(SubSketch):

    def setup(self):
        noStroke()
        self.subject = Person()
        self.subject.setColors()
        self.subject.umbrella.setColor(h=0, s=0.4, b=1)
        self.subject.umbrella.close(animated=False)

    def draw(self):
        self.subject.draw()
