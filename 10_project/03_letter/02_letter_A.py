from mcpi.minecraft import Minecraft
from cubeSet import cubeSet
mc = Minecraft.create()
Px, Py, Pz = mc.player.getPos()

char_a = str(574616734124315355412452)
charLoop = len(char_a)//3#cycle loop @ every character set
list_a  = list(char_a)

k = 0
for i in range(1,charLoop+1):
    cubeSet.cubeSetNo(list_a[k],Px+int(list_a[k+1]),Py+int(list_a[k+2]))
    k = i*3