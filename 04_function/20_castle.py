from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
#清空區域、城牆寬度的一半、城牆高度、塔的半徑、塔的高度、牆的深度
area , width , high , radius , tall, depth = 20 ,  15 , 5 , 8 ,12 ,5 
def clear():
    mc.setBlocks(x-area,y,z-area,x+area ,y+area, z+area, 0)
def wall():
    mc.setBlocks(x-width+radius,y-depth,z+width,x+width-radius,y+high,z+width,4)#south wall
    mc.setBlocks(x-width+radius,y-depth,z-width,x+width-radius,y+high,z-width,4)   #north wall
    mc.setBlocks(x+width,y-depth,z-width+radius,x+width,y+high,z+width-radius,4)#east wall
    mc.setBlocks(x-width,y-depth,z-width+radius,x-width,y+high,z+width-radius,4)#west wall
    mc.setBlocks(x-3,y-depth,z+width,x+3,y+3,z+width,5)#gate toward to south
def tower():
    for h in range(tall+1):
        for i in range(-radius,radius+1):
            for j in range(-radius ,radius+1):
                if i**2+j**2 <= radius**2 and  i**2+j**2 > (radius-1)**2:
                    mc.setBlock(x+width+i,y-depth+h,z+width+j,4)
                    mc.setBlock(x-width+i,y-depth+h,z+width+j,4)
                    mc.setBlock(x+width+i,y-depth+h,z-width+j,4)
                    mc.setBlock(x-width+i,y-depth+h,z-width+j,4)
                for k in range(radius+1):
                    if i**2+j**2+k**2 <= radius**2 and  i**2+j**2+k**2 > (radius-1)**2:
                        mc.setBlock(x+width+i,y-depth+tall+k,z+width+j,4)
                        mc.setBlock(x-width+i,y-depth+tall+k,z+width+j,4)
                        mc.setBlock(x+width+i,y-depth+tall+k,z-width+j,4)
                        mc.setBlock(x-width+i,y-depth+tall+k,z-width+j,4)
def pyrimid(size):
    for i in range(size):
        mc.setBlocks(x-size+i, y+i-1,z-size+i,x+size-i ,y+i-1, z+size-i,41)
        mc.setBlocks(x-size+i+1, y+i-1,z-size+i+1,x+size-i-1 ,y+i-1, z+size-i-1,0)     
                
wall()
tower()
pyrimid(5)
#mc.player.setPos(x,y+5,z)
