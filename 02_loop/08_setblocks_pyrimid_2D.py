from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
mc.setBlocks(x-3, y     ,  z,x+3 ,y       , z, 1)
mc.setBlocks(x-2, y+1, z,x+2 ,y+1 , z, 1)
mc.setBlocks(x-1, y+2, z,x+1 ,y+2 , z, 1)
mc.setBlocks(x    , y+3, z,x      ,y+3 , z, 1)

'''
把零寫入協助判斷規則變動
mc.setBlocks(x-3+0, y+0,z,x+3-0 ,y+0 , z, 1)
mc.setBlocks(x-3+1, y+1,z,x+3-1 ,y+1 , z, 1)
mc.setBlocks(x-3+2, y+2,z,x+3-2 ,y+2 , z, 1)
mc.setBlocks(x-3+3, y+3,z,x+3-3 ,y+3 , z, 1)
'''
