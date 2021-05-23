from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
playerPos= mc.player.getPos()
block = list(playerPos)+list(mc.getBlockWithData(x,y-1,z))#測試block的位置list與block資料能否合併
mc.setBlock(block)#看能否將方塊正常放置