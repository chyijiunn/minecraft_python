from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
File = open('tiles','r')
for line in File:
    data = File.readline()
    print(data.rstrip())
    #mc.setBlock(tuple(data.rstrip()))
File.close