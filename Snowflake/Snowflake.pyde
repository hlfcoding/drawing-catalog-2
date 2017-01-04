from animation import *
from layout import *

presentationMode = True

w = 300
h = 300
s = None
sTaper = 0.2

a = Animator()
a.addSequence('show',
              [Animation(id='base', duration=0.3),
               Animation(id='branch', duration=0.3),
               Animation(id='subBranch', duration=0.3)])
a.isEnabled = presentationMode

def setup():
    size(w, h)
    colorMode(RGB, 1)

    global s
    s = createSegmentShape()

    global l
    l = BranchLayout(shape=s, taper=sTaper, coreRadius=8)

def draw():
    if presentationMode:
        background(0)

    translate(w / 2, h / 2)
    if presentationMode:
        rotatePerSecond(0.1)

    l.update(animator=a)
    drawBranches()

    a.updateSequence('show')

def createSegmentShape():
    h = 30
    w = 10

    s = createShape()
    s.beginShape()
    if presentationMode:
        s.fill(1, 0.8)
        s.stroke(1, 0.8)

    s.vertex(w * sTaper, 0)
    s.vertex(w * (1 - sTaper), 0)
    s.vertex(w, h)
    s.vertex(0, h)

    s.endShape(CLOSE)
    return s

def drawBranches(n=6):
    for i in range(0, n):
        drawBranch()
        pushMatrix()
        rotate(TWO_PI / n)
    for i in range(0, n):
        popMatrix()

def drawBranch():
    pushMatrix()

    translate(*l.base.translation)
    drawSegment(*l.base.scale)

    translate(*l.branch.translation)
    drawSegment(*l.branch.scale)

    drawSubBranches()

    popMatrix()

def drawSubBranches():
    pushMatrix()
    translate(*l.leftSubBranch.translation)
    rotate(l.leftSubBranch.rotation)
    drawSegment(*l.leftSubBranch.scale)
    popMatrix()

    pushMatrix()
    translate(*l.rightSubBranch.translation)
    rotate(l.rightSubBranch.rotation)
    drawSegment(*l.rightSubBranch.scale)
    popMatrix()

def drawSegment(scaleX, scaleY):
    pushMatrix()
    scale(scaleX, scaleY)
    shape(s)
    popMatrix()
