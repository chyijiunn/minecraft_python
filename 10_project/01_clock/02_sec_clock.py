from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
front , high = 15 ,2
brick = 1
import time
from time import sleep
def one(i):
    mc.setBlocks(x+i-1,y+high,z-front,x+i+1,y+high+4,z-front,brick)
    mc.setBlocks(x+i-1,y+high+3,z-front,x+i-1,y+high+1,z-front,0)
    mc.setBlocks(x+i+1,y+high+4,z-front,x+i+1,y+high+1,z-front,0)
def two(i):
    mc.setBlocks(x+i-1,y+high,z-front,x+i+1,y+high+4,z-front,brick)
    mc.setBlocks(x+i-1,y+high+3,z-front,x+i,y+high+3,z-front,0)
    mc.setBlocks(x+i,y+high+1,z-front,x+i+1,y+high+1,z-front,0)
def three(i):
    mc.setBlocks(x+i-1,y+high,z-front,x+i+1,y+high+4,z-front,brick)
    mc.setBlocks(x+i-1,y+high+3,z-front,x+i,y+high+3,z-front,0)
    mc.setBlocks(x+i-1,y+high+1,z-front,x+i,y+high+1,z-front,0)
def four(i):
    mc.setBlocks(x+i-1,y+high,z-front,x+i+1,y+high+4,z-front,brick)
    mc.setBlocks(x+i,y+high+3,z-front,x+i,y+high+4,z-front,0)
    mc.setBlocks(x+i-1,y+high,z-front,x+i,y+high+1,z-front,0)
def five(i):
    mc.setBlocks(x+i-1,y+high,z-front,x+i+1,y+high+4,z-front,brick)
    mc.setBlocks(x+i,y+high+3,z-front,x+i+1,y+high+3,z-front,0)
    mc.setBlocks(x+i-1,y+high+1,z-front,x+i,y+high+1,z-front,0)
def six(i):
    mc.setBlocks(x+i-1,y+high,z-front,x+i+1,y+high+4,z-front,brick)
    mc.setBlocks(x+i,y+high+3,z-front,x+i+1,y+high+3,z-front,0)
    mc.setBlock(x+i,y+high+1,z-front,0)
def seven(i):
    mc.setBlocks(x+i-1,y+high,z-front,x+i+1,y+high+4,z-front,brick)
    mc.setBlocks(x+i-1,y+high,z-front,x+i,y+high+3,z-front,0)
def eight(i):
    mc.setBlocks(x+i-1,y+high,z-front,x+i+1,y+high+4,z-front,brick)
    mc.setBlock(x+i,y+high+1,z-front,0)
    mc.setBlock(x+i,y+high+3,z-front,0)
def nine(i):
    mc.setBlocks(x+i-1,y+high,z-front,x+i+1,y+high+4,z-front,brick)
    mc.setBlocks(x+i-1,y+high+1,z-front,x+i,y+high+1,z-front,0)
    mc.setBlock(x+i,y+high+3,z-front,0)
def zero(i):
    mc.setBlocks(x+i-1,y+high,z-front,x+i+1,y+high+4,z-front,brick)
    mc.setBlocks(x+i,y+high+1,z-front,x+i,y+high+3,z-front,0)
while True:
    clock = time.localtime()
    a = [clock.tm_hour // 10,clock.tm_hour % 10,clock.tm_min //10,clock.tm_min % 10,clock.tm_sec //10,clock.tm_sec % 10]
    for j in range(5):
        for i in range(-12,13,4):
            if a[j] == 0:
                zero(i)
            elif a[j] == 1:
                one(i)
            elif a[j] ==2:
                two(i)
            elif a[j] ==3:
                three(i)
            elif a[j] == 4:
                four(i)
            elif a[j] == 5:
                five(i)
            elif a[j] == 6:
                six(i)
            elif a[j] == 7:
                seven(i)
            elif a[j] == 8:
                eight(i)
            elif a[j] == 9:
                nine(i)
    sleep(1)
    mc.setBlocks(x+i-1,y+high,z-front,x+i+1,y+high+4,z-front,0)


