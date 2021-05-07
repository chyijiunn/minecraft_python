# 'w' = write , 'a' = append , 'r' = read , 'r+'= read & write
locationFile = open('location','w')
locationFile.write('My 1st time to write a file')
locationFile.close()