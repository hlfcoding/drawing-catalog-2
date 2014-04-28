from elements import *
from forces import *

el = None


def setup():
    size(300, 300, P2D)
    colorMode(HSB)
    global el
    el = ContainerElement(
        name='yinyang',
        size={'width': 200, 'height': 200}
    )
    yin = Element(
        name='yin',
        position={'x': 0, 'y': -50},
        # Rainbow skin.
        skin={
            'fill': lambda: color((yinForce.theta(yin) * 30) % 255, 200, 200),
            'stroke': None
        }
        # Plain skin.
        #skin={'fill': 0, 'stroke': None}
    )
    yinForce = SwirlingForce(
        radius=50
    )
    yin.forces.append(yinForce)
    yang = Element(
        name='yang',
        position={'x': 0, 'y': 50},
        # Rainbow skin.
        skin={
            'fill': lambda: color((yangForce.theta(yang) * 30) % 255, 200, 200),
            'stroke': None
        }
        # Plain skin.
        #skin={'fill': 255, 'stroke': None}
    )
    yangForce = SwirlingForce(
        offset=PI,
        radius=50
    )
    yang.forces.append(yangForce)
    el.children.extend([yin, yang])


def draw():
    global el
    pushMatrix()
    translate(width / 2, height / 2)
    el.update()
    el.draw()
    popMatrix()

