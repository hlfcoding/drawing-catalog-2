presentationMode = True

w = 300
h = 300
s = None
sW = 10
sH = 30
sTaper = 0.2
hR = 8  # hole radius

aDuration = 0.3
aProgress = 0
aSpeed = 1.0 / (60 * aDuration)
aStage = 0

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

    updateAnimationProgress()

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
    sY = 0.2 * animationStageProgress(0)
    h = sH * sY
    y = -(hR + h)
    translate(0, y)
    pushMatrix()
    scale(1.8, sY)
    shape(s)
    popMatrix()
    return y

def drawBranchSegment(y):
    sY = animationStageProgress(1)
    h = sH * sY
    translate(0, -(sH + 1) - y + (sH - h) / 2)
    pushMatrix()
    scale(1, sY)
    shape(s)
    popMatrix()

def drawSubBranches():
    sX = 0.6
    sY = 0.5 * animationStageProgress(2)
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

def animationStageProgress(stage):
    if aStage == stage:
        return aProgress
    elif aStage > stage:
        return 1.0
    else:
        return 0

def updateAnimationProgress():
    global aProgress
    if aProgress >= 1:
        return
    aProgress += aSpeed
    aProgress = min(1, aProgress)
    updateAnimationStage()

def updateAnimationStage():
    global aProgress
    global aStage
    if aStage >= 3 or aProgress < 1:
        return
    aProgress = 0
    aStage += 1
