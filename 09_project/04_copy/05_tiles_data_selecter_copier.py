from mcpi.minecraft import Minecraft
mc = Minecraft.create()
File = open('tiles','w')
input('copy startpoint , press Enter')
xs,ys,zs = mc.player.getPos()
input('copy endpoint , press Enter')
xe,ye,ze = mc.player.getPos()
ds_x = int(xe-xs)
ds_y = int(ye-ys)
ds_z = int(ze-zs)
if ds_x > 0:
    count_x = 1
else :count_x = -1
if ds_y > 0:
    count_y = 1
else :count_y = -1
if ds_z > 0:
    count_z = 1
else :count_z = -1
for i in range(0 , ds_x ,count_x):
    for j in range(0 , ds_y ,count_y):
        for k in range(0 , ds_z ,count_z):
            axis = [i,j,k]
            block_0 =str(axis+list(mc.getBlockWithData(xs+i,ys+j,zs+k)))
            block_1=''.join(block_0.split(' '))#remove space
            block_2 = block_1.lstrip('[')
            block = block_2.rstrip(']')
            File.write(block+'\n')
File.close()