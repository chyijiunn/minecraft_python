from mcpi.minecraft import Minecraft
mc = Minecraft.create()                          
x, y, z = mc.player.getPos()        #讀取玩家所在座標，傳給x(東西向),y（上下方）,z（南北向）
mc.player.setPos(x,y+20,z)        #設定位置垂直往上20單位。若亦要往東北方移動20單位應如何修正呢？