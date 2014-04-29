from core_elements import *
from forces import *
from arrangements import *

el = None
swirl = None
shouldLoop = True
shouldExport = False

backgroundColor = color(225)
#childCount = 2
childCount = 3
thetaToColorScalar = 5
thetaToColorRange = 100
thetaVelocityScalar = 2


def setup():
    global el
    global swirl
    global thetaVelocityScalar
    margin = 0.15
    stageSize = 300
    elementSize = stageSize * (1 - margin * 2)
    size(stageSize, stageSize)
    colorMode(HSB)
    background(backgroundColor)
    if shouldExport:
        fps = 24
        frameRate(fps)
        thetaVelocityScalar *= 60 / fps
    el = ContainerElement(
        name='yinyangyon',
        size={'width': elementSize, 'height': elementSize}
    )
    swirl = SwirlingArrangement(el, createChildElements(childCount))
    for element in el.childElements:
        element.forces['swirl'].dampener *= thetaVelocityScalar


def draw():
    global el
    pushMatrix()
    translate(width / 2, height / 2)
    el.update()
    el.draw()
    popMatrix()
    if shouldExport:
        saveFrame('frames/frame-####.png')


def mousePressed():
    global shouldLoop
    shouldLoop = not shouldLoop
    if shouldLoop:
        loop()
    else:
        noLoop()


def createChildElements(count):
    global backgroundColor
    elements = []
    thetaToColorOffset = thetaToColorRange / count

    # Rainbow skin.
    def fillColor(element):
        hueValue = (element.forces['swirl'].theta(element)
                    * (thetaToColorScalar * count)
                    + element.skin['thetaToColorOffset']
                    ) % 255
        return color(hueValue, 200, 200)

    def drawOutline(element):
        arcAngularOffset = atan2(element.position.y, element.position.x)
        arcLengthFactor = 1.13 if count == 3 else 1
        noFill()
        element._strokeSize(element.skin['strokeSize'])
        stroke(backgroundColor)
        arc(
            element.position.x,
            element.position.y,
            element.width,
            element.height,
            0 + arcAngularOffset,
            arcLengthFactor * PI + arcAngularOffset
        )

    for i in range(count):
        # Plain skin.
        # if count == 2:
        #    fillColor = 0 if (i == 0) else 255
        element = Element(
            name='element {}'.format(i + 1),
            skin={
                'fill': fillColor,
                'stroke': None,
                'strokeSize': lambda element: element.width / 9,
                # Custom entries.
                'thetaToColorOffset': i * thetaToColorOffset
            }
        )
        if count > 2:
            element.decorators['before'].append(drawOutline)
        elements.append(element)
    return elements

