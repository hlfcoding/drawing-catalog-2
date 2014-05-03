p = None  # Position
v = None  # Velocity
a = None  # Acceleration
g = None  # Gravity

aP = None  # Attractor Position

d = 0.1   # Damping
s = 5     # Size
m = 5     # Max Velocity


def setup():
    size(100, 100)

    global p, v, a, g, d, aP
    p = PVector(width / 2, height / 2)
    v = PVector()
    a = PVector(0.005, 0)
    g = PVector(0, 0.1)

    aP = PVector(p.x, p.y)


def draw():
    global p, v, a, g, d, aP

    aA = PVector.sub(aP, p)
    aA.normalize()
    aA.mult(0.01)
    v.add(aA)
    v.add(a)
    v.add(g)
    v.limit(m)

    setY = True
    if p.y > height - s and v.y > 0:
        v.y = v.y * -(1 - d) + 0.1
    elif p.y < s and v.y < 0:
        v.y = v.y * -(1 - d) - 0.1
    else:
        setY = False
    if setY and abs(v.y) < 0.1:
        v.y = 0
    setX = True
    if p.x > width - s and v.x > 0:
        v.x *= -(1 - d)
        v.x += 0.1
    elif p.x < s and v.x < 0:
        v.x *= -(1 - d)
        v.x -= 0.1
    else:
        setX = False
    if setX and abs(v.x) < 0.1:
        v.x = 0

    p.add(v)

    background(0)
    fill(255)
    noStroke()
    ellipse(p.x, p.y, s * 2, s * 2)
    stroke(255)
    line(p.x, p.y, aP.x, aP.y)

def mousePressed():
    global p, s, v
    hit = PVector.dist(PVector(mouseX, mouseY), p) < s * 5
    if hit:
        v.add(0, 10, 0)


def mouseMoved():
    global aP
    aP.set(mouseX, mouseY)

