from mcpi.minecraft import Minecraft
from cubeSet import cubeSet
from time import sleep
mc = Minecraft.create()
Px, Py, Pz = mc.player.getPos()
letterData = dict(
A=547616737124315355412452,
B=117114111416413547644641753,
C=315547512616641737731,
D=416314117111355547641,
E=117114111247241416413,
F=317313114227247,
G=547512616315131244453737,
H=313317353357114244,
I=121127336433,
J=357354121413,
K=317313114543645757751,
L=317314111241,
M=313316356353517646735,
N=313316517735244357353,
O=316356413453121127,
P=317313713127124456714,
Q=512533547315355452231737616,
R=313316353117224547644,
S=512515544547641616731734737,
T=117247336333,
U=314317354357121,
V=417415513631454357,
W=317314611733542354357,
X=417525543751757645612711,
Y=317357124333,
Z=117247645623412121751
    )
while True:
    for k in letterData.keys():
        char_a = str(letterData[k])
        charLoop = len(char_a)//3#cycle loop @ every character set
        list_a  = list(char_a)
        
        k = 0
        for i in range(1,charLoop+1):
            cubeSet.cubeSetNo(int(list_a[k]),float(list_a[k+1]),float(list_a[k+2]))
            k = i*3
        sleep(1)
        n=10 #清理的範圍設定值
        mc.setBlocks(Px,Py,Pz-n,Px+n ,Py+n, Pz+n, 0)
