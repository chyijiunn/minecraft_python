from mcpi.minecraft import Minecraft
mc = Minecraft.create()
places = {'entry_maze': (-21,8,-82),
          'check': (-20,-7,-84),
          'castle_entry': (-11.7,-32,-91.8),
          'castle': (-11.7,-32,-78.9),}
x ,y, z = places['entry_maze']
mc.player.setPos(x, y, z)