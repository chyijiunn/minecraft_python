from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
data_brick = open('data','r')
for line in data_brick:
    a = line.split()
    n = 10 # thickness of layer
    for layer in range(2):#front & back layer
        for i in range(len(a)):
            xAxis = int(a[i].split(',')[0])
            yAxis = int(a[i].split(',')[1])
            colorPar = int(a[i].split(',')[2])
            mc.setBlock(x+xAxis, y+yAxis, z+(layer*n),35,colorPar)
    for layer in range(1,n,1):#middle layer
        for i in range(len(a)):
            xAxis = int(a[i].split(',')[0])
            yAxis = int(a[i].split(',')[1])
            colorPar = int(a[i].split(',')[2])
            if colorPar == 1:
                mc.setBlock(x+xAxis, y+yAxis, z+layer,35,colorPar)#solid content
                
data_brick.close()
