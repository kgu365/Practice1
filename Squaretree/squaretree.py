from point import Point
from rectangle import Rectangle
import math
class SquareTree:
	def __init__(self):
		self.pointset = []
		self.set = set()

	def is_empty(self):
		if len(self.pointset) == 0:
			return True

		else:
			return False	
			

	def get_size(self):
		return len(self.pointset)

	def add(self, p):
		if p in self.set:
			print("already in set")
			
			
		else:
			self.pointset.append(p)
			self.set.add(p)
			print("add successful")

	def contains(self, p):
		if p in self.set:
			return True

		else:
			return False

	def range(self, rectangle):
	 	# use rectangle valid point to get list of points in the rectangle range
	 	vp_list = []
	 	for i in self.pointset:
	 		if rectangle.valid_point(i):
	 			vp_list.append(i)

	 	
	 	return vp_list


	def nearest(self, p):

		if len(self.pointset) == 0:
			return None
		cur_min = float('inf')
		output = None
		for i in self.pointset:
			if i == p:
				continue
			s_distance = ((p.x - i.x) ** 2) + ((p.y - i.y) ** 2)	
			distance = math.sqrt(s_distance)
			if distance < cur_min:
				cur_min = distance
				output = i
				
		return output


if __name__ == '__main__':
	t = SquareTree()
	x = Point(0.7, 0.1)
	print(t.nearest(x))
	#isempty
	print("is_empty tests and add")
	if t.is_empty() == True:
		print("Passed")
	else:
		print("Failed")	

	a = Point(.7, .2)
	b = Point(0, 4)
	c = Point(.2, .3)
	d = Point(.4, .7)
	e = Point(.9, .6)
	f = Point(.66, .66)
	g = Point(.5, .5)
	h = Point(8, 8)
	print(t.add(a))
	print(t.add(a))
	print(t.add(b))
	print(t.add(c))
	print(t.add(d))
	print(t.add(g))
	if t.is_empty() == False:
		print("Passed")
	else:
		print("Failed")	

	
	# get_size	
	print(t.get_size())
	if t.get_size() == 5:
		print("Passed")
	else:
		print("Failed")
	t.add(e)
	print(t.get_size())	
	if t.get_size() == 6:
		print("Passed")
	else:
		print("Failed")	
	t.add(f)	
	print(t.get_size())
	if t.get_size() == 7:
		print("Passed")
	else:
		print("Failed")				



	# contains


	print("does the set contain (.5, .5) " + str(t.contains(g)))
	if t.contains(g) == True:
		print("Passed")
	else:
		print("False")	
	print("does the set contain (.9, .6) " + str(t.contains(e)))
	if t.contains(e) == True:
		print("Passed")
	else:
		print("False")	
	print("does the set contain (.9, .6) " + str(t.contains(h)))
	if t.contains(h) == False:
		print("Passed")
	else:
		print("False")	

	#range

	s_rectangle = Rectangle(0,4,0,5)
	print(len(t.range(s_rectangle)))


	if (len(t.range(s_rectangle))) == 7:
		print("Passed")
	else:
		print("Failed")	

	for i in t.range(s_rectangle):
		print(str(i))	

	for i in range(6,100):
		j = Point(i,i)
		t.add(j)

		
	print(len(t.range(s_rectangle)))
	if (len(t.range(s_rectangle))) == 7:
		print("Passed")
	else:
		print("Failed")	
	for i in t.range(s_rectangle):
		print(str(i))	

	
	
	# print(t.range(s_rectangle)) #added 6 elements one is repeated so pointset holds 5 - point b is out of range so vp_list holds 4 objects
	

	#nearest point
	print("Nearest Point Is " + str(t.nearest(g)))
	x = Point(0.7, 0.1)
	print("Nearest Point Is " + str(t.nearest(x)))
	z = Point(0.5, 0.5)
	print("Nearest Point Is " + str(t.nearest(z)))
	y = Point(30, 30)
	print("Nearest Point Is " + str(t.nearest(y)))



