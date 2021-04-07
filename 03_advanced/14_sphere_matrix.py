from mcpi.minecraft import Minecraft
import math
import random
mc = Minecraft.create()
pos= mc.player.getPos()
x , y ,z = pos.x ,pos.y ,pos.z
r = 3 # size of sphere
c = 0 # color of sphere
for k in range(3):# set x axis numbers
    for l in range(5):# set y axis numbers
        for h in range (-r,r,1):
            for i in range (-r,r,1):
                for j in range (-r,r,1):
                    d = h*h + i*i + j*j
                    if d >=(r-1)**2 and d <= r**2:
                        mc.setBlock(x+h,y+r+i,z+j,35,c)
        y = y + 2*r + 1 # y-axis space between the core of spheres
        c = c + 1 # change color
    y = pos.y# y reset 
    x = x + 2*r + 1 # x-axis space between the core of spheres
mc.player.setPos(x,40,z)
