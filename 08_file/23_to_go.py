File = open('goTo','a')
List = ''
Item = input ("Enter location like : 'where': (x,y,z),:")
while Item != 'exit':
    List = List + Item +'\n'
    Item = input ("'where': (x,y,z),")
File.write(List)
File.close()