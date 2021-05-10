from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
File = open('tiles','w')
copyRange = 5
for i in range(-copyRange,copyRange+1):
    for j in range(copyRange):
        for k in range(-copyRange,copyRange+1):
            axis = [i,j,k]
            block_0 =str(axis+list(mc.getBlockWithData(x+i,y-1+j,z+k)))
            block_1=''.join(block_0.split(' '))#remove space
            block_2 = block_1.lstrip('[')
            block = block_2.rstrip(']')
            File.write(block+'\n')
File.close()