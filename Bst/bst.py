
class Tree_node:
    #helper class
    def __init__ (self, value):
        self.value = value
        self.left = None
        self.right = None

    def _insert(self, value):
        if self.value == value:
            return False
        elif self.value > value:
            if self.left:
                return self.left._insert(value)
            else:
                self.left = Tree_node(value)
                return True
        else:
            if self.right:
                return self.right._insert(value)
            else:
                self.right = Tree_node(value)
                return True

    def _find(self, value):
        if self.value == value:
            return True
        elif self.value > value:
            if self.left:
                return self.left._find(value)
            else:
                return False
        else:
            if self.right:
                return self.right._find(value)
            else:
                return False

    def _preorder(self):
        if self:
            print(self.value)
            if self.left:
                self.left._preorder()
            if self.right:
                self.right._preorder()    

    def _postorder(self):
        if self:
            if self.left:
                self.left._postorder()
            if self.right:
                self.right._postorder()
            print(self.value)

    def _inorder(self):
        if self:
            if self.left:
                self.left._inorder()
            print(self.value)
            if self.right:
                self.right._inorder()                                                                                                        

class Bst:
    def __init__ (self, name="bob"):
        self.name = name
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Tree_node(value)
        else:
            return self.root._insert(value)    
    def find(self, value):
        if self.root:
            return self.root._find(value)

        else:
            return False    

    def preorder(self):
        print("Preorder")
        if self.root:
            
            self.root._preorder()

        
    def postorder(self):
        print("Postorder")
        if self.root:
            
            self.root._postorder()

    def inorder(self):
        print("Inorder")
        if self.root:
            
            self.root._inorder()
                    
            
    # prints a string representation of the tree
    def __repr__(self):
        if self.root is None:
            return "Empty tree"
        return str(self.root.val)

if __name__ == '__main__':
    print ("Hello world") 
    tree = Bst()   
    tree.insert(3)
    tree.insert(1)
    tree.insert(4)

    tree.inorder()