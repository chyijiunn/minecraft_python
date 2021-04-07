from mcpi.minecraft import Minecraft #引入Minecraft 
mc = Minecraft.create()                             #縮寫為mc
mc.player.setpos(0.5,20,0.5)                   #穿梭去的座標，注意 setPos 要大寫的部份