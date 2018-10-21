class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Queue:
    def __init__ (self):
        self.front = self.rear = None
    def isEmpty(self):
        if self.front is None:
            
            
            return True
        else:
            return False
            
    def Enqueue(self, item):
        temp = Node(item)
        
        if self.rear is None:
            
            self.front = self.rear = temp
            return
        
        self.rear.next = temp
        self.rear = temp

    def Dequeue(self):
        if self.front is None:
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear is None
  
        return str(temp.value)

    def __repr__(self):
    	if self.front == None:
    		return "Empty"
    	cur = self.front
    	output = ""
    	while cur:
    		output += str(cur.value)
    		cur = cur.next	
    	return output	    
# if __name__ == '__main__':
#     print ("Hello world")
    
#     q = Queue()
#     q.isEmpty()
#     q.Enqueue(3)
#     q.Enqueue(4)
#     q.isEmpty()
#     q.Enqueue(5)
#     q.Dequeue()
#     q.Dequeue()
#     q.Dequeue()
#     q.Dequeue()	

if __name__ == '__main__':
	q = Queue()
	VALS = 100
	print(q.isEmpty())
	for i in range(VALS):
		
		print("added",i,q)
		q.Enqueue(i)
	for j in range(50):
		print('removed',q.Dequeue())
		q.Enqueue(j)
	print(q)
