from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
mc.setBlock(x, y, z,46,1) #於所在位置的東方一格處，放一個 1 號磚塊，且要懸浮，記得選一個磚塊編號
'''
0	空氣	
1	石頭	
2	草	
3	污垢	
4	鵝卵石	
5	木板
'''