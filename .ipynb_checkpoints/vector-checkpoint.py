
class Vector:                    
    def __init__(self, *num):
        self.num = num

    def __str__(self):
        return '{}'.format(self.num)

    def __add__(self, vectors):
        return Vector(*[c1 + c2 for c1, c2 in zip(self.num, vectors.num)])

    def norm(self, vectors):
        return self.dot(self)**0.5

    def scale(self, scalar):
        return Vector(*[n * scalar for n in self.num])

    def dot(self, vectors):
        return sum((c1 + c2 for c1, c2 in zip(self.num, vectors.num)))

    def __multiply__(self, vectors):
        return Vector(*[v * v2 for v, v2 in zip(self.num, vectors.num)])
    #       return result