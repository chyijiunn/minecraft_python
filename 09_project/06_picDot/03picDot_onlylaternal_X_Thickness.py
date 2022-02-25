from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
data_brick = open('pics/01star','r')
for line in data_brick:
    a = line.split()
    lenthline = int(len(a))
    n = 10 # thickness of layer
    for layer in range(2):#front & back layer
        for i in range(lenthline):
            xAxis = int(a[i].split(',')[0])
            yAxis = int(a[i].split(',')[1])
            colorPar = int(a[i].split(',')[2])
            mc.setBlock(x+xAxis, y+yAxis, z+(layer*n),35,colorPar)
    for layer in range(1,n,1):#middle layer,only top & bottom of yAxis
        for i in range(len(a)):
            xAxis = int(a[0].split(',')[0])
            yAxis = int(a[0].split(',')[1])
            colorPar = int(a[0].split(',')[2])
            mc.setBlock(x+xAxis, y+yAxis, z+layer,35,colorPar)
            xAxis = int(a[lenthline-1].split(',')[0])
            yAxis = int(a[lenthline-1].split(',')[1])
            colorPar = int(a[lenthline-1].split(',')[2])
            mc.setBlock(x+xAxis, y+yAxis, z+layer,35,colorPar)
data_brick.close() 