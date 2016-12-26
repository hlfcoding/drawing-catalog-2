presentationMode = True

w = 300
h = 300
s0 = None
s0W = 20
s0H = 6
s1 = None
s1W = 10
s1H = 30
s2 = None
s2W = 5
s2H = 10

def setup():
    size(w, h)
    
    global s0
    global s1
    global s2
    s0 = createSegmentShape(s0W, s0H)
    s1 = createSegmentShape(s1W, s1H)
    s2 = createSegmentShape(s2W, s2H)

def draw():
    if presentationMode:
        background(0)

    translate(w/2, h/2)
    if presentationMode:
        v = 10
        secs = float(millis()) / 1000
        rotate(radians(secs * v % 360))
    drawBranches()

def createSegmentShape(w, h, taper=0.2):
    s = createShape()
    s.beginShape()
    s.fill(255)
    if presentationMode:
        s.noStroke()

    s.vertex(w * taper, 0)
    s.vertex(w * (1-taper), 0)
    s.vertex(w, h)
    s.vertex(0, h)
    
    s.endShape(CLOSE)
    return s

def drawBranches(n=6):
    shapeMode(CENTER)
    for i in range(0, n):
        pushMatrix()
        translate(0, -13)
        shape(s0)
        translate(0, -17)
        shape(s1)
        drawSubBranches()
        popMatrix()
        pushMatrix()
        rotate(TWO_PI/n)
    for i in range(0, n):
        popMatrix()

def drawSubBranches():
    t = PI/3
    x = abs(s2H * sin(degrees(t))) # sin(t) = x/s2H
    x += s1W/2 * 0.9 # taper
    pushMatrix()
    translate(x, 0)
    pushMatrix()
    rotate(PI/3)
    shape(s2)
    popMatrix()
    popMatrix()

    pushMatrix()
    translate(-x, 0)
    pushMatrix()
    rotate(-PI/3)
    shape(s2)
    popMatrix()
    popMatrix()
