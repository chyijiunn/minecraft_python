from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
playerPos= mc.player.getPos()
File = open('tiles','w')#打開tiles檔案，並且進行寫入
block = str(list(playerPos)+list(mc.getBlockWithData(x,y-1,z)))+'\n'#每寫完一行，斷行
File.write(block)	#進行寫入
File.close()		#關閉tiles檔案