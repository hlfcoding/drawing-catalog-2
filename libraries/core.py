class Sketch(object):
  """
  A structured approach to sharing global configuration (sorely missing from
  the Processing API) as well as provide additional helpers.
  """
  def __init__(self):
    self.colorScale = 1.0

  def invert(self, colorValue):
    pivot = self.colorScale / 2
    return pivot + (pivot - colorValue)

sketch = Sketch()

class Exporting(object):

  def __init__(self, fps=24.0):
    self.fps = fps
    self.isEnabled = False

  def setup(self):
    if self.isEnabled:
      frameRate(self.fps)

  def update(self):
    if self.isEnabled:
      saveFrame('frames/frame-####.png')

class SubSketch(object):

  active = None

  def __init__(self):
    self.isCentered = True

  def activate(self):
    SubSketch.active = self

  def setup(self):
    pass

  def setupSketch(self):
    self.bg = 0.87

    self.setup()

  def draw(self):
    pass

  def drawSketch(self):
    background(self.bg)
    if self.isCentered:
      pushMatrix()
      translate(width / 2, height / 2)

    self.draw()

    if self.isCentered:
      popMatrix()
