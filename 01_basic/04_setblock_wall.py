from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
#請問下面的結果會長啥樣？
mc.setBlock(x+0, y, z, 1)
mc.setBlock(x+1, y, z, 1)
mc.setBlock(x+2, y, z, 1)
mc.setBlock(x+3, y, z, 1)
mc.setBlock(x+4, y, z, 1)
mc.setBlock(x+5, y, z, 1)
mc.setBlock(x+6, y, z, 1)
mc.setBlock(x+7, y, z, 1)
mc.setBlock(x+8, y, z, 1)
mc.setBlock(x+9, y, z, 1)
#有沒有更好的作法？