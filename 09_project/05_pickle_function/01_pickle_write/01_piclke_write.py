import pickle
location = {'home':'try','cave':'my','bed':'hears'}
File = open("file","wb")
pickle.dump(location,File)