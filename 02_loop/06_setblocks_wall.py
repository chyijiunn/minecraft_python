from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
mc.setBlocks(x-3, y+1,z,x+3 ,y+4, z, 1) #格式為(x起始點,y起始點,z起始點,x結束點,y結束點,z結束點,磚塊編號)，
                                                                      # z 方向不變，只放置 x , y 方向，會是一堵立牆
                                                                      # 如何作一個 3x3x3的正立方塊？