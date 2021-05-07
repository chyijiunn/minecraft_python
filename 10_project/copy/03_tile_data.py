from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
playerPos= mc.player.getPos()
File = open('axis','w')
block = str(list(playerPos)+list(mc.getBlockWithData(x,y-1,z)))+'\n'
File.write(block)
File.close()