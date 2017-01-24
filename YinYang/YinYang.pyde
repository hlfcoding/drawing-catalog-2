from hlf.animation import rotatePerSecond

rainbowMode = True
shouldLoop = True
shouldExport = False

w = 300
h = 300
sh = None
d = 150
fps = 30.0

def setup():
    size(w, h)
    colorMode(HSB, 1)
    shapeMode(CENTER)

    if shouldExport:
        global fps
        fps = 24.0
        frameRate(fps)

    global sh
    sh = createTriangleShape()

    background(0.9)

def draw():
    translate(w / 2, h / 2)

    pushMatrix()
    rotatePerSecond(0.1, direction=-1, fps=fps)
    s = d / sh.width
    scale(s)
    n = 500.0
    i = 1.0
    dS = s / n
    dR = 1.3 * TWO_PI / n
    p = 25.0 # color-shift period
    while i < n:
        rotate(-(0.001 + dR * pow((n - i) / n, 1.5)))
        scale(1.0 - dS * pow(i / n, 0.5))
        i += 1.0

        pushMatrix()
        if rainbowMode:
            drawTriangleFan(colorOffset=0.1 + (i / n) / 4,
                            colorShift=(frameCount / fps) / p % 1)
        else:
            drawTriangleFan()
        popMatrix()
    popMatrix()

    drawCleanup()

    if shouldExport:
        saveFrame('frames/frame-####.png')

def createTriangleShape():
    w = 30.0
    h = w / 2 / tan(PI / 3)  # half is 30-60-90 triangle

    s = createShape()
    s.beginShape()
    s.disableStyle()

    s.vertex(0, -h)
    s.vertex(w, -h)
    s.vertex(w / 2, 0)

    s.endShape(CLOSE)
    return s

def drawCleanup():
    noFill()
    wt = 4
    w = h = d + 15 + 2 * wt
    stroke(0.7)
    strokeWeight(wt)
    ellipse(0, 0, w, h)
    
def drawTriangleFan(colorOffset=0, colorShift=0):
    dS = constrain(colorOffset, 0, 1)
    dH = constrain(colorShift, 0, 1)
    noStroke()
    fill((0 + dH) % 1, 1 - dS, 1)
    shape(sh)

    rotate(TWO_PI / 3)
    if colorOffset == 0:
        fill(0, 0, 1)
    else:
        fill((0.33 + dH) % 1, 1 - dS, 1)
    shape(sh)

    rotate(TWO_PI / 3)
    fill((0.66 + dH) % 1, 1 - dS, 1)
    shape(sh)

def mousePressed():
    global shouldLoop
    shouldLoop = not shouldLoop
    if shouldLoop:
        loop()
    else:
        noLoop()
