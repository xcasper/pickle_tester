import unittest, os, shutil
import time
from pickler import list_pickler, unpickler

class PickleTests(unittest.TestCase):

    def setUp(self):
        self.pickle_list = [1,2,3,'a','b','c']
        self.path = './pickle_temp'
        os.makedirs(self.path)
        self.file = os.path.join(self.path, 'list.pk1') #taken from solution - fixed file creation issue
        print "Setup is complete..."

    def test_original_list_same_as_unpickled_list(self):
        list_pickler(self.file, self.pickle_list)
        unpickled_list = unpickler(self.file)
        self.assertEqual(self.pickle_list, unpickled_list)
        print "Test complete..."

    def tearDown(self):
                                 #copied from solution github
                                 #didnt know how to do teardown
        shutil.rmtree(self.path) #shutil.rmtree deletes a dir and all contents
        
