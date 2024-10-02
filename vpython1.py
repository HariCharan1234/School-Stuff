import vpython as vp


p = vp.sphere(radius = 0.4, color = vp.color.red)
e1 = vp.ring(color = vp.color.red, thickness = 0.05)
e2 = vp.ring(color = vp.color.green, thickness = 0.05)
e3 = vp.ring(color = vp.color.blue, thickness = 0.05, radius = 1.25)

e1.axis = vp.vector(1, -1.25, 0)
e2.axis = vp.vector(1, 1.25, 0)
e3.axis = vp.vector(1, 0, 0)

a1 = vp.arrow(length = 1, color = vp.color.red, axis = vp.vector( 1, 0, 0), pos = vp.vector(4, 0, 0))
a2 = vp.arrow(length = 1, color = vp.color.green, axis = vp.vector( 0, 1, 0), pos = vp.vector(4, 0, 0))
a3 = vp.arrow(length = 1, color = vp.color.blue, axis = vp.vector( 0, 0, 1), pos = vp.vector(4, 0, 0))

s1, s2, s3 = vp.sphere(radius = 0.1, color = vp.color.red, pos = vp.vector(1, -1.25, 0)), vp.sphere(radius = 0.1, color = vp.color.green, pos = vp.vector(1, 1.25, 0)), vp.sphere(radius = 0.1, color = vp.color.blue, pos = vp.vector(1, 0, 0))

s1.pos, s2.pos, s3.pos = vp.vector(0, 0, 1), vp.vector(0,0, 1), vp.vector(0, 0, 1.25)

cyl = vp.cylinder(length = 0.85, axis = vp.vector(0, 0, 1))

cyl2, cyl3 = vp.cylinder(length = 0.85, axis = vp.vector(0, 0, 1), radius = 0.0000000001), vp.cylinder(length = 0.85, axis = vp.vector(0, 0, 1), radius = 0.0000000001)
cyl.radius = 0.0000000001

eo1 = vp.compound([s1, cyl])
eo2 = vp.compound([s2, cyl2])
eo3 = vp.compound([s3, cyl2])


sp1 = vp.sphere(radius = 1, opacity = 0.25)
sp2 = vp.sphere(radius = 1.25, opacity = 0.25)
c1, c2, c3 = vp.cylinder(length = 0.85, axis = vp.vector(0, 0, 1), radius = 0.000000001), vp.cylinder(length = 0.85, axis = vp.vector(0, 0, 1), radius = 0.0000000001), vp.cylinder(length = 0.85, radius = 0.0000000001)
is1, is2, is3 = vp.compound([eo1, c1, e1]), vp.compound([eo2, c2, e2]), vp.compound([eo3, c3, e3])
while True:
    vp.rate(60)
    #eo1.rotate(angle=5 * (3.14/180), axis=vp.vector(1, -1.25, 0), origin=vp.vector(0, 0, 0))
    #eo2.rotate(angle=5 * (3.14/180), axis=vp.vector(1, 1.25, 0), origin=vp.vector(0, 0, 0))
    #eo3.rotate(angle=5 * (3.14/180), axis=vp.vector(1, 0, 0), origin=vp.vector(0, 0, 0))
    is1.rotate(angle=10 * (3.14/180), axis = vp.vector(0, 1, 0), origin=vp.vector(0, 0, 0))
    is2.rotate(angle=10 * (3.14/180), axis = vp.vector(1, 0, 0), origin=vp.vector(0, 0, 0))
    is3.rotate(angle=10 * (3.14/180), axis = vp.vector(1, 0, 1), origin=vp.vector(0, 0, 0))
