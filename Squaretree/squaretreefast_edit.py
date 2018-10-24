from pointfast import Point
from rectangle import Rectangle
import math

# Darek - Remove all the line spaces. 
# Darek - Remove all the print statements.
class SquareTree:
	def __init__(self):
		self.root = None
		self.size = 0	

	def is_empty(self):
		if self.root is None:
			return True

		else:
			return False

	def get_size(self):
		return self.size	

	def add(self, p):
		if self.root is None:
			self.root = p
			self.size += 1
		def helper(self, root, rootval, pval, level):
			if pval > rootval:
				if root.right is None:
					root.right = p
					self.size += 1			
				else: 
					if level % 2 != 0:
						helper(self, root.right,root.right.y, p.y, level + 1)
					else:
						helper(self, root.right, root.right.x, p.x, level + 1)	 
			if pval < rootval:
				if root.left is None:
					root.left = p
					self.size += 1		
				else: 
					if level % 2 != 0:
						helper(self, root.left, root.left.y, p.y, level + 1)
					else:
						helper(self, root.left, root.left.x, p.x, level + 1)							
		helper(self, self.root, self.root.x, p.x, 1)
		
	def inorder(self):
		def helper(self,root):

			if root:
				helper(self, root.left)
				print((root.x, root.y))
				helper(self, root.right)

		helper(self, self.root)		

	def contains(self, p):
		if self.root == p:
			return True
		output = [0]	
		def helper(self, root, rootval, pval, level):
			if root == p:
				print(root.x,root.y)
				output[0] = 1
				return
			if pval > rootval:
				if root.right is None:
					return		
				else:
					if level % 2 != 0:
						helper(self, root.right, root.right.y, p.y, level + 1)
					else:
						helper(self, root.right, root.right.x, p.x, level + 1)				 
			if pval < rootval:
				if root.left is None:
					return 		
				else: 
					if level % 2 != 0:
						helper(self, root.left, root.left.y, p.y, level + 1)
					else:
						helper(self, root.left, root.left.x, p.x, level + 1)			
		helper(self, self.root, self.root.x, p.x, 1)
		print(output)
		if output[0] == 1:
			return True
		else:
			return False	

	def range(self, rectangle):
		vp_list = []
		def helper(self, root, level, x):
			if rectangle.valid_point(root):
				vp_list.append(root)
			if level % 2 != 0:
				c = Rectangle(x.xmin, x.xmax, x.ymin, root.y)
				d = Rectangle(x.xmin, x.xmax, root.y, x.ymax)
				if rectangle.r_intersects(c) and root.left:
					helper(self, root.left, level + 1, c)
				if rectangle.r_intersects(d) and root.right:
					helper(self, root.right, level + 1, d)
			else:
				c = Rectangle(x.xmin, root.x, x.ymin, x.ymax)
				d = Rectangle(root.x, x.xmax, x.ymin, x.ymax)
				if rectangle.r_intersects(c) and root.left:
					helper(self, root.left, level + 1, c)
				if rectangle.r_intersects(d) and root.right:
					helper(self, root.right, level + 1, d)	
		helper(self, self.root, 0, Rectangle(0,1,0,1))
		for i in vp_list:
			print (i.x,i.y)
		return vp_list					

	def nearest(self, p):
		cur_min = 1000
		output = None
		def helper(self, root, level, c):
			nonlocal cur_min
			nonlocal output
			distance = math.sqrt(((p.x - root.x) ** 2) + ((p.y - root.y) ** 2))	
			if level % 2 != 0:
				x = Rectangle(c.xmin, c.xmax, root.y, c.ymax)
				if cur_min > x.distance_to_point(p):	
					if cur_min > distance:
						cur_min = distance
						output = root
					if root.right:
						helper(self, root.right, level + 1, x)
				y = Rectangle(c.xmin,c.xmax,c.ymin,root.y)
				if cur_min > y.distance_to_point(p):
					if cur_min > distance:
						cur_min = distance
						output = root
					if root.left:	
						helper(self, root.left, level + 1, y)
			else:
				x = Rectangle(root.x, c.xmax, c.ymin, c.ymax)
				if cur_min > x.distance_to_point(p):
					if cur_min > distance:
						cur_min = distance
						output = root
					if root.right:	
						helper(self, root.right, level + 1, x)
				y = Rectangle(c.xmin,root.x,c.ymin,c.ymax)
				if cur_min > y.distance_to_point(p):
					if cur_min > distance:
						cur_min = distance
						output = root
					if root.left:
						helper(self, root.left, level + 1, y)	
		helper(self, self.root, 0, Rectangle(0,1,0,1) )
		return output


if __name__ == '__main__':
	t = SquareTree()
	# print(t.nearest(x))
	#isempty
	print("is_empty tests and add")
	if t.is_empty() == True:
		print("Passed")
	else:
		print("Failed")	
	# Darek - can you make this into a for loop?
	a = Point(.7, .2)
	b = Point(0.5, 0.4)
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
	print("does the set contain (8, 8) " + str(t.contains(h)))
	if t.contains(h) == False:
		print("Passed")
	else:
		print("False")

	#range
	print("range tests")
	print(t.get_size())
	print("Test 1")
	s_rectangle = Rectangle(0.1,0.6,0,1)
	print(t.inorder())
	t.range(s_rectangle)

	print("Test 2")
	a_rectangle = Rectangle(0.5, 0.9,0.5,1)
	t.range(a_rectangle)
	
	# print(t.range(s_rectangle)) #added 6 elements one is repeated so pointset holds 5 - point b is out of range so vp_list holds 4 objects
	
	# nearest point
	# print("Nearest Point Is " + str(t.nearest(g)))
	x = Point(0.7, 0.1)
	print("Nearest Point Is " + str(t.nearest(x)))
	z = Point(0.5, 0.5)
	print("Nearest Point Is " + str(t.nearest(z)))
	o = Point(0.9,0.5)
	print("Nearest Point Is " + str(t.nearest(o)))
	y = Point(0.21, 0.3)
	print("Nearest Point Is " + str(t.nearest(y)))
	n = Point(0.9, 0.8)
	print("Nearest Point Is " + str(t.nearest(n)))
	print(t.get_size())

	for i in range(1,10):
		n = Point(i/10, i/10)
		m = Point(i/10, 0.9)
		print("Nearest Point Is " + str(t.nearest(n)))
		print("Nearest Point Is " + str(t.nearest(m)))

