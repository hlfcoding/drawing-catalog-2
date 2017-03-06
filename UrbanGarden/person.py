from hlf.core import SubSketch
from umbrella import *

# s-media-cache-ak0.pinimg.com/564x/c6/a1/96/c6a1969a6895bd4c67301338c94dc428.jpg

class Person(object):

    blackHair = (0.05, 0.1, 0.3)
    whiteShirt = (0.2, 0.05, 1)

    def __init__(self):
        self.umbrella = Umbrella()
        self.shape = self.createShape()

    @property
    def head(self):
        return self.shape.getChild('head')

    @property
    def body(self):
        return self.shape.getChild('body')

    def setColors(self, head=blackHair, body=whiteShirt):
        self.head.setFill(color(*head))
        self.body.setFill(color(*body))

    def createShape(self):
        s = createShape(GROUP)

        h = 10
        w = 18
        body = createShape()
        body.beginShape()
        body.vertex(-w/2, -h/2)
        body.vertex(w/2, -h/2)
        body.vertex(w/2, h/2)
        body.vertex(-w/2, h/2)
        body.endShape(CLOSE)
        s.addChild(body)
        s.addName('body', body)

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
