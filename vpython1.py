import vpython as vp
from math import *

p = vp.sphere(radius = 0.4, color = vp.color.red)
e1 = vp.ring(color = vp.color.red, thickness = 0.05)
e2 = vp.ring(color = vp.color.green, thickness = 0.05)
e3 = vp.ring(color = vp.color.blue, thickness = 0.05, radius = 1.5)

e1.axis = vp.vector(1, -1.25, 0)
e2.axis = vp.vector(1, 1.25, 0)
e3.axis = vp.vector(1, 0, 0)

a1 = vp.arrow(length = 1, color = vp.color.red, axis = vp.vector( 1, 0, 0), pos = vp.vector(4, 0, 0))
a2 = vp.arrow(length = 1, color = vp.color.green, axis = vp.vector( 0, 1, 0), pos = vp.vector(4, 0, 0))
a3 = vp.arrow(length = 1, color = vp.color.blue, axis = vp.vector( 0, 0, 1), pos = vp.vector(4, 0, 0))

s1, s2, s3 = vp.sphere(radius = 0.1, color = vp.color.red), vp.sphere(radius = 0.1, color = vp.color.green), vp.sphere(radius = 0.1, color = vp.color.blue)

s1.pos, s2.pos, s3.pos = vp.vector(0, 0, 1), vp.vector(0,0, 1), vp.vector(0, 0, 1.5)

cyl = vp.cylinder(length = 0.85, axis = vp.vector(0, 0, 1))

cyl2, cyl3 = vp.cylinder(length = 0.85, axis = vp.vector(0, 0, 1), radius = 0.0000000001), vp.cylinder(length = 0.85, axis = vp.vector(0, 0, 1.5), radius = 0.0000000001)
cyl.radius = 0.0000000001

eo1 = vp.compound([s1, cyl])
eo2 = vp.compound([s2, cyl2])
eo3 = vp.compound([s3, cyl2])

while True:

    vp.rate = 100
    eo1.rotate(angle=1 * (pi/180), axis=vp.vector(1, -1.25, 0), origin=vp.vector(0, 0, 0))
    eo2.rotate(angle=1 * (pi/180), axis=vp.vector(1, 1.25, 0), origin=vp.vector(0, 0, 0))
    eo3.rotate(angle=1 * (pi/180), axis=vp.vector(1, 0, 0), origin=vp.vector(0, 0, 0))
