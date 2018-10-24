# Implement a minimum heap with the array implementation. 
# The height of the element at the heap is determined by the index in the list.

class MinHeap:
    # Initializes an empty heap
    def __init__(self):
        self.minheap = []

    # returns the size of the heap
    def size(self):
        return len(self.minheap)
        

    # This helper function is to assist in the insert method
    # it is intended to swim a node up the heap until it 
    # is in the correct position. Here i represents the index in the list
    def _swim(self,i):
        if i % 2 == 0:
            c = (i - 2) // 2
            if self.minheap[i] <  self.minheap[c]:
                temp = self.minheap[c]
                self.minheap[c] = self.minheap[i]
                self.minheap[i] = temp
                if c != 0:
                    self._swim(c)

        else: 
            c = (i - 1) // 2 
            if self.minheap[i] < self.minheap[c]:
                temp = self.minheap[c]
                self.minheap[c] = self.minheap[i]
                self.minheap[i] = temp
                if c != 0:
                    self._swim(c)



    # This helper function is to assist in the del_min method
    # it is intended to sink a node into the correct position in the heap
    # Here i represents the index in the list of the element you are sinking
    def _sink(self,i):
        c = (2 * i) + 1
        d = (2 * i) + 2
        
        if d < len(self.minheap):

            if self.minheap[i] > self.minheap[c] or self.minheap[i] > self.minheap[d]:

                if self.minheap[c] <= self.minheap[d]:
                    temp = self.minheap[i]
                    self.minheap[i] = self.minheap[c]
                    self.minheap[c] = temp
                    self._sink(c)
                else:
                    temp = self.minheap[i]
                    self.minheap[i] = self.minheap[d] 
                    self.minheap[d] = temp
                    self._sink(d)   
            

    # Inserts element k into the heap, while maintaining the heap property
    def insert(self,k):
        if len(self.minheap) == 0:
            self.minheap.append(k)
        else:
            self.minheap.append(k)

            self._swim(len(self.minheap) - 1)    

    # Deletes the minimum element (the root) 
    # from the heap and returns that minimum element.
    def del_min(self):
        if len(self.minheap) == 0:
            return None

        if len(self.minheap) == 2:
            
            if self.minheap[0] <= self.minheap[1]:
                return self.minheap.pop(0)
            else:
                return self.minheap.pop(1) 
        if len(self.minheap) == 1:
            return self.minheap.pop()            

              
        temp = self.minheap[0]
        self.minheap[0] = self.minheap[len(self.minheap) - 1]
        self.minheap[len(self.minheap) - 1] = temp
        min_e = self.minheap.pop()
        self._sink(0)
        return min_e

if __name__ == '__main__':
    t = MinHeap()        
    
    t.insert(1)
    t.insert(2)
    t.insert(17)
    t.insert(4)
    t.insert(15)

    print(t.del_min())

    print(t.size())


    t.insert(7)
    t.insert(8)
    t.insert(6)
    t.insert(9)
    t.insert(10)
    print(t.size())
    t.insert(0)
    t.insert(5)
    

    print(t.size())
    print("Start Popping")
    
    print(t.del_min())
    print(t.del_min())
    print(t.del_min())
    print(t.del_min())
    print(t.del_min())
    print(t.del_min())
    print(t.del_min())
    print(t.del_min())
    print(t.del_min())
    print(t.del_min())
    print(t.del_min())
    print(t.del_min())
    print(t.del_min())
    print(t.del_min())
    print(t.del_min())
    




