
shouldLoop = True
shouldExport = False

w = 300
h = 300

def setup():
    size(w, h)
    colorMode(RGB, 1)

    if shouldExport:
        frameRate(24)


    background(0.9)

def draw():
    translate(w / 2, h / 2)
    if shouldExport:
        saveFrame('frames/frame-####.png')

def mousePressed():
    global shouldLoop
    shouldLoop = not shouldLoop
    if shouldLoop:
        loop()
    else:
        noLoop()
