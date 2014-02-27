import unittest
from pickler import list_pickler, unpickler

class PickleTests(unittest.TestCase):

    def setUp(self):
        
    def test_original_list_same_as_unpickled_list(self):
        list_pickler(self.file, self.pickle_list)
        unpickled_list = unpickler(self.file)
        self.assertEqual(self.pickle_list, unpickled_list)

    def tearDown(self):                   
