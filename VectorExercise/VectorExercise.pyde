from hlf.element import Element, Size, Skin

w = 100
h = 100

d = 0.1  # damping
m = 5  # max velocity

el = Element('ball', position=PVector(w / 2, h / 2))

attractTo = el.position.copy()
def attraction():
    f = PVector.sub(attractTo, el.position)
    f.normalize()
    f.mult(0.01)
    return f

el.forces.append(attraction)
el.forces.append(PVector(0, 0.1))  # gravity
el.forces.append(PVector(0.005, 0))  # wind

def setup():
    size(w, h)
    colorMode(RGB, 1)
    shapeMode(CENTER)

    el.skin.fill = color(1)

def draw():
    background(0)

    el.updateVelocity()
    el.velocity.limit(m)
    wrap()
    el.updatePosition()
    el.draw()

    stroke(1)
    line(el.position.x, el.position.y, attractTo.x, attractTo.y)

def mousePressed():
    hit = PVector.dist(
        PVector(mouseX, mouseY), el.position) < el.size.radius * 5
    if hit:
        el.velocity.add(0, 10, 0)

def mouseMoved():
    global attractTo
    attractTo.set(mouseX, mouseY)

def wrap():
    p = el.position
    v = el.velocity
    s = el.size.radius

    setY = True
    if p.y > h - s and v.y > 0:
        v.y = v.y * -(1 - d) + 0.1
    elif p.y < s and v.y < 0:
        v.y = v.y * -(1 - d) - 0.1
    else:
        setY = False
    if setY and abs(v.y) < 0.1:
        v.y = 0

    setX = True
    if p.x > w - s and v.x > 0:
        v.x *= -(1 - d)
        v.x += 0.1
    elif p.x < s and v.x < 0:
        v.x *= -(1 - d)
        v.x -= 0.1
    else:
        setX = False
    if setX and abs(v.x) < 0.1:
        v.x = 0
