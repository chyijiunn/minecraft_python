from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
File = open('tiles','r')	#讀取tiles檔案
for line in File:		#對檔案當中的每一行進行處理
    x1 , y1 , z1 , brick , dat = line.split(',')	#將資料讀出後，依照','進行資料分隔
    mc.setBlock(x+int(x1) , y+int(y1) , z+int(z1) , int(brick) ,int(dat))#放磚塊時，分別讀取 x ,y ,z ,brick , data
File.close