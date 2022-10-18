from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
for i in range(?):# 要蓋4層，問號應該要輸入多少呢？
    mc.setBlocks(x-3+i, y+i,z,x+3-i ,y+i , z, 1)
    # i = 0 , x-3 ~ x+3
    # i = 1 , x-2 ~ x+2
    # i = 2 , x-1 ~ x+1
    # i = 3 , x-0 ~ x+0 