"""Utilities
"""
# pylint: disable=no-member

import collections.abc
import math
import os


def floor(value, size, offset=200): # -offset ~ offset 범위의 숫자 중 value보다 작은 size의 배수인 수를 반환
    """Floor of `value` given `size` and `offset`.

    The floor function is best understood with a diagram of the number line::

         -200  -100    0    100   200
        <--|--x--|-----|--y--|--z--|-->

    The number line shown has offset 200 denoted by the left-hand tick mark at
    -200 and size 100 denoted by the tick marks at -100, 0, 100, and 200. The
    floor of a value is the left-hand tick mark of the range where it lies. So
    for the points show above: ``floor(x)`` is -200, ``floor(y)`` is 0, and
    ``floor(z)`` is 100.

    >>> floor(10, 100)
    0.0
    >>> floor(120, 100)
    100.0
    >>> floor(-10, 100)
    -100.0
    >>> floor(-150, 100)
    -200.0
    >>> floor(50, 167)
    -33.0

    """
    return float(((value + offset) // size) * size - offset)


def path(filename): # 전체 경로 반환 (filename의 경로를 알려줌)
    """Return full path to `filename` in freegames module."""
    filepath = os.path.realpath(__file__) # 파일 이름을 가져옴
    dirpath = os.path.dirname(filepath )# 디렉터리 반환
    fullpath = os.path.join(dirpath, filename) # 경로 구성 요소를 결합하여 전체 경로를 만듦.
    return fullpath


def line(a, b, x, y): # a,b 좌표에서 x, y좌표로 선을 그음
    """Draw line from `(a, b)` to `(x, y)`."""
    import turtle # turtle 모듈 선언
    turtle.up() # 거북이가 이동할 때는 그림을 그리지 않음
    turtle.goto(a, b) # (a,b로 이동)
    turtle.down() # 거북이가 이동할 때 그림 그림
    turtle.goto(x, y) # (x,y로 이동)


def square(x, y, size, name):  #x,y 좌표에서 size만큼의 정사각형을 그려줍니다. 해당 정사각형은 name의  색
    """Draw square at `(x, y)` with side length `size` and fill color `name`.

    The square is oriented so the bottom left corner is at (x, y).

    """
    import turtle

    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color(name) # 색을 name으로 바꿈
    turtle.begin_fill() # 거북이가 그릴 도형 채움

    for count in range(4):
        turtle.forward(size) # 거북이를 size 만큼 이동
        turtle.left(90) # 거북이를 왼쪽으로 90도 회전

    turtle.end_fill() # 거북이가 그릴 도형을 채우지 X


class vector(collections.abc.Sequence): # 2차원 벡터를 나타내는 클래스
    """Two-dimensional vector.

    Vectors can be modified in-place.

    >>> v = vector(0, 1)
    >>> v.move(1)
    >>> v
    vector(1, 2)
    >>> v.rotate(90)
    >>> v
    vector(-2.0, 1.0)

    """

    # pylint: disable=invalid-name - > 동일한 에러를 발생시키지 않는
    PRECISION = 6

    __slots__ = ('_x', '_y', '_hash') # 기존의 딕셔너리로 관리하는 속성을 집합 형태의 Set으로 바꿈

    def __init__(self, x, y): # init 생성자 메소드로 클래스를 만들때 본인 값을x ,y 로 초기화
        """Initialize vector with coordinates: x, y.

        >>> v = vector(1, 2)
        >>> v.x
        1
        >>> v.y
        2

        """
        self._hash = None
        self._x = round(x, self.PRECISION)
        self._y = round(y, self.PRECISION)

    @property
    def x(self): #벡터의 x축 성분 반환값 x
        """X-axis component of vector.

        >>> v = vector(1, 2)
        >>> v.x
        1
        >>> v.x = 3
        >>> v.x
        3

        """
        return self._x

    @x.setter #x의 setter 메소드
    def x(self, value):
        if self._hash is not None: # _hash가 None이 아니면
            raise ValueError('cannot set x after hashing') # 예외 처리
        self._x = round(value, self.PRECISION)

    @property
    def y(self): #벡터의 y축 성분 반환값 y
        """Y-axis component of vector.

        >>> v = vector(1, 2)
        >>> v.y
        2
        >>> v.y = 5
        >>> v.y
        5

        """
        return self._y

    @y.setter  #y값 설정 setter 메소드 
    def y(self, value):
        if self._hash is not None: # _hash가 None이 아니면
            raise ValueError('cannot set y after hashing')
        self._y = round(value, self.PRECISION)

    def __hash__(self): # x, y 값 고정 __ hash __ 는 동일한 객체에 대해 동일한 값을 반환해야함
        """v.__hash__() -> hash(v)

        >>> v = vector(1, 2)
        >>> h = hash(v)
        >>> v.x = 2
        Traceback (most recent call last):
            ...
        ValueError: cannot set x after hashing

        """
        if self._hash is None: # _hash가 None이 아니면
            pair = (self.x, self.y) # pair에 (_x, _y) 저장
            self._hash = hash(pair)
        return self._hash

    def __len__(self): # 벡터 길이 반환 메소드
        """v.__len__() -> len(v)

        >>> v = vector(1, 2)
        >>> len(v)
        2

        """
        return 2

    def __getitem__(self, index): # x,y 좌표 반환 메소드
        """v.__getitem__(v, i) -> v[i]

        >>> v = vector(3, 4)
        >>> v[0]
        3
        >>> v[1]
        4
        >>> v[2]
        Traceback (most recent call last):
            ...
        IndexError

        """
        if index == 0: # index가 0이면
            return self.x # _x 반환
        if index == 1: # index가 1이면
            return self.y # _y 반환
        raise IndexError # 예외 발생

    def copy(self):  #벡터의 복사본 반환 메소드
        """Return copy of vector.

        >>> v = vector(1, 2)
        >>> w = v.copy()
        >>> v is w
        False

        """
        type_self = type(self) # 벡터의 생성자 저장
        return type_self(self.x, self.y)

    def __eq__(self, other): # 벡터의 동일함 판별, 정의
        """v.__eq__(w) -> v == w

        >>> v = vector(1, 2)
        >>> w = vector(1, 2)
        >>> v == w
        True

        """
        if isinstance(other, vector): # isinstance(other, vector)가 true라면
            return self.x == other.x and self.y == other.y # _x에 other.x, _y에 other.y 저장
        return NotImplemented

    def __ne__(self, other): # notequal를 판별, 정의
        """v.__ne__(w) -> v != w

        >>> v = vector(1, 2)
        >>> w = vector(3, 4)
        >>> v != w
        True

        """
        if isinstance(other, vector): # isinstance(other, vector)가 true라면
            return self.x != other.x or self.y != other.y 
        return NotImplemented

    def __iadd__(self, other): # (본인의 값, add값) += 연산자 판별, 정의
        """v.__iadd__(w) -> v += w

        >>> v = vector(1, 2)
        >>> w = vector(3, 4)
        >>> v += w
        >>> v
        vector(4, 6)
        >>> v += 1
        >>> v
        vector(5, 7)

        """
        if self._hash is not None: 
            raise ValueError('cannot add vector after hashing')
        if isinstance(other, vector): # isinstance(other, vector)가 true라면
            self.x += other.x # self.x에 other.x를 더함
            self.y += other.y # self.y에 other.y를 더함
        else: # 그렇지 않다면
            self.x += other # self.x에 other를 더함
            self.y += other # self.y에 other를 더함
        return self

    def __add__(self, other): # add 메소드-> + 연산자 판별, 정의
        """v.__add__(w) -> v + w

        >>> v = vector(1, 2)
        >>> w = vector(3, 4)
        >>> v + w
        vector(4, 6)
        >>> v + 1
        vector(2, 3)
        >>> 2.0 + v
        vector(3.0, 4.0)

        """
        copy = self.copy() # self.copy를 copy에 저장
        return copy.__iadd__(other) # 반환

    __radd__ = __add__ # __radd__에 __add__ 저장

    def move(self, other): #self 값에서 other값을 더해 이동해주는 메소드
        """Move vector by other (in-place).

        >>> v = vector(1, 2)
        >>> w = vector(3, 4)
        >>> v.move(w)
        >>> v
        vector(4, 6)
        >>> v.move(3)
        >>> v
        vector(7, 9)

        """
        self.__iadd__(other)

    def __isub__(self, other): #본인값을 기준 -= 연산자 판별, 정의
        """v.__isub__(w) -> v -= w

        >>> v = vector(1, 2)
        >>> w = vector(3, 4)
        >>> v -= w
        >>> v
        vector(-2, -2)
        >>> v -= 1
        >>> v
        vector(-3, -3)

        """
        if self._hash is not None: # _hash가 None이 아니면
            raise ValueError('cannot subtract vector after hashing') # 예외 발생
        if isinstance(other, vector): # isinstance(other, vector)가 true라면
            self.x -= other.x # _x에 other.x를 뺀다
            self.y -= other.y # _y에 other.y를 뺀다
        else: # 그렇지 않다면
            self.x -= other # _x에 other를 뺀다
            self.y -= other # _y에 other를 뺀다
        return self

    def __sub__(self, other): #뺄셈(-) 역할 메소드
        """v.__sub__(w) -> v - w

        >>> v = vector(1, 2)
        >>> w = vector(3, 4)
        >>> v - w
        vector(-2, -2)
        >>> v - 1
        vector(0, 1)

        """
        copy = self.copy()
        return copy.__isub__(other)

    def __imul__(self, other): #본인 값을 기준 ,곱셈 역할(*=) 메소드
        """v.__imul__(w) -> v *= w

        >>> v = vector(1, 2)
        >>> w = vector(3, 4)
        >>> v *= w
        >>> v
        vector(3, 8)
        >>> v *= 2
        >>> v
        vector(6, 16)

        """
        if self._hash is not None:
            raise ValueError('cannot multiply vector after hashing')
        if isinstance(other, vector):
            self.x *= other.x # _x에 other.x를 곱한다
            self.y *= other.y # _y에 other.y를 곱한다
        else:
            self.x *= other # _x에 other를 곱한다
            self.y *= other # _y에 other를 곱한다
        return self

    def __mul__(self, other): #곱셈 역할(*) 메소드
        """v.__mul__(w) -> v * w

        >>> v = vector(1, 2)
        >>> w = vector(3, 4)
        >>> v * w
        vector(3, 8)
        >>> v * 2
        vector(2, 4)
        >>> 3.0 * v
        vector(3.0, 6.0)

        """
        copy = self.copy()
        return copy.__imul__(other)

    __rmul__ = __mul__

    def scale(self, other): # (imul사용) other로 self를 스케일링
        """Scale vector by other (in-place).

        >>> v = vector(1, 2)
        >>> w = vector(3, 4)
        >>> v.scale(w)
        >>> v
        vector(3, 8)
        >>> v.scale(0.5)
        >>> v
        vector(1.5, 4.0)

        """
        self.__imul__(other) # self.__imul__(other)를 호출

    def __itruediv__(self, other):  # v를 w로 나누는(/=) 메소드
        """v.__itruediv__(w) -> v /= w

        >>> v = vector(2, 4)
        >>> w = vector(4, 8)
        >>> v /= w
        >>> v
        vector(0.5, 0.5)
        >>> v /= 2
        >>> v
        vector(0.25, 0.25)

        """
        if self._hash is not None:
            raise ValueError('cannot divide vector after hashing')
        if isinstance(other, vector):
            self.x /= other.x # _x에 other.x를 나눈다
            self.y /= other.y # _y에 other.y를 나눈다
        else:
            self.x /= other # _x에 other를 나눈다
            self.y /= other # _y에 other를 나눈다
        return self

    def __truediv__(self, other): # w를 v로 나누는(/) 메소드
        """v.__truediv__(w) -> v / w

        >>> v = vector(1, 2)
        >>> w = vector(3, 4)
        >>> w / v
        vector(3.0, 2.0)
        >>> v / 2
        vector(0.5, 1.0)

        """
        copy = self.copy()
        return copy.__itruediv__(other)

    def __neg__(self): # v에 -1을 곱한 값 출력 (음수를 정의)
        """v.__neg__() -> -v

        >>> v = vector(1, 2)
        >>> -v
        vector(-1, -2)

        """
        # pylint: disable=invalid-unary-operand-type
        copy = self.copy()
        copy.x = -copy.x
        copy.y = -copy.y
        return copy

    def __abs__(self): # 밑변과 높이를 이용해 빗변을 알아내는 메소드
        # 벡터의 크기를 알려줌
        """v.__abs__() -> abs(v)

        >>> v = vector(3, 4)
        >>> abs(v)
        5.0

        """
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def rotate(self, angle):  # 좌표를 x축 기준으로 뒤집은 결과를 보여주는 메소드
        # 벡터 회전
        """Rotate vector counter-clockwise by angle (in-place).

        >>> v = vector(1, 2)
        >>> v.rotate(90)
        >>> v == vector(-2, 1)
        True

        """
        if self._hash is not None:
            raise ValueError('cannot rotate vector after hashing')
        radians = angle * math.pi / 180.0
        cosine = math.cos(radians)
        sine = math.sin(radians)
        x = self.x
        y = self.y
        self.x = x * cosine - y * sine
        self.y = y * cosine + x * sine

    def __repr__(self): # 벡터를 문자열로 나타냄
        """v.__repr__() -> repr(v)

        >>> v = vector(1, 2)
        >>> repr(v)
        'vector(1, 2)'

        """
        type_self = type(self)
        name = type_self.__name__
        return '{}({!r}, {!r})'.format(name, self.x, self.y) # 문자열로 만들어서 반환
