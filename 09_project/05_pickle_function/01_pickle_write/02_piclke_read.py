import pickle
File = open("file.txt","rb")
location = pickle.load(File)
print(location)