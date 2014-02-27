import sys
import pickle

def list_pickler(path, pickle_list):
    f = open(path, 'wb')
    pickle.dump(pickle_list, f)
    f.close()

def unpickler(path):
    f = open(path, 'rb')
    pickle_list = pickle.load(f)
    f.close()
    return pickle_list
