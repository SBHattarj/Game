import numpy as np
from numpy import dtype
from numpy.typing import _SupportsArray, _NestedSequence
from typing import Iterable, Any
import math

class Vector(np.ndarray):
    def __new__(cls, items: Iterable):
        obj = np.asarray(items).view(cls)
        return obj

    def clone(self):
        return type(self)(self)

    @property
    def sqr_length(self):
        return np.sum(np.square(self))

    def cross(
        self, 
        other: 
            _SupportsArray[dtype[Any]] 
            | _NestedSequence[_SupportsArray[dtype[Any]]] 
            | Any 
            | _NestedSequence[Any]
    ):
        return np.cross(self, other)

    def normalize(self):
        l2 = np.atleast_1d(np.linalg.norm(self))
        if l2 == 0:
            newVector = self.clone()
            newVector[0] = 1
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
        Other = type(self)(other)
        return Other * self.dot(Other) / Other.dot(Other)
    
    
    
class Vector2D(Vector):

    Degree = True

    def __new__(cls, x: float, y: float):
        return super().__new__(cls, [x, y])

    @classmethod
    def from_angle(cls, angle: float, length: float = 1):
        slop = math.tan(math.radians(angle) if cls.Degree else angle)
        return cls(1, slop).set_length(length)

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
    
    @property
    def slope(self):
        if self.x == self.y == 0: return 0
        if self.x == 0: return np.inf
        return self.y / self.x

    def angle_to(self, other: Iterable[float] | 'Vector2D'):
        if not isinstance(other, Vector2D): other = Vector2D(other[0], other[1])
        normal_self = self.normalize()
        normal_other = other.normalize()
        return np.degrees(np.arccos(normal_self.dot(normal_other))) if self.Degree else np.arccos(normal_self.dot(normal_other))
        
    @property
    def angle(self):
        if self.Degree: return self.angle_to([1, 0])
        return self.angle_to([1, 0])

    @angle.setter
    def angle(self, value: float):
        newSelf = self.from_angle(value, self.length)
        self.dtype = newSelf.dtype
        self[:] = newSelf[:]


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


v = Vector2D(-1, 0)

print(v.angle)