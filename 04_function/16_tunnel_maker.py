from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()
n=0.5 #清理的範圍設定值
while True:
    x, y, z = mc.player.getPos()
    mc.setBlocks(x-n,y,z-n,x+n ,y+2, z+n, 0)#清理的範圍為 -n ~ +n，共 2n
    sleep(0.5)
