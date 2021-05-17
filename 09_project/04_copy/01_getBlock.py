from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
block = mc.getBlockWithData(x,y-1,z)	#取得腳下磚塊編號以及參數
print(block)				#列印出磚塊編號和參數