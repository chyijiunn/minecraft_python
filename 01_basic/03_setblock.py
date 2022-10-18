from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
mc.setBlock(x, y, z, 磚塊編號) #於所在東方一格處，放個懸浮磚塊，選一個磚塊編號
'''
0	空氣	
1	石頭	
2	草	
3	污垢	
4	鵝卵石	
5	木板
'''