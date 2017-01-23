import weakref

class BranchLayout(object):

    def __init__(self, animator, taper=0.2, coreRadius=8, subBranchCount=2):
        self.animator = weakref.ref(animator)
        self.taper = taper
        self.coreRadius = coreRadius

        self.base = SegmentTransform()
        self.branch = SegmentTransform()
        self.subBranchPairs = []
        for i in range(0, subBranchCount):
            self.subBranchPairs.append((SegmentTransform(), SegmentTransform()))

    def update(self):
        shapeMode(CENTER)
        a = self.animator()
        if a.sequences['show'].progress == 1:
            return

        h = self.shape.height
        w = self.shape.width

        sY = 0.3 * a.getSequenceAnimationProgress('show', 'base')
        self.base.scale = (3, -sY)
        y = -h * sY * 2
        self.base.translation = (0, y)

        sY = a.getSequenceAnimationProgress('show', 'branch')
        self.branch.scale = (1, sY)
        y -= 3 - (-h * (sY - 1) / 2)
        self.branch.translation = (0, y)

        spaces = len(self.subBranchPairs) + 1
        spacing = 1.0 / spaces
        for i, p in enumerate(self.subBranchPairs):
            i += 1
            left, right = p
            sX = sqrt(i * spacing) * 0.9 
            sY = (i * spacing) * a.getSequenceAnimationProgress('show', 'subBranch')
            left.scale = right.scale = (sX, sY)
            t = PI / 3
            left.rotation = -t
            right.rotation = t
            x = abs((h * sY) * sin(degrees(t))) # sin(t) = x/s.height
            x += (w / 2) * (1 - ((spaces - i - 1) * self.taper))
            y = (-h / 2) + ((i * spacing) * h) 
            left.translation = (-x, y)
            right.translation = (x, y)

    def useShape(self, shape):
        self.shape = shape

class SegmentTransform(object):

    def __init__(self):
        self.rotation = 0
        self.scale = (1, 1)
        self.translation = (0, 0)
