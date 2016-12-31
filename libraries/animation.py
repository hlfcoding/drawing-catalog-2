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
        self.currentAnimation = None
        self.isEnabled = True 
        self.sequences = {}

    def addSequence(self, id, animations):
        sequence = {}
        sequence['current'] = animations[0]
        sequence['animations'] = animations
        self.sequences[id] = sequence

    def getSequenceAnimationProgress(self, sid, aid):
        if not self.isEnabled:
            return 1.0
        animation = next(a for a in self.sequences[sid]['animations'] if a.id == aid)
        return animation.progress

    def updateSequence(self, id):
        if not self.isEnabled:
            return
        sequence = self.sequences[id]
        animation = sequence['current']
        animations = sequence['animations']
        animation.updateProgress()
        if animation is animations[-1] or animation.progress < 1:
            return
        sequence['current'] = animations[animations.index(animation) + 1]

def rotatePerSecond(times):
    seconds = millis() / 1000.0
    rotate(radians(times * seconds * 360 % 360))
