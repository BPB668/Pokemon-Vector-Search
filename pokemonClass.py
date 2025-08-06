import math

class Pokemon:

    def __init__(self, vector):
        self.vector = vector

    def dot(self, other):
        return sum(a * b for a, b in zip(self.vector, other.vector))/(self.mag * other.mag)
    
    def mag(self):
        return math.sqrt(sum(x**2 for x in self))