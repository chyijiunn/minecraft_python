from mcpi.minecraft import Minecraft
mc = Minecraft.create()                          
posx, posy, posz = mc.player.getPos()
x = posx
y=posy
z=posz
brick =1 
p= [
    [[[0,1],[0,3]],[[0,1],[0,3]]], #F0
    [[[-1,3],[-1,1]],[[1,4],[1,1]]], #F1
    [[[-1,3],[-0,3]],[[0,1],[1,1]]], #F2
    [[[-1,3],[0,3]],[[-1,1],[0,1]]], #F3
    [[[0,4],[0,3]],[[-1,1],[0,0]]], #F4
    [[[0,3],[1,3]],[[-1,1],[0,1]]], #F5
    [[[0,3],[1,3]],[[0,1],[0,1]]], #F6
    [[[-1,3],[0,0]],[[-1,3],[0,0]]], #F7
    [[[0,3],[0,3]],[[0,1],[0,1]]], #F8
    [[[0,3],[0,3]],[[-1,1],[0,1]]], #F9
    ]
for i in range(10):
    mc.setBlocks(x-1,y, z,x+1,y+4,z,brick)
    for F in range(2):
        mc.setBlocks(x+p[i][F][0][0],y+p[i][F][0][1], z,x+p[i][F][1][0],y+p[i][F][1][1],z,0)
    x=x+4