import weakref

class BranchLayout(object):

    def __init__(self, animator, taper=0.2, coreRadius=8):
        self.animator = weakref.ref(animator)
        self.taper = taper
        self.coreRadius = coreRadius

        self.base = SegmentTransform()
        self.branch = SegmentTransform()
        self.leftSubBranch = SegmentTransform()
        self.rightSubBranch = SegmentTransform()

    def update(self):
        shapeMode(CENTER)
        h = self.shape.height
        w = self.shape.width

        sY = 0.3 * self.animator().getSequenceAnimationProgress('show', 'base')
        self.base.scale = (3, -sY)
        y = -h * sY * 2
        self.base.translation = (0, y)

        sY = self.animator().getSequenceAnimationProgress('show', 'branch')
        self.branch.scale = (1, sY)
        y -= 3 - (-h * (sY - 1) / 2)
        self.branch.translation = (0, y)

        sY = 0.5 * self.animator().getSequenceAnimationProgress('show', 'subBranch')
        self.leftSubBranch.scale = self.rightSubBranch.scale = (0.6, sY)
        t = PI / 3
        self.leftSubBranch.rotation = -t
        self.rightSubBranch.rotation = t
        x = abs(h * sY * sin(degrees(t))) # sin(t) = x/s.height
        x += w / 2 * (1 - self.taper / 2)
        self.leftSubBranch.translation = (-x, 0)
        self.rightSubBranch.translation = (x, 0)

    def useShape(self, shape):
        self.shape = shape

class SegmentTransform(object):

    def __init__(self):
        self.rotation = 0
        self.scale = (1, 1)
        self.translation = (0, 0)
