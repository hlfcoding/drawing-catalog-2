class BranchLayout(object):

    def __init__(self, shape, taper, coreRadius):
        self.shape = shape
        self.taper = taper
        self.coreRadius = coreRadius

        self.base = SegmentTransform()
        self.branch = SegmentTransform()
        self.leftSubBranch = SegmentTransform()
        self.rightSubBranch = SegmentTransform()

    def update(self, animator):
        shapeMode(CENTER)

        sY = 0.2 * animator.getSequenceAnimationProgress('show', 'base')
        self.base.scale = (1.8, sY)
        y = self.coreRadius + self.shape.height * sY
        self.base.translation = (0, -y)

        sY = animator.getSequenceAnimationProgress('show', 'branch')
        self.branch.scale = (1, sY)
        y = (self.shape.height + 1) - y
        y -= self.shape.height * (1 - sY) / 2
        self.branch.translation = (0, -y)

        sY = 0.5 * animator.getSequenceAnimationProgress('show', 'subBranch')
        self.leftSubBranch.scale = self.rightSubBranch.scale = (0.6, sY)
        t = PI / 3
        self.leftSubBranch.rotation = -t
        self.rightSubBranch.rotation = t
        x = abs(self.shape.height * sY * sin(degrees(t))) # sin(t) = x/s.height
        x += self.shape.width / 2 * (1 - self.taper / 2)
        self.leftSubBranch.translation = (-x, 0)
        self.rightSubBranch.translation = (x, 0)

class SegmentTransform(object):

    def __init__(self):
        self.rotation = 0
        self.scale = (1, 1)
        self.translation = (0, 0)
