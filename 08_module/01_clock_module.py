from mcpi.minecraft import Minecraft
from time import sleep
import time
import module.number as no
mc = Minecraft.create()
x, y, z = mc.player.getPos()
south , high = -15 ,2
brick = 41

while True:
    clock = time.localtime()
    now = [clock.tm_hour // 10,clock.tm_hour % 10,clock.tm_min //10,clock.tm_min % 10,clock.tm_sec //10,clock.tm_sec % 10]
    for digit in range(6):
        xStartPoint = digit *4 - 11
        mc.setBlocks(x+xStartPoint-1,y+high,z+south,x+xStartPoint+1,y+high+4,z+south,brick)
        for F in range(2):
            mc.setBlocks(x+xStartPoint+no.index(now[digit])[F][0][0],y+high+no.index(now[digit])[F][0][1], z+south,x+xStartPoint+no.index(now[digit])[F][1][0],y+high+no.index(now[digit])[F][1][1],z+south,0)
    sleep(1)