from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
File = open('tiles','w')
copyRange = 3
for i in range(copyRange):
    for j in range(copyRange):
        for k in range(copyRange):
            block = list((int(x)+i,int(y)-1+j,int(z)+k))+list(mc.getBlockWithData(x+i,y-1+j,z+k))
            File.write(str(block)+'\n')
File.close()
