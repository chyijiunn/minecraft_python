from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
for i in range(?):# 要蓋4層，問號應該要輸入多少呢？
    #西-3~東＋3，每次 i 都會 +1 ，依次為 -3 ~ +3 , -2 ~ +2 , -1 ~ +1 , 最後 0~0，共 ？ 層
    mc.setBlocks(x-3+i, y+i,z,x+3-i ,y+i , z, 1)