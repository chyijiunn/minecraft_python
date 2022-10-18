from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()
while True:
    x, y, z = mc.player.getPos()
    mc.setBlock(x,y,z,51)
    sleep(1)