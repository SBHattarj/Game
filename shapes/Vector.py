import numpy as np
from typing import Iterable

class Vector(np.ndarray):
    def __new__(cls, items: Iterable):
        obj = np.asarray(items).view(cls)
        return obj

    def clone(self):
        return type(self)(self)

    @property
    def sqr_length(self):
        return np.sum(np.square(self))

    @property
    def length(self):
        return np.linalg.norm(self)

    def dot(self, other: Iterable[float] | np.ndarray | 'Vector'):
        Other = Vector(other)
        len_def = len(self) - len(Other)
        if len_def == 0:
            return np.dot(self, Other)

        if len_def > 0:
            edited_other = type(self)([*Other] + [0] * len_def)
            return np.dot(self, edited_other)

        if len_def < 0:
            edited_self = type(self)([*self] + [0] * (-len_def))
            return np.dot(edited_self, Other)

    def cross(self, other: Iterable[float] | np.ndarray | 'Vector'):
        return np.cross(self, other)

    def normalize(self):
        l2 = np.atleast_1d(self.length)
        if l2 == 1: return self.clone()
        l2[l2==0] = 1
        normalized = self / l2

        return normalized if normalized.length == 1.0 else normalized.normalize()

    def set_length(self, length: float | Iterable[float] | np.ndarray | 'Vector'):
        return self.normalize() * length

    @length.setter
    def length(self, length: float | Iterable[float] | np.ndarray | 'Vector'):
        self[0], self[1] = self.set_length(length)

    def project(self, other: Iterable[float] | np.ndarray | 'Vector'):
        return self * self.dot(other) / self.dot(self)
    
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

v = Vector3D(1, 2, 3)
print(v.z)