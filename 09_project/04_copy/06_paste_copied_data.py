from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
File = open('tiles','r')
for line in File:
    x1 , y1 , z1 , brick , dat = line.split(',')
    mc.setBlock(x+int(x1) , y+int(y1) , z+int(z1) , int(brick) ,int(dat))
File.close