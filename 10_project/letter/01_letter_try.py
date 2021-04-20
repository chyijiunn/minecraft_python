from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()

char_a = str(574616734124315355412452)
charLoop = len(char_a)//3#cycle loop @ every character set
list_a  = list(char_a)
'''
print(list_a[:len(char_a):3])#cubeNo. in serial
print(list_a[1:len(char_a):3])#cubeNo. arrange @x axis
print(list_a[2:len(char_a):3])#cubeNo. arrange @y axis
'''
k = 0
for i in range(1,charLoop+1):
    print(list_a[k],list_a[k+1],list_a[k+2])
    k = i*3
    
    