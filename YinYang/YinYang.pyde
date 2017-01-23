from hlf.animation import rotatePerSecond

shouldLoop = True
shouldExport = False

w = 300
h = 300
sh = None

def setup():
    size(w, h)
    colorMode(RGB, 1)
    noStroke()
    shapeMode(CENTER)

    if shouldExport:
        frameRate(24)

    global sh
    sh = createTriangleShape()

    background(0.9)

def draw():
    translate(w / 2, h / 2)
    rotatePerSecond(0.1, direction=-1)

    n = 500.0
    i = 1.0
    s = 5.0
    dS = s / n
    dR = 1.3 * TWO_PI / n
    scale(s)
    while i < n:
        rotate(-(0.001 + dR * pow((n - i) / n, 1.5)))
        scale(1.0 - dS * pow(i / n, 0.5))
        i += 1.0

        pushMatrix()
        drawTriangleFan()
        popMatrix()

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

def drawTriangleFan():
    fill(1, 0, 0)
    shape(sh)

    rotate(TWO_PI / 3)
    fill(0, 0, 1)
    shape(sh)

    rotate(TWO_PI / 3)
    fill(1)
    shape(sh)

def mousePressed():
    global shouldLoop
    shouldLoop = not shouldLoop
    if shouldLoop:
        loop()
    else:
        noLoop()
