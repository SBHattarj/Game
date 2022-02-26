import numpy as np
from numpy import dtype
from numpy.typing import _SupportsArray, _NestedSequence
from typing import Iterable, Any

class Vector(np.ndarray):
    def __new__(cls, items: Iterable):
        obj = np.asarray(items).view(cls)
        return obj

    def clone(self):
        return type(self)(self)

    @property
    def sqr_length(self):
        return np.sum(np.square(self))

    
    
    def cross(self, other: _SupportsArray[dtype[Any]] | _NestedSequence[_SupportsArray[dtype[Any]]] | Any | _NestedSequence[Any]):
        return np.cross(self, other)

    def normalize(self):
        l2 = np.atleast_1d(np.linalg.norm(self))
        if l2 == 0:
            newVector = self.clone()
            newVector[1] = 1
            return newVector
        if l2 == 1: return self.clone()
        l2[l2==0] = 1
        normalized = self / l2

        return normalized if normalized.length == 1.0 else normalized.normalize()

    def set_length(self, length: float | Iterable[float] | np.ndarray | 'Vector'):
        return self.normalize() * length
    
    @property
    def length(self):
        return np.linalg.norm(self)

    @length.setter 
    def length(self, length: float | Iterable[float] | np.ndarray | 'Vector'):
        new_self = self.set_length(length)
        self.dtype = new_self.dtype
        self[:] = new_self

    def project(self, other: Iterable[float] | np.ndarray | 'Vector'):
        return self * self.dot(Vector(other)) / self.dot(self)
    
class Vector2D(Vector):
    def __new__(cls, x: float, y: float):
        return super().__new__(cls, [x, y])
    
    def clone(self):
        return type(self)(self.x, self.y)

    @property
    def x(self):
        return self[0]

    @x.setter
    def x(self, value: float):
        self[0] = value

    @property
    def y(self):
        return self[1]

    @y.setter
    def y(self, value: float):
        self[1] = value

class Vector3D(Vector):
    def __new__(cls, x: float, y: float, z: float):
        return super().__new__(cls, [x, y, z])

    x = Vector2D.x

    y = Vector2D.y

    @property
    def z(self):
        return self[2]
    
    @z.setter
    def z(self, value: float):
        return self[2]


v = Vector([1, 2, 3])
v.length = 6
print(v)