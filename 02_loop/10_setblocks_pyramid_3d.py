from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()
x, y, z = mc.player.getPos()
n = 5
for i in range(n):
    mc.setBlocks(x-n+i, y+i-1,z-n+i,x+n-i ,y+i-1, z+n-i,79)
#蓋完後，卻卡在裡面了啦，怎辦？