from forces import SwirlingForce

class SwirlingArrangement(object):

    def __init__(self, containerElement, childElements):
        self.containerElement = containerElement
        self.childElements = childElements
        self.initContainerElement()
        self.initChildElements()

    def initContainerElement(self):
        self.containerElement.childElements.extend(self.childElements)

    def initChildElements(self):
        childCount = len(self.childElements)
        forceRadius = self.containerElement.radius / 2
        if childCount == 2:
            elementRadius = self.containerElement.radius
        elif childCount == 3:
            elementRadius = 0.822 * self.containerElement.radius # Temp. 
        forceOffset = TWO_PI / childCount
        for i, element in enumerate(self.childElements):
            element.radius = elementRadius
            element.forces['swirl'] = SwirlingForce(
                offset=forceOffset * i,
                radius=forceRadius
            )

    def log(self, value, label=None):
        output = 'swirling arrangement: {0} {1}'.format(
            value,
            '({})'.format(label) if label is not None else ''
        )
        println(output)
