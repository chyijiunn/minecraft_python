import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(12,GPIO.IN)

def hodocan(x,y,z,block,sleep_time,attack_range,start_point):
    for i in range(attack_range):
        mc.setBlock(x,y,z+i+start_point,block)
        mc.setBlock(x+i+start_point,y,z,block)
        mc.setBlock(x-i-start_point,y,z,block)
        mc.setBlock(x,y,z-i-start_point,block)
        sleep(sleep_time)
        mc.setBlock(x,y,z+i+1+start_point,block)
        mc.setBlock(x+i+1+start_point,y,z,block)
        mc.setBlock(x,y,z-i-1-start_point,block)
        mc.setBlock(x-i-1-start_point,y,z,block)
        sleep(sleep_time)
        mc.setBlock(x,y,z+i+start_point,0)
        mc.setBlock(x+i+start_point,y,z,0)
        mc.setBlock(x,y,z-i-start_point,0)
        mc.setBlock(x-i-start_point,y,z,0)
        sleep(sleep_time)
    mc.setBlock(x,y,z+attack_range+start_point,0)
    mc.setBlock(x+attack_range+start_point,y,z,0)
    mc.setBlock(x,y,z-attack_range-start_point,0)
    mc.setBlock(x-attack_range-start_point,y,z,0)

while True:
    input_value = GPIO.input(12)
    if input_value == False:
        print('fire!')
        x,y,z = mc.player.getPos()
        hodocan(x,y,z,10,0.05,10,2)
        while input_value == False:
            input_value = GPIO.input(12)
