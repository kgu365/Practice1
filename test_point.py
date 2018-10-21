from point import Point
import unittest
import random
import math

class TestPoint(unittest.TestCase):
	def test_getxandy(self):
		points = []
		nums = []
		LIMIT = 50
		for _ in range(LIMIT):
			numx = (random.random()-.5)*10
			numy = (random.random()-.5)*10
			points.append(Point(numx,numy))
			nums.append((numx,numy))
		for (x,y),point in zip(nums,points):
			self.assertEqual(x,point.get_x())
			self.assertEqual(y,point.get_y())

	def test_dist(self):
		LIMIT = 50
		prev = None
		for _ in range(LIMIT):
			numx = (random.random()-.5)*10
			numy = (random.random()-.5)*10
			cur = Point(numx,numy)
			if prev != None:
				d = math.sqrt(((prev.x - cur.x)**2 + (prev.y - cur.y)**2))
				self.assertTrue(abs(prev.get_distance(cur) - d) < 0.00001)
			prev = cur

	def test_cmp(self):
		LIMIT = 50
		prev = None

		samex = (random.random()-.5)*10
		samey = (random.random()-.5)*10
		p1 = Point(samex,samey)
		p2 = Point(samex,samey)
		self.assertTrue(0 == p1.compare_to(p2))

		for _ in range(LIMIT):
			numx = random.randint(-1,1)
			numy = random.randint(0,1)
			cur = Point(numx,numy)
			if prev != None:
				val = 0
				if cur.y > prev.y:
					val = 1
				elif cur.y < prev.y:
					val = -1
				else:
					if cur.x > prev.x:
						val = 1
					elif cur.x < prev.x:
						val = -1
				self.assertTrue(abs(cur.compare_to(prev) - val) < 0.00001)
			prev = cur
	def test_str(self):
		LIMIT = 50
		prev = None
		for _ in range(LIMIT):
			numx = random.randint(-100,100)
			numy = random.randint(-100,100)
			p = Point(numx,numy)
			s = "(" + str(p.x) + ", " + str(p.y) + ")";
			self.assertEqual(str(p), s)

if __name__ == '__main__':
	unittest.main()