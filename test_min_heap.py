import unittest
from min_heap import MinHeap

class TestMinHeap(unittest.Testcase):
	def test_init(self):
		x = MinHeap()
		self.assertTrue(x.size() == 0)



if __name__ == '__main__':
	unittest.main()
