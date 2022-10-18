from mcpi.minecraft import Minecraft
from time import sleep     #引入時間模組
mc = Minecraft.create()
x, y, z = mc.player.getPos()
n = 10
for i in range(n):
    mc.setBlocks(x-n+i, y+i-1,z-n+i,x+n-i ,y+i-1, z+n-i, 1)
    sleep(1)#每一個迴圈都暫停一秒鐘