import pickle
location = {'home':'try','cave':'my','bed':'hears'}
File = open("file.txt","wb")
pickle.dump(location,File)