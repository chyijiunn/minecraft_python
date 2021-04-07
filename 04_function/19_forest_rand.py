from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
def forest(x,y,z):
    h_tree = random.randint(3,8)#設定樹的高度隨機範圍
    mc.setBlocks(x,y,z,x,y+h_tree+4,z,17,2)
    mc.setBlocks(x-2,y+4,z-2,x+2,y+h_tree+4,z+2,18,3)
    mc.setBlocks(x-1,y+5,z-1,x+1,y+h_tree+5,z+1,18,3)
    mc.setBlocks(x,y+6,z,x,y+h_tree+6,z,18,3)
x, y, z = mc.player.getTilePos()
for i in range(10):
    for j in range(10):
        a = random.randint(0,2)
        forest(2*i*a+x,y,2*i*j+z+2)#設定樹的隨機範圍
