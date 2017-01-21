import weakref

class Effects(object):

    def __init__(self, animator):
        self.animator = weakref.ref(animator)
        self.shimmer = 0
        self.specSize = 0.3

    @property
    def baseAlpha(self):
        return 0.5 + 0.3 * self.shimmer

    @property
    def specAlpha(self):
        return 1 - self.baseAlpha

    def updateShimmer(self):
        animation = self.animator().getSequenceAnimation('shimmer')
        self.shimmer = 1
        if animation.id == 'begin':
            self.shimmer *= animation.progress
        elif animation.id == 'end':
            self.shimmer *= (1 - animation.progress)
