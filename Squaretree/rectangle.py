
from point import Point
import math
class Rectangle:

	# initialize a rectangle object with 4 arguments
	# xmin, xmax, ymin, ymax

	def __init__(self, xmin, xmax, ymin, ymax):
		self.xmin = min(xmin,xmax)
		self.xmax = max(xmax, xmin)
		self.ymin = min(ymin,ymax)
		self.ymax = max(ymax, ymin)


	# function that returns the min x-coordinate

	def get_xmin(self):
		return self.xmin

	# function that returns the max x-coordinate

	def get_xmax(self):
		return self.xmax

	# function that returns the min y-coordinate

	def get_ymin(self):
		return self.ymin

	# function that returns the max y-coordinate

	def get_ymax(self):
		return self.ymax

	# function that returns a boolean indicating if point p
	# lies within this rectangle. (either inside or on the boundary)
	def valid_point(self, p):
		if p.x < self.xmin or p.x > self.xmax or p.y < self.ymin or p.y > self.ymax:
			return False
		else:
			return True	


	# function that returns a boolean indicating if this rectangle intersects 
	# another rectangle which is passed in as an argument (at one or more points?)

	def r_intersects(self, crectangle):
		# If any corner of the crectangle is inside the self rectangle then return True, otherwise return False
		corners = []
		corner1 = Point(crectangle.xmin,crectangle.ymin)
		corners.append(corner1)
		corner2 = Point(crectangle.xmax,crectangle.ymin)
		corners.append(corner2)
		corner3 = Point(crectangle.xmin,crectangle.ymax)
		corners.append(corner3)
		corner4 = Point(crectangle.xmax,crectangle.ymax)
		corners.append(corner4)

		

		for i in corners:
			if (i.x >= self.xmin and i.x <= self.xmax):
		
				if (corner1.y >= self.ymin and corner1.y <= self.ymax):
					return True
				
				if corner3.y >= self.ymin and corner3.y <= self.ymax:
					return True	

				if corner1.y <= self.ymin and corner3.y >= self.ymax:
					return True	

		for j in corners:
			if j.y >= self.ymin and j.y <= self.ymax:
				
				if corner1.x >= self.xmin and corner1.x <= self.xmax:
					return True

				if corner2.x >= self.xmin and corner2.x <= self.xmax:
					return True		
				
				if corner1.x <= self.xmin and corner2.x >= self.xmax:
					return True					
					
		if (corner1.x < self.xmin and corner1.y < self.ymin) and (corner4.x > self.xmax and corner4.y > self.ymax):
			return True
		if (self.xmin < corner1.x and self.ymin < corner1.y) and (self.xmax > corner4.x and self.ymax > corner4.y):
			return True

		return False		

	# function called distance_to_point that returns a float 
	# indicating the squared distance from point p to the closest point in 
	# this rectangle. p is a point passed as an argument.

	def distance_to_point(self, p):
		
		# iterate through all the previous poins in the rectangle
		if p.x >= self.xmin and p.x <= self.xmax and p.y >= self.ymin and p.y <= self.ymax:
			return 0

		output = None

		cur_min = float('inf')
		r_point = []
		a = Point(self.xmin,self.ymin)
		r_point.append(a)
		b = Point(self.xmax, self.ymin)
		r_point.append(b)
		c = Point(self.xmin, self.ymax)
		r_point.append(c)
		d = Point(self.xmax, self.ymax)
		r_point.append(d)

		#right bot 
		if p.x > self.xmax and p.y < self.ymin:
			
			output = ((p.y - b.y) ** 2) + ((p.x - b.x) ** 2)
			return output

		#right top	
		if p.x > self.xmax and p.y > self.ymax:
			output = ((p.y - d.y)) ** 2 + ((p.x - d.x) ** 2)	
			return output

		#left bot	
		if p.x < self.xmin and p.y < self.ymin:
			output = ((p.y - a.y) ** 2) + ((p.x - a.x) ** 2)
			return output

		#left top	
		if p.x < self.xmin and p.y > self.ymax:
			output = ((p.y - c.y) ** 2) + ((p.x - c.x) ** 2)
			return output

		if p.x < self.xmin:
			return (p.x - self.xmin) ** 2

		if p.x > self.xmax:
			return (p.x - self.xmax) ** 2	

		if p.y < self.ymin:
			return (p.y - self.ymin) ** 2

		if p.y > self.ymax:
			return (p.y - self.ymax) ** 2		

		






	# function equals returns a boolean indicating if this rectangle equals 
	# that rectangle. that rectangle is a Rectangle passed in as an argument

	def equal_rectangle(self,rectangle):
		if self.xmin == rectangle.xmin and self.xmax == rectangle.xmax and self.ymin == rectangle.ymin and self.ymax == rectangle.ymax:
			return True

		else:
			return False	


	def __str__(self):
		a = self.get_xmin()
		b = self.get_xmax()
		c = self.get_ymin()
		d = self.get_ymax()
		e = (a,b,c,d)
		return str(e) 

# you can put your main method here to test rectangle
if __name__ == '__main__':

	new_rectangle = Rectangle(0,4,0,5)
	comparison_rectangle = Rectangle(4,6,0,1)
	print(new_rectangle)
	print(new_rectangle.get_xmin())

	p = Point(1,2)
	print(new_rectangle.valid_point(p))
	print(new_rectangle.r_intersects(comparison_rectangle))


	# p1 = Point(1,1)	
	# print(new_rectangle.distance_to_point(p1))

	equal_rectangle = Rectangle(-47.15012640518837,30.5430286082209,-3.1242678889508935,49.01437284541317)
	print(new_rectangle.equal_rectangle(equal_rectangle))
	print(new_rectangle.distance_to_point(p))
