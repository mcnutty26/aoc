from nutty_utils import *

#point2d
p1 = point2d()
p2 = point2d(3,4)
p3 = point2d(1,2)
p4 = point2d(1,3)
p5 = point2d(1,2)
p6 = dict()
p7 = point2d(0,0)
p6[p5] = p4

assert p1.x == 0 and p1.y == 0
assert p1.distance(p7) == 0
assert p1.distance(p2) == 7
assert p2 > p3
assert p3 < p2
assert not p2 == p3
assert p3 == p5
assert not p3 < p5
assert not p5 < p3
assert not p3 > p5
assert not p5 > p3

#point3d
p1 = point3d()
p2 = point3d(0,3,4)
p3 = point3d(0,1,2)
p4 = point3d(0,1,3)
p5 = point3d(0,1,2)
p6 = dict()
p7 = point3d(0,0)
p6[p5] = p4

assert p1.x == 0 and p1.y == 0 and p1.z == 0
assert p1.distance(p7) == 0
assert p1.distance(p2) == 7
assert p2 > p3
assert p3 < p2
assert not p2 == p3
assert p3 == p5
assert not p3 < p5
assert not p5 < p3
assert not p3 > p5
assert not p5 > p3
