from py532lib.i2c import *
from py532lib.frame import *
from py532lib.constants import *
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
pn532 = Pn532_i2c()
pn532.SAMconfigure()

data = {
    b'K\x01\x01\x00D\x00\x07\x04\xec>\xfa\xacW\x80':'diamond',
    b'K\x01\x01\x00D\x00\x07\x04\xe6>\xfa\xacW\x80':'wood',
    b'K\x01\x01\x00D\x00\x07\x04\xf0@\xfa\xacW\x80':'grass',
    b'K\x01\x01\x00D\x00\x07\x04\xdf>\xfa\xacW\x80':'plane',
    b'K\x01\x01\x00D\x00\x07\x04\xcd>\xfa\xacW\x80':'flower'
    }

while True:
    card_data = pn532.read_mifare().get_data()
    trans = bytes(card_data)

    if trans in data:
        print(data.get(trans))
    else:
        print('.')
        
        
    sleep(1)