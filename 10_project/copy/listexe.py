from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
copyRange = 3
for i in range(copyRange):
    for j in range(copyRange):
        for k in range(copyRange):
            block = str([x+i,y-1+j,z+k]+list(mc.getBlockWithData(x+i,y-1+j,z+k)))+'\n'
            print(block)


