from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
mc.setBlocks(x-3, y+1,z,x+3 ,y+4, z, 1) #格式為(x起始,y起始,z起始,x結束,y結束,z結束,磚塊編號)
                                                                      # z 方向不變，只放置 x , y 方向，會是一堵立牆
                                                                      # 如何作一個 3x3x3的正立方塊？