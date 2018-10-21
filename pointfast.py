import math
import random
class Point:
	def __init__(self, x,y):
		self.x = x
		self.y = y
		self.left = None
		self.right = None


	# Constructor initializes a point (x,y).
	# Requires an x,y coordinate pair

	# function that returns the x-coordinate
	def get_x(self):
		return self.x
		
	# function that returns y-coordinate
	def get_y(self):
		return self.y
		
	# function that returns square of distance between this point and another point
	def get_distance(self, new_point):
		x1 = self.x
		y1 = self.y
		x2 = new_point.x
		y2 = new_point.y
		slope_t = y2 - y1
		slope_b = x2 - x1

		square_distance = (slope_t ** 2) + (slope_b ** 2)
		return math.sqrt(square_distance)
		
	# write a compare_to method 
	# compare by y-coordinate, breaking ties by x-coordinate
	def compare_to(self, cpoint):
		if self.y > cpoint.y:
			return 1
		elif self.y < cpoint.y:
			return -1	
		elif self.y == cpoint.y:
			if self.x > cpoint.x:
				return 1
			elif self.x < cpoint.x:
				return -1
			else:
				return 0		
				

	# write a to_string method 
	# returns a string of the point like so
	# (x, y)
	def __str__(self):
		return str((self.get_x(), self.get_y()))




# main method you can use to test
if __name__ == '__main__':

	points = []
	for num in range(50):
		x = random.randint(0,50) / 10
		y = random.randint(0,50) / 10
		item = Point(x,y)
		points.append(item)
	#object creation test cases

	for i in points:
		if i.x == i.x and i.y == i.y:
		 	print("Object Creation Successful")
		else:
			print("Failed Object Creation")	 

	
	#get coordinate test cases
	for i in points:
		print(i.get_x())
		print(i.get_y())


	#get_distance_testcases
	for i in range(len(points) - 1):
		print(points[i].get_distance(points[i + 1]))


	#compare_to_testcases
	for i in range(len(points) - 1):
		print(points[i].compare_to(points[i + 1]))






