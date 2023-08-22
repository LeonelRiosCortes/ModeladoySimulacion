import math


def tiroParabolico(vx, vy, t):
    posx = vx * t
    posy = vy * t
    return[posx, posy]

    
v0 = 100
theta = 45
vx = (v0)*(math.cos(math.radians(theta)))
vy = (v0)*(math.sin(math.radians(theta)))

for t in range (14):
    #print("Tiro parabolico ( %f , %f, %i)" %(vx, vy, t))
    print(tiroParabolico(vx, vy, t))


