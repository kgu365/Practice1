# Helper Node class
class Node:
	def __init__(self, value = None):
		self.value = value
		self.next = None
		self.prev = None

class Deque:
	# initialize an empty deque
	def __init__(self):
		self.front = None
		self.end = None
		self.size = 0
	# is the deque empty?
	# returns a Boolean 
	def isEmpty(self):
		if self.front is None and self.end is None:
			return True
		else:
			return False	


	# returns the number of items in the deque
	def get_size(self):
		return self.size

	# inserts item to the front of the deque
	def addFirst(self, item):
		
		if self.front is None and self.end is None:

			a = Node(item)
			self.front = a
			self.end = a


		
		else:

			a = Node(item)
			temp = self.front
			self.front = a 
			self.front.next = temp


			if temp.next is None:
				self.end = temp
				self.end.prev = self.front


		self.size += 1		
	# inserts item at the end of the deque
	def addLast(self, item):
		
		if self.front is None and self.end is None:
			b = Node(item)
			self.end = b
			self.front = b
		else:
			
			b = Node(item)
			self.end.next = b
			temp = self.end
			self.end = self.end.next
			self.end.prev = temp

			if temp.prev is None:
				self.front = temp


		self.size += 1		

	# delete and return the item at the front of the deque 
	def removeFirst(self):
		
		if self.size == 0:
			self.front = None
			self.end = None
			
			return self.front
		else:
			
			if self.size == 1:
				r = self.front
				self.front = None
				self.end = None
				self.size -= 1
				return r.value

			else:
				r = self.front
				temp = self.front.next
				self.front.next = None
				self.front = temp
				self.front.prev = None
				self.size -= 1
				return r.value


		



	# delete and return the item at the end of the deque
	def removeLast(self):

		if self.size == 0:
			self.front = None
			self.end = None
			return self.end
		else:
			
			if self.size == 1:
				r = self.end
				self.front = None
				self.end = None
				self.size -= 1
				return r.value

			else:
				r = self.end
				temp = self.end.prev
				self.end.prev = None
				self.end = temp
				self.end.next = None
				self.size -= 1
				return r.value

				

	
	# return an iterator over items in order from front to end (can be a list in Python)
	def iterator(self):
		i_list = []
		if self.size == 0:
			return i_list
		def helper(self, root):
			while root:
				i_list.append(root.value)
				root = root.next

		helper(self,self.front)
		return i_list
		




# main method , put unit tests here.
if __name__ == "__main__":
	t = Deque()
	print(t.isEmpty())
	print(t.get_size())
	t.addFirst(3)
	t.addFirst(4)
	t.addFirst(5)
	t.addLast(2)
	t.addLast(1)

	print(t.isEmpty())
	print(t.get_size())

	print(t.iterator())

	t.removeLast()
	t.removeFirst()
	t.removeLast()
	

	print(t.iterator())
	print(t.get_size())
	print(t.isEmpty())


	t.addLast(2)
	t.addFirst(1)

	print(t.iterator())
	print(t.get_size())
	print(t.isEmpty())
