class Animatable(object):

    fps = 60

    def __init__(self, id, delay, speed, times):
        self.id = id
        self.delay = delay
        self.speed = speed
        self.times = times
        self._resetProgress()

    def updateProgress(self):
        if self.progress == 1.0:
            if not self._repeat():
                return False
            self._resetProgress()
        if self._delay():
            return False
        return True

    def _delay(self):
        if self.delay == 0 or self.delayProgress == 0:
            return False
        if self.delayProgress is None:
            self.delayProgress = Animatable.fps * self.delay
        self.delayProgress -= 1
        return True

    def _incrementProgress(self):
        self.progress += self.speed
        self.progress = min(1.0, self.progress)

    def _repeat(self):
        self.times = max(0, self.times - 1)
        if self.times == 0:
            return False
        return True

    def _resetProgress(self):
        self.delayProgress = None
        self.progress = 0

class Animation(Animatable):

    def __init__(self, id, duration, delay=0, times=1):
        self.duration = duration
        speed = 1.0 / (Animatable.fps * duration)
        Animatable.__init__(self, id, delay, speed, times)

    def updateProgress(self):
        if not Animatable.updateProgress(self):
            return False
        Animatable._incrementProgress(self)
        return True

class Animator(object):

    def __init__(self):
        self.isEnabled = True
        self.sequences = {}

    def addSequence(self, id, animations):
        sequence = {}
        sequence['current'] = animations[0]
        sequence['animations'] = animations
        self.sequences[id] = sequence

    def getSequenceAnimationProgress(self, sid, aid=None):
        if not self.isEnabled:
            return 1.0
        if aid is None:
            aid = sid
        animation = next(a for a in self.sequences[sid]['animations'] if a.id == aid)
        return animation.progress

    def updateSequence(self, id):
        if not self.isEnabled:
            return
        sequence = self.sequences[id]
        animation = sequence['current']
        animations = sequence['animations']
        animation.updateProgress()
        if animation is animations[-1] or animation.progress < 1.0:
            return
        sequence['current'] = animations[animations.index(animation) + 1]

def rotatePerSecond(times):
    seconds = millis() / 1000.0
    rotate(radians(times * seconds * 360 % 360))
