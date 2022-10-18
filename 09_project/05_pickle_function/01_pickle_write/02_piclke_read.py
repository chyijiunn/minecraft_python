import pickle
File = open("file","rb")
location = pickle.load(File)
print(location)