from mcpi.minecraft import Minecraft
mc = Minecraft.create()
File = open('tiles','w')
input('copy startpoint , press Enter')
xs,ys,zs = mc.player.getPos()
input('copy endpoint , press Enter')
xe,ye,ze = mc.player.getPos()
for i in range(int(xs),int(xe)+1,1):
    for j in range(int(ys),int(ye)+1,1):
        for k in range(int(zs),int(ze)+1,1):
            axis = [i,j,k]
            block_0 =str(axis+list(mc.getBlockWithData(xs+i,ys+j,zs+k)))
            block_1=''.join(block_0.split(' '))#remove space
            block_2 = block_1.lstrip('[')
            block = block_2.rstrip(']')
            File.write(block+'\n')
File.close()