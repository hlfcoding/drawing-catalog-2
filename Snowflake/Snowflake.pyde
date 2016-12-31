from animation import *

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

    global s
    s = createSegmentShape()

def draw():
    if presentationMode:
        background(0)

    translate(w / 2, h / 2)
    if presentationMode:
        rotatePerSecond(0.1)

    drawBranches()

    a.updateSequence('show')

def createSegmentShape():
    h = 30
    w = 10

    s = createShape()
    s.beginShape()
    s.fill(255)
    if presentationMode:
        s.noStroke()

    s.vertex(w * sTaper, 0)
    s.vertex(w * (1 - sTaper), 0)
    s.vertex(w, h)
    s.vertex(0, h)

    s.endShape(CLOSE)
    return s

def drawBranches(n=6):
    shapeMode(CENTER)
    for i in range(0, n):
        drawBranch()
        pushMatrix()
        rotate(TWO_PI / n)
    for i in range(0, n):
        popMatrix()

def drawBranch():
    pushMatrix()
    drawBranchSegment(drawBaseSegment())
    drawSubBranches()
    popMatrix()

def drawBaseSegment():
    coreRadius = 8
    sX = 1.8
    sY = 0.2 * a.getSequenceAnimationProgress('show', 'base')
    h = s.height * sY
    y = -(coreRadius + h)
    translate(0, y)
    drawSegment(sX, sY)
    return y

def drawBranchSegment(y):
    sY = a.getSequenceAnimationProgress('show', 'branch')
    h = s.height * sY
    y = -(s.height + 1) - y
    y += (s.height - h) / 2
    translate(0, y)
    drawSegment(1, sY)

def drawSubBranches():
    sX = 0.6
    sY = 0.5 * a.getSequenceAnimationProgress('show', 'subBranch')
    t = PI / 3
    x = abs(s.height * sY * sin(degrees(t)))  # sin(t) = x/s.height
    x += s.width / 2 * (1 - sTaper / 2)

    pushMatrix()
    translate(x, 0)
    rotate(t)
    drawSegment(sX, sY)
    popMatrix()

    pushMatrix()
    translate(-x, 0)
    rotate(-t)
    drawSegment(sX, sY)
    popMatrix()

def drawSegment(scaleX, scaleY):
    pushMatrix()
    scale(scaleX, scaleY)
    shape(s)
    popMatrix()
