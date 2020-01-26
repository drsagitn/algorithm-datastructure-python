class BSTNode:    
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def put(self, value):
        if self.value is None:
            self.value = value
        elif value < self.value:
            if(self.left is None):
                self.left = BSTNode(value)
            else:
                self.left.put(value)
        elif value > self.value:
            if(self.right is None):
                self.right = BSTNode(value)
            else:
                self.right.put(value)

    def traverse(self):
        ret = []
        if self.left is not None:
            ret += self.left.traverse()
        ret.append(self.value)
        if self.right is not None:
            ret += self.right.traverse()
        return ret
    
    def remove(self, value):
        if value > self.value:
            if self.right is not None:
                self.right = self.right.remove(value)
            return self
        elif value < self.value:
            if self.left is not None:
                self.left = self.left.remove(value)
            return self        
        elif value == self.value:# case value == self.value
            # node has one child
            if self.left is not None and self.right is None:
                self.value = self.left.value
                self.right = self.left.right
                self.left = self.left.left                
                return self
            elif self.right is not None and self.left is None:
                self.value = self.right.value
                self.left = self.right.left
                self.right = self.right.right
                return self
            # node has no child
            elif self.right is None and self.left is None:                
                return None
            else:
                # Node with two children: Get the inorder successor 
                # (smallest in the right subtree) 
                smallest_succ = self.minValueNode(self.right)
                self.value = smallest_succ.value
                self.right = self.right.remove(smallest_succ.value)                
                return self

    def minValueNode(self, node):
        while node.left is not None:
            node = node.left
        return node


    def is_contains(self, value):
        if self.value == value:
            return True
        if value < self.value and self.left is not None:
            return self.left.is_contains(value)
        if value > self.value and self.right is not None:
            return self.right.is_contains(value)
        return False

n = BSTNode()
n.put(1)
n.put(8)
n.put(3)
n.put(9)
print(n.traverse())
# print(n.is_contains(7))
# print(n.is_contains(8))
# print(n.is_contains(1))
# print(n.is_contains(0))
n.remove(8)
print(n.traverse())
n.remove(1)
print(n.traverse())
n.remove(5)
print(n.traverse())
n.remove(3)
print(n.traverse())

n2 = BSTNode()
n2.put(5)
n2.put(3)
n2.put(7)
n2.put(2)
n2.put(4)
n2.put(6)
n2.put(8)
print(n2.traverse())
n2.remove(2)
print(n2.traverse())
n2.remove(3)
print(n2.traverse())
n2.remove(5)
print(n2.traverse())

            

