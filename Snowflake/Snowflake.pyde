w = 300
h = 300
s1 = None
s1W = 10
s1H = 30
s2 = None
s2W = 5
s2H = 10

def setup():
    size(w, h)
    
    global s1
    global s2
    s1 = createSegmentShape(s1W, s1H)
    s2 = createSegmentShape(s2W, s2H)

def draw():
    background(0)

    translate(w/2, h/2)
    pushMatrix()
    secs = float(millis()) / 1000
    rotate(radians(secs * 10 % 360))
    drawBranches()
    popMatrix()

def createSegmentShape(w, h):
    s = createShape()
    s.fill(255)
    s.noStroke()
    s.beginShape()
    s.vertex(0, 0)
    s.vertex(w, 0)
    s.vertex(w, h)
    s.vertex(0, h)
    s.endShape(CLOSE)
    return s

def drawBranches():
    shapeMode(CENTER)
    n = 6
    for i in range(0, n):
        pushMatrix()
        translate(0, -30)
        shape(s1)
        drawSubBranches()
        popMatrix()
        pushMatrix()
        rotate(TWO_PI/n)
    for i in range(0, n):
        popMatrix()

def drawSubBranches():
    pushMatrix()
    translate(s2H, 0)
    pushMatrix()
    rotate(PI/3)
    shape(s2)
    popMatrix()
    popMatrix()

    pushMatrix()
    translate(-s2H, 0)
    pushMatrix()
    rotate(-PI/3)
    shape(s2)
    popMatrix()
    popMatrix()
