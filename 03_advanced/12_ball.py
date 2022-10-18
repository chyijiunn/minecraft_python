from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
r = 9
for h in range (-r,r,1):#如果不要用三層迴圈，可以怎作呢?
    for i in range (-r,r,1):
        for j in range (-r,r,1):
            d = h*h + i*i + j*j
            if d >=(r-1)**2 and d <= r**2:
                mc.setBlock(x+h,y+i,z+j,1)
mc.player.setPos(x,y+(2*r)+2,z)
