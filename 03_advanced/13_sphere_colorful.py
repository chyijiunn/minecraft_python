from mcpi.minecraft import Minecraft
import math
import random
#n = random.randrange(0,16,1)
mc = Minecraft.create()
x, y, z = mc.player.getPos()
r = 9
for h in range (-r,r,1):
    for i in range (-r,r,1):
        for j in range (-r,r,1):
            d = h*h + i*i + j*j
            if d >=(r-1)**2 and d <= r**2:
                mc.setBlock(x+h,y+i,z+j,35,random.randrange(0,16,1))
mc.player.setPos(x,y+20,z)