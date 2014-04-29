class Element(object):

    def __init__(self,
                 name='unknown',
                 position={'x': 0, 'y': 0},
                 size={'width': 100, 'height': 100},
                 skin={'fill': None, 'stroke': None, 'strokeSize': 1}):
        self.name = name
        self.position = PVector(position['x'], position['y'])
        self.width = size['width']
        self.height = size['height']
        self.skin = skin
        self.forces = {}
        self.decorators = {
            'before': [],
            'after': []
        }

    def draw(self):
        for decorate in self.decorators['before']:
            if callable(decorate):
                decorate(self)
        if self.skin['fill'] is None:
            noFill()
        else:
            self._fill(self.skin['fill'])
        if self.skin['stroke'] is None:
            noStroke()
        else:
            self._stroke(self.skin['stroke'])
            self._strokeSize(self.skin['strokeSize'])
        ellipseMode(CENTER)
        ellipse(
            self.position.x,
            self.position.y,
            self.width,
            self.height
        )
        for decorate in self.decorators['after']:
            if callable(decorate):
                decorate(self)

    @property
    def radius(self):
        if self.width != self.height:
            raise Exception(
                'Immeasurable element radius. Width and height not the same.'
            )
        return self.width / 2

    @radius.setter
    def radius(self, value):
        self.width = self.height = value

    @property
    def tick(self):
        return frameCount

    def update(self):
        for name, force in self.forces.iteritems():
            force.apply(self)

    def log(self, value, label=None):
        output = 'element \'{0}\': {1} {2}'.format(
            self.name,
            value,
            '({})'.format(label) if label is not None else ''
        )
        println(output)

    def _fill(self, fillColor):
        if callable(fillColor):
            fillColor = fillColor(self)
        fill(fillColor)
        return fillColor

    def _stroke(self, strokeColor):
        if callable(strokeColor):
            strokeColor = strokeColor(self)
        stroke(strokeColor)
        return strokeColor

    def _strokeSize(self, strokeSize):
        if callable(strokeSize):
            strokeSize = strokeSize(self)
        strokeWeight(strokeSize)
        return strokeSize

class ContainerElement(Element):

    def __init__(self, *args, **kwargs):
        super(ContainerElement, self).__init__(*args, **kwargs)
        self.childElements = []

    def draw(self, *args, **kwargs):
        super(ContainerElement, self).draw(*args, **kwargs)
        for element in self.childElements:
            element.draw()

    def update(self, *args, **kwargs):
        super(ContainerElement, self).update(*args, **kwargs)
        for element in self.childElements:
            element.update()

