def constructor():
    data_brick = open('picDot/plane','r')
    for line in data_brick:
        a = line.split()
        for i in range(len(a)):
            xAxis = int(a[i].split(',')[0])
            yAxis = int(a[i].split(',')[1])
            zAxis = int(a[i].split(',')[2])
            colorPar = int(a[i].split(',')[3])
            mc.setBlock(x+xAxis, y+yAxis, z+zAxis,35,colorPar)
    data_brick.close()
