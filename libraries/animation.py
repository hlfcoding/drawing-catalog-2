class Animation(object):

    def __init__(self, id, duration):
        self.id = id
        self.duration = duration
        self.progress = 0
        self.speed = 1.0 / (60 * duration)

    def updateProgress(self):
        if self.progress >= 1:
            return
        self.progress += self.speed
        self.progress = min(1, self.progress)

class Animator(object):

    def __init__(self):
        self.sequences = {}
        self.currentAnimation = None

    def addSequence(self, id, animations):
        sequence = {}
        sequence['current'] = animations[0]
        sequence['animations'] = animations
        self.sequences[id] = sequence

    def getSequenceAnimation(self, sid, aid):
        return next(a for a in self.sequences[sid]['animations'] if a.id == aid)

    def updateSequence(self, id):
        sequence = self.sequences[id]
        animation = sequence['current']
        animations = sequence['animations']
        animation.updateProgress()
        if animation is animations[-1] or animation.progress < 1:
            return
        sequence['current'] = animations[animations.index(animation) + 1]
