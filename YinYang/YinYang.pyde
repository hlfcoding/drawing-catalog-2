from hlf.core_elements import *

from arrangements import *

shouldLoop = True
shouldExport = False

#childCount = 2
childCount = 3
thetaToColorScalar = 5
thetaToColorRange = 100
thetaVelocityScalar = 2

w = 300
h = 300

el = None
swirl = None

backgroundColor = color(225)

def setup():
    size(w, h)
    colorMode(HSB)

    margin = 0.15
    elementSize = w * (1 - margin * 2)
    if shouldExport:
        fps = 24
        frameRate(fps)
        global thetaVelocityScalar
        thetaVelocityScalar *= 60 / fps

    global el
    el = ContainerElement(
        name='yinyangyon',
        size={'width': elementSize, 'height': elementSize}
    )

    global swirl
    swirl = SwirlingArrangement(el, createChildElements(childCount))

    for element in el.childElements:
        element.forces['swirl'].dampener *= thetaVelocityScalar

    background(backgroundColor)

def draw():
    pushMatrix()
    translate(w / 2, h / 2)
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
