from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
r = 9                                   #設定圓的半徑
for i in range (-r,r,1):
    for j in range (-r,r,1):
        d = i*i + j*j                   #回憶一下畢氏定理：三角形斜邊 c 的平方 = a 和 b 的平方和 
        if d <= r**2:                   #如果距離小於半徑
            mc.setBlock(x,y+i,z+j,1)    #就放一個方塊吧！
mc.player.setPos(x,y+r+2,z)             #這裡作一個跳出
#如果這個圓要空心要怎作呢？
