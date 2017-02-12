from umbrella import *

class Person(object):

    def __init__(self):
        self.umbrella = Umbrella()

    def draw(self):
        shape(self.umbrella.shape)
