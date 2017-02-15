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

  def draw(self):
    pass

  def drawSketch(self):
    if self.isCentered:
      pushMatrix()
      translate(width / 2, height / 2)

    self.draw()

    if self.isCentered:
      popMatrix()
