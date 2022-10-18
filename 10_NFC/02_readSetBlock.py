from py532lib.i2c import *
from py532lib.frame import *
from py532lib.constants import *
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
pn532 = Pn532_i2c()
pn532.SAMconfigure()

def setblockNFC(blocktype):
    mc.setBlock(x, y , z ,blocktype)
    mc.player.setPos(x,y+1,z)

diamond = b'K\x01\x01\x00D\x00\x07\x04\xec>\xfa\xacW\x80'
wood = b'K\x01\x01\x00D\x00\x07\x04\xe6>\xfa\xacW\x80'
grass = b'K\x01\x01\x00D\x00\x07\x04\xf0@\xfa\xacW\x80'

while True:
    x, y, z = mc.player.getPos()
    card_data = pn532.read_mifare().get_data()
    trans = bytes(card_data)
    
    if trans == diamond:
        setblockNFC(56)
    elif trans == wood:
        setblockNFC(17)
    elif trans == grass:
        setblockNFC(2)

    sleep(0.1)