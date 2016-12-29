from animation import *

presentationMode = True

w = 300
h = 300
s = None
sW = 10
sH = 30
sTaper = 0.2
hR = 8  # hole radius

a = Animator()
a.addSequence('show',
              [Animation(id='base', duration=0.3),
               Animation(id='branch', duration=0.3),
               Animation(id='subBranch', duration=0.3)])

def setup():
    size(w, h)

    global s
    s = createSegmentShape()

def draw():
    if presentationMode:
        background(0)

    translate(w / 2, h / 2)
    if presentationMode:
        v = 10
        secs = float(millis()) / 1000
        rotate(radians(secs * v % 360))
    drawBranches()

    a.updateSequence('show')

def createSegmentShape():
    s = createShape()
    s.beginShape()
    s.fill(255)
    if presentationMode:
        s.noStroke()

    s.vertex(sW * sTaper, 0)
    s.vertex(sW * (1 - sTaper), 0)
    s.vertex(sW, sH)
    s.vertex(0, sH)

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
    y = drawBaseSegment()
    drawBranchSegment(y)
    drawSubBranches()
    popMatrix()

def drawBaseSegment():
    sY = 0.2 * a.getSequenceAnimation('show', 'base').progress
    h = sH * sY
    y = -(hR + h)
    translate(0, y)
    pushMatrix()
    scale(1.8, sY)
    shape(s)
    popMatrix()
    return y

def drawBranchSegment(y):
    sY = a.getSequenceAnimation('show', 'branch').progress
    h = sH * sY
    y = -(sH + 1) - y
    y += (sH - h) / 2
    translate(0, y)
    pushMatrix()
    scale(1, sY)
    shape(s)
    popMatrix()

def drawSubBranches():
    sX = 0.6
    sY = 0.5 * a.getSequenceAnimation('show', 'subBranch').progress
    t = PI / 3
    x = abs(sH * sY * sin(degrees(t)))  # sin(t) = x/sH
    x += sW / 2 * (1 - sTaper / 2)

    pushMatrix()
    translate(x, 0)
    rotate(t)
    drawSubBranchSegment(sX, sY)
    popMatrix()

    pushMatrix()
    translate(-x, 0)
    rotate(-t)
    drawSubBranchSegment(sX, sY)
    popMatrix()

def drawSubBranchSegment(scaleX, scaleY):
    pushMatrix()
    scale(scaleX, scaleY)
    shape(s)
    popMatrix()
