from mcpi.minecraft import Minecraft
mc = Minecraft.create()
File = open('tiles','w')
input('copy startpoint , press Enter')	# 讀取複製起始點座標
xs,ys,zs = mc.player.getPos()		# xs = start point of x
input('copy endpoint , press Enter')	# 讀取複製結束點座標
xe,ye,ze = mc.player.getPos()		# xe = end point of x
ds_x = int(xe-xs)			# ds_x 為結束點減去起始點
ds_y = int(ye-ys)
ds_z = int(ze-zs)
if ds_x > 0:				# 若 ds_x 變化值 > 0，則逐步 +1 到 range 的第三個參數
    count_x = 1
else :count_x = -1			# 若 ds_x 變化值 < 0，則逐步 -1 到 range 的第三個參數
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
            block_1=''.join(block_0.split(' '))
            block_2 = block_1.lstrip('[')
            block = block_2.rstrip(']')
            File.write(block+'\n')
File.close()