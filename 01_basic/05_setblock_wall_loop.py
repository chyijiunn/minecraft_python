from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
for i in range()# i 從 0 ～ 9 共 10 個數字 , 最後要冒號
mc.setBlock(x+i, y, z, 1)# 內縮4格，或一個 Tab 鍵
