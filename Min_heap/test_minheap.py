import unittest
from min_heap import MinHeap
import time

class TestMinHeap(unittest.TestCase):
	def test_init(self):
		x = MinHeap()
		self.assertTrue(x.size() == 0)

	def test_size_insert(self):
		
		x = MinHeap()
		for i in range(10):
			x.insert(i)

		self.assertEqual(x.size(), 10)
	
	
	def test_size_insert_del(self):
		x = MinHeap()
		for i in range(10):
			x.insert(i)
			
		x.del_min()
		x.del_min()
		self.assertEqual(x.size(), 8)
		

	def test_del_empty(self):
		x = MinHeap()
		self.assertEqual(x.del_min(), None)

			
	# def test__swim(self):
	# 	private
	# def test__sink(self):
	# 	private
	# def test_insert(self):
	# 	no return value
	def test_swim_sink_del_min(self):
		x = MinHeap()
		x.insert(1)
		x.insert(2)
		x.insert(17)
		x.insert(4)
		x.insert(15)
		self.assertEqual(x.size(), 5)
		self.assertEqual(x.del_min(), 1)
		self.assertEqual(x.size(), 4)

		x.insert(7)
		x.insert(8)
		x.insert(6)
		x.insert(9)
		x.insert(10)
		x.insert(0)
		x.insert(5)
		
		self.assertEqual(x.del_min(), 0)
		self.assertEqual(x.del_min(), 2)
		self.assertEqual(x.del_min(), 4)
		self.assertEqual(x.del_min(), 5)
		self.assertEqual(x.del_min(), 6)
		self.assertEqual(x.del_min(), 7)
		self.assertEqual(x.del_min(), 8)
		self.assertEqual(x.del_min(), 9)
		self.assertEqual(x.del_min(), 10)
		self.assertEqual(x.del_min(), 15)
		self.assertEqual(x.del_min(), 17)
		self.assertEqual(x.size(), 0)

	def test_runtime_insert(self):
		print("insert runtime")
		a = []
		b = []
		c = []
		d = []
		time_start = time.time()
		for i in range(0,1000):
			a.append(i)

		time_end = time.time()
		time_run = time_end - time_start
		time_run *= 10000
		print(time_run)

		time_start = time.time()
		for i in range(0,10000):
			b.append(i)

		time_end = time.time()
		time_run = time_end - time_start
		time_run *= 10000
		print(time_run)

		time_start = time.time()
		for i in range(0,100000):
			c.append(i)

		time_end = time.time()
		time_run = time_end - time_start
		time_run *= 10000
		print(time_run)

		time_start = time.time()
		for i in range(0,1000000):
			d.append(i)

		time_end = time.time()
		time_run = time_end - time_start
		time_run *= 10000
		print(time_run)




		x = MinHeap()
		for i in range(1, 1000):
			x.insert(i)
		time_start = time.time()
		x.insert(0)
		time_end = time.time()
		time_run = time_end - time_start
		time_run *= 10000
		t = time_run
		print(time_run)	

		x = MinHeap()
		for i in range(1, 10000):
			x.insert(i)
		time_start = time.time()
		x.insert(0)
		time_end = time.time()
		time_run = time_end - time_start
		time_run *= 10000
		print(time_run)	

		x = MinHeap()
		for i in range(1, 100000):
			x.insert(i)
		time_start = time.time()
		x.insert(0)
		time_end = time.time()
		time_run = time_end - time_start
		time_run *= 10000
		print(time_run)	

		x = MinHeap()
		for i in range(1, 1000000):
			x.insert(i)
		time_start = time.time()
		x.insert(0)
		time_end = time.time()
		time_run = time_end - time_start
		time_run *= 10000
		o = time_run
		print(time_run)	

		self.assertTrue(o < (10 * t))

	def test_runtime_del(self):
		print ("del runtime")
		a = []
		b = []
		c = []
		d = []
		time_start = time.time()
		for i in range(0,1000):
			a.append(i)

		time_end = time.time()
		time_run = time_end - time_start
		time_run *= 10000
		print(time_run)

		time_start = time.time()
		for i in range(0,10000):
			b.append(i)

		time_end = time.time()
		time_run = time_end - time_start
		time_run *= 10000
		print(time_run)

		time_start = time.time()
		for i in range(0,100000):
			c.append(i)

		time_end = time.time()
		time_run = time_end - time_start
		time_run *= 10000
		print(time_run)

		time_start = time.time()
		for i in range(0,1000000):
			d.append(i)

		time_end = time.time()
		time_run = time_end - time_start
		time_run *= 10000
		print(time_run)




		x = MinHeap()
		for i in range(1, 1000):
			x.insert(i)
		time_start = time.time()
		x.del_min()
		time_end = time.time()
		time_run = time_end - time_start
		time_run *= 10000
		t = time_run
		print(time_run)	

		x = MinHeap()
		for i in range(1, 10000):
			x.insert(i)
		time_start = time.time()
		x.del_min()
		time_end = time.time()
		time_run = time_end - time_start
		time_run *= 10000
		print(time_run)	

		x = MinHeap()
		for i in range(1, 100000):
			x.insert(i)
		time_start = time.time()
		x.del_min()
		time_end = time.time()
		time_run = time_end - time_start
		time_run *= 10000
		print(time_run)	

		x = MinHeap()
		for i in range(1, 1000000):
			x.insert(i)
		time_start = time.time()
		x.del_min()
		time_end = time.time()
		time_run = time_end - time_start
		time_run *= 10000
		o = time_run
		print(time_run)	

		self.assertTrue(o < (10*t))










if __name__ == '__main__':
	unittest.main()
