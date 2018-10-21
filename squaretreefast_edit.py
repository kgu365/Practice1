from pointfast import Point
from rectangle import Rectangle
import math

# Darek- In general reduce the number of line spacses.
class SquareTree:
	def __init__(self):
		self.root = None
		self.size = 0	

	def is_empty(self):
		if self.root is None:
			return True

		else:
			return False	
			
	# Darek - this method should be constant time
	def get_size(self):
		return self.size
		
		

	def add(self, p):

		if self.root is None:
			self.root = p
			self.size += 1

		# Darek - Can you do reduce the number of conditionals here?
		def helper(self, root, p, level):
			
			if level % 2 != 0:

				if p.x > root.x:
					if root.right is None:
						root.right = p
						self.size += 1	

					else: 
						helper(self, root.right, p, level + 1) 

				if p.x < root.x:
					if root.left is None:
						root.left = p
						self.size += 1
						
					else: 
						helper(self, root.left, p, level + 1)		
					
			else: 
				if p.y > root.y:
					if root.right is None:
						root.right = p
						self.size += 1
						

					else:
						helper(self, root.right, p, level + 1)

				if p.y < root.y:
					if root.left is None:
						root.left = p
						self.size += 1

					else: 
						helper(self, root.left, p, level + 1)				
		helper(self, self.root, p, 1)
		
	def inorder(self):
		def helper(self,root):

			if root:
				helper(self, root.left)
				print((root.x, root.y))
				helper(self, root.right)

		helper(self, self.root)		


	# Darek - can you reduce the number of conditionals?
	def contains(self, p):
		if self.root == p:
			return True
		output = [0]	
		def helper(self, root, p, level):
			if level % 2 != 0:
				if root == p:
					print(root.x,root.y)
					output[0] = 1
					return

				if p.x > root.x:
					if root.right is None:
						return
						

					else: 
						helper(self, root.right, p, level + 1) 

				if p.x < root.x:
					if root.left is None:
						return 
						
					else: 
						helper(self, root.left, p, level + 1)		
					
			else: 
				if root == p:
					print(root.x, root.y)
					output[0] = 1
					return 
				
				if p.y > root.y:
					if root.right is None:
						return 
						print(root.right)

					else:
						print("recursion")
						helper(self, root.right, p, level + 1)

				if p.y < root.y:
					if root.left is None:
						root.left = p
						print(root.left)

					else: 
						print("recursion")
						helper(self, root.left, p, level + 1)	
			
			

		helper(self, self.root, p, 1)
		print(output)
		if output[0] == 1:
			return True
		else:
			return False	

	# Darek - can you comibine helperright and helperleft into one function? 
	# Darek - once you do the above, can you reduce the number of conditionals 
	# in helperright.
	def range(self, rectangle):
		# use rectangle valid point to get list of points in the rectangle range
		vp_list = []
		if rectangle.valid_point(self.root):
			vp_list.append(self.root)


		c = Rectangle(rectangle.xmin,self.root.x,rectangle.ymin,rectangle.ymax)
		d = Rectangle(self.root.x,rectangle.xmax,rectangle.ymin,rectangle.ymax)

		def helperleft(self, root, level, c):

			if level % 2 != 0:

				if c.valid_point(root):
					vp_list.append(root)

					if root.left:
						x = c
						x = Rectangle(c.xmin,c.xmax,c.ymin,c.ymax)
						print(x)
						print(c)
						x.ymax = root.y
						print(x)
						print(c)
						helperleft(self, root.left, level + 1, x)	
					if root.right:
						x = c
						x = Rectangle(c.xmin, c.xmax, c.ymin, c.ymax)
						x.ymin = root.y	
						
						helperright(self, root.right, level + 1, x)
				else:
					return		

			else:

				if c.valid_point(root):
					vp_list.append(root)

					if root.left:
						x = c
						x = Rectangle(c.xmin,c.xmax,c.ymin,c.ymax)
						x.xmax = root.x
						helperleft(self, root.left, level + 1, x)	
					if root.right:
						x = c
						x = Rectangle(c.xmin,c.xmax,c.ymin,c.ymax)
						x.xmin = root.x	
						helperright(self, root.right, level + 1, x)
				else:
					return	

		def helperright(self, root, level, d):
			if level % 2 != 0:

				if d.valid_point(root):
					vp_list.append(root)

					if root.left:
						y = d
						y = Rectangle(d.xmin,d.xmax,d.ymin,d.ymax)
						y.ymax = root.y
						helperleft(self, root.left, level + 1, y)	
					if root.right:
						y = d
						y = Rectangle(d.xmin,d.xmax,d.ymin,d.ymax)
						y.ymin = root.y	
						helperright(self, root.right, level + 1, y)

			else:

				if d.valid_point(root):
					vp_list.append(root)

					if root.left:
						y = d
						y = Rectangle(d.xmin,d.xmax,d.ymin,d.ymax)
						y.xmax = root.x
						helperleft(self, root.left, level + 1, y)	
					if root.right:
						y = d
						y = Rectangle(d.xmin,d.xmax,d.ymin,d.ymax)
						y.xmin = root.x	

						helperright(self, root.right, level + 1, y)
				else:
					return					

		#left x becomes xmax changes
		#right xmin changes
		#left y becomes ymax
		#right y becomes ymin 
		helperleft(self, self.root.left, 1, c)
		helperright(self, self.root.right, 1, d)

		# print(vp_list)
		# print(len(vp_list))
		# for i in vp_list:
		# 	print (i.x,i.y)
		return vp_list				

		
	#  	return vp_list
	# Darek - can you comibine helperright and helperleft into one function? 
	# Darek - once you do the above, can you reduce the number of conditionals 
	# in helperright.
	def nearest(self, p):

		s_distance = ((p.x - self.root.x) ** 2) + ((p.y - self.root.y) ** 2)	
		distance = math.sqrt(s_distance)
		cur_min = distance
		output = self.root
		c = Rectangle(0,self.root.x,0,1)
		d = Rectangle(self.root.x,1,0,1)
		
		def helperleft(self, root, level, c):
			nonlocal cur_min
			nonlocal output

			if level % 2 != 0:

				x = Rectangle(c.xmin, c.xmax, c.ymin, c.ymax)
				x.ymin = root.y	
				if cur_min > x.distance_to_point(p):
					s_distance = ((p.x - root.x) ** 2) + ((p.y - root.y) ** 2)
					distance = math.sqrt(s_distance)
					if cur_min > distance:
						cur_min = distance
						output = root
					if root.right:
						
						helperleft(self, root.right, level + 1, x)


				
				y = Rectangle(c.xmin,c.xmax,c.ymin,c.ymax)
				y.ymax = root.y
				
				if cur_min > y.distance_to_point(p):
					s_distance = ((p.x - root.x) ** 2) + ((p.y - root.y) ** 2)
					distance = math.sqrt(s_distance)
					if cur_min > distance:
						cur_min = distance
						output = root
					if root.left:	
						helperleft(self, root.left, level + 1, y)
			else:

				x = Rectangle(c.xmin, c.xmax, c.ymin, c.ymax)
				x.xmin = root.x	
				if cur_min > x.distance_to_point(p):
					s_distance = ((p.x - root.x) ** 2) + ((p.y - root.y) ** 2)
					distance = math.sqrt(s_distance)
					if cur_min > distance:
						cur_min = distance
						output = root
					if root.right:
						
						helperleft(self, root.right, level + 1, x)

				
				y = Rectangle(c.xmin,c.xmax,c.ymin,c.ymax)
				x.xmax = root.x
				
				if cur_min > y.distance_to_point(p):
					s_distance = ((p.x - root.x) ** 2) + ((p.y - root.y) ** 2)
					distance = math.sqrt(s_distance)
					if cur_min > distance:
						cur_min = distance
						output = root
					if root.left:
						
						helperleft(self, root.left, level + 1, y)	


		def helperright(self, root, level, d):
			nonlocal cur_min
			nonlocal output

			if level % 2 != 0:

				x = Rectangle(d.xmin, d.xmax, d.ymin, d.ymax)
				x.ymin = root.y	
				if cur_min > x.distance_to_point(p):
					s_distance = ((p.x - root.x) ** 2) + ((p.y - root.y) ** 2)
					distance = math.sqrt(s_distance)
					if cur_min > distance:
						cur_min = distance
						output = root
					if root.right:
						
						helperright(self, root.right, level + 1, x)


				
				y = Rectangle(d.xmin,d.xmax,d.ymin,d.ymax)
				y.ymax = root.y
				
				if cur_min > y.distance_to_point(p):
					s_distance = ((p.x - root.x) ** 2) + ((p.y - root.y) ** 2)
					distance = math.sqrt(s_distance)
					if cur_min > distance:
						cur_min = distance
						output = root
					if root.left:	
						helperright(self, root.left, level + 1, y)
			else:

				x = Rectangle(d.xmin, d.xmax, d.ymin, d.ymax)
				x.xmin = root.x	
				if cur_min > x.distance_to_point(p):
					s_distance = ((p.x - root.x) ** 2) + ((p.y - root.y) ** 2)
					distance = math.sqrt(s_distance)
					if cur_min > distance:
						cur_min = distance
						output = root
					if root.right:
						
						helperright(self, root.right, level + 1, x)

				
				y = Rectangle(d.xmin,d.xmax,d.ymin,d.ymax)
				x.xmax = root.x
				
				if cur_min > y.distance_to_point(p):
					s_distance = ((p.x - root.x) ** 2) + ((p.y - root.y) ** 2)
					distance = math.sqrt(s_distance)
					if cur_min > distance:
						cur_min = distance
						output = root
					if root.left:
						
						helperright(self, root.left, level + 1, y)


		helperleft(self, self.root.left, 1, c)
		helperright(self, self.root.right, 1, d)		
		return output


if __name__ == '__main__':
	t = SquareTree()
	x = Point(0.7, 0.1)
	# print(t.nearest(x))
	#isempty
	print("is_empty tests and add")
	if t.is_empty() == True:
		print("Passed")
	else:
		print("Failed")	
	# Darek - can you make this into a for loop?
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
	s_rectangle = Rectangle(0,50,0,50)
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
	if (len(t.range(s_rectangle))) == 52:
		print("Passed")
	else:
		print("Failed")	
	for i in t.range(s_rectangle):
		print(str(i))	
	
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

