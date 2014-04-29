class Element(object):

    def __init__(self,
                 name='unknown',
                 position={'x': 0, 'y': 0},
                 size={'width': 100, 'height': 100},
                 skin={'fill': None, 'stroke': None}):
        self.name = name
        self.position = PVector(position['x'], position['y'])
        self.width = size['width']
        self.height = size['height']
        self.skin = skin
        self.forces = []

    def draw(self):
        fillColor = self.skin['fill']
        if fillColor is None:
            noFill()
        else:
            if callable(fillColor):
                fillColor = fillColor()
            fill(fillColor)
        strokeColor = self.skin['stroke']
        if self.skin['stroke'] is None:
            noStroke()
        else:
            if callable(strokeColor):
                strokeColor = strokeColor()
            stroke(strokeColor)
        ellipseMode(CENTER)
        ellipse(
            self.position.x,
            self.position.y,
            self.width,
            self.height
        )

    @property
    def tick(self):
        return frameCount

    def update(self):
        for force in self.forces:
            force.apply(self)

    def log(self, value, label=None):
        output = 'element \'{0}\': {1} {2}'.format(
            self.name,
            value,
            '({})'.format(label) if label is not None else ''
        )
        println(output)


class ContainerElement(Element):

    def __init__(self, *args, **kwargs):
        super(ContainerElement, self).__init__(*args, **kwargs)
        self.children = []

    def draw(self, *args, **kwargs):
        super(ContainerElement, self).draw(*args, **kwargs)
        for element in self.children:
            element.draw()

    def update(self, *args, **kwargs):
        super(ContainerElement, self).update(*args, **kwargs)
        for element in self.children:
            element.update()

