class Node:
	def __init__(self, value = None):
		self.value = value
		self.left = None
		self.right = None

	# def get_value(self, root, value):
	# 	if root.value == value:
	# 		return True
	# 	if root.value > value:
	# 		if root.left:
	# 			print("recursion")
	# 			get_value(root.left, value)
	# 		else:
	# 			return False		
					
class BST:
	# initializes an empty BST
	def __init__(self):
		self.root = None

	# inserts the given value into the BST
	def put(self, value):
		node = Node(value)
		if self.root is None:
			self.root = node

		def insert(self, root, node):
			if root.value > node.value:
				if root.left is None:
					print("node added left")
					root.left = node

				else:
					print ("recursion")
					insert(self, root.left, node)

			if root.value < node.value:
				if root.right is None:
					print("node added right")
					root.right = node
				else:
					print("recursion")
					insert(self, root.right, node)					

		insert(self, self.root, node)

	def inorder(self):
		def helper(self, root):

			if root:
				helper(self, root.left)
				print(root.value)
				helper(self, root.right)

		helper(self, self.root)	

	def preorder(self):
		def helper(self, root):

			if root:
				print(root.value)
				helper(self, root.left)
				helper(self, root.right)

		helper(self, self.root)	

	def postorder(self):
		def helper(self, root):

			if root:
				
				helper(self, root.left)
				helper(self, root.right)
				print(root.value)

		helper(self, self.root)				
				


	# Return true if BST contains the value
	# returns false otherwise
	# def contains(self, value):
	# 	if self.root.value == value:
	# 		return True
	# 	else:
	# 		return Node().get_value(self.root, value)	
	# # deletes the given value from the BST if it exists, 
	# # returns that value if it exists. Returns null if the value does not exist
	# def delete(self, value):

	# # returns the size of this BST
	# def size(self):

	# # returns true if the BST is empty, false otherwise
	# def is_empty(self):

	# # returns an iterator for all values in this BST in order
	# def iterator(self):




if __name__ == '__main__':
	# node not in main method
	t = 5
	a = 8
	b = BST()
	print(b.put(a))
	print (b)
	print(b.put(t))
	print(b)
	c = 3
	print(b.put(c))
	d = 6
	print(b.put(d))
	print(b.put(10))
	print(b.put(9))
	print(b.put(12))
	print("Inorder Great Job Kelvin")
	print(b.inorder())
	print("Preorder Great Job Kelvin")
	print(b.preorder())
	print("Postorder Great Job Kelvin")
	print(b.postorder())
	
	# print(b.contains(1))
	
	
	# print(b.get_node(d))


