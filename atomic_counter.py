########################################################################
class AtomicCounter(object):
    #----------------------------------------------------------------------
    def __init__(self, initval=0):
        self.val = RawValue('i', initval)
        self.lock = Lock()

    #----------------------------------------------------------------------
    def increment(self):
        with self.lock:
            self.val.value += 1
            return self.val.value

    #----------------------------------------------------------------------
    def value(self):
        with self.lock:
            return self.val.value

    def __eq__(self, other):
        with self.lock, other.lock:
            return self.value() == other.value()
    def __ne__(self, other):
        with self.lock, other.lock:
            return not self.value() == other.value()
    def __gt__(self, other):
        with self.lock, other.lock:
            return self.value() > other.value()
    def __lt__(self, other):
        with self.lock, other.lock:
            return self.value() < other.value()
    def __ge__(self, other):
        with self.lock, other.lock:
            return (self > other) or (self == other)
    def __le__(self, other):
        with self.lock, other.lock:
            return (self < other) or (self == other)
