locationFile = open('location','r')
#print(locationFile.read()) # read all
print(locationFile.readline()) # read line
print(locationFile.readline()) 
locationFile.close()