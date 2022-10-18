from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
n=6 #清理的範圍設定值
mc.setBlocks(x-n,y,z-n,x+n ,y+n, z+n, 0)#清理的範圍為 -n ~ +n，共 2n 的長、寬、高