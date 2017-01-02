class BranchLayout(object):
    
    def __init__(self, shape, coreRadius):
        self.shape = shape
        self.coreRadius = coreRadius
        self.base = SegmentTransform()
        self.branch = SegmentTransform()
        self.subBranch = SegmentTransform()

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

class SegmentTransform(object):
    
    def __init__(self):
        self.rotation = 0
        self.scale = (1, 1)
        self.translation = (0, 0)
