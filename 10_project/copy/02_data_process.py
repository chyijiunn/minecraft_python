from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
playerPos= mc.player.getPos()
block = list(playerPos)+list(mc.getBlockWithData(x,y-1,z))
mc.setBlock(block)