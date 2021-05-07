from mcpi.minecraft import Minecraft
from cubeSet import cubeSet
mc = Minecraft.create()
Px, Py, Pz = mc.player.getPos()

char_a = str(512533547315355452231737616)
charLoop = len(char_a)//3#cycle loop @ every character set
list_a  = list(char_a)

k = 0
for i in range(1,charLoop+1):
    cubeSet.cubeSetNo(int(list_a[k]),float(list_a[k+1]),float(list_a[k+2]))
    k = i*3