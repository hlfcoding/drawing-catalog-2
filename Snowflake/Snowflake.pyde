presentationMode = True

w = 300
h = 300
s = None
sW = 10
sH = 30
sTaper = 0.2

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
        pushMatrix()
        translate(0, -14)
        drawBaseSegment()
        translate(0, -17)
        drawBranchSegment()
        drawSubBranches()
        popMatrix()
        pushMatrix()
        rotate(TWO_PI / n)
    for i in range(0, n):
        popMatrix()

def drawBaseSegment():
    pushMatrix()
    scale(1.8, 0.2)
    shape(s)
    popMatrix()

def drawBranchSegment():
    shape(s)

def drawSubBranches():
    sX = 0.6
    sY = 0.5
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
