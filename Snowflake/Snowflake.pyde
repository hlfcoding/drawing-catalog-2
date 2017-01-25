from hlf.animation import Animation, Animator, Sequence, rotatePerSecond
from hlf.core import Exporting 

from fx import Effects
from layout import BranchLayout

# qz.com/581000

presentationMode = True

w = 300
h = 300
b = 6

a = Animator()
a.addSequence(Sequence(id='show',
                       animations=[Animation(id='base', duration=0.3),
                                   Animation(id='branch', duration=0.3),
                                   Animation(id='subBranch', duration=0.3)]))
a.addSequence(Sequence(id='shimmer',
                       animations=[Animation(id='begin', duration=0.5, delay=3),
                                   Animation(id='end', duration=0.5, delay=1)],
                       times=sys.maxint))
a.isEnabled = presentationMode

e = Exporting()
e.isEnabled = True

fx = Effects(animator=a)
l = BranchLayout(animator=a)

def setup():
    size(w, h)
    colorMode(RGB, 1)
    shapeMode(CENTER)
    e.setup()

    l.useShape(createSegmentShape())

def draw():
    if presentationMode:
        background(0)

    translate(w / 2, h / 2)
    if presentationMode:
        rotatePerSecond(0.1)

    l.update()
    drawBranches()

    a.updateSequence('shimmer')
    a.updateSequence('show')

    e.update()

def createSegmentShape():
    h = 35
    w = 10

    s = createShape()
    s.beginShape()
    s.disableStyle()

    s.vertex(w * l.taper, 0)
    s.vertex(w * (1 - l.taper), 0)
    s.vertex(w, h)
    s.vertex(0, h)

    s.endShape(CLOSE)
    return s

def drawBranches():
    if presentationMode:
        fx.updateShimmer()

    for i in range(0, b):
        drawBranch()
        pushMatrix()
        rotate(TWO_PI / b)
    for i in range(0, b):
        popMatrix()

def drawBranch():
    pushMatrix()

    pushMatrix()
    rotate(-PI / b)
    translate(*l.base.translation)
    drawSegment(*l.base.scale, specAxis='x')
    popMatrix()

    translate(*l.base.translation)
    translate(*l.branch.translation)
    drawSegment(*l.branch.scale)

    drawSubBranches()

    popMatrix()

def drawSubBranches():
    for p in l.subBranchPairs:
        left, right = p

        pushMatrix()
        translate(*left.translation)
        rotate(left.rotation)
        drawSegment(*left.scale)
        popMatrix()
    
        pushMatrix()
        translate(*right.translation)
        rotate(right.rotation)
        drawSegment(*right.scale)
        popMatrix()

def drawSegment(scaleX, scaleY, specAxis='y'):
    fill(1, fx.baseAlpha)
    stroke(1, fx.baseAlpha / 2)
    pushMatrix()
    scale(scaleX, scaleY)
    shape(l.shape)
    popMatrix()

    fill(1, fx.specAlpha)
    noStroke()
    pushMatrix()
    if specAxis == 'y':
        scale(fx.specSize * scaleX, scaleY)
    elif specAxis == 'x':
        scale(scaleX, fx.specSize * scaleY)
    shape(l.shape)
    popMatrix()
