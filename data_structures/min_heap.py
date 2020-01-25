class MinHeap:
    heap = []
    
    def put(self, value):
        self.heap.append(value)
        self.bubble_up(len(self.heap)-1)

    def remove(self):
        self.heap[0] = self.heap[len(self.heap)-1]
        self.heap.pop()
        self.bubble_down(0)        
    
    def peek(self):
        return self.heap[0]

    def getLeftChild(self, parentIdx):
        idx = int(parentIdx*2+1)
        if idx < 0 or idx >= len(self.heap):
            return None, None
        return (idx, self.heap[idx])

    def getRightChild(self, parentIdx):
        idx = int(parentIdx*2+2)
        if idx < 0 or idx >= len(self.heap):
            return None, None
        return (idx, self.heap[idx])
    def getParent(self, childIdx):
        idx = int((childIdx-1)/2)
        if idx < 0 or idx >= len(self.heap):
            return None, None
        return (idx, self.heap[idx])
    
    def bubble_down(self, nodeIdx):
        l_idx, l_child_val = self.getLeftChild(nodeIdx)
        r_idx, r_child_val = self.getRightChild(nodeIdx)
        if r_idx is None and l_idx is None: return
        if( l_idx is not None and r_idx is None):
            target_idx = l_idx     
        elif( r_idx is not None and l_idx is None): 
            target_idx = r_idx
        else: 
            target_idx = r_idx if l_child_val > r_child_val else l_idx
        if(self.heap[nodeIdx] > self.heap[target_idx]):
            self.swap(nodeIdx, target_idx)
            self.bubble_down(target_idx)
            
    def bubble_up(self, nodeIdx):
        p_idx, p_val = self.getParent(nodeIdx)
        if p_idx is None: return
        if(self.heap[nodeIdx] < p_val):
            self.swap(p_idx, nodeIdx)
            self.bubble_up(p_idx)


    def swap(self, idx1, idx2):
        tmp = self.heap[idx1]
        self.heap[idx1] = self.heap[idx2]
        self.heap[idx2] = tmp

        

h = MinHeap()
for i in [3,7,3,8,34,1,9]:
    h.put(i)
print(h.heap, h.peek())
h.remove()
print(h.heap, h.peek())
h.remove()
print(h.heap, h.peek())
h.remove()
print(h.heap, h.peek())
h.remove()
print(h.heap, h.peek())
h.remove()
print(h.heap, h.peek())
h.put(0)
print(h.heap, h.peek())

