from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
block = 4
def cubeSetNo(setNo,shift_x,shift_y):
    def cubeSet_1():
        mc.setBlock(x+shift_x,y+shift_y,z,block)
        mc.setBlock(x+shift_x+1,y+shift_y,z,block)
        mc.setBlock(x+shift_x+2,y+shift_y,z,block)
    def cubeSet_2():
        mc.setBlock(x+shift_x,y+shift_y,z,block)
        mc.setBlock(x+shift_x+1,y+shift_y,z,block)
    def cubeSet_3():
        mc.setBlock(x+shift_x,y+shift_y,z,block)
        mc.setBlock(x+shift_x,y+shift_y-1,z,block)
        mc.setBlock(x+shift_x,y+shift_y-2,z,block)
    def cubeSet_4():
        mc.setBlock(x+shift_x,y+shift_y,z,block)
        mc.setBlock(x+shift_x,y+shift_y-1,z,block)
    def cubeSet_5():
        mc.setBlock(x+shift_x,y+shift_y,z,block)
        mc.setBlock(x+shift_x+1,y+shift_y-1,z,block)
    def cubeSet_6():
        mc.setBlock(x+shift_x,y+shift_y,z,block)
        mc.setBlock(x+shift_x+1,y+shift_y+1,z,block)
    def cubeSet_7():
        mc.setBlock(x+shift_x,y+shift_y,z,block)
    if setNo == 1:cubeSet_1()
    elif setNo == 2:cubeSet_2()
    elif setNo == 3:cubeSet_3()
    elif setNo == 4:cubeSet_4()
    elif setNo == 5:cubeSet_5()
    elif setNo ==6 :cubeSet_6()
    elif setNo ==7 :cubeSet_7()