from mcpi.minecraft import Minecraft
mc = Minecraft.create()
def tree(x,y,z):#種一棵樹的函式
    mc.setBlocks(x,y,z,x,y+4,z,17,2)
    mc.setBlocks(x-2,y+4,z-2,x+2,y+4,z+2,18,3)
    mc.setBlocks(x-1,y+5,z-1,x+1,y+5,z+1,18,3)
    mc.setBlocks(x,y+6,z,x,y+6,z,18,3)
x, y, z = mc.player.getTilePos()
for i in range(10):
    for j in range(10):
        tree(7*i+x,y,7*j+z)#呼叫一棵樹的函式
