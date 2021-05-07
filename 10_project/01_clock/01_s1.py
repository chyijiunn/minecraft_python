from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
front , high = 3 ,2
brick = 1
import time
from time import sleep
def one():
    mc.setBlocks(x+front-1,y+high,z,x+front+1,y+high+4,z,brick)
    mc.setBlocks(x+front-1,y+high+3,z,x+front-1,y+high+1,z,0)
    mc.setBlocks(x+front+1,y+high+4,z,x+front+1,y+high+1,z,0)
def two():
    mc.setBlocks(x+front-1,y+high,z,x+front+1,y+high+4,z,brick)
    mc.setBlocks(x+front-1,y+high+3,z,x+front,y+high+3,z,0)
    mc.setBlocks(x+front,y+high+1,z,x+front+1,y+high+1,z,0)
def three():
    mc.setBlocks(x+front-1,y+high,z,x+front+1,y+high+4,z,brick)
    mc.setBlocks(x+front-1,y+high+3,z,x+front,y+high+3,z,0)
    mc.setBlocks(x+front-1,y+high+1,z,x+front,y+high+1,z,0)
def four():
    mc.setBlocks(x+front-1,y+high,z,x+front+1,y+high+4,z,brick)
    mc.setBlocks(x+front,y+high+3,z,x+front,y+high+4,z,0)
    mc.setBlocks(x+front-1,y+high,z,x+front,y+high+1,z,0)
def five():
    mc.setBlocks(x+front-1,y+high,z,x+front+1,y+high+4,z,brick)
    mc.setBlocks(x+front,y+high+3,z,x+front+1,y+high+3,z,0)
    mc.setBlocks(x+front-1,y+high+1,z,x+front,y+high+1,z,0)
def six():
    mc.setBlocks(x+front-1,y+high,z,x+front+1,y+high+4,z,brick)
    mc.setBlocks(x+front,y+high+3,z,x+front+1,y+high+3,z,0)
    mc.setBlock(x+front,y+high+1,z,0)
def seven():
    mc.setBlocks(x+front-1,y+high,z,x+front+1,y+high+4,z,brick)
    mc.setBlocks(x+front-1,y+high,z,x+front,y+high+3,z,0)
def eight():
    mc.setBlocks(x+front-1,y+high,z,x+front+1,y+high+4,z,brick)
    mc.setBlock(x+front,y+high+1,z,0)
    mc.setBlock(x+front,y+high+3,z,0)
def nine():
    mc.setBlocks(x+front-1,y+high,z,x+front+1,y+high+4,z,brick)
    mc.setBlocks(x+front-1,y+high+1,z,x+front,y+high+1,z,0)
    mc.setBlock(x+front,y+high+3,z,0)
def zero():
    mc.setBlocks(x+front-1,y+high,z,x+front+1,y+high+4,z,brick)
    mc.setBlocks(x+front,y+high+1,z,x+front,y+high+3,z,0)
def digit6():
    x = x + 12

while True:
    clock = time.localtime()
    h1 , h2 = clock.tm_hour // 10 , clock.tm_hour % 10
    m1,m2 =clock.tm_min //10 ,clock.tm_min % 10
    s1 ,s2 = clock.tm_sec //10 , clock.tm_sec % 10
    if s2 == 0:
        zero()
    elif s2 == 1:
        one()
    elif s2 ==2:
        two()
    elif s2 ==3:
        three()
    elif s2 == 4:
        four()
    elif s2 == 5:
        five()
    elif s2 == 6:
        six()
    elif s2 == 7:
        seven()
    elif s2 == 8:
        eight()
    elif s2 == 9:
        nine()
    sleep(1)
    mc.setBlocks(x+front-1,y+high,z,x+front+1,y+high+4,z,0)


