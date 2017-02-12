from hlf.core import SubSketch
from umbrella import *

class Person(object):

    def __init__(self):
        self.umbrella = Umbrella()

    def draw(self):
        shape(self.umbrella.shape)

class PersonTest(SubSketch):

    def setup(self):
        self.subject = Person()
        self.subject.umbrella.setColor(0, 0.4, 1)

    def draw(self):
        self.subject.draw()
