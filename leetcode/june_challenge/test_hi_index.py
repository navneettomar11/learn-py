import unittest
from .h_index_ii import h_index

class HIndexText(unittest.TestCase):

    def test_h_idex(self):
        h_index([3,0,6,1,5])
