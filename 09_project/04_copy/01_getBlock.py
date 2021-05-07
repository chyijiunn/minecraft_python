from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
block = mc.getBlockWithData(x,y-1,z)
print(block)