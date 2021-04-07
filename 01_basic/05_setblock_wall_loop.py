from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
for i in range()# i 從 0 開始 到 9共 10 個數字 , 後面要有冒號
mc.setBlock(x+i, y, z, 1)# 內縮4格，或者一個 Tab 鍵
