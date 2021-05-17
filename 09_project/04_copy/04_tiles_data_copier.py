from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
File = open('tiles','w')
copyRange = 5#設定複製的範圍
for i in range(-copyRange,copyRange+1):	#從-x～ｘ，每次跳一　
    for j in range(copyRange):		#從-ｙ～ｙ，每次跳一
        for k in range(-copyRange,copyRange+1):#從-ｚ～ｚ，每次跳一
            axis = [i,j,k]
            block_0 =str(axis+list(mc.getBlockWithData(x+i,y-1+j,z+k)))#將座標與磚塊資料轉為string才能寫入
            block_1=''.join(block_0.split(' '))	#將空格移除
            block_2 = block_1.lstrip('[')	#去掉list左邊的'['
            block = block_2.rstrip(']')		#去掉list右邊的']'
            File.write(block+'\n')		#寫入剩下的資料
File.close()