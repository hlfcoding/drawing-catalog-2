import weakref

class Effects():

    def __init__(self, animator):
        self.animator = weakref.ref(animator)

    def updateShimmer(self):
        animation = self.animator().getSequenceAnimation('shimmer')
        base = 0.8
        shimmer = 1 - base
        if animation.id == 'begin':
            shimmer *= animation.progress
        elif animation.id == 'end':
            shimmer *= (1 - animation.progress)
        fill(1, base + shimmer)
        stroke(1, base + shimmer)
