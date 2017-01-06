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

class Sequence(Animatable):

    def __init__(self, id, animations, delay=0, times=1):
        self.animations = animations
        speed = 1.0 / len(animations)
        Animatable.__init__(self, id, delay, speed, times)

    def updateProgress(self):
        if not Animatable.updateProgress(self):
            return False
        if not self.current.updateProgress():
            return False
        if self.current.progress < 1.0:
            return False
        if self.current is not self.animations[-1]:
            index = self.animations.index(self.current)
            self.current = self.animations[index + 1]
        Animatable._incrementProgress(self)

    def _resetProgress(self):
        Animatable._resetProgress(self)
        self.current = self.animations[0]
        for a in self.animations:
            a._resetProgress()

class Animator(object):

    def __init__(self):
        self.isEnabled = True
        self.sequences = {}

    def addSequence(self, sequence):
        self.sequences[sequence.id] = sequence

    def getSequenceAnimation(self, sid, aid=None):
        if aid is None:
            return self.sequences[sid].current
        return next(a for a in self.sequences[sid].animations if a.id == aid)

    def getSequenceAnimationProgress(self, sid, aid=None):
        if not self.isEnabled:
            return 1.0
        return self.getSequenceAnimation(sid, aid).progress

    def updateSequence(self, id):
        if not self.isEnabled:
            return
        self.sequences[id].updateProgress()

def rotatePerSecond(times):
    seconds = millis() / 1000.0
    rotate(radians(times * seconds * 360 % 360))
