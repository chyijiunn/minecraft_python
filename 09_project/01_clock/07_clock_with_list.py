from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
south , high = -15 ,2
brick = 41
import time
from time import sleep
num = [
    [[[0,1],[0,3]],[[0,1],[0,3]]], #num_0
    [[[-1,3],[-1,1]],[[1,4],[1,1]]], #num_1
    [[[-1,3],[-0,3]],[[0,1],[1,1]]], #num_2
    [[[-1,3],[0,3]],[[-1,1],[0,1]]], #num_3
    [[[0,4],[0,3]],[[-1,1],[0,0]]], #num_4
    [[[0,3],[1,3]],[[-1,1],[0,1]]], #num_5
    [[[0,3],[1,3]],[[0,1],[0,1]]], #num_6
    [[[-1,3],[0,0]],[[-1,3],[0,0]]], #num_7
    [[[0,3],[0,3]],[[0,1],[0,1]]], #num_8
    [[[0,3],[0,3]],[[-1,1],[0,1]]], #num_9
    ]
while True:
    clock = time.localtime()
    now = [clock.tm_hour // 10,clock.tm_hour % 10,clock.tm_min //10,clock.tm_min % 10,clock.tm_sec //10,clock.tm_sec % 10]
    for digit in range(6):
        xStartPoint = digit *4 - 11
        mc.setBlocks(x+xStartPoint-1,y+high,z+south,x+xStartPoint+1,y+high+4,z+south,brick)
        for F in range(2):
            mc.setBlocks(x+xStartPoint+num[now[digit]][F][0][0],y+high+num[now[digit]][F][0][1], z+south,x+xStartPoint+num[now[digit]][F][1][0],y+high+num[now[digit]][F][1][1],z+south,0)
    sleep(1)