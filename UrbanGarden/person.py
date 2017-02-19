from hlf.core import SubSketch
from umbrella import *

class Person(object):

    def __init__(self):
        self.umbrella = Umbrella()

    def draw(self):
        self.umbrella.draw()

class PersonTest(SubSketch):

    def setup(self):
        noStroke()
        self.subject = Person()
        self.subject.umbrella.setColor(h=0, s=0.4, b=1)
        self.subject.umbrella.close(animated=False)

    def draw(self):
        self.subject.draw()
