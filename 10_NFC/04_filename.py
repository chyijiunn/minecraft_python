from py532lib.i2c import *
from py532lib.frame import *
from py532lib.constants import *
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
pn532 = Pn532_i2c()
pn532.SAMconfigure()

def constructor(filename):
    file = 'picDot/'+str(filename)
    data_brick = open(file,'r')
    for line in data_brick:
        a = line.split()
        for i in range(len(a)):
            xAxis = int(a[i].split(',')[0])
            yAxis = int(a[i].split(',')[1])
            zAxis = int(a[i].split(',')[2])
            colorPar = int(a[i].split(',')[3])
            mc.setBlock(x+xAxis, y+yAxis, z+zAxis,35,colorPar)
    data_brick.close()

NFC_Tag = {
    b'K\x01\x01\x00D\x00\x07\x04\xec>\xfa\xacW\x80':'diamond',
    b'K\x01\x01\x00D\x00\x07\x04\xe6>\xfa\xacW\x80':'wood',
    b'K\x01\x01\x00D\x00\x07\x04\xf0@\xfa\xacW\x80':'grass',
    b'K\x01\x01\x00D\x00\x07\x04\xdf>\xfa\xacW\x80':'plane',
    b'K\x01\x01\x00D\x00\x07\x04\xcd>\xfa\xacW\x80':'flower'
    }

while True:
    x, y, z = mc.player.getPos()
    card_data = pn532.read_mifare().get_data()
    trans = bytes(card_data)

    if trans in NFC_Tag:
        constructor(NFC_Tag.get(trans))
        
    sleep(1)